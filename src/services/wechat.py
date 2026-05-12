"""WeChat webhook notification service."""

import hashlib
import hmac
import json
import os
import secrets
import time
from typing import List, Optional

import httpx

from ..models import WechatConfig, WechatReceiverConfig


class WechatNotifier:
    """WeChat webhook notification handler."""

    def __init__(self, config: Optional[WechatConfig]):
        self.config = config
        self.enabled = config.enabled if config else False

    def _generate_signature(self, webhook_key: str, timestamp: str, nonce: str, body: str) -> str:
        """Generate HMAC-SHA256 signature for webhook verification."""
        sign_string = f"key={webhook_key}&timestamp={timestamp}&nonce={nonce}&body={body}"
        return hmac.new(
            webhook_key.encode(),
            sign_string.encode(),
            hashlib.sha256,
        ).hexdigest()

    def _build_message(self, content: str, receivers: List[WechatReceiverConfig]) -> dict:
        """Build webhook message payload."""
        targets = []
        for receiver in receivers:
            receiver_item = {
                "type": receiver.type,
                "name": receiver.name,
                "id": receiver.id,
            }
            if receiver.type == "group" and receiver.mentioned_list:
                receiver_item["mentioned_list"] = receiver.mentioned_list
            targets.append(receiver_item)

        return {
            "msgtype": "text",
            "content": content,
            "targets": targets,
        }

    async def send_notification(self, content: str, title: str = "Horizon Daily") -> bool:
        """Send notification to configured receivers."""
        if not self.enabled or not self.config:
            return False

        if not self.config.webhook_url:
            print("[warning] WeChat webhook_url not configured, skipping notification")
            return False

        if not self.config.receivers:
            return False

        webhook_key = os.getenv(self.config.webhook_key_env)
        if not webhook_key:
            print(
                f"[warning] WeChat webhook_key not configured "
                f"(env {self.config.webhook_key_env}), skipping notification"
            )
            return False

        webhook_url = self.config.webhook_url
        if "{webhook_key}" in webhook_url:
            webhook_url = webhook_url.replace("{webhook_key}", webhook_key)
        else:
            webhook_url = webhook_url + webhook_key

        message_content = f"{title}\n\n{content}"
        timestamp = str(int(time.time()))
        nonce = secrets.token_hex(8)

        payload = self._build_message(message_content, self.config.receivers)
        body = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
        signature = self._generate_signature(webhook_key, timestamp, nonce, body)

        headers = {
            "Content-Type": "application/json",
            "X-Webhook-Timestamp": timestamp,
            "X-Webhook-Nonce": nonce,
            "X-Webhook-Signature": signature,
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    webhook_url,
                    content=body.encode(),
                    headers=headers,
                )
                response.raise_for_status()
                return True
        except Exception as e:
            print(f"Failed to send WeChat notification: {e}")
            return False
