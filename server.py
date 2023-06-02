# -*- coding: utf-8 -*-
import modules.dresseur as dresseur
from flask import Flask, redirect, url_for, request, render_template, jsonify, abort
from flask_cors import CORS
import modules.db as db
app = Flask(__name__)
CORS(app)


@ app.route("/")
def index():
    return render_template("index.html")


def toTeam(trainer, team):
    mycursor = db.mydb.cursor()
    mycursor.close()


@ app.route("/PokimacDresseur")
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
    return render_template("PokimacDresseur.html", PokimacDresseur_aff=affichage_dresseur)


@ app.route("/PokimacDresseurForm", methods=['GET', 'POST'])
def formDresseur():
    affichage_pokemon = []
    affichage_type = []
    affichage_team = []

    if request.method == 'POST':
        type = request.json["type"]
        print(type)
        idType = db.requestSelect_From("types", "id", "name", type)
        myresultPokemon = db.requestSelectColumn(
            "pokemons", "name", "type_0", type, True)

        for x in myresultPokemon:
            print(x)
            affichage_pokemon.append(x)

        myresultType = db.requestSelectColumn("types", "name")
        for x in myresultType:
            affichage_type.append(x)
        # data = {affichage_pokemon, affichage_type}
        return jsonify(Pokemon_aff=affichage_pokemon, Type_aff=affichage_type), 201

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
    return render_template("PokimacDresseurForm.html", Pokemon_aff=affichage_pokemon, Type_aff=affichage_type)


@ app.route("/PokimacDresseurFiche", methods=['GET'])
def afficherDresseurIndividuel():
    pokimac = request.args.get('pokimac')
    mycursor = db.mydb.cursor()
    mycursor.execute("""SELECT * FROM dresseurs WHERE id=%s""", [pokimac])
    affichage_fiche = mycursor.fetchall()

    affichage_fiche = affichage_fiche[0]
    titres_fiche = ["ID :", "Nom :", "Team :",
                    "Type :", "Promotion IMAC :", "Pokémon totem :"]

    mycursor.close()
    return render_template("PokimacDresseurFiche.html", ficheDresseur=affichage_fiche, ficheTitre=titres_fiche)


@ app.route("/ajouterPokimacDresseur", methods=['POST'])
def ajouterDresseur():
    pokimac = request.json["pokimac"]
    mycursor = db.mydb.cursor()
    pokimac["type_id"] = db.requestSelect_From(
        "types", "id", "name", pokimac["type_id"])
    pokimac["pokemon_totem_id"] = db.requestSelect_From(
        "pokemons", "id", "name", pokimac["pokemon_totem_id"])
    mycursor.execute("""INSERT INTO dresseurs (username, type_id, promotion_IMAC, pokemon_totem_id ) VALUES (%s, %s,  %s, %s)""",
                     (pokimac["username"], pokimac["type_id"], pokimac["promotion_IMAC"], pokimac["pokemon_totem_id"]))

    db.mydb.commit()
    mycursor.close()
    toTeam(pokimac["username"], pokimac["team"])
    print("Redirecting to /PokimacDresseur")
    return redirect('/PokimacDresseur')


@ app.route("/modifierPokimacDresseur")
def modifierDresseur():

    return redirect("/PokimacDresseur")


@ app.route("/supprimerPokimacDresseur", methods=['GET'])
def supprimerDresseur():
    pokimac = request.args.get('pokimac')
    mycursor = db.mydb.cursor()
    mycursor.execute("""DELETE FROM dresseurs WHERE id=%s""", [pokimac])
    db.mydb.commit()
    mycursor.close()
    return redirect("/PokimacDresseur")


# equipe

@ app.route("/PokimacEquipe")
def afficherEquipe():
    affichage_equipe = []
    mycursor = db.mydb.cursor()
    mycursor.execute(db.requestSelectAll("equipe_dresseurs"))
    myresult = mycursor.fetchall()

    for x in myresult:
        x = list(x)
        affichage_equipe.append(x)

    mycursor.close()
    return render_template("PokimacEquipe.html", PokimacEquipe_aff=affichage_equipe)


@ app.route("/AjoutEquipe")
def formEquipe():
    return render_template("AjoutEquipe.html")


@ app.route("/ajouterPokimacEquipe", methods=['POST'])
def ajouterEquipe():
    pokimac = request.json["pokimac"]
    mycursor = db.mydb.cursor()
    mycursor.execute(
        """INSERT INTO equipe_dresseurs (nom) VALUES (%s)""", (pokimac["nom"],))
    db.mydb.commit()
    mycursor.close()
    print("Redirecting to /PokimacEquipe")
    return redirect('/PokimacEquipe')


@ app.route("/modifierPokimacEquipe")
def modifierEquipe():

    return redirect("/PokimacEquipe")


@ app.route("/supprimerPokimacEquipe", methods=['GET'])
def supprimerEquipe():
    pokimac = request.args.get('pokimac')
    mycursor = db.mydb.cursor()
    mycursor.execute("""DELETE FROM equipe_dresseurs WHERE id=%s""", [pokimac])
    db.mydb.commit()
    mycursor.close()
    return redirect("/PokimacEquipe")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
