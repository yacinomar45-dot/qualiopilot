import os
import anthropic
import json

# Clé API Anthropic (à remplir plus tard)
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
def analyser_texte(texte):
    # Vérifier que le texte n'est pas vide
    if not texte or texte.strip() == "":
        return {"erreur": "Texte vide, impossible d'analyser."}

    # Créer le client Anthropic
    client = anthropic.Anthropic(api_key=API_KEY)

    # Prompt envoyé à Claude
    prompt = f"""
Tu es un expert en certification Qualiopi pour les organismes de formation.

Analyse le texte suivant et identifie :
1. Les preuves de conformité Qualiopi présentes
2. Les éléments manquants
3. Un score de conformité estimé sur 100

Réponds UNIQUEMENT en JSON avec ce format :
{{
    "preuves_trouvees": ["preuve1", "preuve2"],
    "elements_manquants": ["element1", "element2"],
    "score_conformite": 75,
    "commentaire": "explication courte"
}}

Texte à analyser :
{texte[:3000]}
"""

    # Appel à l'API Claude
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extraire la réponse JSON
    try:
        resultat = json.loads(message.content[0].text)
    except Exception:
        resultat = {"reponse_brute": message.content[0].text}

    return resultat


# Test
if __name__ == "__main__":
    texte_test = input("Entre un texte à analyser : ")
    resultat = analyser_texte(texte_test)
    print("\n--- RÉSULTAT ANALYSE ---")
    print(json.dumps(resultat, indent=2, ensure_ascii=False))