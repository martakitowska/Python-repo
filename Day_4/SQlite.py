from sqlalchemy import create_engine, text, String, Column, Integer
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///moja_baza.db"
engine = create_engine(DATABASE_URL)

def get_users():
    # polaczenie sie zamyka dzieki with
    # connect do potwierdzenia zmian
    with engine.connect() as connection:
        result = connection.execute(text("SELECT id, name, age FROM users"))
        for row in result:
            print("name:", row.name)

def init_db():
    with engine.begin() as connection:
        connection.execute(text("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            );"""))

def add_user(name, age):
    with engine.begin() as connection:
        connection.execute(
            text("INSERT INTO users (name, age) VALUES (:name, :age)"),
            {"name": name, "age": age}
        )

#init_db()
#add_user('Lukasz', 15)
#get_users()

#add_user('Lukasz', "15'); DROP TABLE users; -- ") ##przykład SQLInjection jeśli nie będziemy używać bindowania parametrów do zaptytania SQL

