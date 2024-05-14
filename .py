import sqlite3

 conn = sqlite3.connect('medicine.db')
 cursor = conn.cursor()
 cursor.execute(
     '''CREATE TABLE IF NOT EXISTS medicine(id INT, name TEXT,bdate INT, price INT)''')
 cursor.execute('''INSERT INTO medicine(id,  name, bdate, price) VALUES  (2, 'kyupen', '6 month', '12000')''')
 cursor.execute('''INSERT INTO medicine(id,  name, bdate, price) VALUES  (6, 'tirmol', '2 years', '8000')''')
 cursor.execute('''INSERT INTO medicine(id,  name, bdate, price) VALUES  (4, 'fastumgel', '8 month', '2000')''')

 nomi = input('Dorini nomini kiriting:')
 cursor.execute('''select * from medicine ''')
 result = cursor.fetchall()
 topildi = False
 for i in result:
   if i[1] == nomi:
        print(f"ID={i[0]}")
        print(f"Name={i[1]}")

        topildi = True

if topildi == False:
    print('Bunday dori topilmadi')

conn.commi
