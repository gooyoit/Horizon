"""WeChat webhook notification service."""

import hmac
import hashlib
import json
import os
import time
import secrets
from typing import Optional, List
import httpx
from ..models import WechatConfig, WechatReceiverConfig


class WechatNotifier:
    """WeChat webhook notification handler."""

    def __init__(self, config: Optional[WechatConfig]):
        """Initialize WeChat notifier.

        Args:
            config: WeChat configuration
        """
        self.config = config
        self.enabled = config.enabled if config else False

    def _generate_signature(self, webhook_key: str, timestamp: str, nonce: str, body: str) -> str:
        """Generate HMAC-SHA256 signature for webhook verification.

        Args:
            webhook_key: Webhook key for signing
            timestamp: Unix timestamp in seconds
            nonce: Random 16-character hex string
            body: Request body (compact JSON string)

        Returns:
            Hex-encoded signature
        """
        # Body is already a compact JSON string
        sign_string = f"key={webhook_key}&timestamp={timestamp}&nonce={nonce}&body={body}"
        return hmac.new(
            webhook_key.encode(),
            sign_string.encode(),
            hashlib.sha256
        ).hexdigest()

    def _build_message(self, content: str, receivers: List[WechatReceiverConfig]) -> dict:
        """Build webhook message payload.

        Args:
            content: Message content
            receivers: List of receivers

        Returns:
            Message payload dict
        """
        # Build receiver_list
        receiver_list = []
        for receiver in receivers:
            receiver_item = {
                "type": receiver.type,
                "name": receiver.name,
                "id": receiver.id,
            }
            if receiver.type == "group" and receiver.mentioned_list:
                receiver_item["mentioned_list"] = receiver.mentioned_list
            receiver_list.append(receiver_item)

        payload = {
            "msgtype": "text",
            "text": {
                "content": content,
                "receiver_list": receiver_list
            }
        }

        return payload

    async def send_notification(self, content: str, title: str = "Horizon Daily") -> bool:
        """Send notification to configured receivers.

        Args:
            content: Message content
            title: Message title (used as prefix)

        Returns:
            True if successful, False otherwise
        """
        if not self.enabled or not self.config:
            return False

        if not self.config.webhook_url:
            print("[warning] WeChat webhook_url not configured, skipping notification")
            return False

        if not self.config.receivers:
            return False

        # Get webhook_key from environment variable
        webhook_key = os.getenv(self.config.webhook_key_env)
        if not webhook_key:
            print(f"[warning] WeChat webhook_key not configured (env {self.config.webhook_key_env}), skipping notification")
            return False

        # Resolve webhook_url - support {webhook_key} placeholder
        webhook_url = self.config.webhook_url
        if "{webhook_key}" in webhook_url:
            webhook_url = webhook_url.replace("{webhook_key}", webhook_key)
        else:
            webhook_url = webhook_url + webhook_key

        # Prepare message content
        message_content = f"{title}\n\n{content}"

        # Generate headers
        timestamp = str(int(time.time()))
        nonce = secrets.token_hex(8)  # 16-character hex string

        # Build message payload
        payload = self._build_message(message_content, self.config.receivers)
        body = json.dumps(payload, separators=(',', ':'), ensure_ascii=False)

        # Generate signature - use body with unicode escapes (as sent to server)
        signature = self._generate_signature(webhook_key, timestamp, nonce, body)

        # Prepare headers
        headers = {
            "Content-Type": "application/json",
            "X-Webhook-Timestamp": timestamp,
            "X-Webhook-Nonce": nonce,
            "X-Webhook-Signature": signature
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    webhook_url,
                    content=body.encode(),
                    headers=headers
                )
                response.raise_for_status()
                return True
        except Exception as e:
            print(f"Failed to send WeChat notification: {e}")
            return False
