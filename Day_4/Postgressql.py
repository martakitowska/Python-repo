from sqlalchemy import create_engine, text

# Wszyscy macie dostęp do tej bazy danych więc uwżajcie by sobie na wzajem nie kasować danych lub tabel
# Możec tworzyć sobie tam tabele swoje np z prefixami od inijalow np lf_users - tak by pracować na swojej "przestrzeni nazwa" :)
DATABASE_URL = "postgresql+psycopg2://weblink_intel:iSA#Intel#2025@pgsql.cyber-folks.pl:5432/weblink_intel"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    with engine.begin() as connection:
        connection.execute(
            text("""CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    age INTEGER
                );"""),
        )

def print_by_age(age):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT id, name, age FROM users WHERE age > {}".format(age)))
        for row in result:
            print(f"ID: {row.id}, Nazwa: {row.name}")

def add_user(name, age):
    with engine.begin() as connection:
        connection.execute(
            text("INSERT INTO users (name, age) VALUES (:name, :age)"),
            {"name": name, "age": age}
        )