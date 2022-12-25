import json
from flask import Flask, jsonify, request
import psycopg2
import random
app = Flask(__name__)
data = []


conn = psycopg2.connect(
    host="localhost",
    database='web',
    user='postgres',
    password='1234'
)
cursor = conn.cursor()



@app.route('/users', methods=['GET'])
def get_users():
    data.clear()
    sql = 'SELECT * FROM users;'
    cursor.execute(sql)
    info = cursor.fetchall()
    conn.commit()
    print(info)
    for i in info:
        user = {'id': i[0], 'name': i[1], 'surname': i[2]}
        data.append(user)
    print(data)
    return jsonify(data)


@app.route('/users', methods=['POST'])
def add_user():
    sql = 'INSERT INTO public.users VALUES (default, %s, %s);'
    name = request.get_json()['name']
    surname = request.get_json()['surname']
    cursor.execute(sql, (name, surname))
    conn.commit()
    return jsonify(data)


@app.route('/users', methods=['DELETE'])
def del_user():
    sql = 'DELETE FROM public.users WHERE id=%s;'
    id = request.get_json()['id']
    cursor.execute(sql, (id,))
    conn.commit()
    return jsonify(data)


@app.route('/users', methods=['PUT'])
def update_user():
    sql = "UPDATE public.users SET id = %s, name =%s, surname =%s WHERE id = %s;"
    id = request.get_json()['id']
    name = request.get_json()['name']
    surname = request.get_json()['surname']
    cursor.execute(sql, (id, name, surname, id))
    conn.commit()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)