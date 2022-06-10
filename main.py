from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import functions
from config import api_id, api_hash
from time import sleep
import subprocess
import os

app = Client("admin", api_id=api_id, api_hash=api_hash)
os.system("clear")
print("Type /help to see the full list of commands")

@app.on_message(filters.command("help", prefixes=".") & filters.me)
async def help(_, msg):
    await msg.edit(f'<b>Help.</b>')


@app.on_message(filters.command("version", prefixes=".") & filters.me)
async def version(_, msg):
    await msg.edit(f'<b>1.0-betta <a href="https://github.com/jzinferno">jzinferno</a></b>')


@app.on_message(filters.command("audio", prefixes=".") & filters.me)
async def audio(_, msg):
    subprocess.run(['rm', '-rf', 'audio.mp3'])
    subprocess.run(['gtts-cli', ''.join(msg.command[2:]), '--lang', ''.join(msg.command[1]), '--nocheck', '--output', 'audio.mp3'])
    await app.send_audio(msg.chat.id, "audio.mp3", title="User Audio Bot", performer="jzinferno", thumb="fire.jpg")

app.run()
