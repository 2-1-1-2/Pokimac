# Pokimac

## Pré-requis

`pip3 install Flask-Cors`
`sudo apt install mysql-server`
`pip install mysql-connector-python`

### Mysql

créer le profil pour la base de donner :
`CREATE USER 'IMAC'@'localhost' IDENTIFIED WITH mysql_native_password BY 'IMAC@2025@3490';`

ou

`CREATE USER 'IMAC'@'localhost' IDENTIFIED BY 'IMAC@2025@3490';`

s'il y a un problème avec le mot de passe :
SQL :
`ALTER USER 'IMAC'@'localhost' IDENTIFIED WITH mysql_native_password BY 'IMAC@2025@3490';`

## Lancer le programme

Mode normal : `flask --app server.py run`
Mode debug : `flask --app server.py --debug run`

## Taches et répartitions

### Pokimac dresseurs (Tanya)

- [ ] Création pokimac dresseur
- [ ] Supprimer pokimac dresseur
- [x] afficher pokimac (pokedex)

### Pokimacdex (Marion)

- [ ] Modification pokimac dresseur
- tri
  - [ ] Ordre alphabétique
  - [ ] Par type

### Affichage (Sara et/ou Nolwenn)

- [ ] afficher individuellement pokimac
- [ ] affichage par équipe
- [ ] Supprimer équipe

### Equipe (Sara et/ou Nolwenn)

- [ ] Création équipe
- [ ] Modification équipe
- [ ] Quitter équipe
