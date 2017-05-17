import sqlite3 #imports sqlite3 from python lib

conn = sqlite3.connect('data/thisdata.db') #connects to my data base

c = conn.cursor() #creates my cursor

def create():
	c.execute('CREATE TABLE IF NOT EXISTS Cart( name TEXT, price REAL)')
    
conn.commit()

c.close
conn.close

if __name__ == "__main__":
    create()
