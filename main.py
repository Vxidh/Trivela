import asyncio
import json
from understat import Understat
import aiohttp
import PySimpleGUI as psg
#set the theme for the screen/window
psg.theme('SandyBeach')
#Defining the layout of the window
layout=[[psg.Text('Choose Year',size=(20, 1), font='Lucida',justification='left')],
        [psg.Combo(['2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
        [psg.Text('Choose Team',size=(30, 1), font='Lucida',justification='left')],
        #psg.combo gives you a drop-down list
        [psg.Combo(['Arsenal','Manchester City','Tottenham', 'Newcastle United','Chelsea','Manchester United','Fulham',
        'Liverpool','Brighton','West Ham','Brentford','Everton','Crystal Palace','Bournemouth',
        'Aston Villa','Southampton','Leicester','Leeds','Wolverhampton Wanderers','Nottingham Forest'],key='team')], #Teams playing in the Premier League
        [psg.Text('Choose additional Facilities',size=(30, 1), font='Lucida',justification='left')],
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]] #Save button and cancel button
#Function to get data from understat
def team_data():
    async def main():
            async with aiohttp.ClientSession() as session:
                understat = Understat(session)
                data = await understat.get_league_players("epl", v['year'], team_title= v['team'])
                print(json.dumps(data))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
#Define Window
win =psg.Window('Expected Goals',layout)
#Read  values entered by user
e,v=win.read()
if e == psg.WINDOW_CLOSED or e == 'Quit':
        win.close()
else:
        win.close()
        team_data()




