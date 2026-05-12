"""Tests for WeChat webhook notification service."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import AsyncMock

import httpx
import pytest

from src.models import WechatConfig, WechatReceiverConfig
from src.services.wechat import WechatNotifier


@pytest.fixture
def wechat_config() -> WechatConfig:
    """Create a test WeChat configuration."""
    return WechatConfig(
        enabled=True,
        webhook_key_env="TEST_WEBHOOK_KEY",
        webhook_url="http://localhost:8001/api/v1/webhook/send",
        receivers=[
            WechatReceiverConfig(type="friend", name="test_user", id="user123"),
            WechatReceiverConfig(
                type="group",
                name="test_group",
                id="group456",
                mentioned_list=["user1", "user2"],
            ),
        ],
    )


@pytest.fixture
def wechat_notifier(wechat_config: WechatConfig) -> WechatNotifier:
    """Create a test WeChat notifier."""
    return WechatNotifier(wechat_config)


class TestGenerateSignature:
    """Tests for signature generation."""

    def test_signature_format(self, wechat_notifier: WechatNotifier) -> None:
        """Test that signature is a valid hex string."""
        signature = wechat_notifier._generate_signature(
            webhook_key="test_key",
            timestamp="1700000000",
            nonce="aabbccddeeff0011",
            body='{"msg":"test"}',
        )
        assert len(signature) == 64
        assert all(c in "0123456789abcdef" for c in signature)

    def test_signature_deterministic(self, wechat_notifier: WechatNotifier) -> None:
        """Test that same inputs produce same signature."""
        signature1 = wechat_notifier._generate_signature(
            webhook_key="test_key",
            timestamp="1700000000",
            nonce="aabbccddeeff0011",
            body='{"msg":"test"}',
        )
        signature2 = wechat_notifier._generate_signature(
            webhook_key="test_key",
            timestamp="1700000000",
            nonce="aabbccddeeff0011",
            body='{"msg":"test"}',
        )
        assert signature1 == signature2

    def test_signature_different_inputs(self, wechat_notifier: WechatNotifier) -> None:
        """Test that different inputs produce different signatures."""
        sig1 = wechat_notifier._generate_signature(
            webhook_key="key1",
            timestamp="1700000000",
            nonce="aabbccddeeff0011",
            body='{"msg":"test"}',
        )
        sig2 = wechat_notifier._generate_signature(
            webhook_key="key2",
            timestamp="1700000000",
            nonce="aabbccddeeff0011",
            body='{"msg":"test"}',
        )
        assert sig1 != sig2


class TestBuildMessage:
    """Tests for message building."""

    def test_single_user_receiver(self, wechat_notifier: WechatNotifier) -> None:
        """Test message with single user receiver."""
        receivers = [WechatReceiverConfig(type="friend", name="test_user", id="user123")]
        payload = wechat_notifier._build_message("test content", receivers)

        assert payload["msgtype"] == "text"
        assert payload["content"] == "test content"
        assert payload["targets"] == [
            {"type": "friend", "name": "test_user", "id": "user123"}
        ]

    def test_multiple_user_receivers(self, wechat_notifier: WechatNotifier) -> None:
        """Test message with multiple user receivers."""
        receivers = [
            WechatReceiverConfig(type="friend", name="user1", id="id1"),
            WechatReceiverConfig(type="friend", name="user2", id="id2"),
        ]
        payload = wechat_notifier._build_message("test content", receivers)

        assert payload["targets"] == [
            {"type": "friend", "name": "user1", "id": "id1"},
            {"type": "friend", "name": "user2", "id": "id2"},
        ]

    def test_group_with_mentioned_list(self, wechat_notifier: WechatNotifier) -> None:
        """Test group receiver with mentioned_list."""
        receivers = [
            WechatReceiverConfig(
                type="group",
                name="test_group",
                id="group123",
                mentioned_list=["user1", "user2"],
            )
        ]
        payload = wechat_notifier._build_message("test content", receivers)

        assert payload["targets"] == [
            {
                "type": "group",
                "name": "test_group",
                "id": "group123",
                "mentioned_list": ["user1", "user2"],
            }
        ]

    def test_mixed_receivers(self, wechat_notifier: WechatNotifier) -> None:
        """Test mixed user and group receivers."""
        receivers = [
            WechatReceiverConfig(type="friend", name="user1", id="id1"),
            WechatReceiverConfig(
                type="group",
                name="group1",
                id="gid1",
                mentioned_list=["u1", "u2"],
            ),
        ]
        payload = wechat_notifier._build_message("test content", receivers)

        assert payload["targets"] == [
            {"type": "friend", "name": "user1", "id": "id1"},
            {"type": "group", "name": "group1", "id": "gid1", "mentioned_list": ["u1", "u2"]},
        ]


class TestSendNotification:
    """Tests for send_notification method."""

    @pytest.mark.asyncio
    async def test_disabled_notifier_returns_false(self) -> None:
        config = WechatConfig(enabled=False, webhook_url="", receivers=[])
        notifier = WechatNotifier(config)

        result = await notifier.send_notification("test", "title")
        assert result is False

    @pytest.mark.asyncio
    async def test_no_webhook_url_returns_false(self, wechat_notifier: WechatNotifier) -> None:
        wechat_notifier.config.webhook_url = ""

        result = await wechat_notifier.send_notification("test", "title")
        assert result is False

    @pytest.mark.asyncio
    async def test_no_receivers_returns_false(self, wechat_notifier: WechatNotifier) -> None:
        wechat_notifier.config.receivers = []

        result = await wechat_notifier.send_notification("test", "title")
        assert result is False

    @pytest.mark.asyncio
    async def test_missing_webhook_key_env_returns_false(
        self, wechat_notifier: WechatNotifier, monkeypatch
    ) -> None:
        monkeypatch.delenv("TEST_WEBHOOK_KEY", raising=False)
        wechat_notifier.config.webhook_url = "https://localhost:8001/webhook?key="

        result = await wechat_notifier.send_notification("test", "title")
        assert result is False

    @pytest.mark.asyncio
    async def test_successful_send(
        self, wechat_notifier: WechatNotifier, monkeypatch
    ) -> None:
        monkeypatch.setenv("TEST_WEBHOOK_KEY", "test_key_value")

        mock_response = AsyncMock()
        mock_response.raise_for_status = lambda: None

        mock_client = AsyncMock()
        mock_client.post = AsyncMock(return_value=mock_response)
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=None)

        monkeypatch.setattr("httpx.AsyncClient", lambda *args, **kwargs: mock_client)

        result = await wechat_notifier.send_notification("test content", "Test Title")

        assert result is True
        mock_client.post.assert_called_once()
        call_args = mock_client.post.call_args
        assert "X-Webhook-Timestamp" in call_args.kwargs["headers"]
        assert "X-Webhook-Nonce" in call_args.kwargs["headers"]
        assert "X-Webhook-Signature" in call_args.kwargs["headers"]

    @pytest.mark.asyncio
    async def test_webhook_url_placeholder_replacement(
        self, wechat_notifier: WechatNotifier, monkeypatch
    ) -> None:
        monkeypatch.setenv("TEST_WEBHOOK_KEY", "my_secret_key")

        mock_response = AsyncMock()
        mock_response.raise_for_status = lambda: None

        mock_client = AsyncMock()
        mock_client.post = AsyncMock(return_value=mock_response)
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=None)

        monkeypatch.setattr("httpx.AsyncClient", lambda *args, **kwargs: mock_client)

        await wechat_notifier.send_notification("test", "title")

        call_args = mock_client.post.call_args
        called_url = call_args.args[0]
        assert "my_secret_key" in called_url
        assert "{webhook_key}" not in called_url

    @pytest.mark.asyncio
    async def test_webhook_url_concatenation(
        self, wechat_notifier: WechatNotifier, monkeypatch
    ) -> None:
        wechat_notifier.config.webhook_url = "http://localhost:8001/api/v1/webhook/send?key="
        monkeypatch.setenv("TEST_WEBHOOK_KEY", "my_secret_key")

        mock_response = AsyncMock()
        mock_response.raise_for_status = lambda: None

        mock_client = AsyncMock()
        mock_client.post = AsyncMock(return_value=mock_response)
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=None)

        monkeypatch.setattr("httpx.AsyncClient", lambda *args, **kwargs: mock_client)

        await wechat_notifier.send_notification("test", "title")

        call_args = mock_client.post.call_args
        called_url = call_args.args[0]
        assert called_url == "http://localhost:8001/api/v1/webhook/send?key=my_secret_key"

    @pytest.mark.asyncio
    async def test_request_exception_returns_false(
        self, wechat_notifier: WechatNotifier, monkeypatch
    ) -> None:
        monkeypatch.setenv("TEST_WEBHOOK_KEY", "test_key_value")

        mock_client = AsyncMock()
        mock_client.post = AsyncMock(side_effect=Exception("Network error"))
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=None)

        monkeypatch.setattr("httpx.AsyncClient", lambda *args, **kwargs: mock_client)

        result = await wechat_notifier.send_notification("test", "title")
        assert result is False

    @pytest.mark.asyncio
    async def test_real_api_call(self, monkeypatch) -> None:
        """Optional smoke test against a real local webhook service."""
        env_file = Path(__file__).resolve().parents[1] / ".env"
        webhook_key = None
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("WECHAT_WEBHOOK_KEY="):
                    webhook_key = line.split("=", 1)[1].strip()
                    break

        if not webhook_key:
            pytest.skip("WECHAT_WEBHOOK_KEY not found in .env file")

        monkeypatch.setenv("WECHAT_WEBHOOK_KEY", webhook_key)

        config = WechatConfig(
            enabled=True,
            webhook_key_env="WECHAT_WEBHOOK_KEY",
            webhook_url="http://localhost:8001/api/v1/webhook/send?key=",
            receivers=[
                WechatReceiverConfig(type="friend", name="张三", id="1234567890"),
                WechatReceiverConfig(type="group", name="测试群", id="1234567890", mentioned_list=["@all"]),
            ],
        )
        notifier = WechatNotifier(config)

        original_post = httpx.AsyncClient.post

        async def capture_post(self, url, *args, **kwargs):
            print(f"\n=== API Request ===")
            print(f"URL: {url}")
            if "headers" in kwargs:
                print(f"Headers: {kwargs['headers']}")
            if "content" in kwargs:
                print(f"Body: {kwargs['content']}")
            response = await original_post(self, url, *args, **kwargs)
            print(f"\n=== API Response ===")
            print(f"Status: {response.status_code}")
            print(f"Body: {response.text}")
            return response

        monkeypatch.setattr("httpx.AsyncClient.post", capture_post)

        result = await notifier.send_notification("这是一条测试消息", "测试标题")
        print(f"\nResult: {result}")


class TestWechatNotifierInit:
    """Tests for WechatNotifier initialization."""

    def test_enabled_with_config(self) -> None:
        config = WechatConfig(enabled=True, webhook_url="http://test.com", receivers=[])
        notifier = WechatNotifier(config)
        assert notifier.enabled is True

    def test_disabled_with_config(self) -> None:
        config = WechatConfig(enabled=False, webhook_url="http://test.com", receivers=[])
        notifier = WechatNotifier(config)
        assert notifier.enabled is False

    def test_disabled_with_none_config(self) -> None:
        notifier = WechatNotifier(None)
        assert notifier.enabled is False
