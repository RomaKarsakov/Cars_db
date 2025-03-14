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

    with open("karsakov_pletenev.sql", "r") as schema_file:
        schema_script = schema_file.read()

    with conn.cursor() as cursor:
        for st in schema_script.split(";"):
            if st.strip():
                e = cursor.execute(st.strip())
                print(f"Executed: {e} ")
    conn.commit()


    print("База данных и таблицы успешно созданы.")


if __name__ == "__main__":
    create_database()
