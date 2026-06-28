const boutons = document.querySelectorAll(".tab-btn");
const contenus = document.querySelectorAll(".tab-content");

boutons.forEach((bouton) => {

    bouton.addEventListener("click", () => {

        boutons.forEach((b) => b.classList.remove("active"));
        contenus.forEach((c) => c.classList.remove("active"));

        bouton.classList.add("active");

        document
            .getElementById(bouton.dataset.tab)
            .classList.add("active");

    });

});

const graphique = document.getElementById("graphiquePoids");

if (graphique) {

    const poids = JSON.parse(graphique.dataset.poids);

    const labels = [];

    for (let i = 0; i < poids.length; i++) {

        labels.push("Mesure " + (i + 1));

    }

    new Chart(graphique, {

        type: "line",

        data: {

            labels: labels,

            datasets: [{

                label: "Evolution du poids",

                data: poids,

                borderWidth: 3,

                tension: 0.4

            }]

        },

        options: {

            responsive: true

        }

    });

}