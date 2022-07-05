from flask import Flask, request, send_file
import mysql.connector
from mysql.connector import Error
import sys

host = "0.0.0.0"
port = 6969

# libraries used
# pip install mysql-connector-python
# pip install flask

def gtfo(err):
    print(err)
    sys.exit(1)

def connection():
    try: # Change this if needed
        conn = mysql.connector.connect(
            host="localhost",
            database="secret_database", # dont change this line
            user="root",
            password="root"
        )
        if conn.is_connected():
            return conn
        else:
            gtfo("kenot connect")
    except Error as e:
        gtfo(e)


def endpoint(query:str):
    # checks for dangerous commands except for ' and --
    temp = query.lower()
    blacklist = ["delete","insert","update","join","union"]
    for item in blacklist:
        if item in temp:
            return "you sneaky little shi-, DONT DO THAT!!"
    try:
        # sends query to db and retreives results
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(query)
        response = cursor.fetchall()
        cursor.close()
        conn.close()
        return str(response)
    except Error as e:
        return "nonono that's not how you solve the challenge!"

app = Flask(__name__)

@app.route("/index.html",methods=["GET"])
def index():

    # parse data to a dictionary
    dictionary = request.args.to_dict()
    try:
        username = dictionary["username"]
        password = dictionary["password"]
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        response = endpoint(query) + " " + query
        return response

    except KeyError:
        # default response
        return send_file("./index.html")

app.run(host=host,port=port)