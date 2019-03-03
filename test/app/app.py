from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

## Give me data in the database for all of the rows in table Student Dreams
def student_dreams_listAll() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'Molly',
        'host': 'db',
        'port': '3306',
        'database': 'students'
    }
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM student_dreams')
        results = [{name: dream} for (name, dream) in cursor]
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print("something went wrong:{}".format(err))
        results = [{"Database is not up!": "Please check db!"}]
    return results


@app.route('/')
## Display data
def index() -> str:
    return json.dumps({'student_dreams': student_dreams_listAll()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8080)
