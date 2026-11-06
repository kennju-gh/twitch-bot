from twitchio.ext import commands

from ..config import DISCORD_URL, DONATE_URL, TG_URL


class CommandsComponent(commands.Component):
    @commands.command(name="tg", aliases=["тг", "телеграм"])
    @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
    async def telegram_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Telegram: {TG_URL}")

    @commands.command(name="ds", aliases=["дс", "дискорд"])
    @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
    async def discord_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Discord: {DISCORD_URL}")

    @commands.command(name="donate", aliases=["донат", "трусы"])
    @commands.cooldown(rate=1, per=60, key=commands.BucketType.chatter)
    async def donate_cmd(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Поддержать стрим: {DONATE_URL}")
