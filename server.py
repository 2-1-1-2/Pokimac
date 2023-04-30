# -*- coding: utf-8 -*-
from flask import Flask, redirect, request, render_template, jsonify, abort
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


if (mydb.is_connected()):  # Création de la DB et des tables si besoin
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


# Dresseurs
def requestSelect_FromId(id, table, column):
    cursorPokemon = mydb.cursor()
    cursorPokemon.execute(f"SELECT {column} FROM {table} WHERE id={id};")
    myresultPokemon = cursorPokemon.fetchone()
    cursorPokemon.close()
    return myresultPokemon[0]


@ app.route("/PokimacDresseur")
def afficherDresseur():
    affichage_dresseur = []
    mycursor = mydb.cursor()
    mycursor.execute(requestSelectAll("dresseurs"))
    myresult = mycursor.fetchall()

    for x in myresult:
        x = list(x)
        if (x[2] == None):
            x[2] = ""
        x[3] = requestSelect_FromId(x[3], "types", "name")
        x[5] = requestSelect_FromId(x[5], "pokemons", "name")
        affichage_dresseur.append(x)

    mycursor.close()
    return render_template("PokimacDresseur.html", PokimacDresseur_aff=affichage_dresseur)


@ app.route("/ajouterPokimacDresseur")
def ajouterDresseur():

    return redirect("/PokimacDresseur")


@ app.route("/modifierPokimacDresseur")
def modifierDresseur():

    return redirect("/PokimacDresseur")


@ app.route("/supprimerPokimacDresseur")
def supprimerDresseur():

    return redirect("/PokimacDresseur")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
