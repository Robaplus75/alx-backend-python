#!/bin/env python3

import asyncio
import aiosqlite

async def async_fetch_users():
   async with aiosqlite.connect("airbnb.db") as db:
       print("Getting All Users")
       async with db.execute("SELECT * FROM users;") as cursor:
           async for row in cursor:
               print(row)

async def async_fetch_older_users():
   async with aiosqlite.connect("airbnb.db") as db:
       print("Getting Users Older than 40")
       async with db.execute("SELECT * FROM users WHERE age>40;") as cursor:
           async for row in cursor:
               print(row)

async def fetch_concurrently():
    return await asyncio.gather(async_fetch_users(), async_fetch_older_users())

asyncio.run(fetch_concurrently())
