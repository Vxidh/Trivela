import PySimpleGUI as psg
my_img = psg.Image(filename='MainLogo.png', key='_CAMIMAGE_')
def Main_Window():
    psg.theme('DarkBlue')
    main_layout=[[psg.Column([[my_img]], justification='center')],
    [psg.Text('Click any button to go ahead')],
    [psg.Button('LEAGUE DATA', font=('Times New Roman',13)), psg.Button('PLAYER STATS', font=('Times New Roman',13))],
    [psg.Button('TEAM FIXTURES', font=('Times New Roman',13)), psg.Button('LEAGUE STANDINGS',font=('Times New Roman',13))],
    [psg.Button('Quit', font=('Times New Roman',12))]]
    main_window = psg.Window('Trivela', main_layout, size=(500,500))
    while True:
        event, values = main_window.read()
        if event == 'Quit':
            break
        elif event == 'LEAGUE DATA':
            league_stats()
def league_stats():
    psg.theme('DarkPurple4')
    layout=[[psg.Text('Choose your preferred League',size=(25,1),font='Georgia',justification='left')],
            [psg.Button('EPL', font=('Times New Roman',12)),psg.Button('La Liga', font=('Times New Roman',12)),
            psg.Button('Bundesliga', font=('Times New Roman',12)),psg.Button('Serie A', font=('Times New Roman',12)),
            psg.Button('Ligue 1', font=('Times New Roman',12)),psg.Button('RFPL', font=('Times New Roman',12))],
            [psg.Button('QUIT',font=('Georgia',12))]]
    window = psg.Window('The Footballer', layout, size=(500, 200))
    while True:
        event, values = window.read()
Main_Window()