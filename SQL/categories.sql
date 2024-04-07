CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255),
    user_id VARCHAR(255)
)

-- INSERT STATEMENT
INSERT INTO categories ("name", "user_id") VALUES ('', '');

-- SELECT STATEMENT
SELECT * FROM categories WHERE user_id = ('')
