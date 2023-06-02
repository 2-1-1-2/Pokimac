document.addEventListener("DOMContentLoaded", async function () {
    const response = await fetch("/PokimacDresseur");
});

console.log("biiip");

// document.getElementById("orderBy").onchange = function create() {
//     console.log("bloup");
//     const column_tri = document.getElementById("orderBy").value;
    
//     const response = fetch("PokimacDresseur", {
//         method: "POST",
//         headers: {
//             Accept: "application/json",
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify({ 'column_tri': column_tri }),
//     });

// }

document.getElementById("orderBy").addEventListener("change", tri);

async function tri() {
    const column_tri = document.getElementById("orderBy").value;
    console.log("on trie par " + column_tri);
    const response = await fetch("/PokimacDresseur", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'column': column_tri }),
    });

    // const data = await response.json();

    // changeData(data)

}

function changeData(data) {
    //console.log(data)
    let dresseurs = document.getElementById("pokemon_totem_id")
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


document.getElementsByName("modify").forEach(item => {
    console.log("zap");
    item.addEventListener('click', modifier); })
   
//  document.getElementById("modify1").addEventListener("click", choix_pokemon)


async function modifier() {
    console.log("ça marche 3");
    const id = this.value;

    const response = await fetch("/PokimacDresseurForm", {
        method: "PUT",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'id_dresseur': id }),
    });
}