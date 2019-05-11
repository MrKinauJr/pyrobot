import requests
from time import sleep
from random import randint
from pyrogram import Filters, Message
from pyrobot import BOT

# -- Helpers -- #


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id

# -- Helpers End -- #

@BOT.on_message(Filters.command("random", ".") & Filters.me)
def randomnumber(bot: BOT, message: Message):
    try:
        cmdstr = " ".join(message.command[1:])
    except IndexError:
        message.edit("__I can't randomize nothing sadly...__")
        sleep(2)
        message.delete()
        return
    number = [int(s) for s in re.findall(r'\b\d+\b', cmdstr)]
    message.edit(ranint(number[0], number[1]),disable_web_page_preview=True)



@BOT.on_message(Filters.command("flip", ".") & Filters.me)
def flipacoin(bot: BOT, message: Message):
    Nummer = randint(1, 2)
    if Nummer == 1:
        message.edit("Heads!",disable_web_page_preview=True)
    else:
        message.edit("Tails!",disable_web_page_preview=True)

@BOT.on_message(Filters.command(["👨‍", ":person:", "person"], "") & Filters.me)
def send_person(bot: BOT, message: Message):
    BOT.send_photo(
        chat_id=message.chat.id,
        photo="https://thispersondoesnotexist.com/image?randomtag=" + str(randint(0,9999)),
        caption="persono",
        reply_to_message_id=ReplyCheck(message)
    )
    if message.from_user.is_self:
        message.delete()