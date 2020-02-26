import discord
import os
from discord.ext import commands

prefix_name = '>'
client = commands.Bot(command_prefix=prefix_name)
client.remove_command("help")


@client.command()
@commands.has_any_role(680810235983691923, 680907434138664979,524317186765094921)
async def testing(ctx, *, text=None):
    testing_embed = discord.Embed(title=text,
                                  icon_url="", color=0x0309e2)
    testing_embed.set_author(name="TESTING", icon_url='https://media.discordapp.net/attachments/676'
                                                      '162768314826753/676180765620437045/'
                                                      'example.png?width=473&height=473')
    testing_embed.set_thumbnail(url="https://media.discordapp.net/attachments/676162768314826753/6761807656"
                                    "20437045/example.png?width=473&height=473")
    if text is None:
        await ctx.send("`Please specify what the content of the embed should be and include a link (optional)`")
    else:
        await ctx.send(embed=testing_embed)
        await discord.Message.delete(ctx.message, delay=None)


@client.command()
async def help(ctx):
    help_embed = discord.Embed(title="Here is a list of all my possible commands:", description="Also if you are"
                                                                                                "wondering my prefix is"
                                                                                                " "
                                                                                                f"`{prefix_name}`",
                               colour=discord.Colour(0x8c63d9))
    help_embed.set_author(name="HELP")
    help_embed.add_field(name="ping", value="This returns the time that it takes for your command to reach this bot."
                         , inline=False)
    help_embed.add_field(name="testing", value="This will send a embed repeat of what you say after the message.")

    await ctx.send(embed=help_embed)


@client.command()
async def ping(ctx):
    ping_embed = discord.Embed(title=f"Your ping is `{client.latency * 1000}`ms",
                               icon_url="https://cdn.discordapp.com/avatars/655460237993574443/301a33f557f93"
                                        "315c1c05288f5dc5eea.png?size=256",
                               color=0x0309e2)
    await ctx.send(embed=ping_embed)

@testing.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("`You are not allowed to run this command.`")
        

client.run(os.environ['DISCORD_TOKEN1'])
