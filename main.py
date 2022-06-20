#!/usr/bin/env python3

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import functions
from config import api_id, api_hash
from gtts import gTTS
from time import sleep
import subprocess
import os

app = Client("admin", api_id=api_id, api_hash=api_hash)
os.system("clear")
print("Type /help to see the full list of commands")

@app.on_message(filters.command("help", prefixes=".") & filters.text)
async def help(_, msg):
    await msg.edit(f'<b>Help.</b>')


@app.on_message(filters.command("version", prefixes=".") & filters.text)
async def version(_, msg):
    await msg.edit(f'<b>1.0-betta <a href="https://github.com/jzinferno">jzinferno</a></b>')


@app.on_message(filters.command("audio", prefixes=".") & filters.text)
async def audio(_, msg):
    tts = gTTS(''.join(msg.command[2:]), lang=''.join(msg.command[1]))
    tts.save('audio.mp3')
    await app.send_audio(msg.chat.id, "audio.mp3", title="User Audio Bot", performer="jzinferno", thumb="fire.jpg")

@app.on_message(filters.command("spam", prefixes=".") & filters.text)
def spam(app, msg):
    spams = 0
    try:
        while spams < int(msg.command[1]):
            sleep(0.01)
            app.send_message(msg.chat.id, " ".join(msg.command[2:]))
            spams = spams + 1
    except FloodWait as e:
        sleep(e.x)

app.run()
