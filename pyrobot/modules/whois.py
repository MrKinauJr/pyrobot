from time import sleep
from datetime import datetime

from pyrogram import Filters, Message, User
from pyrogram.errors import PeerIdInvalid
from pyrogram.api import functions
from pyrobot import BOT

# -- Constants -- #

WHOIS = (
    "**WHO IS \"{full_name}\"?**\n"
    "[Link to profile](tg://user?id={user_id})\n"
    "════════════════\n"
    "UserID: `{user_id}`\n"
    "First Name: `{first_name}`\n"
    "Last Name: `{last_name}`\n"
    "Username: `{username}`\n"
    "Last Online: `{last_online}`\n"
    "Common Groups: `{common_groups}`\n"
    "════════════════\n"
    "Bio:\n{bio}")
WHOIS_PIC = (
    "**WHO IS \"{full_name}\"?**\n"
    "[Link to profile](tg://user?id={user_id})\n"
    "════════════════\n"
    "UserID: `{user_id}`\n"
    "First Name: `{first_name}`\n"
    "Last Name: `{last_name}`\n"
    "Username: `{username}`\n"
    "Last Online: `{last_online}`\n"
    "Common Groups: `{common_groups}`\n"
    "════════════════\n"
    "Profile Pics: `{profile_pics}`\n"
    "Last Updated: `{profile_pic_update}`\n"
    "════════════════\n"
    "Bio:\n{bio}")

# -- Constants End -- #

# -- Helpers -- #


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


def LastOnline(user: User):
    if user.is_bot:
        return ""
    elif user.status.recently:
        return "Recently"
    elif user.status.within_week:
        return "Within the last week"
    elif user.status.within_month:
        return "Within the last month"
    elif user.status.long_time_ago:
        return "A long time ago :("
    elif user.status.online:
        return "Currently Online"
    elif user.status.offline:
        return datetime.fromtimestamp(user.status.date).strftime("%a, %d %b %Y, %H:%M:%S")


def GetCommon(get_user):
    common = BOT.send(
        functions.messages.GetCommonChats(
            user_id=BOT.resolve_peer(get_user),
            max_id=0,
            limit=0))
    return common


def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


def ProfilePicUpdate(user_pic):
    return datetime.fromtimestamp(user_pic.photos[0].date).strftime("%d.%m.%Y, %H:%M:%S")

# -- Helpers End -- #


@BOT.on_message(Filters.command("whois", ".") & Filters.me)
def who_is(bot: BOT, message: Message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif message.reply_to_message and len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = BOT.get_users(get_user)
    except PeerIdInvalid:
        message.edit("I don't know that User.")
        sleep(2)
        message.delete()
        return
    desc = BOT.get_chat(get_user).description
    user_pic = BOT.get_user_profile_photos(user.id)
    common = GetCommon(user.id)

    if not user.photo:
        message.edit(
            WHOIS.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "",
                username=user.username if user.username else "",
                last_online=LastOnline(user),
                common_groups=len(common.chats),
                bio=desc if desc else "`No bio set up.`"),
            disable_web_page_preview=True)
    elif user.photo:
        BOT.send_photo(
            message.chat.id,
            user_pic.photos[0].sizes[-1].file_id,
            WHOIS_PIC.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "",
                username=user.username if user.username else "",
                last_online=LastOnline(user),
                profile_pics=user_pic.total_count,
                common_groups=len(common.chats),
                bio=desc if desc else "`No bio set up.`",
                profile_pic_update=ProfilePicUpdate(user_pic)),
            reply_to_message_id=ReplyCheck(message))
        message.delete()
