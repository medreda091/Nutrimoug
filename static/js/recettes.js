const boutonsRecette =
    document.querySelectorAll(".recipe-btn");

boutonsRecette.forEach((bouton) => {

    bouton.addEventListener("click", () => {

        ouvrirModal(bouton);

    });

});

const boutonsVoirFavori =
    document.querySelectorAll(".voir-favori");

boutonsVoirFavori.forEach((bouton) => {

    bouton.addEventListener("click", () => {

        ouvrirModal(bouton);

    });

});