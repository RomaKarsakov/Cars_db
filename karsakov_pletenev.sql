CREATE TABLE IF NOT EXISTS CARS (
    id SERIAL PRIMARY KEY,
    model TEXT NOT NULL,
    year INT NOT NULL,
    color TEXT NOT NULL,
    number TEXT UNIQUE,
    car_type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS DTP (
    id SERIAL PRIMARY KEY,
    dtp_date DATE NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS CARSDTP (
    car_id integer references CARS(id),
    dtp_id integer references DTP(id)
);

