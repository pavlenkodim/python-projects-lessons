import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv()

configs = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_USER_PASSWORD")
}

with mysql.connector.connect(**configs) as conn:
    with conn.cursor() as cursor:
        # Создание таблицы если ее нет
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, salary DECIMAL(10, 2) NOT NULL)")

        # Добавляем одного пользователя
        cursor.execute("INSERT INTO users (name, salary) VALUES (%s, %s)", ("Misha", 3300.00))

        # Добавляем несколько пользователе сразу
        users = [
            ("Ann", 2250.00),
            ("Lenny", 1830.00),
        ]
        cursor.executemany("INSERT INTO users (name, salary) VALUES (%s, %s)", users)

        # Созранить изменения в БД
        conn.commit()

        # Получить пользователей по фильтру
        cursor.execute("SELECT * FROM `users` WHERE `salary` > '1400' AND `salary` <= '2500' LIMIT 50")

        print(cursor.fetchall())

cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
print("Database version : ", cursor.fetchone()[0])

cursor.execute("select * from users")
print(cursor.fetchall())

cursor.close()
conn.close()

# ООП исполнение
class MyORM:
    def __init__(self, config, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.config = config

        self.db = mysql.connector.connect(**config)
        self.cursor = self.db.cursor()

    def create_user(self, name, salary):
        self.cursor.execute("INSERT INTO users (name, salary) VALUES (%s, %s)", (name, salary))
        self.db.commit()

    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.db.close()


db = MyORM(configs)

db.create_user("Sergey", 1740.00)

users = db.get_users()

db.close_connection()

print(users)