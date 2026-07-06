const planningModal =
    document.getElementById("planningModal");

const btnPlanning =
    document.getElementById("btnPlanning");

const closePlanning =
    document.querySelector(".close-planning");

const btnValiderPlanning =
    document.getElementById("validerPlanning");

btnPlanning.addEventListener("click", () => {

    planningModal.classList.add("show");

});

closePlanning.addEventListener("click", () => {

    planningModal.classList.remove("show");

});

window.addEventListener("click", (e) => {

    if(e.target === planningModal){

        planningModal.classList.remove("show");

    }

});

btnValiderPlanning.addEventListener("click", () => {

    const jour =
        document.getElementById("planningJour").value;

    const repas =
        document.getElementById("planningRepas").value;

    fetch("/planning", {

        method:"POST",

        headers:{

            "Content-Type":
            "application/x-www-form-urlencoded"

        },

        body:
            "recette=" +
            encodeURIComponent(recetteSelectionnee)
            +
            "&jour=" +
            encodeURIComponent(jour)
            +
            "&repas=" +
            encodeURIComponent(repas)

    })

    .then(response => response.json())

    .then(data => {

        if(data.success){

            alert("✅ Recette ajoutée au planning.");

            planningModal.classList.remove("show");

        }

        else{

            alert(data.message);

        }

    });

});