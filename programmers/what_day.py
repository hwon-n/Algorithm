from datetime import datetime

def solution(a, b):

    dateDict = {
        0: 'MON',
        1: 'TUE',
        2: 'WED',
        3: 'THU',
        4: 'FRI',
        5: 'SAT',
        6: 'SUN'}
    
    date = datetime.strptime(f'2016-{a}-{b}', '%Y-%m-%d').weekday()
    
    return dateDict[date]
