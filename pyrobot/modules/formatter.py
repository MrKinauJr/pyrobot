import requests
from time import sleep
import hashlib
from pyrobot import BOT
from pyrogram import Filters, Message
import string

# -- Helpers -- #

def GiveReplyObj(message: Message):
    reply_id = message

    if message.reply_to_message:
        reply_id = message.reply_to_message

    return reply_id


def rot(n):
    n = int(n)
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

# -- Helpers End -- #


@BOT.on_message(Filters.command("blank", ".") & Filters.me)
def format_blank(bot: BOT, message: Message):
        if message.reply_to_message:
            GiveReplyObj(message).edit("󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰")
            message.delete()
        else:
            message.edit("󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰󠇰")

@BOT.on_message(Filters.command("toBinary", ".") & Filters.me)
def format_blank(bot: BOT, message: Message):
        try:
            cmdstr = " ".join(message.command[1:])
        except IndexError:
            message.edit("__I can't...__")
            sleep(2)
            message.delete()
            return

        message.edit(' '.join(format(ord(x), 'b') for x in cmdstr))


@BOT.on_message(Filters.command("toMD5", ".") & Filters.me)
def format_blank(bot: BOT, message: Message):
        try:
            cmdstr = " ".join(message.command[1:])
        except IndexError:
            message.edit("__I can't...__")
            sleep(2)
            message.delete()
            return

        message.edit(hashlib.md5(cmdstr.encode('utf-8')).hexdigest())

@BOT.on_message(Filters.command("toSHA512", ".") & Filters.me)
def format_blank(bot: BOT, message: Message):
        try:
            cmdstr = " ".join(message.command[1:])
        except IndexError:
            message.edit("__I can't...__")
            sleep(2)
            message.delete()
            return

        message.edit(hashlib.sha512(cmdstr.encode('utf-8')).hexdigest())

@BOT.on_message(Filters.command("toSHA256", ".") & Filters.me)
def format_blank(bot: BOT, message: Message):
        try:
            cmdstr = " ".join(message.command[1:])
        except IndexError:
            message.edit("__I can't...__")
            sleep(2)
            message.delete()
            return

        message.edit(hashlib.sha256(cmdstr.encode('utf-8')).hexdigest())

@BOT.on_message(Filters.command("toSHA384", ".") & Filters.me)
def format_blank(bot: BOT, message: Message):
        try:
            cmdstr = " ".join(message.command[1:])
        except IndexError:
            message.edit("__I can't...__")
            sleep(2)
            message.delete()
            return

        message.edit(hashlib.sha384(cmdstr.encode('utf-8')).hexdigest())

@BOT.on_message(Filters.command("toSHA1", ".") & Filters.me)
def format_blank(bot: BOT, message: Message):
        try:
            cmdstr = " ".join(message.command[1:])
        except IndexError:
            message.edit("__I can't...__")
            sleep(2)
            message.delete()
            return

        message.edit(hashlib.sha1(cmdstr.encode('utf-8')).hexdigest())

@BOT.on_message(Filters.command("toSHA224", ".") & Filters.me)
def format_blank(bot: BOT, message: Message):
        try:
            cmdstr = " ".join(message.command[1:])
        except IndexError:
            message.edit("__I can't...__")
            sleep(2)
            message.delete()
            return

        message.edit(hashlib.sha224(cmdstr.encode('utf-8')).hexdigest())

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

@BOT.on_message(Filters.command("rot", ".") & Filters.me)
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

        if message == reply:
            replacelist = cmdstr.split(";")
            replytext = rot(replacelist[0])(replacelist[1])
            reply.edit(replytext)
        else:
            replytext = rot(int(cmdstr))(reply.text)
            reply.edit(replytext)
            message.delete()
