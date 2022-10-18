import PySimpleGUI as psg
#set the theme for the screen/window
psg.theme('SandyBeach')
#define layout
layout=[[psg.Text('Choose Year',size=(20, 1), font='Lucida',justification='left')],
        [psg.Combo(['2015','2016','2017', '2018','2019','2020','2021','2022'],key='year')],
        [psg.Text('Choose Team',size=(30, 1), font='Lucida',justification='left')],
        [psg.Combo(['Arsenal','Manchester City','Tottenham Hotspurs', 'Chelsea','Manchester United',
        'Liverpool','Leicester City','West Ham'],key='team')],
         [psg.Text('Choose additional Facilities',size=(30, 1), font='Lucida',justification='left')],
         #[psg.Listbox(values=['Welcome Drink', 'Extra Cushions', 'Organic Diet','Blanket', 'Neck Rest'], select_mode='extended', key='fac', size=(30, 6))],
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]
#Define Window
win =psg.Window('Customise your Journey',layout)
#Read  values entered by user
e,v=win.read()
#close first window
win.close()
# #access the selected value in the list box and add them to a string
# strx=""
# for val in v['fac']:
#     strx=strx+ " "+ val+","
        
#display string in a popup         
psg.popup('Team chosen is: '+v['team']+' from the year: '+v['year'])

