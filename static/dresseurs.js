//Au chargement on affiche la liste des absences
document.addEventListener("DOMContentLoaded", async function () {
    const response = await fetch("/PokimacDresseur");
});


document.getElementById("orderBy").addEventListener("change", trie)

async function trie() {
    const column = document.getElementById("orderBy").value;
    console.log("on trie par " + column);
    const response = await fetch("/PokimacDresseur", {
        method: "PUT",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'column_tri': column }),
    });

    const data = await response.json();

    changeData(data)

}

function changeData(data) {
    //console.log(data)
    let liste_dresseurs = document.getElementById("listeDresseurs")
    
    // console.log(data["PokimacDresseur_aff"][0])
    liste_dresseurs.innerHTML = "";
    let test = ""
    test += "<tr><th>ID</th><th>Nom</th><th>Team</th><th>Type</th><th>Promotion IMAC</th><th>Pokémon totem</th></tr>"

    data["PokimacDresseur_aff"].forEach(element => {
        test += "<tr>"
        i=0;
        element.forEach(value => {
            test += "<td>"
            if(i==0){
                test +=`<a href='/PokimacDresseur/${value}'>Fiche</a>`
                test += `<button class='btn update' id='${value}'>Modifier</button>`
                test += `<button class='btn delete' id='${value}'>Supprimer</button>`
            } else {
                test += `${value}`
            }
            test += "</td>"
            i++;
        })
        test += "</tr>"

        // test += ` <option value='${element}'>${element}</option> `

    });

    console.log(test)
    liste_dresseurs.innerHTML = test;


}

const buttons = document.getElementsByTagName("button");

const buttonPressed = e => {
    if (e.target.className.split(" ")[1] == "delete") delete_(e.target.id)
    // else if (e.target.className.split(" ")[1] == "update") update_(e.target.id)
    // Get ID of Clicked Element
}

for (let button of buttons) {
    button.addEventListener("click", buttonPressed);
}

async function delete_(id) {
    console.log(id)
    const response = await fetch("/PokimacDresseur/" + id, { method: 'DELETE' });
}


// async function update_(id) {
//     console.log("update "+id)
//     const response = await fetch("/PokimacDresseur/" +id, {method: 'PUT'});

//     // const username = document.getElementById("username").value;
//     // const type_id = document.getElementById("type_id").value;
//     // const promotion_IMAC = document.getElementById("promotion_IMAC").value;
//     // const pokemon_totem_id = document.getElementById("pokemon_totem_id").value;
//     // const pokimacDresseur = { username, type_id, promotion_IMAC, pokemon_totem_id };

//     // const response = await fetch("/PokimacDresseurForm/", { 
//     //     method: "PUT",
//     //     headers: {
//     //     Accept: "application/json",
//     //     "Content-Type": "application/json",
//     //     },
//     //     body: JSON.stringify({ 'id_dresseur': id }),
//     // });
// }


