import discord
import asyncio
import os
from discord.ext import commands


@commands.command()
async def announce(self, ctx, *, message : str = None):
    content = ' '.join(args)
    announcement = discord.Embed(color=0x3B88C3)
    author_name = f'{message.author.name}#{message.author.discriminator}'
    announcement.set_author(name=author_name, url=member.avatar_url)
    announcement.add_field(name=f'🌐 A Global {cmd.bot.user.name} Announcement', value=content)
    announcement.set_footer(text=f'Announced from {message.guild.name}', icon_url=message.guild.icon_url)
    sent_counter = 0
    for server in self.bot.guilds:
        try:
            await ctx.send(embed=announcement)
            sent_counter += 1
        except discord.Forbidden:
            pass
        except discord.NotFound:
            pass
    response = discord.Embed(color=0x77B255, title=f'✅ Announcement sent to {sent_counter} guilds.')
    await ctx.send(embed=response)

    
def setup(bot):
    bot.add_cog(broadcast(bot))     
