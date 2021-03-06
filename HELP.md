# PyroBot - A help page

## General Information

This program is a Userbot for the [Telegram Messenger](https://telegram.org) based on [Pyrogram](https://github.com/pyrogram/pyrogram).

## Features

* Check if your bot is running with `.alive` or `.up`
* Mute, kick or ban people
* Convert video files from any format to Telegram Gif (.mp4)
* Evaluate and Execute code with `.eval` and `.exec`
* Get information about your admins and members, as well as files.
* Annoy people with memes (:
* Get a blank steam account with `?acc`
* Check Information about a user with `.whois`. Works with Username, Userid and by reply.
* Test your servers (or PCs) speed and ping your connection to Telegram servers.
* Send your videonotes as a replacement for GIFs
* Greet new people with custom welcome messages

### First Commands (`1start.py`)

| Command | Action |
|---|---|
| `.alive` | Tells you that the bot is running |
| `.help` | Gives out a link to this document |

### Administration (`admin.py`)

| Command | Action |
|---------|--------|
| `?ban x` | Bans a replied-to user for time `x` |
| `?unban` | Unbans a replied-to user |
| `?mute x` | Mutes a replied-to user for time `x` |
| `?unmute` | Unmutes a replied-to user |
| `?kick` | Kicks a replied-to user |
| `!cclean` | Remove Deleted Accounts from your chat |

With the exception of `!cclean`, the above commands only work in reply.

Timed restrictions can be applied in the following scheme:

* `1d` - 1 day
* `2h` - 2 hours
* `3w` - 3 weeks

**Note:** Only one of those will work at a time. You cannot combine those.

### Converting (`cloudconvert.py`)

* `!conv <url>` - Convert the given Url to an animation fit for Telegram.

### Evaluation (`evaluation.py`)

Evaluate and Execute whithin Telegram

| Command | Description |
|---|---|
| `.eval <query>` | Evaluate a string of x (e.g. `message.chat.title` for chat title) |
| `.exec <query>` | Execute a string of x.* |

***Note:** Using `.eval` for `from_user` or `send_*` attributes/methods is NOT recommended as you might expose your phone number unwillingly.

### Information (`get_info.py`)

Get information about your administration, members of your chat and all your chats.

| Command | Description |
|---------|-------------|
| `!admins` | Gives out a list of all admins in a chat. |
| `!members` | Gives out counter of all members, bots and deleted accounts in that group. |
| `.id` | Gives out the File ID of a replied-to media. If there is neither a media nor a reply it will be the Chat ID. |
| `!chats` | Get an overview on how many chats you have in groups, supergroup, with bots, etc. |
| `!unread` | Get an overview on unread messages, mentions and chats marked as unread |

### Memes (`memes.py`)

| Command | Description | Source |
|---------|-------------|--------|
| `dog`, 🐕, 🐶, 🐩 | Sends an image of a dog 🐶🐕 | [random.dog](https://random.dog/)[*](https://github.com/AdenFlorian/random.dog#api) |
| `cat`, `:cat:`, 🐱| Sends an image of a cat 🐱🐱 | [random.cat](https://random.cat/) |
| `.mock` | Send mocking Spongebob 🧽 | [@Stickerizerbot](https://t.me/Stickerizerbot) |
| `.ggl` | Send a Google Search 🔍 | Same as `.mock` |

### Random (`randomness.py`)

| Command | Description | Source |
|---------|-------------|--------|
| `.random` <leastAmount> <biggestAmount> | A random Number betweet set Numbers |
| `person`, `:person:`, 👨‍ Sends an image of a Person 👨‍👨‍ | [thispersondoesnotexist.com](https://thispersondoesnotexist.com/) |

### Hastebin (`haste.py`)

| Command | Description |
|---------|-------------|
| `.haste` <something you want to paste> | Pasting something to Hastebin.com |
 
### Miscellaneous (`misc.py`)

* `.up` - Gives out the current uptime of the bot.

### Steam (`steam.py`)

* `?steam` - Gives a clean Steam Account

### Videonotes (`videonotes.py`)

Save and send videontoes with these commands.

| Command | Description |
|---------|-------------|
| `.savenote x` | Save a video as a videonote with name `x` |
| `.rmnote x` | Remove a videonote with name `x` |
| `.note x` | Send a videonote with name `x` |
| `.notes` | Send a list of all saved videonotes to your Saved Messages |

**Note:** Videos have to have an aspect ratio of 1:1 to be saved as a Videonote.

### Welcome Messages (`welcome.py`)

Greet new people who join your chat or get invited.

| Command | Description |
|---------|-------------|
| `.setwelcome <text>` | Set a new welcome message or overwrite an existing one with the given `<text>` |
| `.rmwelcome` | Remove the currently set welcome message |
| `.welcome` | Check the chats welcome message |
| `!welcome` | Get welcome messages of all chats in your Saved Messages |

There are some supported replacements:

| Variable     | Replacement                                    |
|--------------|------------------------------------------------|
| `{title}`    | Current Chat Title                             |
| `{name}`     | Name of the new member                         |
| `{namelink}` | Name of the new member linked to their profile |

### Who Is ...? (`whois.py`)

* `.whois` - Gives out information about a user

### World Wide Web (`www.py`)

| Command | Description |
|---------|-------------|
| `.speed` | Run a speedtest |
| `.dc` | Give out information about the closest Telegram Datacenter to you |
| `.ping` | Milliseconds between two instant edits (The latency to Telegram) |
