
# [
# {"name": "Michhael", "score": 99},
# {"name": "Bob", "score": 85},
# {"name": "Bart", "score": 59},
# {"name": "Lisa", "score": 87}
# ]

import sqlite3, os

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
# cursor.execute("insert into user(id,name) values (\'1\',\'Lennon\')")
# cursor.rowcount
# cursor.close()
# conn.commit()
# conn.close()


# conn = sqlite3.connect("test.db")
# cursor = conn.sursor()
# cursor.execute("select * from user where id=?", ('1',))
# values = cursor.fetchall()
# values
# cursor.close()
# conn.close()


db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)


conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001','Adam', 95)")
cursor.execute(r"insert into user values ('A-002','Bart', 62)")
cursor.execute(r"insert into user values ('A-003','Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low,high):
	'返回指定分数区间的名字，按分数从低到高排序'
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute('select name from user where score between ? and ? order by score',(low,high))
	values = cursor.fetchall()
	L = []
	for i in values:
		L.append(i[0])
	return L


assert get_score_in(80,95) == ['Adam'], get_score_in(80,95)
assert get_score_in(60,80) == ['Bart','Lisa'], get_score_in(60,80)
assert get_score_in(60,100) == ['Bart', 'Lisa','Adam'], get_score_in(60,100)
print("Pass")

