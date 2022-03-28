import sqlite3
con = sqlite3.connect('db')
cursor = con.cursor()
cursor.execute('INSERT INTO api_play(name,point,help,bank) values("李白","18","12","13")')
con.commit()