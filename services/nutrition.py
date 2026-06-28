def calculer_imc(poids, taille):

    imc = poids / ((taille / 100) ** 2)

    if imc < 18.5:
        categorie = "Maigreur"

    elif imc < 25:
        categorie = "Poids normal"

    elif imc < 30:
        categorie = "Surpoids"

    else:
        categorie = "Obésité"

    return round(imc, 1), categorie


def calculer_calories(poids, taille, age, sexe, activite, objectif):

    if sexe == "Homme":
        mb = 10 * poids + 6.25 * taille - 5 * age + 5

    else:
        mb = 10 * poids + 6.25 * taille - 5 * age - 161

    if activite == "Faible":
        calories = mb * 1.2

    elif activite == "Modéré":
        calories = mb * 1.55

    else:
        calories = mb * 1.725

    if objectif == "Perte de poids":
        calories -= 300

    elif objectif == "Prise de masse":
        calories += 300

    return round(calories)


def calculer_macros(calories, poids):

    proteines = poids * 2

    lipides = poids

    glucides = (calories - (proteines * 4 + lipides * 9)) / 4

    return (
        round(proteines),
        round(glucides),
        round(lipides)
    )


def calculer_eau(poids):

    return round(poids * 0.035, 1)


def calculer_conseil(imc):

    if imc < 18.5:

        return "Vous êtes en insuffisance pondérale. Augmentez progressivement vos apports caloriques."

    elif imc < 25:

        return "Votre poids est normal. Continuez à maintenir une alimentation équilibrée."

    elif imc < 30:

        return "Vous êtes en surpoids. Réduisez les aliments riches en sucres et graisses."

    else:

        return "Votre IMC est élevé. Privilégiez les légumes, l'activité physique et l'hydratation."