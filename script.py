#!/usr/bin/env python3

import random
import pickle
import asyncio
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from config import api_id, api_hash
import subprocess
import textwrap
import os

app = Client('admin', api_id, api_hash)
app.start()
app.stop()
os.system("clear")
print("Type /help to see the full list of commands")

# help
@app.on_message(filters.command("help", prefixes="/") & filters.me)
async def valentine(app, msg):
    await msg.edit(f'''
<b>/help</b>   - print help msg.
<b>/version</b>   - print version.
<b>/love[1..2]</b>   - love msg.
<b>/spam [int] [str]...</b>   - text spammer.
<b>/system</b>   - print shell cmd.
    ''')
# help

# version
@app.on_message(filters.command("version", prefixes="/") & filters.me)
async def valentine(app, msg):
    await msg.edit(f'1.0-betta @jzinferno')
# version

# love1
@app.on_message(filters.command("love1", prefixes="/") & filters.me)
def valentine(_, msg):
    try:
        msg.edit(f'🧡 🧡')
        sleep(0.3)
        msg.edit(f'💛 I 💛')
        sleep(0.4)
        msg.edit(f'💚 I l 💚')
        sleep(0.3)
        msg.edit(f'💙 I lo 💙')
        sleep(0.3)
        msg.edit(f'💜 I lov 💜')
        sleep(0.3)
        msg.edit(f'🧡 I love 🧡')
        sleep(0.4)
        msg.edit(f'💛 I love y 💛')
        sleep(0.3)
        msg.edit(f'💚 I love yo 💚')
        sleep(0.3)
        msg.edit(f'💙 I love you 💙')
        sleep(0.3)
        msg.edit(f'💜 I love you! 💜')
        sleep(0.8)
        msg.edit(f'😘😘 I love you !!! 😘😘')
    except:
        pass
# love1

# spam
@app.on_message(filters.command("spam", prefixes="/") & filters.me)
def spam(app, msg):
    spams = 0
    while spams < int(msg.command[1]):
        sleep(0.01)
        app.send_message(msg.chat.id, " ".join(msg.command[2:]))
        spams = spams + 1
# spam

# system
@app.on_message(filters.command("system", prefixes="/") & filters.me)
async def valentine(app, msg):
    await msg.edit(subprocess.check_output(msg.command[1:]).decode('utf-8').strip())
# system

# love2
@app.on_message(filters.command("love2", prefixes="/") & filters.me)
def valentine(_, msg):
    try:
        msg.edit(f'loading ...')
        sleep(0.9)
        msg.edit(f'🤍🤍🤍🤍🤍🤍🤍🤍')
        sleep(0.5)
        msg.edit(f'💜🤍🤍🤍🤍🤍🤍🤍')
        sleep(0.5)
        msg.edit(f'💜💜🤍🤍🤍🤍🤍🤍')
        sleep(0.5)
        msg.edit(f'💜💜💜🤍🤍🤍🤍🤍')
        sleep(0.5)
        msg.edit(f'💜💜💜💜🤍🤍🤍🤍')
        sleep(0.5)
        msg.edit(f'💜💜💜💜💜🤍🤍🤍')
        sleep(0.5)
        msg.edit(f'💜💜💜💜💜💜🤍🤍')
        sleep(0.5)
        msg.edit(f'💜💜💜💜💜💜💜🤍')
        sleep(0.5)
        msg.edit(f'💜💜💜💜💜💜💜💜')
        sleep(0.9)
        msg.edit(f'🥰🥰 I love you !!! 🥰🥰')
    except:
        pass
# love2

app.run()
