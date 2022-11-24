import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 
import asyncio
import aiohttp
import mysql.connector as msc
import PySimpleGUI as psg
from understat import Understat

Main_Logo=psg.Image(filename='MainLogo.png', key='_SUUUI_')
Premier_League=psg.Image(filename='PremierLeague.png', key='_HAALAND_')
La_Liga=psg.Image(filename='LaLiga.png',key='_LEWANDISNEY_')
Ligue1=psg.Image(filename='Ligue1.png',key='_MBAPPAYPAL_')
Bundesliga_Image=psg.Image(filename='Bundesliga.png',key='_SADIO_')
Serie_A=psg.Image(filename='SerieA.png',key='_DYBALA_')
RFPL_Image=psg.Image(filename='RFPL.png',key='_IRREVELANT_')

def database_ls(n): #Overall League stats
    dub = msc.connect(host='localhost',username='root',password='sql123')
    cursor=dub.cursor()
    cursor.execute('create database if not exists expectedgoals;')
    cursor.execute('use expectedgoals;')

    cursor.execute('drop table if exists league_stats;')
    cursor.execute('create table league_stats(league_id varchar(20), league_name varchar(20), h varchar(30), a varchar(30), hxg varchar(30), axg varchar(30),year varchar(10), month varchar(10), matches varchar(20));')
    
    for i in n:
        cursor.execute("insert into league_stats values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i['league_id'],i['league'],i['h'],i['a'],i['hxg'],i['axg'],i['year'],i['month'],\
            i['matches']))
    dub.commit()

def database_lt(n): #League Table 
    dub = msc.connect(host='localhost',username='root',password='sql123')
    cursor=dub.cursor()
    cursor.execute('create database if not exists expectedgoals;')
    cursor.execute('use expectedgoals;')

    cursor.execute('drop table if exists league_table;')
    cursor.execute('create table league_table (Team varchar(35), Matches varchar(20), Wins varchar(10), Draws varchar(10), Defeats varchar(10), GS varchar(10), GS_against varchar(10), Points varchar(20), xG varchar(20), xG_Against varchar(20), Expected_Points varchar(20))')

    for i in (n):
        cursor.execute('insert into league_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
    dub.commit()

def database_lf(n):
    dub = msc.connect(host='localhost',username='root',password='sql123')
    cursor=dub.cursor()
    cursor.execute('create database if not exists expectedgoals;')
    cursor.execute('use expectedgoals;')

    cursor.execute('drop table if exists league_fixtures')
    cursor.execute('create table league_fixtures (ID varchar(10), Result varchar(10), home varchar(45), away varchar(45), date_time varchar(30)')

    for i in (n):
        cursor.execute('insert into league_fixtures values(%s,%s,%s,%s,%s)',(i['id'], i['isResult'], i['h'], i['away'], i['date_time']))
    dub.commit()


def database_td(n): #SQL function for Team Data
    dub = msc.connect(host='localhost',username='root',password='sql123')
    cursor=dub.cursor()

    cursor.execute('create database if not exists expectedgoals;')
    cursor.execute('use expectedgoals;')
    cursor.execute('drop table if exists team_data')
    cursor.execute('create table team_data(id varchar(4), player_name varchar(30), games varchar(20), time varchar(20),goals varchar(20),xG varchar(20), assists varchar(20), xA varchar(20), shots varchar(20), key_passes varchar(20), yellow_cards varchar(20), red_cards varchar(20) )')
    for i in n:
        cursor.execute("insert into team_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i['id'],i['player_name'],i['games'],i['goals'],i['time'],i['xG'],i['assists'],i['xA'],i['shots'],i['key_passes'],i['yellow_cards'],i['red_cards']))
    dub.commit()

def league_fixtures(l):
    async def main():
            async with aiohttp.ClientSession() as session:
                understat = Understat(session)
                data = await understat.get_league_fixtures(l, int(2022))
                for i in data:
                    del data['goals']
                    del data['xG']
                
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

def league_stats(l,m): #Understat for league data and displaying the tables
    async def main():
            async with aiohttp.ClientSession() as session:
                understat = Understat(session)
                data = await understat.get_stats({"league": l, "month": str(m)})
                database_ls(data)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

def league_table(l,s): #Understat for league standings and displaying the tables
    async def main():
            async with aiohttp.ClientSession() as session:
                understat = Understat(session)
                data = await understat.get_league_table(l,s)
                for i in data:
                    i.pop(9)
                    del i[10:16]
                database_lt(data)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

def team_data(n,y,t): #Understat for team data and displaying the tables
    async def main():
            async with aiohttp.ClientSession() as session:
                understat = Understat(session)
                data = await understat.get_league_players(n, y, team_title=t)
                database_td(data)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
 
def EPL_window():
    psg.theme('LightBlue')
    layout_=[[psg.Column([[Premier_League]], justification='center')],
        [psg.Text('Welcome to the English Premier League')],
            [psg.Text('Choose the year and team data from below')],
            [psg.Combo(['Arsenal','Manchester City','Tottenham', 'Newcastle United','Chelsea','Manchester United','Fulham',
            'Liverpool','Brighton','West Ham','Brentford','Everton','Crystal Palace','Bournemouth',
            'Aston Villa','Southampton','Leicester','Leeds','Wolverhampton Wanderers','Nottingham Forest'],key='team')],
            [psg.Combo(['2014','2015','2016','2017','2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('QUIT', font=('Times New Roman',12))]
    ]

    eplw=psg.Window('English Premier League',layout_)
    
    while True:
        events1, values1=eplw.read()
        if events1 == 'QUIT' or events1 == psg.WIN_CLOSED:
            break
        elif events1=='CONTINUE':
            team_data('epl',int(values1['year']),values1['team'])

def LaLiga_Window():
    psg.theme('HotDogStand')
    layout_=[[psg.Column([[La_Liga]], justification='center')],
        [psg.Text('Hola! Bienvenido a la liga')],
            [psg.Text('Choose your team')],
            [psg.Combo(['Real Madrid','Barcelona','Atletico Madrid','Real Betis','Real Sociedad','Athletic Club','Osasuna','Villareal',
            'Rayo Vallecano','Valencia','Real Valladolid','Mallorca','Almeria','Getafe','Espanyol','Celta Vigo','Girona','Sevilla','Cadiz',
            'Elche'],key='team')],
            [psg.Text('Choose year')],
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('QUIT', font=('Times New Roman',12))]]
    
    lalw=psg.Window('La Liga',layout_)
    while True:
        events1, values1=lalw.read()
        if events1 == 'QUIT' or events1 == psg.WIN_CLOSED:
            break
        elif events1=='CONTINUE':
            team_data('La Liga',int(values1['year']),values1['team'])

def Bundes_Window():
    psg.theme('DarkBrown4')
    layout_=[[psg.Column([[Bundesliga_Image]], justification='center')],
            [psg.Text('Hallo! Willkommen in der Bundesliga')],
            [psg.Text('Choose your team')],
            [psg.Combo(['Union Berlin','Bayern Munich','Freiburg','Borussia Dortmund','Eintracht Frankfurt','RasenBallsport Leizpig',
            'Hoffenheim','Werder Bremen','Mainz 05','FC Cologne','Borussia M.Gladbach','Wolfsburg','Augsburg',
            'Hertha Berlin','VfB Stuttgart','Bayer Leverkusen','Bochum','Schalke 04'],key='team')],
            [psg.Text('Choose year')],
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('QUIT', font=('Times New Roman',12))]]
    bundw=psg.Window('La Liga',layout_)
    while True:
        events1, values1=bundw.read()
        if events1 == 'QUIT' or events1 == psg.WIN_CLOSED:
            break
        elif events1=='CONTINUE':
            team_data('Bundesliga',int(values1['year']),values1['team'])

def SerieA_Window():
    psg.theme('DarkTeal7')
    layout_=[[psg.Column([[Serie_A]], justification='center')],
        [psg.Text('Ciao! Benvenuto alla Serie A')],
            [psg.Text('Choose your team')],
            [psg.Combo(['Napoli','Atalanta','AC Milan','Roma','Lazio','Inter',
            'Juventus','Udinese','Torino','Salernitana','Sassuolo','Bologna','Fiorentina',
            'Empoli','Monza','Spezia','Lecce','Sampdoria','Verona','Cremonese'],key='team')],
            [psg.Text('Choose year')],
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('QUIT', font=('Times New Roman',12))]]
    seriaw=psg.Window('La Liga',layout_)
    while True:
        events1, values1=seriaw.read()
        if events1 == 'QUIT' or events1 == psg.WIN_CLOSED:
            break
        elif events1=='CONTINUE':
            team_data('Serie A',int(values1['year']),values1['team'])

def Ligue1_Window():
    psg.theme('DarkTeal')
    layout_=[[psg.Column([[Ligue1]], justification='center')],
        [psg.Text('Bonjour! Bienvenue en ligue 1')],
            [psg.Text('CHOOSE YOUR TEAM')],
            [psg.Combo(['Paris Saint Germain','Lens','Rennes','Lorient','Marseille','Monaco',
            'Lille','Lyon','Clermont Foot','Nice','Toulouse','Troyes','Reims',
            'Montpellier','Nantes','Auxerre','Strasbourg','Brest','Ajaccio','Angers'],key='team')],
            [psg.Text('CHOOSE YEAR')],
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('QUIT', font=('Times New Roman',12))]]
    ligue1w=psg.Window('La Liga',layout_)
    
    while True:
        events1, values1=ligue1w.read()
        if events1 == 'QUIT' or events1 == psg.WIN_CLOSED:
            break
        elif events1 == 'CONTINUE':
            team_data('Ligue 1',int(values1['year']),values1['team'])

def RFPL_Window():
    psg.theme('DarkRed1')
    layout_=[[psg.Column([[RFPL_Image]], justification='center')],
        [psg.Text('Privet! Dobro pozhalovat v RFPL')],
            [psg.Text('Choose your team')],
            [psg.Combo(['Zenit St. Petersburg','Spartak Moscow','CSKA Moscow','FC Rostov','Dinamo Moscow','FC Krasnodar',
            'FK Akhmat','FC Orenburg','PFC Sochi','Krylya Sovetov Samara','Ural','Nizhny Novgorod','Fakel',
            'Lokomotiv Moscow','Khimki','Torpedo Moscow'],key='team')],
            [psg.Text('Choose year')],
            [psg.Combo(['2014','2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
            [psg.Button('CONTINUE', font=('Times New Roman',12)),psg.Button('QUIT', font=('Times New Roman',12))]]
    rfplw=psg.Window('La Liga',layout_)
    while True:
        events1, values1=rfplw.read()
        if events1 == 'QUIT' or events1 == psg.WIN_CLOSED:
            break
        elif events1=='CONTINUE':
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
        if event == 'QUIT' or event == psg.WIN_CLOSED:
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
        if event == 'QUIT' or event == psg.WIN_CLOSED:
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
        if event == 'QUIT' or event == psg.WIN_CLOSED:
            break
        elif event == 'CONTINUE':
            league_table(values['team'],values['year'])

def Upcoming_LeagueFixturesWindow():
    
    psg.theme('DarkBrown4')
    lflayout=[[psg.Text('Choose your preferred League',size=(25,1),font='Georgia',justification='left')],
        [psg.Combo(['EPL','La Liga','Ligue 1', 'Serie A','RFPL'],key='team')],
        [psg.Button('CONTINUE',font=('Georgia',12)), psg.Button('QUIT',font=('Georgia',12))]]

    LFwin=psg.Window('UPCOMING LEAGUE FIXTURES',lflayout)

    while True:
        events,values=LFwin.read()
        if events == 'QUIT' or events == psg.WIN_CLOSED:
            break
        elif events == 'CONTINUE':
            league_fixtures(values['team'])

def MainWindow():
    psg.theme('DarkBlue')
    main_layout=[[psg.Column([[Main_Logo]], justification='center')],
    [psg.Text('CLICK ANY BUTTON TO GO AHEAD',font=('Times New Roman',15))],
    [psg.Button('TEAM DATA', font=('Times New Roman',14)), psg.Button('LEAGUE STATS', font=('Times New Roman',14))],
    [psg.Button('LEAGUE STANDINGS',font=('Times New Roman',14)), psg.Button('UPCOMING LEAGUE FIXTURES',font=('Times New Roman',14))],
    [psg.Column([[psg.Button('QUIT',font=('Times New Roman',13))]],justification='center')]
    ]

    main_window = psg.Window('Trivela', main_layout, resizable = True, size=(550,450))

    while True:
        event, values = main_window.read()
        if event == 'QUIT' or event == psg.WIN_CLOSED:
            break
        elif event == 'LEAGUE STATS':
            LeagueStats_Window()
        elif event == 'TEAM DATA':
            TeamData_Window()
        elif event == 'LEAGUE STANDINGS':
            LeagueTable_Window()
        elif event == 'UPCOMING LEAGUE FIXTURES':
            Upcoming_LeagueFixturesWindow()

MainWindow()