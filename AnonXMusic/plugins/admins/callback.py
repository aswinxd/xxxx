import asyncio

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonXMusic import YouTube, app
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import SUDOERS, db
from AnonXMusic.utils.database import (
    get_active_chats,
    get_lang,
    get_upvote_count,
    is_active_chat,
    is_music_playing,
    is_nonadmin_chat,
    music_off,
    music_on,
    set_loop,
)
from AnonXMusic.utils.decorators.language import languageCB
from AnonXMusic.utils.formatters import seconds_to_min
from AnonXMusic.utils.inline import close_markup, stream_markup
from AnonXMusic.utils.stream.autoclear import auto_clean
from AnonXMusic.utils.thumbnails import get_thumb
from config import (
    BANNED_USERS,
    SOUNCLOUD_IMG_URL,
    STREAM_IMG_URL,
    TELEGRAM_AUDIO_URL,
    TELEGRAM_VIDEO_URL,
    adminlist,
    confirmer,
    votemode,
)
from strings import get_string

checker = {}
upvoters = {}


@app.on_callback_query(filters.regex("ADMIN") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    # The existing callback function code remains unchanged

async def markup_timer():
    while not await asyncio.sleep(7):
        active_chats = await get_active_chats()
        for chat_id in active_chats:
            try:
                if not await is_music_playing(chat_id):
                    continue
                playing = db.get(chat_id)
                if not playing:
                    continue
                duration_seconds = int(playing[0]["seconds"])
                if duration_seconds == 0:
                    continue
                try:
                    mystic = playing[0]["mystic"]
                except:
                    continue
                try:
                    language = await get_lang(chat_id)
                    _ = get_string(language)
                except:
                    _ = get_string("en")
                try:
                    buttons = stream_markup(
                        _,
                        chat_id,
                    )
                    await mystic.edit_reply_markup(
                        reply_markup=InlineKeyboardMarkup(buttons)
                    )
                except:
                    continue
            except:
                continue

asyncio.create_task(markup_timer())
