#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect(host='localhost',
                     user='ano',
                     password='1234a',
                     database='hotel_db',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS guests")

# Create table as per requirement
sql = """CREATE TABLE guests (
              ID  INT(255) AUTO_INCREMENT PRIMARY KEY NOT NULL,
              NAME  varchar(600) NOT NULL,
              AGE INT(255) NOT NULL,  
              ADDRESS VARCHAR(600) NOT NULL,
              EMAIL VARCHAR(600) NOT NULL,
              PHONE VARCHAR(600) NOT NULL,
              NAT_ID VARCHAR(600) NOT NULL, 
              ROOM_REG INT(255) NOT NULL, 
              P_NO INT(255) NOT NULL, 
              ROOM_SYS VARCHAR(600) NOT NULL, 
              DAY_NUM INT(255) NOT NULL, 
              PAY VARCHAR(600) NOT NULL, 
              BILL INT(255)  NOT NULL)"""

cursor.execute(sql)

# disconnect from server
db.close()