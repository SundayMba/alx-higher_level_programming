-- script that converts hbtn_0c_0 database to UTF8
-- (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

-- CONVERT DATABASE TO utf8mb4
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- CONVERT TABLE TO utf8mb4
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- CONVERT COLUMN TO utf8mb4
ALTER TABLE first_table
MODIFY name
VARCHAR(256) COLLATE utf8mb4_unicode_ci;
