import os
from extractor import extraire_texte
from database import get_session, Document, Texte, initialiser_base

def traiter_document(chemin_fichier):
    # Vérifier que le fichier existe
    if not os.path.exists(chemin_fichier):
        print("Erreur : fichier introuvable.")
        return

    print(f"Traitement de : {chemin_fichier}")

    # Étape 1 : Extraire le texte
    print("Extraction du texte...")
    texte_extrait = extraire_texte(chemin_fichier)

    if not texte_extrait or texte_extrait.strip() == "":
        print("Erreur : aucun texte extrait.")
        return

    print(f"Texte extrait ({len(texte_extrait)} caractères)")

    # Étape 2 : Sauvegarder dans la base de données
    print("Sauvegarde dans la base de données...")
    session = get_session()

    nom_fichier = os.path.basename(chemin_fichier)
    extension = os.path.splitext(chemin_fichier)[1].lower()

    document = Document(
        nom_fichier=nom_fichier,
        type_fichier=extension,
        chemin=chemin_fichier
    )
    session.add(document)
    session.commit()

    texte = Texte(
        document_id=document.id,
        contenu=texte_extrait
    )
    session.add(texte)
    session.commit()
    session.close()

    print("Document sauvegardé avec succès.")
    print("\n--- APERÇU DU TEXTE EXTRAIT ---")
    print(texte_extrait[:500])
    print("...")

# Test
if __name__ == "__main__":
    initialiser_base()
    chemin = input("Entre le chemin d'un fichier (PDF, image ou Word) : ")
    traiter_document(chemin)