"""
https://understat.readthedocs.io/en/latest/classes/understat.html#the-functions
https://www.fantasyfootballfix.com/blog-index/how-we-calculate-expected-goals-xg/

"""


import asyncio
import json

import aiohttp

from understat import Understat
from bs4 import BeautifulSoup
with open("https://fbref.com/en/comps/9/Premier-League-Stats") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print(BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))

# async def main():
#     async with aiohttp.ClientSession() as session:
#         understat = Understat(session)
#         data = await understat.get_league_players("epl", 2018, {"team_title": "Manchester City"})
#         print(json.dumps(data))


# if __name__ == "__main__":
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(main())