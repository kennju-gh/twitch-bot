import os

from dotenv import load_dotenv

load_dotenv()


def get_env(key: str) -> str:
    """Returns the environment variable or raises a clear error."""
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Critical error: environment variable {key} is not set!")
    return value


# Twitch settings
CLIENT_ID = get_env("CLIENT_ID")
CLIENT_SECRET = get_env("CLIENT_SECRET")
BOT_ID = get_env("BOT_ID")
OWNER_ID = get_env("OWNER_ID")

# Links
TG_URL = get_env("TG_URL")
DISCORD_URL = get_env("DISCORD_URL")
DONATE_URL = get_env("DONATE_URL")
# WISHLIST_URL = get_env("WISHLIST_URL")

PERIODIC_LINKS = [
    f"Telegram: {TG_URL}",
    f"Discord: {DISCORD_URL}",
    f"Поддержать стрим: {DONATE_URL}",
    # f"Вишлист: {WISHLIST_URL}",
]
