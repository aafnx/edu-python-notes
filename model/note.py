from datetime import datetime

def create(note):
   date = datetime.now().strftime('%d:%m:%Y %H:%M')
   return {'date': date, 'note': note} 

def format(note):
    res = note['date']
    res += '\n' 
    res += note['note']
    res += '\n' 
    res += '---'
    return res
