DROP TABLE IF EXISTS bucketlist;
DROP TABLE IF EXISTS cities;


CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visited BOOLEAN
);



CREATE TABLE bucketlist (
  id SERIAL PRIMARY KEY
  
);
