from pydantic import BaseSettings


class Settings(BaseSettings):
    telegram_token: str
    telegram_channel_id: str

    vk_token: str
    vk_group_id: int = 61034234
    vk_group_name: str = "eight_out_ten"
    vk_base_url: str = "https://api.vk.com/method"
    vk_api_version: str = "5.131"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()  # type: ignore
