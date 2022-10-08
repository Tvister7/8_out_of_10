from datetime import datetime
from typing import Any

from httpx import AsyncClient
from loguru import logger

from .settings import settings


async def _get_group_posts() -> dict[str, Any]:
    async with AsyncClient() as client:
        url = f"{settings.vk_base_url}/wall.get"
        params = {
            "access_token": settings.vk_token,
            "v": settings.vk_api_version,
            "owner_id": -settings.vk_group_id,
            "filter": "owner",
            "count": 5
        }
        response = await client.get(url, params=params)
        return response.json()


async def get_group_memes():
    current_timestamp = datetime.utcnow().timestamp()
    posts: list[dict[str, Any]] = (await _get_group_posts()).get("response", {}).get("items")  # type: ignore
    all_post_images = []
    for post in posts:
        # remove old posts
        if post.get("date", 0) < current_timestamp - 3600:
            continue
        # remove ads
        attachments: list[dict[str, Any]] = post.get("attachments", [])
        if len(attachments) > 4:
            continue

        best_quality_image_urls = []

        for attachment in attachments:
            if attachment.get("type") != "photo":
                continue
            best_quality_image_url = ''
            current_pixel_size = 0
            photo = attachment.get("photo", {})
            for image in photo.get("sizes", []):
                pixel_size = image.get("height", 0) \
                    * image.get("width", 0)
                if pixel_size > current_pixel_size:
                    current_pixel_size = pixel_size
                    best_quality_image_url = image.get("url", "")

            best_quality_image_urls.append(best_quality_image_url)
        all_post_images.append(best_quality_image_urls)
    logger.info(all_post_images)
    return all_post_images
