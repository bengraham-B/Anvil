CREATE TABLE transaction(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(255),
    details VARCHAR(255),
    amount FLOAT,
    category VARCHAR(255),
    class VARCHAR(255),
    date DATE
);
