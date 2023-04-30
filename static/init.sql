CREATE DATABASE IF NOT EXISTS Pokimac;

USE Pokimac;

CREATE TABLE IF NOT EXISTS dresseurs (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  username varchar(255),
  team_dresseur_id integer,
  type_id integer,
  promotion_IMAC integer,
  pokemon_totem_id integer
);

CREATE TABLE IF NOT EXISTS equipe_dresseurs (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  nom varchar(255)
);

CREATE TABLE IF NOT EXISTS pokemons (
  id integer,
  pokedexID integer,
  name varchar(255),
  image varchar(255),
  sprite varchar(255),
  slug varchar(255),
  `apiTypes/0/name` varchar(255),
  `apiTypes/1/name` varchar(255),
  PRIMARY KEY (id, pokedexID)
);

CREATE TABLE IF NOT EXISTS types (
  id integer PRIMARY KEY,
  name varchar(255),
  iamge varchar(255),
  englishName varchar(255)
);

ALTER TABLE dresseurs ADD FOREIGN KEY (team_dresseur_id) REFERENCES equipe_dresseurs (id);

ALTER TABLE dresseurs ADD FOREIGN KEY (pokemon_totem_id) REFERENCES pokemons (id);

ALTER TABLE dresseurs ADD FOREIGN KEY (type_id) REFERENCES types (id);

LOAD DATA LOCAL INFILE './static/csv/pokemons.csv'
INTO TABLE pokemons
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './static/csv/types.csv'
INTO TABLE types
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
