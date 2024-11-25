CREATE TABLE user (
    username TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT,
    fitness_level INTEGER NOT NULL,
    gym_membership TEXT, 
    activities TEXT,
    motivation_text TEXT,
    profile_photo TEXT

);

CREATE TABLE matches (
    match_id INTEGER PRIMARY KEY,
    username_1 TEXT NOT NULL,
    username_2 TEXT NOT NULL,
    confirmed BOOLEAN DEFAULT 0,

    FOREIGN KEY (username_1) REFERENCES user(username),
    FOREIGN KEY (username_2) REFERENCES user(username),
);