import psycopg2


def create_database():
    db_config = {
        "dbname": "school_db",
        "user": "school",
        "password": "School1234*",
        "host": "79.174.88.238",
        "port": "15221"
    }

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    with open("karsakov_pletenev.sql", "r") as schema_file:
        schema_script = schema_file.read()

    conn.commit()
    cursor.close()
    conn.close()

    print("База данных и таблицы успешно созданы.")


if __name__ == "__main__":
    create_database()
