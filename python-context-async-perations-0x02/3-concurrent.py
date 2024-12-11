#!/bin/env python3

import asyncio
import aiosqlite

async def async_fetch_users():
   async with aiosqlite.connect("airbnb.db") as db:
       print("Getting All Users")
       await db.execute("SELECT * FROM users;")

async def async_fetch_older_users():
   async with aiosqlite.connect("airbnb.db") as db:
       print("Getting Users Older than 40")
       await db.execute("SELECT * FROM users WHERE age>40;")

async def fetch_concurrently():
    await asyncio.gather(async_fetch_users(), async_fetch_older_users())

asyncio.run(fetch_concurrently())
