import discord
import random
from random import randint
from discord.ext.commands import Bot

BOT_PREFIX = ('$')

# opens and reads the .txt file where the bot token is stored
with open('Discord_Bot_Token.txt', 'r') as reader:
    token = reader.readline()

# instantiates the discord bot

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='dice')  # command that rolls dice
async def roll_dice(ctx, dice: str):
    total_roll = []
    num_dice = int(dice.split('d')[0])
    dice_type = int(dice.split('d')[1])

    for x in range(0, num_dice):
        total_roll.append(randint(1, dice_type))
    rolling = ' '.join(map(str, total_roll))
    rolling += 'Total: ' + str(sum(total_roll))
    await ctx.send(str(rolling))


@client.command(name='8ball')  # command that answers yes or no questions
async def eight_ball(ctx):
    possible_responses = [
        'That is an ASTOUNDING NOPE!',
        'It is not looking likely',
        'The future is Hazy',
        'It does look like a YES',
        '100 PERCENT YES! YES! YES!']
    await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)


@client.command()  # command that will square a number
async def square(ctx, number: int):
    squared_value = int(number)**2
    await ctx.send(str(number) + " squared is " + str(squared_value))


# once logged in prints confirmation
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# # # # # Old code Keeping for reference # # # # # # # # #
# when someone types into a channel the bot looks
# for certain phrases.
# @client.event
# async def on_message(message):
#    if message.author == client.user:
#        return

#    if message.content.startswith('hello'):
#        await message.channel.send('Hello!')
#    await client.process_commands(message)


@client.event
async def on_message(message):
    if message.author == client.user:  # bot doesnt respond to itself
        return

    palandrome = message.content.lower()  # used in palandrome check
    palandrome = str(palandrome.replace(" ", ""))
    ispalandrome = palandrome[::-1]  # reversed palandrome
    sarcasm = message.content.lower()
    # print(sarcasm)
    sarcasm = str(sarcasm.replace("'", "").replace("’", ""))
    # print(sarcasm[1]) #testing why replace isnt working right
    # print(sarcasm) #iphone apostrophe char is different than single quote
    print(palandrome)
    print(ispalandrome)
    if sarcasm.startswith('im '):
        await message.channel.send(f"Hi {sarcasm[2:]}, I'm Test Bot, and I'm the dad joke master")

    if palandrome == ispalandrome:  # checks if a word is a palandrome
        await message.channel.send("T-A-C-O-C-A-T... TACOCAT, TACOCAT!!!!")

    await client.process_commands(message)

client.run(token)
