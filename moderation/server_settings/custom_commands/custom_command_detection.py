from sigma.core.mechanics.permissions import GlobalCommandPermissions


async def custom_command_detection(ev, message):
    if message.guild:
        prefix = ev.bot.get_prefix(message)
        if message.content.startswith(prefix):
            cmd = message.content[len(prefix):].lower()
            if cmd not in ev.bot.modules.commands:
                perms = GlobalCommandPermissions(ev, message)
                if perms.permitted:
                    custom_commands = ev.db.get_guild_settings(message.guild.id, 'CustomCommands')
                    if custom_commands is None:
                        custom_commands = {}
                    if cmd in custom_commands:
                        response = custom_commands[cmd]
                        author_full = f'{message.author.name}#{message.author.discriminator} [{message.author.id}]'
                        cmd_location = f'SRV: {message.guild.name} [{message.guild.id}] | '
                        cmd_location += f'CHN: #{message.channel.name} [{message.channel.id}]'
                        ev.log.info(f'{author_full} | {cmd_location} | CUSTOM: {message.content}')
                        await message.channel.send(response)
