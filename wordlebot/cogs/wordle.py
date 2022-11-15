from discord import Message
from discord.ext import commands

from utils.wordle_utils import (
    daily_puzzle_id,
    generate_info_embed,
    generate_puzzle_embed,
    process_message_as_guess,
    random_puzzle_id,
)

class Wordle(commands.GroupCog, name="Wordle"):
    """Play a game of Discord Wordle."""

    COG_EMOJI = "❇"

    def __init__(self, bot):
        self.bot = bot
        super().__init__()  # this is now required in this context.

    @commands.hybrid_command()
    @commands.guild_only()
    async def daily(
        self,
        ctx: commands.Context
    ):
        """Play a random, by it's ID, or the daily game of Wordle"""
        await ctx.reply(embed=generate_puzzle_embed(ctx.author, daily_puzzle_id()), mention_author=False)

    @commands.hybrid_command()
    @commands.guild_only()
    async def random(
        self,
        ctx: commands.Context
    ):
        """Play a random, by it's ID, or the daily game of Wordle"""
        await ctx.reply(embed=generate_puzzle_embed(ctx.author, random_puzzle_id()), mention_author=False)

    @commands.hybrid_command()
    @commands.guild_only()
    async def id(
        self,
        ctx: commands.Context,
        Wordle_ID: int = "ID of the Wordle to guess"
    ):
        """Play a random, by it's ID, or the daily game of Wordle"""
        await ctx.reply(embed=generate_puzzle_embed(ctx.author, Wordle_ID), mention_author=False)

    @commands.hybrid_command(name="info")
    @commands.guild_only()
    async def info(
        self,
        ctx: commands.Context,
    ):
        """How to play Discord Wordle"""
        await ctx.reply(embed=generate_info_embed(), mention_author=False)

    @commands.Cog.listener()
    async def on_message(
        self,
        message: Message
    ):
        """When a message is sent, process it as a guess."""
        await process_message_as_guess(self.bot, message)

async def setup(bot: commands.bot):
    await bot.add_cog(Wordle(bot))