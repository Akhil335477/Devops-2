from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# Database connection details
DB_HOST = "database-1.cpyq2gyi86w0.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "WiKkm5X3sTcG1odYdAWF"
DB_NAME = "database-1"

# Connect to the database
def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route('/')
def index():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, skill FROM skills")
        data = cursor.fetchall()
    connection.close()
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    skill = request.form['skill']
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO skills (name, skill) VALUES (%s, %s)", (name, skill))
        connection.commit()
    connection.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
