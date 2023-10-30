import logging
from aiogram import Bot , Dispatcher , executor , types
from dotenv import load_dotenv
import os
import openai
import sys

class Reference:
    '''
    A class  to store previously responce from chatgpt api
    '''
    def __init__(self):
        self.responce = ""

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

reference = Reference()

TOKEN = os.getenv("TOKEN")

# Model Name

Model_Name = 'gpt-3.5-turbo'

## Initialize Bot and Dispatcher 

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    '''
    A funtion to clear previous content
    '''
    reference.responce = ""

@dispatcher.message_handler(commands=["start","help"])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    
    await message.reply("Hi \n I am Tele Bot ! \n Powered By Namit Chaudhari. How Can I Assist You ?")


@dispatcher.message_handler(commands=["clear"])
async def clear(message: types.Message):
    """
    This function clears the previous context 
    """
    clear_past()
    await message.reply("I have Created the past Conversation and context")

@dispatcher.message_handler(commands=["help"])
async def helper(message: types.Message):
    """
    This function displays help menu 
    """
    help_command = """"
    Hi There, I'm chatGPT Telegram bot created by Namit! Please follow these commands
    /start to start the conversation
    /clear to clear the past conversation and context.
    /help to get this help menu.
    I Hope this helps, :

    """
    await message.reply(help_command)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)