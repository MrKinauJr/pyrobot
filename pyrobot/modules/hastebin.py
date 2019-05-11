import os
from time import sleep

from pyrogram import Filters, Message
from pyrogram.api import functions, types
from pyrobot import BOT
import requests
from ..helpers import LogMessage



def post(content):
    post = requests.post("https://hastebin.com/documents", data=content)
    return "https://hastebin.com/" + post.json()["key"]


### Helper End ###



@BOT.on_message(Filters.command("haste", ".") & Filters.me)
def evaluation(bot: BOT, message: Message):
    try:
        cmdstr = " ".join(message.command[1:])
    except IndexError:
        message.edit("__I can't paste nothing sadly...__")
        sleep(2)
        message.delete()
        return

    if cmdstr:
        message.edit(post(cmdstr))  ## Making the Paste and give out the Link for the Response

