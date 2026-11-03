FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:0.11.21 /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_PROJECT_ENVIRONMENT=/usr/local

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project --no-dev

COPY . .

RUN uv sync --frozen --no-dev

CMD ["uv", "run", "python", "-m", "twitch_bot"]
