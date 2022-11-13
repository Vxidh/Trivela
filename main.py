import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import asyncio
import json
from understat import Understat
import aiohttp
import PySimpleGUI as psg
import mysql.connector as msc
def database_ls(n): #Overall League stats
    dub = msc.connect(host='localhost',username='root',password='sql123')
    cursor=dub.cursor()
    cursor.execute('create database if not exists expectedgoals;')
    cursor.execute('use expectedgoals;')

    cursor.execute('drop table if exists league_stats;')
    cursor.execute('create table league_stats\
                    (league_id varchar(20) primary key, league_name varchar(20), h varchar(30), a varchar(30), hxg varchar(30), axg varchar(30)\
                    year varchar(10), month varchar(10), matches varchar(20));')
    
    for i in n:
        cursor.execute("insert into table league_stats(%s,%s,%s,%s,%s,%s,%s,%s,%s);",(i['league_id'],i['league'],i['h'],i['a'],i['hxg'],i['axg'],i['year'],i['month'],\
            i['matches']))

def database_lt(n): #League Table 
    dub = msc.connect(host='localhost',username='root',password='sql123')
    cursor=dub.cursor()
    cursor.execute('create database if not exists expectedgoals;')
    cursor.execute('use expectedgoals;')

    cursor.execute('drop table if exists league_table;')
    cursor.execute('create table league_table\
                    (Team varchar(20), Matches varchar(20), Wins varchar(10), Draws varchar(10), Defeats varchar(10), Goals Scored varchar(10), Goals scored against varchar(10),\
                        Points varchar(20), Expected Goals varchar(20), Expected Goals Against varchar(20), Expected Points varchar(20));')

    for i in (n):
        cursor.execute('insert into table league_table(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))

def database_td(n): #Team Data
    dub = msc.connect(host='localhost',username='root',password='sql123')
    cursor=dub.cursor()

    cursor.execute('create database if not exists expectedgoals;')
    cursor.execute('use expectedgoals;')
    cursor.execute('drop table if exists team_data')
    cursor.execute('create table team_data\
                    (id varchar(4) primary key, player_name varchar(30) not null, games varchar(20), time varchar(20),goals varchar(20),xG varchar(20),\
                    assists varchar(20), xA varchar(20), shots varchar(20), key_passes varchar(20), yellow_cards varchar(20), red_cards varchar(20));')
    for i in n:
        cursor.execute("insert into table team_data(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(i['id'],i['player_name'],i['games'],i['time'],i['xG'],i['assists'],i['xA'],\
                        i['shots'],i['key_passes'],i['yellow_cards'],i['red_cards']))

def league_stats(l,m): #Understat for league data
    async def main():
            async with aiohttp.ClientSession() as session:
                understat = Understat(session)
                data = await understat.get_stats({"league": l, "month": m})
                d=json.dumps(data)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

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

def team_data(n,y,t): #Understat for team data
    async def main():
            async with aiohttp.ClientSession() as session:
                understat = Understat(session)
                data = await understat.get_league_players(n, y, team_title=t)
                print(json.dumps(data))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
 
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
        if events1 in (None, 'Quit'):
            break
        else:
            team_data('epl',int(values1['year']),values1['team'])

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
        if events1 in (None, 'Quit'):
            break
        else:
            team_data('La Liga',int(values1['year']),values1['team'])

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
        if events1 in (None, 'Quit'):
            break
        else:
            team_data('Bundesliga',int(values1['year']),values1['team'])

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
        if events1 in (None, 'Quit'):
            break
        else:
            team_data('Serie A',int(values1['year']),values1['team'])

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
        if events1 in (None, 'Quit'):
            break
        else:
            team_data('Ligue 1',int(values1['year']),values1['team'])

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
        if events1 in (None, 'Quit'):
            break
        else:
            team_data('RFPL',int(values1['year']),values1['team'])


def TeamData_Window():
    psg.theme('DarkPurple4')

    tdlayout=[[psg.Text('Choose your preferred League',size=(25,1),font='Georgia',justification='left')],
            [psg.Button('EPL', font=('Times New Roman',12)),psg.Button('La Liga', font=('Times New Roman',12)),
            psg.Button('Bundesliga', font=('Times New Roman',12)),psg.Button('Serie A', font=('Times New Roman',12)),
            psg.Button('Ligue 1', font=('Times New Roman',12)),psg.Button('RFPL', font=('Times New Roman',12))],
            [psg.Button('QUIT',font=('Georgia',12))]]
    
    TDwin=psg.Window('Team Data',tdlayout)
    while True:
        event, values = TDwin.read()
        if event == 'QUIT':
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

def LeagueStats_Window():
    lslayout=[[psg.Text('Choose your preferred League',size=(25,1),font='Georgia',justification='left')],
        [psg.Combo(['EPL','La Liga','Ligue 1', 'Serie A','RFPL'],key='team')],
        [psg.Text('Choose your preferred month: ',size=(25,1),font='Georgia',justification='left')],
        [psg.Combo(['1','2','3', '4','5','6','7','8','9','10','11','12'],key='month')],
        [psg.Button('CONTINUE',font=('Georgia',12)), psg.Button('QUIT',font=('Georgia',12))]
    ]
    LSwin=psg.Window('League Stats',lslayout)

    while True:
        event,values = LSwin.read()
        if event == 'QUIT':
            break
        elif event == 'CONTINUE':
            league_stats(values['team'],values['month'])

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

def MainWindow():
    psg.theme('DarkBlue')
    main_layout=[[psg.Image('MainLogo.png')],
    [psg.Text('Click any button to go ahead')],
    [psg.Button('TEAM DATA', font=('Times New Roman',13)), psg.Button('LEAGUE STATS', font=('Times New Roman',13))],
    [psg.Button('LEAGUE STANDINGS',font=('Times New Roman',13))],
    [psg.Button('QUIT',font=('Times New Roman',13))]]

    main_window = psg.Window('Trivela', main_layout, size=(500,500))

    while True:
        event, values = main_window.read()
        if event in (None, 'QUIT'):
            break
        elif event == 'LEAGUE DATA':
            LeagueStats_Window()
        elif event == 'TEAM DATA':
            TeamData_Window()
        elif event == 'LEAGUE STANDINGS':
            LeagueTable_Window

MainWindow()