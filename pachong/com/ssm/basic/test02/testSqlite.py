import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
sql = '''
    insert into company (id,name,age,address,salary)
    values (1,'张三',22,'山西',8000)
'''
sql = '''
    select * from company
'''
cursor = c.execute(sql)
for row in cursor:
    print('id=',row[0])
    print('name=',row[1])
    print('age=',row[2])
    print('address=',row[3])
# conn.commit()
conn.close()
print("成功")