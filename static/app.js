document.addEventListener("DOMContentLoaded", async function () {
    const response = await fetch("/PokimacDresseur");
});


document.getElementById("orderBy").onchange = function create() {
    console.log("bloup");
    const column_tri = document.getElementById("orderBy").value;
    
    const response = fetch("PokimacDresseur", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'column_tri': column_tri }),
    });

}


document.getElementsByName("modify").forEach(item => {
    item.addEventListener('click', modifier) })
   
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