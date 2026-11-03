# Twitch Bot

A Python-based Twitch chat bot built with TwitchIO 3

## Features

- Greets new followers
- Responds to chat commands
- Periodically posts links to social media, donations, and wishlist

## Tech Stack

- Python 3.14
- TwitchIO
- uv (package manager)
- Docker

## Local Development

1. Copy `.env.example` to `.env` and fill in your Twitch credentials
2. Run `uv sync` to install dependencies
3. Run `uv run python -m twitch_bot` to start the bot

## Deployment

Build the Docker image:
``` bash
docker build -t twitch-bot .
```
