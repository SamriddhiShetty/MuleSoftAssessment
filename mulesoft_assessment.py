import sqlite3
conn=sqlite3.connect("movie_DB.db")
conn.execute(
'''CREATE TABLE MOVIES1
         (MOV_NAME VARCHAR2(50) PRIMARY KEY,
         ACTOR VARCHAR2(50),
         ACTRESS VARCHAR2(50),
         DIRECTOR VARCHAR2(20),
         YR_RELEASE VARCHAR2(10)
);
''')
conn.close()

#INSERT STATEMENTS
conn=sqlite3.connect("movie_DB.db")
conn.execute("INSERT INTO MOVIES1 VALUES('DHOOM','AMIR','KATRINA','SANJAY','2018')")
conn.execute("INSERT INTO MOVIES1 VALUES('RRR','NTR','ALIA','RAJAMOULI','2022')")
conn.execute("INSERT INTO MOVIES1 VALUES('TARE ZAMEEN PAR','AMIR','MAYA','AMOLE','2007')")
conn.commit()
conn.close()

# #SELECT STATEMENTS

conn=sqlite3.connect("movie_DB.db")
cur1=conn.cursor()
cur1.execute("SELECT * FROM MOVIES1 WHERE ACTOR='AMIR'")
response1 = cur1.fetchall()
print(response1)

cur2=conn.cursor()
cur2.execute("SELECT * FROM MOVIES1 WHERE MOV_NAME='DHOOM'")
response2 = cur2.fetchall()
print(response2)

cur3=conn.cursor()
cur3.execute("SELECT * FROM MOVIES1")
response3 = cur3.fetchall()
print(response3)

conn.commit()
conn.close()
