#Docker Learning
from flask import Flask, render_template
import MySQLdb
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    db = MySQLdb.connect(
        host="mydb", # Hostname of the MYSQL container
        user="root", # Username to connect to MYSQL
        passwd="my-secret-pw", #Password for the MYSQL user
        db="mysql"  # Name of the database to connect to
    )
    cur = db.cursor() # Opens a cursor — a tool used to send SQL queries to the database
    cur.execute("SELECT VERSION()") # Sends the SQL query to MySQL. VERSION() is a built-in MySQL function that returns the database version
    version = cur.fetchone() # Fetches one row from the result
    cur.close() # Closes the cursor — frees up the resource after the query is done
    db.close() #Closes the database connection entirely
    return render_template('index.html', version=version[0]) # loads templates/index.html and passes the version string into the template
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)