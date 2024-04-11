SELECT 'CREATE DATABASE idlr_db' 
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'idlr_db');

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password1 VARCHAR(255) NOT NULL,
    email VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
); 

INSERT INTO users (username, password1, email) VALUES ('user', '123', 'user@user.com');