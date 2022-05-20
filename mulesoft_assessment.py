import sqlite3
# conn=sqlite3.connect("movies.db")
# conn.execute(
# '''CREATE TABLE MOVIES1
#          (MOV_NAME VARCHAR2(50) PRIMARY KEY,
#          ACTOR VARCHAR2(50),
#          ACTRESS VARCHAR2(50),
#          DIRECTOR VARCHAR2(20),
#          YR_RELEASE VARCHAR2(10)
# );
# ''')
# conn.close();

# conn=sqlite3.connect("movies.db")
# conn.execute("INSERT INTO MOVIES1 VALUES('DHOOM','AMIR','KATRINA','SANJAY','2018');")
# conn.execute("INSERT INTO MOVIES1 VALUES('RRR','NTR','ALIA','RAJAMOULI','2022');")
# conn.execute("INSERT INTO MOVIES1 VALUES('TARE ZAMEEN PAR','AMIR','MAYA','AMOLE','2007');")
# conn.commit()
# conn.close()

conn=sqlite3.connect("movies.db")
conn.execute("SELECT * FROM MOVIES1 WHERE ACTOR='AMIR';")
response1=conn.cursor()
details_mov=response1.fetchall()
print(details_mov)

# conn=sqlite3.connect("movies.db")
# conn.execute("SELECT * FROM MOVIES1 WHERE MOV_NAME='DHOOM';")
# response2=conn.cursor()
# details_act=response2.fetchall()
# print(details_act)

conn.commit()
conn.close()
