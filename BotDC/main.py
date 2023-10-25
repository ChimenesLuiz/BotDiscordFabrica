import discord
import sys  
from discord.ext import commands
from exs import *
import random
from ias import *  
from googletrans import Translator 
from dotenv import load_dotenv 
import os
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # Configurar a intenção como True

bot = commands.Bot(intents=intents, command_prefix='$')

# o discord dos donos do BOT 
donos = ['ninjasupremobr','luizg7954']

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    channel_id = 1165027062545928243  # Substitua pelo ID do canal desejado
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(" :fire:  **Estou online e pronto!**  :fire:")
#         msg = """**$ex** - gera um exercício de maratonas de programação(Codewars e Senac)
# **$conselho** - receba um conselho do bot
# **$chat** - Converse com o bot
# **$piada** -  Gera uma piada
# **$d {numero}** -  roda um dado que vc escolher
# **$img {img_desejada}** - gera uma imagem sobre o que preferir"""

#         embed = discord.Embed(
#         title=f"**COMANDOS**",
#         description=f"{msg}",
#         color=0x00ffff
#         )
            
#         await channel.send(embed=embed)


@bot.command()
async def teste(ctx, *args):
    # Responder ao comando !teste com a mensagem "teste"
    msg = " ".join(args)
    await ctx.send(f"{msg}")

@bot.command()
async def commands(ctx):
    msg = """**$ex** - gera um exercício de maratonas de programação(Codewars e Senac)
**$conselho** - receba um conselho do bot
**$chat** - Converse com o bot
**$piada** -  Gera uma piada
**$d {numero}** -  roda um dado que vc escolher
**$img {img_desejada}** - gera uma imagem sobre o que preferir
**$commands** - Todos os comandos do BOT
"""

    embed = discord.Embed(
    title=f"**COMANDOS**",
    description=f"{msg}",
    color=0x00ffff
    )
        
    await ctx.send(embed=embed)

@bot.command()
async def ex(ctx):
    emojis=[":dotted_line_face:",":face_with_raised_eyebrow:",":joy:",":star:",":face_with_monocle:",":interrobang:",":face_in_clouds:",":detective:",":smiling_imp:",":disguised_face:",":hot_face:",":fire:",":grimacing:",":shushing_face:"]
    questao = random_ex()
    print(questao[0])
    
    if(questao[0] == 1 or questao[0] == 2):

        embed = discord.Embed(
        title=f"{random.choice(emojis)} {questao[1]['dificuldade']} - {questao[1]['nome']}",
        description=f"{questao[1]['descricao']}",
        color=0x00ffff
        )
        embed.set_image(url=questao[1]['image'])
        embed.set_thumbnail(url="https://iili.io/JKT3QWX.png")
        embed.set_footer(text="© Questão Original da Fábrica de Software", icon_url="https://iili.io/JKT3QWX.png")

        
    else:
        
       
         
        embed = discord.Embed(
        title=f"{random.choice(emojis)} {questao[1][0]}",
        description=questao[1][1],
        color=0x00ffff
        )
        
    
   
    
    
    await ctx.send(embed=embed)
    
@bot.command()
async def d(ctx,num):
    
    
    num_rand = random.randrange(1, int(num))
    if(num_rand == 4 or num_rand == 24):
        descricao = "Hummm, la ele"
        
    else:
        descricao = ""
        
    embed = discord.Embed(
        title=f"{num_rand}",
        description=descricao,
        color=0x00ff00  # Cor do embed (verde)
    )
    
    await ctx.send(embed=embed)

@bot.command()
async def conselho(ctx):
    embed = discord.Embed(
        title=f"**Conselho**",
        description=f"{get_conselho()}",
        color=0x032078  # Cor do embed (verde)
    )
    
    await ctx.send(embed=embed)

@bot.command()
async def piada(ctx):
    
    emojis=[":dotted_line_face:",":face_with_raised_eyebrow:",":joy:",":star:",":face_with_monocle:",":interrobang:",":face_in_clouds:",":detective:",":smiling_imp:",":disguised_face:",":hot_face:",":fire:",":grimacing:",":shushing_face:"]
    piada = random_joke()
    embed = discord.Embed(
        
        title=f"{random.choice(emojis)} **{piada[0]}**",
        description=f"{piada[1]}", 
        color=0x00ffff  # Cor do embed (verde)
    )
    await ctx.send(embed=embed)

@bot.command()
async def chat(ctx,*args):
    msg = " ".join(args)
    
    
    prefix = "Sr(a)" if str(ctx.author) in donos else "" 
    embed = discord.Embed(
        
        title=f":space_invader: Olá, {prefix} {ctx.author}",
        description=f"{generate_chatGPT(msg)}", 
        color=0x00ffff  # Cor do embed (verde)
    )
    await ctx.send(embed=embed)
     
           
@bot.command()
async def img(ctx,*args):
    msg = " ".join(args)
    # msg = Translator().translate(msg,'en').text
    msg = msg.replace(" ","-")
    
    embed = discord.Embed(
        
        title=f":frame_photo: **{msg}**", 
        color=0x00ffff  # Cor do embed (verde)
    ) 
    embed.set_image(url=f"https://source.unsplash.com/400x300/?{msg}")
    embed.set_image(url="icon.jpeg")
    await ctx.send(embed=embed)
@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel): 
        server = bot.get_guild(1046231965872967690)
        
        channel = server.get_channel(1165027062545928243)
        
        if server and channel: 
            await channel.send(f"{message.author}: {message.content}")
    await bot.process_commands(message) 

@bot.event
async def play(clx):
    try:
        channel = bot.author.voice.voice_channel
        await clx.join_voice_channel(channel)
    except discord.errors.InvalidArgument:
        await clx.send_bot(bot.channel, "O bot ja esta em um canal de voz")
    except Exception as error:
        await clx.send_bot(bot.channel, "Ein Error: ```{error}```".format(error=error))      

token = os.environ.get("TOKEN")   
bot.run(token=token) 
