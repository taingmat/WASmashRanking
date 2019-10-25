import pymysql
import Credentials


# Open database connection

#db = pymysql.connect(host = "192.168.1.130",
#db = pymysql.connect(host = "29",
db = pymysql.connect(host = "71.231.186.99",
                     port = 3306,
                     db = "WASMASH",
                     user = Credentials.get_user(),
                     passwd = Credentials.get_password())

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

cursor.execute("SHOW TABLES")

data = cursor.fetchall()

print(data)
# disconnect from server
db.close()
