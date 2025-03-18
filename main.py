import psycopg2


def load_car(id):
    cursor.execute("SELECT * FROM karsakov_pletenev.CARS WHERE id = %s;", (id,))
    print(cursor.fetchone())


def save_car(id,model,year,color,number,type):
    cursor.execute("INSERT INTO karsakov_pletenev.CARS VALUES (%s,%s,%s,%s,%s,%s)", (id,model,year,color,number,type))
    cursor.commit()
    conn.commit()


db_config = {
    "dbname": "school_db",
    "user": "school",
    "password": "School1234*",
    "host": "79.174.88.238",
    "port": "15221"
}

conn = psycopg2.connect(**db_config)

with open("migrations.sql", "r") as schema_file:
    schema_script = schema_file.read()

with conn.cursor() as cursor:
    for st in schema_script.split(";"):
        if st.strip():
            e = cursor.execute(st.strip())
            print(f"Executed: {e} ")
    conn.commit()

cursor = conn.cursor()


print("База данных и таблицы успешно созданы.")


if __name__ == "__main__":
    # save_car(int(input()),input(),int(input()),input(),input(),input())
    load_car(int(input()))
    cursor.close()
    conn.close()
