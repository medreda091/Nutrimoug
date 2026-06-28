def calculer_statistiques(historique):

    if not historique:

        return 0, 0, 0

    poids = [float(m["poids"]) for m in historique]

    poids_min = min(poids)

    poids_max = max(poids)

    poids_moyen = round(sum(poids) / len(poids), 1)

    return poids_min, poids_max, poids_moyen