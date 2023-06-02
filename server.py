# -*- coding: utf-8 -*-
import modules.dresseur as dresseur
from flask import Flask, redirect, url_for, request, render_template, jsonify, abort
from flask_cors import CORS
import modules.db as db
import modules.dresseur as pokiD
import modules.equipe as pokiE
app = Flask(__name__)
CORS(app)


@ app.route("/")
def index():
    return render_template("index.html")


@ app.route("/PokimacDresseur", methods=['GET', 'POST'])
def PokimacDresseur():
    if request.method == 'GET':
        affichage_dresseur = pokiD.afficherDresseur()
        return render_template("PokimacDresseur.html", PokimacDresseur_aff=affichage_dresseur)
    elif request.method == 'POST':
        pokimac = request.json["pokimac"]
        pokiD.ajouterDresseur(pokimac)
        return redirect('/PokimacDresseur')


@ app.route("/PokimacDresseur/<int:id>",  methods=['PUT', 'DELETE', 'GET'])
def PokimacDresseurModif(id):
    if request.method == 'DELETE':
        print("DELETE : " + str(id))
        print("on supprime \n")
        pokiD.supprimerDresseur(id)

    elif request.method == 'PUT':
        pokiD.modifierDresseur(id)
    elif request.method == 'GET':
        affichage_fiche, titres_fiche = pokiD.profilDresseur(id)
        return render_template("PokimacDresseurFiche.html", ficheDresseur=affichage_fiche, ficheTitre=titres_fiche)

# TODO : RECHARGER LA PAGE OU
    return redirect("/PokimacDresseur")


@ app.route("/PokimacDresseurForm", methods=['GET', 'POST'])
def formDresseur():
    if request.method == 'POST':
        type = request.json["type"]
        affichage_pokemon, affichage_type, affichage_team = pokiD.typeAdaptation(
            type)
        return jsonify(Pokemon_aff=affichage_pokemon, Type_aff=affichage_type), 201

    elif request.method == 'GET':
        affichage_pokemon, affichage_type, affichage_team = pokiD.affichageForm()
        return render_template("PokimacDresseurForm.html", Pokemon_aff=affichage_pokemon, Type_aff=affichage_type)


# equipe

@ app.route("/PokimacEquipe")
def afficherEquipe():

    affichage_equipe = pokiE.afficherEquipe()
    return render_template("PokimacEquipe.html", PokimacEquipe_aff=affichage_equipe)


@ app.route("/Equipe", methods=['GET', 'POST'])
def formEquipe():
    if request.method == 'GET':
        return render_template("AjoutEquipe.html")

    if request.method == 'POST':
        pokiE.ajouterEquipe(request.json["pokimac"])
        return redirect('/PokimacEquipe')


@ app.route("/Equipe/<int:id>",  methods=['PUT', 'DELETE'])
def PokimacEquipeModif(id):
    if request.method == 'DELETE':
        print("DELETE : " + str(id))
        print("on supprime \n")
        pokiE.supprimerEquipe(id)

    elif request.method == 'PUT':
        pokiD.modifierEquipe(id)
# TODO : RECHARGER LA PAGE OU
    return redirect("/PokimacEquipe")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
