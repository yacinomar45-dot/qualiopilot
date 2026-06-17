import json
from datetime import datetime

def generer_rapport(nom_fichier, resultat_analyse):
    # Date du rapport
    date = datetime.now().strftime("%d/%m/%Y à %H:%M")

    # Récupérer les données de l'analyse
    preuves = resultat_analyse.get("preuves_trouvees", [])
    manquants = resultat_analyse.get("elements_manquants", [])
    score = resultat_analyse.get("score_conformite", 0)
    commentaire = resultat_analyse.get("commentaire", "")

    # Construire le rapport
    rapport = f"""
╔══════════════════════════════════════════════════════╗
║           RAPPORT DE CONFORMITÉ QUALIOPI             ║
╚══════════════════════════════════════════════════════╝

Document analysé : {nom_fichier}
Date du rapport  : {date}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORE DE CONFORMITÉ : {score}/100
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ PREUVES TROUVÉES ({len(preuves)}) :
"""
    for preuve in preuves:
        rapport += f"   • {preuve}\n"

    rapport += f"""
❌ ÉLÉMENTS MANQUANTS ({len(manquants)}) :
"""
    for element in manquants:
        rapport += f"   • {element}\n"

    rapport += f"""
💬 COMMENTAIRE :
   {commentaire}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rapport généré par Qualiopilot
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return rapport


def sauvegarder_rapport(nom_fichier, rapport):
    nom_rapport = nom_fichier.replace(".pdf", "").replace(".docx", "").replace(".png", "")
    nom_rapport = f"rapport_{nom_rapport}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nom_rapport, "w", encoding="utf-8") as f:
        f.write(rapport)
    print(f"Rapport sauvegardé : {nom_rapport}")
    return nom_rapport


# Test
if __name__ == "__main__":
    # Exemple de résultat d'analyse simulé
    resultat_test = {
        "preuves_trouvees": [
            "Programme de formation présent",
            "Objectifs pédagogiques définis",
            "Feuilles de présence mentionnées"
        ],
        "elements_manquants": [
            "Questionnaire de satisfaction absent",
            "CV des formateurs manquant",
            "Analyse de besoin non documentée"
        ],
        "score_conformite": 65,
        "commentaire": "Le document présente une base solide mais manque de preuves sur le suivi des bénéficiaires."
    }

    rapport = generer_rapport("document_test.pdf", resultat_test)
    print(rapport)
    sauvegarder_rapport("document_test.pdf", rapport)