CREATE DATABASE IF NOT EXISTS Pokimac;

USE Pokimac;

CREATE TABLE IF NOT EXISTS dresseurs (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  username varchar(255),
  team_dresseur_id integer REFERENCES equipe_dresseurs (id),
  type_id integer REFERENCES types (id),
  promotion_IMAC integer,
  pokemon_totem_id integer REFERENCES pokemons (id)
);

CREATE TABLE IF NOT EXISTS equipe_dresseurs (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  nom varchar(255)
);

CREATE TABLE IF NOT EXISTS types (
  id integer PRIMARY KEY,
  name varchar(255),
  image varchar(255),
  englishName varchar(255)
);


CREATE TABLE IF NOT EXISTS pokemons (
  id integer,
  pokedexID integer,
  name varchar(255),
  slug varchar(255),
  type_0 varchar(255) REFERENCES types(name),
  type_1 varchar(255) REFERENCES types(name),
  PRIMARY KEY (id, pokedexID)
);



