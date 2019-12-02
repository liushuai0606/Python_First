import sqlite3

conn = sqlite3.connect('qytangconfig.sqlite')
cursor = conn.cursor()
cursor.execute("create table config_md5 (ip varchar(40), config varchar(99999), md5 config varchar(999))")
