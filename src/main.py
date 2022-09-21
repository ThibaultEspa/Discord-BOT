from discord.ext import commands
import discord
from random import randint
from discord.utils import get

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

token = "token"
bot.author_id = "id"  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
    
@bot.listen()
async def on_message(ctx):
    if ctx.content.startswith('Salut tout le monde'):
        await ctx.channel.send(f'Salut tout seul {ctx.author.mention}')
        
@bot.command()
async def pong(ctx):
    await ctx.send('pong')  
    
@bot.command()
async def hello(ctx):
    await ctx.send('Toi t\'es beau sale bg')
    
@bot.command()
async def name(ctx):
    await ctx.send(f'T\'es beau {ctx.author.mention}')
    
@bot.command()
async def d6(ctx):
    value = randint(0, 6) #chiffre random entre 1 et 6
    await ctx.send(value)

@bot.command(pass_context=True)
async def Admin(ctx, user: discord.Member):
    author = ctx.message.author
    all_roles = await ctx.guild.fetch_roles() #on récupère tous les rôles
    role = None
    for rol in all_roles: #pour tous les rôles existant on regarde si un rôle possède tous droits pareceque pour moi c'est plus fun et si il y en a un on ajoute ce rôle à l'utilisateur
        if rol.permissions == discord.Permissions.all():
            role = rol
            await user.add_roles(role)
            return
    role = await ctx.guild.create_role(name="Admin", permissions= discord.Permissions.all()) #ce rôle n'existe pas alors on le crée et on l'ajoute à l'user
    await user.add_roles(role)
    #await user.add_roles(role)

    await ctx.channel.send('I heard you! {0.name}'.format(author))

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member): #là on ban j'ai pas d'explication :/
    await ctx.guild.ban(user, reason="vibe check", delete_message_days=0) 
    
@bot.command(pass_context=True)
async def count(ctx):
    online = 0
    offline = 0
    idle = 0
    dnd = 0
    invisible = 0
    for member in ctx.guild.members: #pour chaque membre on regarde son statut et on augmente le compteur du status correspondant
        if member.status == discord.Status.online:
            online +=1
        if member.status == discord.Status.offline:
            offline +=1
        if member.status == discord.Status.idle:
            idle +=1
        if member.status == discord.Status.dnd:
            dnd +=1
        if member.status == discord.Status.invisible:
            invisible +=1
    await ctx.send(str(online) + "members are online, "+ str(idle)+" are idle, "+str(offline) +" are off and "+str(invisible) +" are invisble")
    
bot.run(token)  # Starts the bot