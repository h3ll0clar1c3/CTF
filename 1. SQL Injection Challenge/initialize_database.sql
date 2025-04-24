-- Initialize the challenge database
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE flags (
    id INTEGER PRIMARY KEY,
    flag TEXT
);

-- Insert initial data
INSERT INTO users (id, username, password) VALUES (1, 'admin', 'admin');
INSERT INTO flags (id, flag) VALUES (1, 'CTF{sql_injection_flag}');