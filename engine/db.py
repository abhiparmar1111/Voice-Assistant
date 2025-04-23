import csv
import sqlite3

con = sqlite3.connect("siri.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command (id integer primary key, name VARCHAR(100), path VARCHAR(1000) )"

# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null, 'Notepad', 'Notepad.exe')"
# cursor.execute(query)
# con.commit()
# word_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"

# # Insert the path into sys_command table
# cursor.execute("INSERT INTO sys_command VALUES (NULL, ?, ?)", ("Word", word_path))

# # Commit and close
# con.commit()
# con.close()
# cursor.execute("DELETE FROM sys_command WHERE id = '7'")
# con.commit()
# query = "CREATE TABLE IF NOT EXISTS web_command (id integer primary key, name VARCHAR(100), url VARCHAR(1000) )"
# cursor.execute(query)

query = "INSERT INTO web_command VALUES(null, 'brave', 'https://brave.com/')"
cursor.execute(query)
con.commit()

# query = "INSERT INTO sys_command VALUES(null, 'Word', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE ')"

# cursor.execute(query)
# con.commit()

# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no  VARCHAR(255), email VARCHAR(255) NULL ) ''')

# desired_columns_indices = [0,18]

# with open('contacts.csv','r',encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id,'name', 'mobile_no') VALUES (null, ?,?);''', tuple(selected_data))
        
# con.commit()
# con.close()

# query=  'Vaatsal'
# query = query.strip().lower()

# cursor.execute("Select mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ("%"+query+"%",query+"%"))
# results = cursor.fetchall()
# print(results[0][0])