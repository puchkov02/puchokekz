import sqlite3


async def on_startup():
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect('upravkomp.db')
    create_tables(conn)  # Создаем таблицы для хранения данных (если их нет)
    conn.close()


def create_tables(conn):
    cursor = conn.cursor()
    conn.commit()

    # Создание таблицы, если они не существует
    create_zhalobi_table_query = '''
        CREATE TABLE IF NOT EXISTS zhalobi (
            zhalobi_id INTEGER PRIMARY KEY,
            home_id INTEGER,
            zhaloba TEXT,
            date DATE,
            room_id INTEGER,
            FOREIGN KEY (home_id) REFERENCES homes(home_id),
            FOREIGN KEY (room_id) REFERENCES rooms(room_id)
        )
    '''
    create_homes_table_query = '''
        CREATE TABLE IF NOT EXISTS homes (
            home_id INTEGER PRIMARY KEY,
            address TEXT,
            year_of_construction INTEGER,
            rooms_count INTEGER
        )
    '''
    create_rooms_table_query = '''
        CREATE TABLE IF NOT EXISTS rooms (
            room_id INTEGER PRIMARY KEY,
            home_id INTEGER,
            room_number INTEGER,
            people_count INTEGER,
            FOREIGN KEY (home_id) REFERENCES homes(home_id)
        )
    '''
    create_categorii_zhalob_table_query = '''
        CREATE TABLE IF NOT EXISTS categorii_zhalob (
            categori_id INTEGER PRIMARY KEY, 
            categori_name TEXT
        )
    '''
    create_status_categorii_table_query = '''
        CREATE TABLE IF NOT EXISTS status_categorii (
            status_id INTEGER PRIMARY KEY, 
            status_name TEXT
        )
    '''
    cursor.execute(create_zhalobi_table_query)
    conn.commit()
    cursor.execute(create_homes_table_query)
    conn.commit()
    cursor.execute(create_rooms_table_query)
    conn.commit()
    cursor.execute(create_categorii_zhalob_table_query)
    conn.commit()
    cursor.execute(create_status_categorii_table_query)
    conn.commit()

    # Запись данных в таблицы
    zhalobi_data = [(1, 1, 'Проблема с электричеством', '2023-07-01', 1),
                    (2, 2, 'Протекает крыша', '2023-07-02', 3),
                    (3, 1, 'Проблема с отоплением', '2023-07-03', 2),
                    (4, 3, 'Проблемы с сантехникой', '2023-07-04', 4)]
    cursor.executemany('INSERT INTO zhalobi VALUES (?, ?, ?, ?, ?)', zhalobi_data)
    conn.commit()

    homes_data = [(1, 'ул. Центральная 1', 2005, 3),
                  (2, 'ул. Парковая 5', 1998, 4),
                  (3, 'ул. Солнечная 10', 2010, 2)]
    cursor.executemany('INSERT INTO homes VALUES (?, ?, ?, ?)', homes_data)
    conn.commit()

    rooms_data = [(1, 1, 101, 2),
                  (2, 1, 102, 1),
                  (3, 2, 201, 2),
                  (4, 3, 301, 3)]
    cursor.executemany('INSERT INTO rooms VALUES (?, ?, ?, ?)', rooms_data)
    conn.commit()

    categorii_zhalob_data = [(1, 'Электрика'),
                             (2, 'Отопление'),
                             (3, 'Водопровод'),
                             (4, 'Кровля')]
    cursor.executemany('INSERT INTO categorii_zhalob VALUES (?, ?)', categorii_zhalob_data)
    conn.commit()

    status_categorii_data = [(1, 'В обработке'),
                             (2, 'В процессе'),
                             (3, 'Завершено')]
    cursor.executemany('INSERT INTO status_categorii VALUES (?, ?)', status_categorii_data)
    conn.commit()

    cursor.close()
    conn.close()
