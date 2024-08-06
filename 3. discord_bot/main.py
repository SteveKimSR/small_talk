import discord
import asyncio
import timetable

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('출력')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('봇의 상태메세지'))


@client.event
async def on_message(message):
    if message.content == "테스트":  # 메세지감지
        # 메세지가 작성된 채널에 SEND (채널)
        await message.channel.send("{} | {} , Hello".format(message.author, message.author.mention))
        # await message.author.send("{} | {} , user, Hello".format(message.author, message.author.mention)) # 메세지를 작성한 사람에게 SEND (DM)

client.run(
    '')  # 우리꺼토큰
