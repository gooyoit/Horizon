"""Product Hunt scraper implementation."""

import calendar
import logging
import re
from datetime import datetime, timezone
from typing import List, Optional
from email.utils import parsedate_to_datetime
import httpx
import feedparser

from .base import BaseScraper
from ..models import ContentItem, SourceType, ProductHuntConfig

logger = logging.getLogger(__name__)

# Product Hunt RSS feed URL
PRODUCTHUNT_RSS_URL = "https://www.producthunt.com/feed"


class ProductHuntScraper(BaseScraper):
    """Scraper for Product Hunt top products via RSS feed."""

    def __init__(self, config: ProductHuntConfig, http_client: httpx.AsyncClient):
        super().__init__(config.model_dump(), http_client)

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch Product Hunt products from RSS feed.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        if not self.config.get("enabled", True):
            return []

        items = []

        try:
            # Fetch RSS feed
            response = await self.client.get(PRODUCTHUNT_RSS_URL, follow_redirects=True)
            response.raise_for_status()

            # Parse feed
            feed = feedparser.parse(response.text)

            fetch_limit = self.config.get("fetch_limit", 10)
            count = 0

            for entry in feed.entries:
                # Parse published date
                published_at = self._parse_date(entry)
                if not published_at or published_at < since:
                    continue

                # Generate unique ID
                entry_id = entry.get("id", entry.get("link", ""))
                product_name = self._extract_product_name(entry)

                # Extract content
                content = self._extract_content(entry)

                item = ContentItem(
                    id=self._generate_id("producthunt", "product", str(hash(entry_id))),
                    source_type=SourceType.PRODUCTHUNT,
                    title=entry.get("title", "Untitled Product"),
                    url=entry.get("link", PRODUCTHUNT_RSS_URL),
                    content=content,
                    author=self._extract_author(entry),
                    published_at=published_at,
                    metadata={
                        "product_name": product_name,
                        "tags": [tag.term for tag in entry.get("tags", [])],
                    }
                )
                items.append(item)
                count += 1

                if count >= fetch_limit:
                    break

        except httpx.HTTPError as e:
            logger.warning("Error fetching Product Hunt feed: %s", e)
        except Exception as e:
            logger.warning("Error parsing Product Hunt feed: %s", e)

        return items

    def _parse_date(self, entry: dict) -> Optional[datetime]:
        """Parse publication date from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            datetime: Parsed publication date or None
        """
        for field in ["published", "updated", "created"]:
            if field in entry:
                try:
                    # Try parsing structured time first
                    if f"{field}_parsed" in entry and entry[f"{field}_parsed"]:
                        return datetime.fromtimestamp(
                            calendar.timegm(entry[f"{field}_parsed"]),
                            tz=timezone.utc
                        )
                    # Fallback to string parsing
                    date_str = entry[field]
                    return parsedate_to_datetime(date_str)
                except Exception:
                    continue

        return None

    def _extract_content(self, entry: dict) -> str:
        """Extract text content from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            str: Extracted text content
        """
        # Try different content fields
        if "summary" in entry:
            content = entry.summary
        elif "description" in entry:
            content = entry.description
        elif "content" in entry and entry.content:
            content = entry.content[0].get("value", "")
        else:
            content = ""

        # Clean HTML tags
        content = re.sub(r'<[^>]+>', ' ', content).strip()
        # Normalize whitespace
        content = re.sub(r'\s+', ' ', content)

        return content

    def _extract_product_name(self, entry: dict) -> str:
        """Extract product name from entry title.

        Args:
            entry: Feed entry data

        Returns:
            str: Product name
        """
        title = entry.get("title", "")
        # Product Hunt RSS titles are usually just the product name
        return title.split(" - ")[0] if " - " in title else title

    def _extract_author(self, entry: dict) -> str:
        """Extract author/maker from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            str: Author name or "Product Hunt"
        """
        # Try to get author from entry
        if "author" in entry:
            return entry.author

        # Try to extract from content
        content = entry.get("summary", "") or entry.get("description", "")
        # Look for patterns like "by @username" or "made by"
        match = re.search(r'(?:by|made by)\s+@?(\w+)', content, re.IGNORECASE)
        if match:
            return match.group(1)

        return "Product Hunt"