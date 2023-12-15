import hashlib
import json
import random

# Fonction qui vérifie la sécurité du mot de passe
def mdp_valide(password):
    erreurs = []
    # critères de sécurité
    if len(password) < 8:
        erreurs.append("Le mot de passe doit avoir au moins 8 caractères.")
    if not any(c.isupper() for c in password):
        erreurs.append("Le mot de passe doit contenir au moins une lettre majuscule.")
    if not any(c.islower() for c in password):
        erreurs.append("Le mot de passe doit contenir au moins une lettre minuscule.")
    if not any(c.isdigit() for c in password):
        erreurs.append("Le mot de passe doit contenir au moins un chiffre.")
    if not any(c in '!@#$%^&*' for c in password):
        erreurs.append("Le mot de passe doit contenir au moins un caractère spécial (!@#$%^&*).")

    return erreurs

# pour générer un mot de passe aléatoir
def generer_mdp_aleatoire():
    #listes pour les différents types de caractères
    majuscules = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3)] # _ est une variable temporaire
    minuscules = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3)]
    chiffres = [random.choice('0123456789') for _ in range(2)]
    speciaux = [random.choice('!@#$%^&*') for _ in range(2)]

    password_chars = majuscules + minuscules + chiffres + speciaux # construire le mot de passe en combinant les listes
    random.shuffle(password_chars)     # mélanger les caractères pour que le mot de passe soit aléatoire
    password = ''.join(password_chars) # joindre les caractères pour former le mot de passe

    return password


# hache le mot de passe avec la norme demandée dans l'énoncé :sha256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# pour enregistrer le mot de passe haché dans un fichier JSON
def enregistrer_mdp_hache(mdp_hache, chemin_fichier='mdp.json'):
    try:
        with open(chemin_fichier, 'r') as fichier: 
            fichier_json = json.load(fichier) # charger le fichier JSON dans un dictionnaire
    except FileNotFoundError: # si le fichier n'existe pas, créer un dictionnaire vide
         fichier_json = {}

    if mdp_hache in  fichier_json.values():
        print("Ce mot de passe est déjà utilisé.")
        return False

    index = str(len( fichier_json) + 1)
    fichier_json[index] = mdp_hache # ajouter le mot de passe haché au dictionnaire

    with open(chemin_fichier, 'w') as fichier: # écrire le dictionnaire dans le fichier JSON
        json.dump( fichier_json, fichier, indent=4)
    return True

# fonction pour lire et afficher les mots de passe hachés
def lire_mdp_haches(chemin_fichier='mdp.json'):
    try:
        with open(chemin_fichier, 'r') as fichier: # ouvrir le fichier JSON en mode lecture
            fichier_json = json.load(fichier) 
            print("Mots de passe hachés :")
            for index, mdp_hache in  fichier_json.items(): # parcourir le dictionnaire et afficher les mots de passe hachés
                print(f"{index}: {mdp_hache}")
    except FileNotFoundError:
        print("Aucun mot de passe haché trouvé.")

# fonction pour afficher le menu
def afficher_menu():
    print("\nMenu:")
    print("1. Entrer un nouveau mot de passe")
    print("2. Générer un mot de passe aléatoire")
    print("3. Voir les mots de passe hachés")
    print("4. Fermer le programme")
    choix = input("Entrez votre choix (1-4): ")
    return choix

# fonction principale
def main():
    while True: # boucle infinie car on veut que cela soit l'utilisateur qui stop le programme
        choix_utilisateur = afficher_menu()

        if choix_utilisateur == '1':
            mdp = input("Choisissez un mot de passe : ")
            erreurs_détectées = mdp_valide(mdp) 
            if erreurs_détectées:
                for i in erreurs_détectées:
                    print(i)
                continue
            hashed_password = hash_password(mdp)
            if enregistrer_mdp_hache(hashed_password):
                print("Mot de passe haché enregistré.")
        elif choix_utilisateur == '2':
            mdp = generer_mdp_aleatoire()
            print(f"Mot de passe généré : {mdp}")
            hashed_password = hash_password(mdp)
            if enregistrer_mdp_hache(hashed_password):
                print("Mot de passe haché enregistré.")
        elif choix_utilisateur == '3':
            lire_mdp_haches()
        elif choix_utilisateur == '4':
            print("Merci d'avoir utilisé notre programme.")
            break
        else:
            print("Choix invalide. Veuillez saisir 1, 2, 3 ou 4 svp.")

# appel de la fonction main pour exécuter le programme
main()