import discord
from discord.ext import commands
def params(list, index):
    return index < len(list)
client = commands.Bot(command_prefix = 'td!')
class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        game = discord.Game("m0untain.agency")
        await client.change_presence(status=discord.Status.dnd, activity=game)

    async def on_message(self, message):
        args = message.content.split()
        if(params(args, 0) and params(args, 1)):
            if(args[0] == client.command_prefix):
                cmd = args[1]
                if(cmd == "ping"):
                    await message.channel.send("ok")


client = MyClient()
client.run('')