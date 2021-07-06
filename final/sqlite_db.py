import sqlite3

con = sqlite3.connect('plot_data.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS date_mark (
            date TEXT PRIMARY KEY,
            mark TEXT);''')

con.commit()
con.close()