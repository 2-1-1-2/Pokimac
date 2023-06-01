# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, request, render_template, jsonify, abort
from flask_cors import CORS
import mysql.connector
import csv
app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
    host="localhost",
    user="IMAC",
    password="IMAC@2025@3490"
)


def requestInsert(table, head):
    return (
        f"INSERT IGNORE INTO {table} " +
        f"({', '.join([f'{_}' for _ in head])})"+" VALUES "
        + f"""({', '.join([f'%s' for _ in head])});"""
    )


def requestSelectAll(table):
    return f"SELECT * FROM {table}; "


def initDB(filename, db):
    file = open(filename, mode='r', encoding='utf-8-sig')
    csv_data = csv.reader(file)
    header = {}
    mycursor = mydb.cursor()
    skipHeader = True
    for row in csv_data:
        if skipHeader:
            header = row[0].split(";")
            skipHeader = False
            continue
        args = row[0].split(';')
        requete = requestInsert(db, header)
        mycursor.execute(requete, args)
    mydb.commit()
    mycursor.close()


if (mydb.is_connected()):  # CrÃ©ation de la DB et des tables si besoin
    print("Connected")
    with open('./static/init.sql', 'r') as sql_file:
        mycursor = mydb.cursor()
        result_iterator = mycursor.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            pass
        mydb.commit()
        mycursor.close()
        initDB('./static/csv/pokemons.csv', 'pokemons')
        initDB('./static/csv/types.csv', 'types')
else:
    print("Not connected")


@ app.route("/")
def index():
    return render_template("index.html")


def requestSelect_From(table, column, where, value):
    cursor = mydb.cursor()
    cursor.execute(
        f"SELECT {column} FROM {table} WHERE {where}='{value}';")
    result = cursor.fetchone()
    cursor.close()
    return result[0]


def requestSelectColumn(table, column, where="", value="", condition=False):
    cursor = mydb.cursor()
    if (condition):
        cursor.execute(f"SELECT {column} FROM {table} WHERE {where}='{value}';")
    else:
        cursor.execute(f"SELECT {column} FROM {table};")
    result = cursor.fetchall()
    cursor.close()
    return result


@ app.route("/PokimacDresseur")
def afficherDresseur():
    affichage_dresseur = []
    mycursor = mydb.cursor()
    mycursor.execute(requestSelectAll("dresseurs"))
    myresult = mycursor.fetchall()

    for x in myresult:
        x = list(x)
        #x[0] = f'<a href="/supprimerPokimacDresseur?pokimac={x[0]}">X</a>'
        if (x[2] == None):
            x[2] = ""
        x[3] = requestSelect_From("types", "name", "id", x[3])
        x[5] = requestSelect_From("pokemons", "name", "id", x[5])
        affichage_dresseur.append(x)

    mycursor.close()
    return render_template("PokimacDresseur.html", PokimacDresseur_aff=affichage_dresseur)


@ app.route("/PokimacDresseurFiche", methods=['GET'])
def afficherDresseurIndividuel():
    pokimac = request.args.get('pokimac')
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT * FROM dresseurs WHERE id=%s""", [pokimac])
    affichage_fiche = mycursor.fetchall()

    for elt in affiche_fiche[0]:
        print(elt)

    mycursor.close()
    return render_template("PokimacDresseurFiche.html", ficheDresseur = affichage_fiche)
    

@ app.route("/PokimacDresseurForm")
def formDresseur():
    affichage_pokemon = []
    affichage_type = []
    """
    if request.method == 'POST':
        type = request.json["type"]
        print(type)
        idType = requestSelect_From("types", "id", "name", type)
        myresultPokemon = requestSelectColumn("types", "name", "id", idType, True)
        for x in myresultPokemon:
            affichage_pokemon.append(x)

        myresultType = requestSelectColumn("types", "name")
        for x in myresultType:
            affichage_type.append(x)
        data = {affichage_pokemon, affichage_type}
        return jsonify(Pokemon_aff=affichage_pokemon, Type_aff=affichage_type), 201
    """
    myresultPokemon = requestSelectColumn("pokemons", "name")
    for x in myresultPokemon:
        affichage_pokemon.append(x)

    myresultType = requestSelectColumn("types", "name")
    for x in myresultType:
        affichage_type.append(x)
    return render_template("PokimacDresseurForm.html", Pokemon_aff=affichage_pokemon, Type_aff=affichage_type)



@ app.route("/ajouterPokimacDresseur", methods=['POST'])
def ajouterDresseur():
    pokimac = request.json["pokimac"]
    mycursor = mydb.cursor()
    pokimac["type_id"] = requestSelect_From("types", "id", "name", pokimac["type_id"])
    pokimac["pokemon_totem_id"] = requestSelect_From("pokemons", "id", "name", pokimac["pokemon_totem_id"])
    mycursor.execute("""INSERT INTO dresseurs (username, type_id, promotion_IMAC, pokemon_totem_id ) VALUES (%s, %s,  %s, %s)""", (pokimac["username"], pokimac["type_id"], pokimac["promotion_IMAC"], pokimac["pokemon_totem_id"]))
    mydb.commit()
    mycursor.close()
    print("Redirecting to /PokimacDresseur")
    return redirect('/PokimacDresseur') 


@ app.route("/modifierPokimacDresseur")
def modifierDresseur():

    return redirect("/PokimacDresseur")


@ app.route("/supprimerPokimacDresseur", methods=['GET'])
def supprimerDresseur():
    pokimac = request.args.get('pokimac')
    mycursor = mydb.cursor()
    mycursor.execute("""DELETE FROM dresseurs WHERE id=%s""", [pokimac])
    mydb.commit()
    mycursor.close()
    return redirect("/PokimacDresseur")



@ app.route("/PokimacEquipe")
def afficherEquipe():
    affichage_equipe = []
    mycursor = mydb.cursor()
    mycursor.execute(requestSelectAll("equipe_dresseurs"))
    myresult = mycursor.fetchall()

    for x in myresult:
        x = list(x)
        affichage_equipe.append(x)

    mycursor.close()
    return render_template("PokimacEquipe.html", PokimacEquipe_aff=affichage_equipe)


@ app.route("/ajouterPokimacEquipe", methods=['POST'])
def ajouterEquipe():
    pokimac = request.json["pokimac"]
    mycursor = mydb.cursor()
    mycursor.execute("""INSERT INTO equipe_dresseurs (username) VALUES (%s)""", (pokimac["name"]))
    mydb.commit()
    mycursor.close()
    print("Redirecting to /PokimacEquipe")
    return redirect('/PokimacEquipe') 


@ app.route("/modifierPokimacEquipe")
def modifierEquipe():

    return redirect("/PokimacEquipe")


@ app.route("/supprimerPokimacEquipe", methods=['GET'])
def supprimerEquipe():
    pokimac = request.args.get('pokimac')
    mycursor = mydb.cursor()
    mycursor.execute("""DELETE FROM equipe_dresseurs WHERE id=%s""", [pokimac])
    mydb.commit()
    mycursor.close()
    return redirect("/PokimacEquipe")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
