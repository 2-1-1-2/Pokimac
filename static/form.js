//Au chargement on affiche la liste des absences
document.addEventListener("DOMContentLoaded", async function () {
    const response = await fetch("/PokimacDresseurForm");
});


document.getElementById("type_id").addEventListener("click", choix_pokemon)


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

    const data = await response.json();

    changeData(data)

}

function changeData(data) {
    //console.log(data)
    let pokemon_totem_id = document.getElementById("pokemon_totem_id")
    //pokemon_totem_id
    console.log(data["Pokemon_aff"])
    pokemon_totem_id.innerHTML = "";
    let test = ""
    data["Pokemon_aff"].forEach(element => {
        test += ` <option value='${element}'>${element}</option> `

    });

    console.log(test)
    pokemon_totem_id.innerHTML = test;


}

document.getElementById("add").onclick = function create() {
    console.log("ça marche");
    const username = document.getElementById("username").value;
    const type_id = document.getElementById("type_id").value;
    const promotion_IMAC = document.getElementById("promotion_IMAC").value;
    const pokemon_totem_id = document.getElementById("pokemon_totem_id").value;
    const pokimacDresseur = { username, type_id, promotion_IMAC, pokemon_totem_id };

    const response = fetch("/PokimacDresseur", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'pokimac': pokimacDresseur }),
    });

    alert("enregistré !");

}


document.getElementById("add").onclick = function create() {
    console.log("ça marche 2");
    const username = document.getElementById("username").value;
    const type_id = document.getElementById("type_id").value;
    const promotion_IMAC = document.getElementById("promotion_IMAC").value;
    const pokemon_totem_id = document.getElementById("pokemon_totem_id").value;
    const pokimacDresseur = { username, type_id, promotion_IMAC, pokemon_totem_id };

    const response = fetch("/PokimacDresseur/" + id,{
        method: "PUT",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'pokimac': pokimacDresseur }),
    });

    alert("enregistré !");

}

