# MIT License
#
# Copyright (c) 2023 CyTheWorker
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import logging
import os
import sys

import discord

import jotobot


async def main() -> None:
    standard = logging.Formatter(
        fmt=r"%(asctime)s %(levelname)-8s %(message)s",
        datefmt=r"%d/%m/%Y %H:%M:%S",
        validate=True
    )

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(standard)

    logger = logging.getLogger("jotobot")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console)


    if (token := os.environ.get("DISCORD_TOKEN")) is None:
        logger.critical("DISCORD_TOKEN not found")
        sys.exit(1)

    intents = discord.Intents(
        guilds=True,
        members=True,
        messages=True,
        message_content=True
    )

    async with jotobot.Bot(
        command_prefix="/",
        case_insensitive=True,
        intents=intents
    ) as bot:
        for extension in ("event", "owner"):
            await bot.load_extension(f"jotobot.extension.{extension}")

        await bot.start(token)


asyncio.run(main())