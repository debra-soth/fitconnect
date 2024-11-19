CREATE TABLE person (
    username TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT,
    age INTEGER,
    fitness_level TEXT,
    gym_membership INTEGER,
    activities TEXT,
    availability TEXT,
    motivation_text TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    profile_photo TEXT

);