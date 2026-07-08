# iPhone Hunter Réunion
# Système de notation des opportunités

def calculer_score(rentabilite, demande, reparation, fiabilite, rapidite):
    """
    Calcule un score sur 100

    Rentabilité : 40 points
    Demande modèle : 20 points
    Réparation : 15 points
    Fiabilité annonce : 15 points
    Rapidité revente : 10 points
    """

    score = (
        rentabilite +
        demande +
        reparation +
        fiabilite +
        rapidite
    )

    return score


def analyser_opportunite(prix_achat, prix_revente, cout_reparation):
    investissement = prix_achat + cout_reparation

    gain = prix_revente - investissement

    if prix_achat > 0:
        marge = (gain / prix_achat) * 100
    else:
        marge = 0

    return {
        "investissement": investissement,
        "gain": gain,
        "marge": round(marge, 2)
    }


# Test
if __name__ == "__main__":
    resultat = analyser_opportunite(
        prix_achat=300,
        prix_revente=650,
        cout_reparation=50
    )

    print(resultat)
