CREATE TABLE transaction(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(255),
    details VARCHAR(255),
    amount FLOAT,
    category VARCHAR(255),
    class VARCHAR(255),
    date DATE,
    day INT,
    month INT,
    year INT
);

ALTER TABLE transaction  
    ADD month VARCHAR(255),
    ADD year VARCHAR(255)

ALTER TABLE transaction
    ADD day VARCHAR(255)
