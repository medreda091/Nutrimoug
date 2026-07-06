const btnFavori = document.getElementById("btnFavori");

btnFavori.addEventListener("click", () => {

    fetch("/favori", {

        method: "POST",

        headers: {

            "Content-Type": "application/x-www-form-urlencoded"

        },

        body:
            "recette=" +
            encodeURIComponent(recetteSelectionnee)

    })

    .then((response) => response.json())

    .then((data) => {

        if(data.success){

            btnFavori.innerHTML =
                "❤️ Ajoutée aux favoris";

            btnFavori.disabled = true;

        }

        else{

            alert(data.message);

        }

    });

});

const boutonsSuppression =
    document.querySelectorAll(".supprimer-favori");

boutonsSuppression.forEach((bouton)=>{

    bouton.addEventListener("click",()=>{

        if(!confirm("Supprimer cette recette des favoris ?")){

            return;

        }

        fetch("/supprimer_favori",{

            method:"POST",

            headers:{

                "Content-Type":"application/x-www-form-urlencoded"

            },

            body:
                "recette=" +
                encodeURIComponent(
                    bouton.dataset.recette
                )

        })

        .then((response)=>response.json())

        .then((data)=>{

            if(data.success){

                bouton
                    .closest(".recipe-card")
                    .remove();

                if(document.querySelectorAll("#favoris .recipe-card").length===0){

                    document.getElementById("favoris").innerHTML=`

                        <div class="section-card">

                            <h2>❤️ Mes recettes favorites</h2>

                            <p>Aucune recette favorite.</p>

                        </div>

                    `;

                }

            }

        });

    });

});