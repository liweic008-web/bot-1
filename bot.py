import os
import asyncio
import discord
from datetime import datetime
import pytz

# 從 GitHub Secrets 中安全讀取變數
TOKEN = os.getenv('MTUyNzY3OTE0MDI2MDc0MTM3MA.GaoP9J.Vu9gtrzprfTaMkKj3PZUvy6tv_PcJE48RnI0Mo')
CHANNEL_ID = 1505906187495800942

def get_weekly_status(day_index):
    days_text = [
        "月曜日：会社行きたくない",
        "火曜日：会社行きたくない",
        "水曜日：会社行きたくない",
        "木曜日：会社行きたくない",
        "金曜日：やっと終わりそう",
        "土曜日：楽しいっ",
        "日曜日：会社行きたくない"
    ]
    days_text[day_index] += " ←今ここ"
    return "\n".join(days_text)

async def main():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f"機器人已登入: {client.user.name}")
        
        # 取得台北/香港時區的今天星期幾
        tz = pytz.timezone("Asia/Taipei")
        day_index = datetime.now(tz).weekday() # 0 = 週一, 6 = 週日
        
        channel = client.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(get_weekly_status(day_index))
            print("訊息發送成功！")
        else:
            print("找不到該頻道，請檢查 CHANNEL_ID 是否正確。")
            
        # 發完訊息後，立刻關閉連線，結束程式
        await client.close()

    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
