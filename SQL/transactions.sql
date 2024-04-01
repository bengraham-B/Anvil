CREATE TABLE transactions(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(255),
    details VARCHAR(255),
    category VARCHAR(255),
    amount INT,
    class class_enum

)

CREATE TYPE class_enum AS ENUM('debit', 'credit');
