const btnFavori =
    document.getElementById("btnFavori");

btnFavori.addEventListener("click", () => {

    fetch("/favori", {

        method: "POST",

        headers: {

            "Content-Type":
                "application/x-www-form-urlencoded"

        },

        body:
            "recette=" +
            encodeURIComponent(
                recetteSelectionnee
            )

    })

    .then(response => response.json())

    .then(data => {

        if(data.success){

            sessionStorage.setItem(
                "activeTab",
                "favoris"
            );

            location.reload();

        }

        else{

            alert(data.message);

        }

    });

});

const boutonsSuppressionFavori =
    document.querySelectorAll(".supprimer-favori");

boutonsSuppressionFavori.forEach((bouton) => {

    bouton.addEventListener("click", () => {

        if(!confirm("Supprimer cette recette des favoris ?")){

            return;

        }

        fetch("/supprimer_favori", {

            method: "POST",

            headers: {

                "Content-Type":
                    "application/x-www-form-urlencoded"

            },

            body:
                "recette=" +
                encodeURIComponent(
                    bouton.dataset.recette
                )

        })

        .then(response => response.json())

        .then(data => {

            if(data.success){

                sessionStorage.setItem(
                    "activeTab",
                    "favoris"
                );

                location.reload();

            }

        });

    });

});