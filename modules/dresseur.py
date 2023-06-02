# -*- coding: utf-8 -*-
import modules.db as db


def toTeam(trainer, team):
    mycursor = db.mydb.cursor()
    mycursor.close()


def afficherDresseur():
    affichage_dresseur = []
    mycursor = db.mydb.cursor()
    mycursor.execute(db.requestSelectAll("dresseurs"))
    myresult = mycursor.fetchall()

    for x in myresult:
        x = list(x)
        # x[0] = f'<a href="/supprimerPokimacDresseur?pokimac={x[0]}">X</a>'
        if (x[2] == None):
            x[2] = ""
        x[3] = db.requestSelect_From("types", "name", "id", x[3])
        x[5] = db.requestSelect_From("pokemons", "name", "id", x[5])
        affichage_dresseur.append(x)

    mycursor.close()
    return affichage_dresseur


def ajouterDresseur(pokimac):
    mycursor = db.mydb.cursor()
    pokimac["type_id"] = db.requestSelect_From(
        "types", "id", "name", pokimac["type_id"])
    pokimac["pokemon_totem_id"] = db.requestSelect_From(
        "pokemons", "id", "name", pokimac["pokemon_totem_id"])
    mycursor.execute("""INSERT INTO dresseurs (username, type_id, promotion_IMAC, pokemon_totem_id ) VALUES (%s, %s,  %s, %s)""",
                     (pokimac["username"], pokimac["type_id"], pokimac["promotion_IMAC"], pokimac["pokemon_totem_id"]))

    db.mydb.commit()
    mycursor.close()
    # toTeam(pokimac["username"], pokimac["team"])
    print("Redirecting to /PokimacDresseur")


def typeAdaptation(type):
    affichage_pokemon = []
    affichage_type = []
    affichage_team = []
    print(type)
    # idType = db.requestSelect_From("types", "id", "name", type)
    myresultPokemon = db.requestSelectColumn(
        "pokemons", "name", "type_0", type, True)

    for x in myresultPokemon:
        print(x)
        affichage_pokemon.append(x)

    myresultType = db.requestSelectColumn("types", "name")
    for x in myresultType:
        affichage_type.append(x)

    return affichage_pokemon, myresultType, affichage_team
    # data = {affichage_pokemon, affichage_type}


def affichageForm():
    affichage_pokemon = []
    affichage_type = []
    affichage_team = []
    myresultType = db.requestSelectColumn("types", "name")
    for x in myresultType:
        affichage_type.append(x)

        """
        myresulTeam = db.requestSelectColumn("equipe_dresseurs", "nom")
        for x in myresulTeam:
            affichage_team.append(x)
            """

    myresultPokemon = db.requestSelectColumn(
        "pokemons", "name", "type_0", affichage_type[0][0], True)
    for x in myresultPokemon:
        affichage_pokemon.append(x)
    return affichage_pokemon, affichage_type, affichage_team


def supprimerDresseur(id):
    mycursor = db.mydb.cursor()
    mycursor.execute("""DELETE FROM dresseurs WHERE id=%s""", [id])
    db.mydb.commit()
    mycursor.close()


def modifierDresseur(id):
    print("cc on modifie")


def profilDresseur(id):
    mycursor = db.mydb.cursor()
    print("GET ID profil" + str(id))
    mycursor.execute("""SELECT * FROM dresseurs WHERE id=%s""", [id])
    affichage_fiche = mycursor.fetchall()

    affichage_fiche = affichage_fiche[0]
    titres_fiche = ["ID :", "Nom :", "Team :",
                    "Type :", "Promotion IMAC :", "Pokémon totem :"]

    mycursor.close()
    return affichage_fiche, titres_fiche
