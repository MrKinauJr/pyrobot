import requests
from time import sleep

from pyrobot import BOT
from pyrogram import Filters, Message

# -- Helpers -- #

def GiveReplyObj(message: Message):
    reply_id = message

    if message.reply_to_message:
        reply_id = message.reply_to_message

    return reply_id

# -- Helpers End -- #


@BOT.on_message(Filters.command("blank", ".") & Filters.me)
def format_blank(bot: BOT, message: Message):
        if message.reply_to_message:
            GiveReplyObj(message).edit("󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰")
            message.delete()
        else:
            message.edit("󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰")


@BOT.on_message(Filters.command("respect", ".") & Filters.me)
def pay_respect(bot: BOT, message: Message):
        message.edit("_ \n |  ___|\n | |_   \n |  _|  \n |_|")


@BOT.on_message(Filters.command("replace", ".") & Filters.me)
def pay_respect(bot: BOT, message: Message):
        try:
            cmdstr = " ".join(message.command[1:])
        except IndexError:
            message.edit("__I can't replace nothing...__")
            sleep(2)
            message.delete()
            return
        replacelist = cmdstr.split(";")
        reply = GiveReplyObj(message)
        
        try:reply.edit(reply.text.replace(replacelist[0], replacelist[1]))
        except IndexError:
            message.edit("__I can't replace nothing...__")
            sleep(2)
            message.delete()
            return
        message.delete()
