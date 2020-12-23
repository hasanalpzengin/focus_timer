import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("tiktokschedule.db")
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS schedules (time text NOT NULL UNIQUE)''')
        self.conn.commit()

    def addTime(self, time):
        try:
            c = self.conn.cursor()
            query = "INSERT INTO schedules(time) VALUES ('{}')".format(time)
            c.execute(query)
            self.conn.commit()
        except:
            print("Error on database")

    def deleteTime(self, time):
        c = self.conn.cursor()
        c.execute("DELETE FROM schedules WHERE time='{}'".format(time))
        self.conn.commit()
    
    def listTime(self):
        c = self.conn.cursor()
        c.execute("SELECT time FROM schedules")
        self.conn.commit()
        return c.fetchall()