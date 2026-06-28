def generer_menu(preference):

    if preference == "Vegan":

        return {
            "petit_dejeuner": "Porridge, lait végétal et fruits",
            "dejeuner": "Quinoa, pois chiches et légumes",
            "collation": "Amandes et pomme",
            "diner": "Tofu et légumes sautés"
        }

    elif preference == "Végétarien":

        return {
            "petit_dejeuner": "Yaourt, flocons d'avoine et fruits",
            "dejeuner": "Omelette, riz et légumes",
            "collation": "Noix et banane",
            "diner": "Pâtes et légumes"
        }

    elif preference == "Halal":

        return {
            "petit_dejeuner": "Pain complet, œufs et lait",
            "dejeuner": "Poulet halal, riz et légumes",
            "collation": "Yaourt et amandes",
            "diner": "Poisson et salade"
        }

    return {
        "petit_dejeuner": "Flocons d'avoine, lait et banane",
        "dejeuner": "Poulet, riz et légumes",
        "collation": "Yaourt et amandes",
        "diner": "Poisson, pommes de terre et salade"
    }