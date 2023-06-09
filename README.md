# Pokimac

## Pré-requis

`pip3 install Flask-Cors`
`sudo apt install mysql-server`
`pip install mysql-connector-python`

### Mysql

créer le profil pour la base de donnée :
`CREATE USER 'IMAC'@'localhost' IDENTIFIED WITH mysql_native_password BY 'IMAC@2025@3490';`

ou

`CREATE USER 'IMAC'@'localhost' IDENTIFIED BY 'IMAC@2025@3490';`

s'il y a un problème avec le mot de passe :
SQL :
`ALTER USER 'IMAC'@'localhost' IDENTIFIED WITH mysql_native_password BY 'IMAC@2025@3490';`

Pour avoir les droits :
`GRANT ALL PRIVILEGES ON * . * TO 'IMAC'@'localhost';`

## Lancer le programme

Mode normal : `flask --app server.py run`
Mode debug : `flask --app server.py --debug run`

## Taches et répartitions

### Pour la V1

#### Pokimac dresseurs (Tanya)

- [x] Création pokimac dresseur
- [x] Supprimer pokimac dresseur
- [x] afficher pokimac (pokedex)

---

#### Pokimac dresseurs (Tanya) - Amélioration :

- [x] pokémon choisi correspond au type sélectionné
- [x] Pouvoir ajouter les team dès l'inscription (toTeam())
- [x] Redirection correcte

#### Pokimacdex (Marion)

- [ ] Modification pokimac dresseur
- tri
  - [ ] Ordre alphabétique
  - [ ] Par type

#### Affichage (Sara)

- [x] afficher individuellement pokimac
- [ ] affichage par équipe
- [x] Supprimer équipe

#### Equipe (Nolwenn)

- [x] Création équipe
- [ ] Modification équipe
- [ ] Quitter équipe

#### Bonus

- [ ] Système de compte avec 1 dresseur par compte

#### Autres

- [ ] Changer equipe_dresseurs => teams
- [ ] Changer teams.nom => teams.name
- [ ] Changer dresseurs => trainers
- [ ] Dans l'affichage équipe : lien menant au profil sur les noms
