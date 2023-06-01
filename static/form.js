//Au chargement on affiche la liste des absences
document.addEventListener("DOMContentLoaded", async function () {
    const response = await fetch("/PokimacDresseurForm");
});
document.addEventListener("DOMContentLoaded", async function () {
    const response = await fetch("/AjoutEquipe");
});


/*


let input = document.getElementById("name");
input.test;
*/
/*
document.getElementById("username").addEventListener("change", choix_pokemon())

async function choix_pokemon() {
    const type_id = document.getElementById("type_id").value;
    console.log("on cherche un pokémon de type " + type_id);
    const response = await fetch("/PokimacDresseurForm", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ type: type_id }),
    });

}*/

document.getElementById("add").onclick = function create() {
    console.log("ça marche");
    const username = document.getElementById("username").value;
    const type_id = document.getElementById("type_id").value;
    const promotion_IMAC = document.getElementById("promotion_IMAC").value;
    const pokemon_totem_id = document.getElementById("pokemon_totem_id").value;
    const pokimacDresseur = { username, type_id, promotion_IMAC, pokemon_totem_id };

    const response = fetch("/ajouterPokimacDresseur", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'pokimac': pokimacDresseur }),
    });

    alert("enregistré !");

}


document.getElementById("addEquipe").onclick = function create() {
    console.log("ça marche");
    const nom = document.getElementById("nom").value;
    const pokimacEquipe = { nom };

    const response = fetch("/ajouterPokimacEquipe", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'pokimacE': pokimacEquipe }),
    });

    alert("enregistré !");

}
