import calendar

calendario = calendar.calendar(2026)

with open('2026.txt',mode='wt',encoding='utf-8') as fichero:
    fichero.write(calendario)