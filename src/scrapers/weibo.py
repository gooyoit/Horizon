"""Weibo hot search scraper implementation."""

import logging
from datetime import datetime, timezone
from typing import List
from urllib.parse import quote
import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, WeiboConfig

logger = logging.getLogger(__name__)

# Weibo hot search API endpoint
WEIBO_HOT_SEARCH_URL = "https://weibo.com/ajax/side/hotSearch"


class WeiboScraper(BaseScraper):
    """Scraper for Weibo hot search topics."""

    def __init__(self, config: WeiboConfig, http_client: httpx.AsyncClient):
        super().__init__(config.model_dump(), http_client)

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch Weibo hot search topics.

        Args:
            since: Only fetch items published after this time
                   (Note: Weibo hot search is real-time, so this is used for filtering)

        Returns:
            List[ContentItem]: Fetched content items
        """
        if not self.config.get("enabled", True):
            return []

        items = []

        try:
            # Set headers to mimic browser request
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Referer": "https://weibo.com/",
            }

            response = await self.client.get(
                WEIBO_HOT_SEARCH_URL,
                headers=headers,
                follow_redirects=True
            )
            response.raise_for_status()

            data = response.json()
            hot_items = data.get("data", {}).get("realtime", [])

            fetch_limit = self.config.get("fetch_limit", 20)
            current_time = datetime.now(tz=timezone.utc)

            for idx, item in enumerate(hot_items[:fetch_limit]):
                # Get title from 'note' or 'word' field
                title = item.get("note", "") or item.get("word", "")
                if not title:
                    continue

                # Get heat value (popularity score)
                heat = item.get("num", 0)

                # Construct search URL
                # Web UI uses: https://s.weibo.com/weibo?q=%23TITLE%23&Refer=top
                search_url = f"https://s.weibo.com/weibo?q={quote(title)}&Refer=top"

                # Generate unique ID
                item_id = f"hot_{idx}_{hash(title)}"

                item = ContentItem(
                    id=self._generate_id("weibo", "hotsearch", item_id),
                    source_type=SourceType.WEIBO,
                    title=title,
                    url=search_url,
                    content=None,  # Hot search items don't have content
                    author="Weibo Hot Search",
                    published_at=current_time,  # Hot search is real-time
                    metadata={
                        "heat": heat,
                        "rank": idx + 1,
                        "category": item.get("category", ""),
                    }
                )
                items.append(item)

            logger.info("Fetched %d Weibo hot search items", len(items))

        except httpx.HTTPError as e:
            logger.warning("Error fetching Weibo hot search: %s", e)
        except Exception as e:
            logger.warning("Error parsing Weibo hot search: %s", e)

        return items