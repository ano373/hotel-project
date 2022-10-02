import pymysql

db = pymysql.connect(host='localhost',
                             user='ano',
                             password='1234a',
                             database='hotel_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
ml= """INSERT INTO guests(NAME,AGE,ADDRESS,EMAIL,PHONE,NAT_ID,
                           ROOM_REG,P_NO,ROOM_SYS,DAY_NUM,PAY,BILL)
                    VALUES ("mario",'6','street','ggo@gmail.com','01234','342341'
                           ,'33','567',"duplexe",'4','card','5500')       """
try:
    cursor.execute(ml)
    db.commit()
except:
    db.rollback()

db.close()

