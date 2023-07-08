from flask import Flask, render_template
from database import on_startup
import sqlite3
import asyncio


app = Flask(__name__)


# Главная страница
@app.route('/')
def index():
    return render_template('index.html')


# Справочные страницы
@app.route('/sprav_pages/')
def sprav_homes():
    # Подключение к базе данных
    conn = sqlite3.connect('upravkomp.db')
    cursor = conn.cursor()

    # Извлечение данных
    cursor.execute('SELECT * FROM homes')
    homes_data = cursor.fetchall()
    cursor.execute('SELECT * FROM categorii_zhalob')
    categorii_zhalob_data = cursor.fetchall()
    cursor.execute('SELECT * FROM status_categorii')
    status_categorii_data = cursor.fetchall()

    # Закрытие соединения с базой данных
    cursor.close()
    conn.close()

    return render_template('sprav_pages.html', homes_data=homes_data, categorii_zhalob_data=categorii_zhalob_data, status_categorii_data=status_categorii_data)


# Целевые страницы
@app.route('/zhalobi/')
def target_zhalobi():
    # Подключение к базе данных
    conn = sqlite3.connect('upravkomp.db')
    cursor = conn.cursor()

    # Извлечение данных из таблицы zhalobi
    cursor.execute('SELECT * FROM zhalobi')
    zhalobi_data = cursor.fetchall()

    # Закрытие соединения с базой данных
    cursor.close()
    conn.close()

    return render_template('target_zhalobi.html', zhalobi_data=zhalobi_data)


@app.route('/rooms/')
def target_rooms():
    # Подключение к базе данных
    conn = sqlite3.connect('upravkomp.db')
    cursor = conn.cursor()

    # Извлечение данных из таблицы rooms
    cursor.execute('SELECT * FROM rooms')
    rooms_data = cursor.fetchall()

    # Закрытие соединения с базой данных
    cursor.close()
    conn.close()

    return render_template('target_rooms.html', rooms_data=rooms_data)


if __name__ == '__main__':
    # asyncio.run(on_startup())
    app.run()
