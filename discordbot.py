from cmath import e
import os
import random
import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='copypasta', help='responds with a random copypasta')
async def curse_word(ctx):
    msgs = [
        (
            'What did you just say, you little kid? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.'

            'I am trained in guerilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you out with precision the likes of which has never been seen before on this Earth, mark my words.'

            'You think you can get away with saying that to me over the Internet? Think again. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands.'

            'Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable self off the face of the continent, you little idiot. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your tongue.'

            'But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will dump fury all over you and you will drown in it.'

            'You’re dead, kiddo.'
        ),
        (
            'Hey guys, did you know that in terms of male human and female Pokémon breeding, Vaporeon is the most compatible Pokémon for humans?'
            ' Not only are they in the field egg group, which is mostly comprised of mammals, Vaporeon are an average of 3”03’ tall and 63.9 pounds, this means they’re large enough to be able handle human dicks, and with their impressive Base Stats for HP and access to Acid Armor, you can be rough with one.'
            '  Due to their mostly water based biology, there’s no doubt in my mind that an aroused Vaporeon would be incredibly wet, so wet that you could easily have sex with one for hours without getting sore.'
            '   They can also learn the moves Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide nipples, so it’d be incredibly easy for one to get you in the mood.'
            '    With their abilities Water Absorb and Hydration, they can easily recover from fatigue with enough water.'
            '     No other Pokémon comes close to this level of compatibility.'
            '      Also, fun fact, if you pull out enough, you can make your Vaporeon turn white.'
            '       Vaporeon is literally built for human dick.'
            '        Ungodly defense stat+high HP pool+Acid Armor means it can take cock all day, all shapes and sizes and still come for more'
        ),
        (
            'UNROLL THE TADPOLE'
            ' UNCLOG THE FROG'
            '  UNLOAD THE TOAD'
            '   UNINHIBIT THE RIBBIT'
            '    UNSTICK THE LICK'
            '     UNIMPRISON THE AMPHIBIAN'
            '      UNMUTE THE NEWT'
            '       UNBENCH THE KENCH'
            '       PERMIT THE KERMIT'
            '        DEFOG THE POLLIWOG'
        ),
        (
            '👌👀👌👀👌👀👌👀👌👀 good shit'
            ' go౦ԁ sHit👌 thats ✔ some good👌👌shit right👌👌th'
            ' 👌 ere👌👌👌 right✔there ✔✔if i do ƽaү so my selｆ'
            ' 💯 i say so 💯 thats what im talking about right'
            ' there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ💯'
            ' 👌👌 👌НO0ОଠＯOOＯOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ👌 👌👌'
            ' 👌 💯 👌 👀 👀 👀 👌👌Good shit'
        ),
        (
            'I sexually Identify as the sun.'
            ' Ever since I was a boy I dreamed of slamming'
            ' hydrogen isotopes into each other to make helium &'
            ' light and send it throught the galaxy. People say to'
            ' me that a person being a star is Impossible and I’m'
            ' fucking retarded but I don’t care, I’m beautiful. I’m'
            ' having a plastic surgeon inflate me with hydrogen'
            ' and raise my temperature to over 6000 °C. From'
            ' now on I want you guys to call me “Sol” and respect'
            ' my right to give you vitamin D and probably'
            ' sunburns. If you can’t accept me you’re a'
            ' fusionphobe and need to check your astral'
            ' privilege. Thank you for being so understanding.'
        )
    ]

    response = random.choice(msgs)
    await ctx.send(response)

bot = commands.Bot(command_prefix='!')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.command(name='create-channel')
@commands.has_role('epic')
async def create_channel(ctx, channel_name='POG-BOT-CHAT'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    try:
        GUILD = discord.utils.get(client.guilds, name=guild) 
        if GUILD is None:
            print("The guild: {} was not found".format(guild))
            return
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{GUILD.name}(id: {994992823063552080})'
        )
    except Exception as e:
        print("An error has occured on_ready() getting the guild: {}".format(e))

    members = '\n - '.join([member.name for member in GUILD.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to this amazing server try not to die!'
    )


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

try:
    client.run(token)
except Exception as f:
    print("Error running client: {}".format(f))

bot.run(token)