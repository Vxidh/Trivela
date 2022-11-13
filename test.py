import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import asyncio
import json
from understat import Understat
import aiohttp
import PySimpleGUI as psg
import mysql.connector as msc
my_img = psg.Image(filename='MainLogo.png', key='_CAMIMAGE_')
def LeagueTable_Window():
    ltlayout=[[psg.Text('Choose your preferred League',size=(25,1),font='Georgia',justification='left')],
        [psg.Combo(['EPL','La Liga','Ligue 1', 'Serie A','RFPL'],key='team')],
        [psg.Text('Choose your preferred month: ',size=(25,1),font='Georgia',justification='left')],
        [psg.Combo(['2014','2015','2016', '2017','2018','2019','2020','2021','2022'],key='year')],
        [psg.Button('CONTINUE',font=('Georgia',12)), psg.Button('QUIT',font=('Georgia',12))]]
    
    LTwin=psg.Window('League Table',ltlayout)

    while True:
        event,values = LTwin.read()
        if event == 'QUIT':
            break
        elif event == 'CONTINUE':
            league_table(values['team'],values['year'])
def league_table(l,s): #Understat for league standings
    async def main():
            async with aiohttp.ClientSession() as session:
                understat = Understat(session)
                data = await understat.get_league_table(l,s)
                for i in data:
                    i.pop(9)
                    del i[10:16]
                    print(i)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
LeagueTable_Window()