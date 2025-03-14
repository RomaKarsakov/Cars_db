CREATE SCHEMA IF NOT EXISTS karsakov_pletenev;

CREATE TABLE IF NOT EXISTS karsakov_pletenev.CARS (
    id SERIAL PRIMARY KEY,
    model TEXT NOT NULL,
    year INT NOT NULL,
    color TEXT NOT NULL,
    number TEXT UNIQUE,
    car_type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS karsakov_pletenev.DTP (
    id SERIAL PRIMARY KEY,
    dtp_date DATE NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS karsakov_pletenev.CARSDTP (
    car_id integer references karsakov_pletenev.CARS(id),
    dtp_id integer references karsakov_pletenev.DTP(id)
);

