import psycopg2


def load_car_id(id):
    cursor.execute("SELECT * FROM karsakov_pletenev.CARS WHERE id = %s;",  (id,))
    # return cursor.fetchone()
    res = dict(zip(('id','model','year','color','number','car_type'),cursor.fetchone()))
    res['dtp'] = []
    print(res)
    return res


def load_car_number(number):
    cursor.execute("SELECT * FROM karsakov_pletenev.CARS WHERE number = %s;",  (number,))
    # return cursor.fetchone()
    res = dict(zip(('id','model','year','color','number','car_type'),cursor.fetchone()))
    print(res)
    return res


def load_dtp(id):
    cursor.execute("SELECT * FROM karsakov_pletenev.CARSDTP WHERE car_id = %s;",  (id,))
    dtps = set()
    dtps2 = []
    while True:
        row = cursor.fetchone()
        print(row)
        if row is None:
            break
        t = dict(zip(('car_id','dtp_id'),row))
        dtps.add(t['dtp_id'])
    for dtp in dtps:
        cursor.execute("SELECT * FROM karsakov_pletenev.DTP WHERE id = %s;", (dtp,))
        dtps2.append(dict(zip(('id','dtp_date','description'),cursor.fetchone())))
    return dtps2


def save_car(car):
    cursor.execute("INSERT INTO karsakov_pletenev.CARS (model, year, color, number, car_type) VALUES (%s,%s,%s,%s,%s) RETURNING id", (car.model, car.year, car.color, car.number, car.car_type))
    id = cursor.fetchone()[0]
    for dtp in car.dtp:
        cursor.execute("INSERT INTO karsakov_pletenev.CARSDTP VALUES (%s,%s)", (car.id, dtp))
    conn.commit()
    return id


def save_car_with_id(car):
    cursor.execute(
        "INSERT INTO karsakov_pletenev.CARS (id, model, year, color, number, car_type) VALUES (%s,%s,%s,%s,%s,%s)",
        (car.id, car.model, car.year, car.color, car.number, car.car_type))
    for dtp in car.dtp:
        cursor.execute("INSERT INTO karsakov_pletenev.CARSDTP VALUES (%s,%s)", (car.id, dtp))
    conn.commit()
    return None


def save_dtp(dtp):
    cursor.execute("INSERT INTO karsakov_pletenev.DTP (dtp_date, description) VALUES (%s,%s) RETURNING id", (dtp.date, dtp.description))
    id = cursor.fetchone()[0]
    conn.commit()
    return id


def update_car(car):
    cursor.execute("UPDATE karsakov_pletenev.CARS SET (model, year, color, number, car_type) = (%s,%s,%s,%s,%s) WHERE id = %s",(car.model, car.year, car.color, car.number, car.car_type, car.id))
    id = car.id
    cursor.execute("DELETE FROM karsakov_pletenev.CARSDTP WHERE car_id = %s",(car.id,))
    for dtp in car.dtp:
        try:
            cursor.execute("INSERT INTO karsakov_pletenev.CARSDTP VALUES (%s,%s)", (car.id, dtp))
        except:
            pass
    conn.commit()
    return id


def update_dtp(dtp):
    cursor.execute("UPDATE karsakov_pletenev.DTP SET (dtp_date, description) = (%s,%s) WHERE id = %s", (dtp.date, dtp.description, dtp.id))
    id = dtp.id
    conn.commit()
    return id


def delete_car(id):
    print(id)
    cursor.execute("DELETE FROM karsakov_pletenev.CARSDTP WHERE car_id = %s",(id,))
    cursor.execute("DELETE FROM karsakov_pletenev.CARS WHERE id = %s",(id,))

    conn.commit()


def delete_dtp(id):
    cursor.execute("DELETE FROM karsakov_pletenev.CARSDTP WHERE dtp_id = %s",(id,))
    cursor.execute("DELETE FROM karsakov_pletenev.DTP WHERE id = %s",(id,))

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
    cursor.close()
    conn.close()
