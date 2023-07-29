from typing import List, Optional

import discord
from discord import app_commands
from discord.ext import commands

from .help import MyHelpCommand

class Meta(commands.Cog, name="meta"):
    """Meta commands."""
    COG_EMOJI = "🔖"

    def __init__(self, bot: discord.Client):
        self.bot:discord.Client = bot

        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

    @app_commands.command()
    async def help(self, interaction: discord.Interaction, command: Optional[str]):
        """Shows help on a command or category of commands."""

        ctx = await self.bot.get_context(interaction, cls=commands.Context)
        #await ctx.reply(f"{INFO} Help on prefix commands", mention_author=False, delete_after=3)
        if command is not None and command != "all":
            await ctx.send_help(command)
        else:
            await ctx.send_help()

    @help.autocomplete("command")
    async def command_autocomplete(self, interaction: discord.Interaction, needle: str) -> List[app_commands.Choice[str]]:
        assert self.bot.help_command
        ctx = await self.bot.get_context(interaction, cls=commands.Context)
        help_command = self.bot.help_command.copy()
        help_command.context = ctx
        """
        if not needle:
            return [
                app_commands.Choice(name=f"{getattr(cog, 'COG_EMOJI', None)} {cog_name}", value=cog_name)
                for cog_name, cog in self.bot.cogs.items()
                if await help_command.filter_commands(cog.get_commands())
            ][:25]
        """
        if needle:
            needle = needle.lower()

            return_commands = []
            for command in await help_command.filter_commands(self.bot.walk_commands(), sort=True):
                if needle in command.qualified_name:
                    return_commands.append(app_commands.Choice(name=command.qualified_name, value=command.qualified_name))

            for cog_name, cog in self.bot.cogs.items():
                if needle in cog_name.casefold():
                    return_commands.append(app_commands.Choice(name=f"{getattr(cog, 'COG_EMOJI', None)} {cog_name}", value=cog_name))

            return_commands = return_commands[:10]

            return return_commands
        else:
            return [app_commands.Choice(name="Type a command or category...", value="all")]

async def setup(bot: commands.bot):
    await bot.add_cog(Meta(bot))
