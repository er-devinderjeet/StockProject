# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:22:05 2017

@author: Devinderjeet
"""

import MySQLdb
#from MySQLdb.connector import errorcode


##===============================================

class DatabaseUtility: 

	def __init__(self, database, table1,table2):
		self.db 			= database
		self.table1 		= table1
		self.table2 		= table2
		
		f = open('C:\\Users\\Devinderjeet\\Desktop\\password.txt', 'r')
		p = f.read(); f.close();
		
		self.cnx = MySQLdb.connect(	user   = 'root',
									passwd = p[3:],
									host   = 'localhost',
									db 	   = self.db)
		print p
		self.cursor = self.cnx.cursor()
    
	def getData(self):
		
		cmd = " SELECT * FROM " + self.table1 
		cmd += " INNER JOIN "+ self.table2 
		cmd += " ON %s.stock_id = %s.stock_id ;" % (self.table1, self.table2)
		return self.runCommand(cmd)
    	
		
	def runCommand(self, cmd):	 
		print ("RUNNING COMMAND: " + cmd)
		try:
			self.cursor.execute(cmd)
		except:
			print "Error running Command"
		try :
			msg = self.cursor.fetchall()
		except:
			msg = "Error running Command"
		return msg
	
	def __del__(self):
		self.cnx.commit()
		self.cursor.close()
		self.cnx.close()
    

if __name__ == '__main__':
	db 		 = 'friend_market'
	table1	 = 'stock_names'
	table2 	 = 'five_min'
	
	dbu = DatabaseUtility(db, table1,table2)
	print (dbu.getData())
