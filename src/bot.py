import discord
import logging
import sys
from discord.ext import commands
from cogs import music, error, meta, tips
import os
bot = commands.Bot(command_prefix=os.environ["prefix"])


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")


COGS = [music.Music, error.CommandErrorHandler, meta.Meta, tips.Tips]


def add_cogs(bot):
    for cog in COGS:
        bot.load_extension(cog(bot))  # Initialize the cog and add it to the bot


def run():
    add_cogs(bot)
    if os.environ["token"] == "":
        raise ValueError(
            "No token has been provided. Please ensure that config.toml contains the bot token."
        )
        sys.exit(1)
    bot.run(os.environ["token"])
run()
