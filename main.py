from dotenv import load_dotenv
from twitchio.ext import commands
import os

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=config.OAUTH_TOKEN, prefix='!', initial_channels=[config.CHANNEL_NAME])

    async def event_ready(self):
        print(f"Logged in as {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return

        print(f"Nachricht erhalten: {message.content}")
        await self.handle_commands(message)

    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send('Testnachricht erfolgreich!')


load_dotenv()
print (os.getenv('OAUTH_TOKEN'))

#bot = Bot()
#bot.run()

