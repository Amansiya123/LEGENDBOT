from datetime import datetime

from telethon import Button

from userbot import Config, legend

from ..core.logger import logging
from ..sql_helper.bot_blacklists import check_is_black_list
from ..sql_helper.globals import gvarstatus

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME


@legend.bot_cmd(
    pattern=f"^/ping({botusername})?([\s]+)?$",
    incoming=True,
)
async def bot_start(event):
    chat = await event.get_chat()
    await legend.get_me()
    if check_is_black_list(chat.id):
        return
    GOOD = [[Button.url("⚜ Lêɠêɳ̃dẞø† ⚜", "https://t.me/LegendBot_XD")]]
    LEGEND_IMG = gvarstatus("BOT_PING_PIC")
    start = datetime.now()
    await event.client.send_file(
        event.chat_id, LEGEND_IMG, caption="Checking LegendBot Ping...", buttons=GOOD
    )
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    LegendBoy = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{mention}』"
    await event.client.edit_message(
        event.chat_id, LEGEND_IMG, caption=LegendBoy, buttons=GOOD
    )
