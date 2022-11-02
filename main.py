import PySimpleGUI as psg
#set the theme for the screen/window
psg.theme('SandyBeach')
#Defining the layout of the window
layout=[[psg.Text('Choose Year',size=(20, 1), font='Lucida',justification='left')],
        [psg.Combo(['2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
        [psg.Text('Choose Team',size=(30, 1), font='Lucida',justification='left')],
        #psg.combo gives you a drop-down list
        [psg.Combo(['Arsenal','Manchester City','Tottenham Hotspurs', 'Newcastle','Chelsea','Manchester United','Fulham',
        'Liverpool','Brighton','West Ham','Brentford','Everton','Crystal Palace','Bournemouth',
        'Aston Villa','Southampton','Leicester City','Leeds United','Wolves','Nottingham Forest'],key='team')], #Teams playing in the Premier League
        [psg.Text('Choose additional Facilities',size=(30, 1), font='Lucida',justification='left')],
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]] #Save button and cancel button

while True:
        #Define Window
        win =psg.Window('Expected Goals',layout)
        #Read  values entered by user
        e,v=win.read()
        if e == sg.WINDOW_CLOSED or e == 'Quit':
                break
        #close first window
        win.close()
        # #access the selected value in the list box and add them to a string
        # strx=""
        # for val in v['fac']:
        #     strx=strx+ " "+ val+","
                
        #display string in a popup         
        psg.popup('Team chosen is: '+v['team']+' from the year: '+v['year'])

