from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

## Give me data in the database for all of the rows in table Student Dreams
def student_dreams_listAll() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'students'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM student_dreams')
    results = [{name: dream} for (name, dream) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
## Display data
def index() -> str:
    return json.dumps({'student_dreams': student_dreams_listAll()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8000)