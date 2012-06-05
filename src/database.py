import sqlite3
#import sys


class Database:
  def __init__(self, database="../db/laamaj.db"):
    self.__con = None
    self.__cur = None
    self.__db = database
    self.__connect()

  def __del__(self):
    self.__close()

  def __connect(self):
    try:
      self.__con = sqlite3.connect(self.__db)
      self.__cur = self.__con.cursor()
      print("Connected to "+self.__db)
    except sqlite3.Error, e:
      print("Error : "+e.args[0])

  def __close(self):
    if self.__con:
      self.__con.close()
      self.__con = None
      self.__cur = None
      print("connection closed")
    else:
      print("no open connection")
      self.__cur = None

  def __commit(self):
    if self.__con:
      self.__con.commit()

  def add_website(self, user, chan, website):
    print("adding website")
    #self.__connect()
    output = self.__cur.execute("INSERT INTO websites (ws_date, ws_user, ws_chan, ws_url) VALUES (date('now'), ?, ?, ?);", (user, chan, website))
    #self.__commit()
    #self.__close()
    return output

  def list_last_sites(self, numero=5):
    print("output sites")
    try:
      #self.__connect()
      print((str(numero)))
      data = self.__cur.execute("select ws_user||\' - \'||ws_chan||\' - \'||ws_url from websites where ws_id > (select max(ws_id) from websites) - ? order by ws_id desc;", (str(numero)))
      if data:
        print (data)
      else:
        data = "No Results"
      #self.__close()
      return(data)
    except sqlite3.Error, e:
      print("Error : ",e.args[0])
      data = "Error : {error}".format(error=e.args[0])
      #self.__close()
      return(data)
    


