//Au chargement on affiche la liste des absences
document.addEventListener("DOMContentLoaded", async function () {
    const response = await fetch("/ajout");
    const data = await response.json();
});

document.getElementById("add").onclick = create();
/*
test = addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        create();
    }
});

let input = document.getElementById("name");
input.test;
*/

async function choix_pokemon() {
    console.log("ça marche");
    const name = document.getElementById("name").value;
    const price = document.getElementById("price").value;
    const desc = document.getElementById("desc").value;
    const jeu = { name, price, desc };

    const guess = "13";
    const response = await fetch("/ajout", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ game: guess }),
    });
    //register(`POST : Il pense que c'est ${guess.value}`, response.status);

    const data = await response.json();
}
