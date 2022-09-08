-- list all records with a score >= 10 in the table of the database
SELECT score, name FROM second_table WHERE id >= 10 GROUP BY score DESC;
