-- list the records of a table ignoring those with null values for name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
