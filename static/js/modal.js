const modal = document.getElementById("recipeModal");

const closeBtn = document.querySelector(".close");

let recetteSelectionnee = "";

function ouvrirModal(bouton){

    recetteSelectionnee = bouton.dataset.nom;

    document.getElementById("modalImage").src =
        bouton.dataset.image;

    document.getElementById("modalNom").textContent =
        bouton.dataset.nom;

    document.getElementById("modalCalories").textContent =
        "🔥 " + bouton.dataset.calories + " kcal";

    document.getElementById("modalProteines").textContent =
        "🥩 " + bouton.dataset.proteines + " g";

    document.getElementById("modalGlucides").textContent =
        "🍚 " + bouton.dataset.glucides + " g";

    document.getElementById("modalLipides").textContent =
        "🥑 " + bouton.dataset.lipides + " g";

    document.getElementById("modalTemps").textContent =
        bouton.dataset.temps;

    document.getElementById("modalPortions").textContent =
        bouton.dataset.portions;

    document.getElementById("modalObjectif").textContent =
        bouton.dataset.objectif;

    const listeIngredients =
        document.getElementById("modalIngredients");

    listeIngredients.innerHTML = "";

    bouton.dataset.ingredients
        .split(",")
        .forEach((ingredient) => {

            const li = document.createElement("li");

            li.textContent = ingredient.trim();

            listeIngredients.appendChild(li);

        });

    const listePreparation =
        document.getElementById("modalPreparation");

    listePreparation.innerHTML = "";

    bouton.dataset.preparation
        .split("|")
        .forEach((etape) => {

            const li = document.createElement("li");

            li.textContent = etape.trim();

            listePreparation.appendChild(li);

        });

    document.body.style.overflow = "hidden";

    modal.classList.add("show");

}

function fermerModal(){

    modal.classList.remove("show");

    document.body.style.overflow = "auto";

}

closeBtn.addEventListener("click", fermerModal);

window.addEventListener("click", (e) => {

    if(e.target === modal){

        fermerModal();

    }

});

document.addEventListener("keydown", (e) => {

    if(e.key === "Escape" && modal.classList.contains("show")){

        fermerModal();

    }

});