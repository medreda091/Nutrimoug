console.log("planning.js chargé");

const planningModal =
    document.getElementById("planningModal");

const closePlanning =
    document.querySelector(".close-planning");

const btnValiderPlanning =
    document.getElementById("validerPlanning");



closePlanning.addEventListener("click", () => {

    planningModal.classList.remove("show");

});

window.addEventListener("click", (e) => {

    if (e.target === planningModal) {

        planningModal.classList.remove("show");

    }

});



btnValiderPlanning.addEventListener("click", () => {

    const jour =
        document.getElementById("planningJour").value;

    const repas =
        document.getElementById("planningRepas").value;

    fetch("/planning", {

        method: "POST",

        headers: {

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

        if (data.success) {

            alert("✅ Recette ajoutée au planning.");

            planningModal.classList.remove("show");

            sessionStorage.setItem("activeTab", "planning");

            location.reload();

        }

        else {

            alert(data.message);

        }

    });

});


const boutonsSuppressionPlanning =
    document.querySelectorAll(".supprimer-planning");

boutonsSuppressionPlanning.forEach((bouton) => {

    bouton.addEventListener("click", () => {

        fetch("/supprimer_planning", {

            method: "POST",

            headers: {

                "Content-Type":
                    "application/x-www-form-urlencoded"

            },

            body:
                "id=" +
                encodeURIComponent(
                    bouton.dataset.id
                )

        })

        .then(response => response.json())

        .then(data => {

            if (data.success) {

                sessionStorage.setItem("activeTab", "planning");

                location.reload();

            }

            else {

                alert("Erreur lors de la suppression.");

            }

        });

    });

});