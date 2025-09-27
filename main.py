import asyncio
from datetime import datetime
from rubpy import Client

async def change_group_title():
    async with Client("sina") as app:
        group_guid = "گوید گروه"
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            new_title = f"sina | {now}"
            await app.edit_group_info(group_guid, title=new_title)
            await asyncio.sleep(60)

asyncio.run(change_group_title())
#ساخته شده توسط @Sinabanis
