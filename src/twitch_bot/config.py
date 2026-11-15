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
YT_URL = get_env("YT_URL")
TG_URL = get_env("TG_URL")
INSTAGRAM_URL = get_env("INSTAGRAM_URL")
DISCORD_URL = get_env("DISCORD_URL")
STEAM_URL = get_env("STEAM_URL")
# WISHLIST_URL = get_env("WISHLIST_URL")
DONATE_URL = get_env("DONATE_URL")

PERIODIC_LINKS = [
    f"YouTube: {YT_URL}",
    f"Telegram: {TG_URL}",
    f"Instagram: {INSTAGRAM_URL}",
    f"Discord: {DISCORD_URL}",
    f"Steam: {STEAM_URL}",
    # f"Wishlist(Fetta): {WISHLIST_URL}",
    f"Поддержать стрим: {DONATE_URL}",
]
