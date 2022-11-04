'''
Changes needed: 1) Need to add SQL interface
NOTES: 1) understat returns data in the form of a list with dictionaries as the elements
       2) keys are: 'id', 'player_name', 'games', 'time', 'goals', 'xG', 'assists', 'xA', 'shots', 'key_passes', 'yellow_cards',
       'red_cards', 'position', 'npg', 'npxG', 'xGchain', 'xGbuildup', 
       3) Might need to add ASCII library to accomodate for the spanish characters in player names
       4) Runs on python 3.7 only
'''
import asyncio
import json
from understat import Understat
import aiohttp
import PySimpleGUI as psg
def team_data(n,y,t):
    async def main():
            async with aiohttp.ClientSession() as session:
                understat = Understat(session)
                data = await understat.get_league_players(n, y, team_title=t)
                print(json.dumps(data))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
psg.theme('DarkPurple4')
layout=[[psg.Text('Choose your preferred League',size=(25,1),font='Georgia',justification='left')],
        [psg.Button('EPL', font=('Times New Roman',12)),psg.Button('La Liga', font=('Times New Roman',12)),
        psg.Button('Bundesliga', font=('Times New Roman',12)),psg.Button('Serie A', font=('Times New Roman',12)),
        psg.Button('Ligue 1', font=('Times New Roman',12)),psg.Button('RFPL', font=('Times New Roman',12))],
        [psg.Button('QUIT',font=('Georgia',12))]]
def EPL_window():
    psg.theme('LightBlue')
    layout_=[[psg.Text('Welcome to the English Premier League')],
            [psg.Text('Choose the year and team data from below')],
            [psg.Combo(['Arsenal','Manchester City','Tottenham', 'Newcastle United','Chelsea','Manchester United','Fulham',
            'Liverpool','Brighton','West Ham','Brentford','Everton','Crystal Palace','Bournemouth',
            'Aston Villa','Southampton','Leicester','Leeds','Wolverhampton Wanderers','Nottingham Forest'],key='team')],
            [psg.Combo(['2014','2015','2016','2017','2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('Quit', font=('Times New Roman',12))]
            ]

    eplw=psg.Window('English Premier League',layout_)
    
    while True:
        events1, values1=eplw.read()
        team_data('epl',int(values1['year']),values1['team'])
        if events1 in (None, 'Quit'):
            break
def LaLiga_Window():
    psg.theme('HotDogStand')
    layout_=[[psg.Text('Hola! Bienvenido a la liga')],
            [psg.Text('Choose your team')],
            [psg.Combo(['Real Madrid','Barcelona','Atletico Madrid','Real Betis','Real Sociedad','Athletic Club','Osasuna','Villareal',
            'Rayo Vallecano','Valencia','Real Valladolid','Mallorca','Almeria','Getafe','Espanyol','Celta Vigo','Girona','Sevilla','Cadiz',
            'Elche'],key='team')],
            [psg.Text('Choose year')],
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('Quit', font=('Times New Roman',12))]]
    
    lalw=psg.Window('La Liga',layout_)
    while True:
        events1, values1=lalw.read()
        team_data('La Liga',int(values1['year']),values1['team'])
        if events1 in (None, 'Quit'):
            break

def Bundes_Window():
    psg.theme('DarkBrown4')
    layout_=[[psg.Text('Hallo! Willkommen in der Bundesliga')],
            [psg.Text('Choose your team')],
            [psg.Combo(['Union Berlin','Bayern Munich','Freiburg','Borussia Dortmund','Eintracht Frankfurt','RasenBallsport Leizpig',
            'Hoffenheim','Werder Bremen','Mainz 05','FC Cologne','Borussia M.Gladbach','Wolfsburg','Augsburg',
            'Hertha Berlin','VfB Stuttgart','Bayer Leverkusen','Bochum','Schalke 04'],key='team')],
            [psg.Text('Choose year')]
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('Quit', font=('Times New Roman',12))]]
    bundw=psg.Window('La Liga',layout_)
    while True:
        events1, values1=bundw.read()
        team_data('Bundesliga',int(values1['year']),values1['team'])
        if events1 in (None, 'Quit'):
            break

def SerieA_Window():
    psg.theme('DarkTeal7')
    layout_=[[psg.Text('Ciao! Benvenuto alla Serie A')],
            [psg.Text('Choose your team')],
            [psg.Combo(['Napoli','Atalanta','AC Milan','Roma','Lazio','Inter',
            'Juventus','Udinese','Torino','Salernitana','Sassuolo','Bologna','Fiorentina',
            'Empoli','Monza','Spezia','Lecce','Sampdoria','Verona','Cremonese'],key='team')],
            [psg.Text('Choose year')],
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('Quit', font=('Times New Roman',12))]]
    seriaw=psg.Window('La Liga',layout_)
    while True:
        events1, values1=seriaw.read()
        team_data('Serie A',int(values1['year']),values1['team'])
        if events1 in (None, 'Quit'):
            break

def Ligue1_Window():
    psg.theme('DarkTeal')
    layout_=[[psg.Text('Bonjour! Bienvenue en ligue 1')],
            [psg.Text('Choose your team')],
            [psg.Combo(['Paris Saint Germain','Lens','Rennes','Lorient','Marseille','Monaco',
            'Lille','Lyon','Clermont Foot','Nice','Toulouse','Troyes','Reims',
            'Montpellier','Nantes','Auxerre','Strasbourg','Brest','Ajaccio','Angers'],key='team')],
            [psg.Text('Choose year')],
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('Quit', font=('Times New Roman',12))]]
    ligue1w=psg.Window('La Liga',layout_)
    
    while True:
        events1, values1=ligue1w.read()
        team_data('Ligue 1',int(values1['year']),values1['team'])
        if events1 in (None, 'Quit'):
            break

def RFPL_Window():
    psg.theme('DarkRed1')
    layout_=[[psg.Text('Privet! Dobro pozhalovat v RFPL')],
            [psg.Text('Choose your team')],
            [psg.Combo(['Zenit St. Petersburg','Spartak Moscow','CSKA Moscow','FC Rostov','Dinamo Moscow','FC Krasnodar',
            'FK Akhmat','FC Orenburg','PFC Sochi','Krylya Sovetov Samara','Ural','Nizhny Novgorod','Fakel',
            'Lokomotiv Moscow','Khimki','Torpedo Moscow'],key='team')],
            [psg.Text('Choose year')],
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('Quit', font=('Times New Roman',12))]]
    rfplw=psg.Window('La Liga',layout_)
    while True:
        events1, values1=rfplw.read()
        team_data('RFPL',int(values1['year']),values1['team'])
        if events1 in (None, 'Quit'):
            break



window = psg.Window('The Footballer', layout, size=(500, 200))

while True:
    event, values = window.read()
    if event in (None, 'Quit'):
        break
    elif event == 'EPL':
        EPL_window()
    elif event == 'La Liga':
        LaLiga_Window()
    elif event == 'Bundesliga':
        Bundes_Window()
    elif event == 'Serie A':
        SerieA_Window()
    elif event == 'Ligue 1':
        Ligue1_Window()
    elif event == 'RFPL':
        RFPL_Window()
    

window.close()





