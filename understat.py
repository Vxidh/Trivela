import asyncio
import json

import aiohttp

from understat import Understat
async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        data = await understat.get_league_players("epl", 2018, {"team_title": "Manchester City"})
        print(json.dumps(data))


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())