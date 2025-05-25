#!/usr/bin/env python3
import asyncio
import aiosqlite


async def async_fetch_users():
    """Fetch all users from the users table."""
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()


async def async_fetch_older_users():
    """Fetch users older than 40 from the users table."""
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()


async def fetch_concurrently():
    """Run both queries concurrently and print the results."""
    results = await asyncio.gather(async_fetch_users(), async_fetch_older_users())
    print(results)
    return results


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
