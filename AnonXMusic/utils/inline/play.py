import math
import asyncio
from pyrogram.types import InlineKeyboardButton

from AnonXMusic.utils.formatters import time_to_seconds

async def stream_markup_timer(_, chat_id, played_time, duration):
    duration = await time_to_seconds(duration)
    played_time = await time_to_seconds(played_time)
    if duration <= 0:
        return [[]]

    current_time = (played_time / duration) * 100
    empty_progress = "▭"
    filled_progress = "▬"

    progress_bar_length = 15
    progress_bar = filled_progress * round(current_time * progress_bar_length / 100) + empty_progress * (
        progress_bar_length - round(current_time * progress_bar_length / 100)
    )

    markup = [
        [
            InlineKeyboardButton(
                text=f"{progress_bar} {current_time:.2f}%",
                callback_data=f"ADMIN Skip|{chat_id}",
            ),
            InlineKeyboardButton(text="Stop 🔇", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="Close ❌", callback_data="close ❌")],
    ]
    return markup

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="Button 1",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="Button 2",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Close ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="Skip ▶️", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="Queue", callback_data=f""),
            InlineKeyboardButton(text="Stop 🔇", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="Settings ⚙️", callback_data=f"SETTINGS|{chat_id}")],
        [InlineKeyboardButton(text="Close ❌", callback_data="close ❌")],
    ]
    return buttons

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="audio",
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="video",
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Close ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="Close ❌",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons

def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text="Button 1",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="Button 2",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Back🔙",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="Close ❌",
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="Next⏭️",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

