-- migrate:up

CREATE TABLE users (
    id          TEXT primary key,
    email       TEXT NOT NULL,
    password    TEXT NOT NULL,
    created_at  TIMESTAMP DEFAULT current_timestamp,
    modified_at TIMESTAMP,
    UNIQUE (email)
);

CREATE INDEX users_email_idx ON users(email);

-- migrate:down

DROP TABLE users;
