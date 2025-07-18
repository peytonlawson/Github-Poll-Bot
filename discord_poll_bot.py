import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True #Enable message content intent for reading messages
bot = commands.Bot(command_prefix='!', intents=intents) 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def poll(ctx, *, question_and_options: str):
    """ 
    Creates a simple poll. 
    Usage: !poll "Your Question" "Option1" "Option2" "Option3" ...
    """
    parts = question_and_options.split('" "')
    if len(parts) < 2:
        await ctx.send("Please provide a question and at least one option.")
        return
    
    question = parts[0].strip('"')
    options = [opt.strip('"') for opt in parts[1:]]

    if not options:
        await ctx.send("Please provide at least one option for the poll.")
        return


    #Create the embed for the poll
    embed = discord.Embed(title= "📊 New Poll!!!", description=question, color=discord.Color.purple())
    
    option_emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣','7️⃣', '8️⃣', '9️⃣', '  /span>  /span>']

    if len(options) > len(option_emojis):
        await ctx.send(f"Too many options! Maximum is {len(option_emojis)}.")
        return
    
    for i, option in enumerate(options):
        embed.add_field(name=f"{option_emojis[i]} {option}", value="\u200b", inline=False)

    poll_message = await ctx.send(embed=embed)

    for i in range(len(options)):
        await poll_message.add_reaction(option_emojis[i])

bot.run('YOUR TOKEN HERE') #Replace with your bot token