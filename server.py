# -*- coding: utf-8 -*-
from flask import Flask, redirect, request, render_template, jsonify, abort
from flask_cors import CORS
import mysql.connector
app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
    host="localhost",
    user="IMAC",
    password="IMAC@2025@3490"
)
if (mydb.is_connected()): # Création de la DB et des tables si besoin
    print("Connected")
    with open('./static/init.sql', 'r') as sql_file:
        mycursor = mydb.cursor()
        result_iterator = mycursor.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            print("Running query: ", res) 
            print(f"Affected {res.rowcount} rows" )
        mydb.commit() 
        mycursor.close()

else:
    print("Not connected")

@app.route("/")
def index():
    return render_template("index.html")


# Dresseurs

@app.route("/Pokimac") 
def afficherDresseur():
    affichage_dresseur={}
    cpt = 0
    mycursor = mydb.cursor()
    mycursor.execute("""select * from dresseurs;""")
    for pokimac in mycursor:
        affichage_dresseur[cpt] = pokimac
        cpt+=1
    print("affichage : \n")
    print(affichage_dresseur)
    print("\n cpt " + str(cpt) + "\n")
    mycursor.close()
    return render_template("Pokimac.html", pokimac_aff = affichage_dresseur)


@app.route("/ajouterPokimac") 
def ajouterDresseur():

    return redirect("/Pokimac")

@app.route("/modifierPokimac") 
def modifierDresseur():

    return redirect("/Pokimac")

@app.route("/supprimerPokimac") 
def supprimerDresseur():

    return redirect("/Pokimac")





if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
