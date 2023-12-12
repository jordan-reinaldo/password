import hashlib
import json

# Fonction qui vérifie la sécurité du mot de passe
def valid_password(password):
    erreurs = [] # liste pour stocker en string les erreurs que l'on a obtenu

    # critères de sécurité, on utilise if not pour vérifier si le mdp ne contient pas les critères, auquel cas le mdp n'est pas conforme 
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

    if erreurs: #vérifie si il y a des erreurs
        print("Erreurs dans le mot de passe :") 
        for i in erreurs:
            print(i) # ici et ci-dessus i est une nouvelle variable qui prend la valeur de chaque élément de la liste erreurs que l'on veut afficher pour que l'utilisateur puisse savoir ce qui n'est pas bon dans le mdp qu'il propose
        return False # si des erreurs sont trouvés la fonction est fausse. 
    return True #aucune erreur trouvée, la fonction est vrai, le mot de passe est bon.

# Fonction pour demander à l'utilisateur d'entrer un mot de passe
def entree_mdp():
    while True:
        user_password = input("Choisissez un mot de passe : ")
        if valid_password(user_password):
            return user_password
        else:
            print("Veuillez réessayer.")

# Fonction pour hacher le mot de passe avec SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Fonction pour enregistrer le mot de passe haché dans un fichier JSON
def enregistrer_mdp_hache(mdp_hache, chemin_fichier='mdp.json'):
    try:
        with open(chemin_fichier, 'r') as fichier:
            data = json.load(fichier)
    except FileNotFoundError:
        data = {}

    # Utiliser un index numérique comme clé
    index = str(len(data) + 1)
    data[index] = mdp_hache

    with open(chemin_fichier, 'w') as fichier:
        json.dump(data, fichier, indent=4)

# Programme principal
mdp = entree_mdp()
hashed_password = hash_password(mdp)
enregistrer_mdp_hache(hashed_password)
print("Mot de passe haché enregistré.")
# [Vos fonctions existantes ici...]

# Fonction pour lire et afficher les mots de passe hachés
def lire_mdp_haches(chemin_fichier='mdp.json'):
    try:
        with open(chemin_fichier, 'r') as fichier:
            data = json.load(fichier)
            print("Mots de passe hachés :")
            for index, mdp_hache in data.items():
                print(f"{index}: {mdp_hache}")
    except FileNotFoundError:
        print("Aucun mot de passe haché trouvé.")

# Fonction pour afficher le menu
def afficher_menu():
    print("\nMenu:")
    print("1. Entrer un nouveau mot de passe")
    print("2. Voir les mots de passe hachés")
    print("3. Fermer le programme")
    choix = input("Entrez votre choix (1-3): ")
    return choix

# Boucle principale
while True:
    choix_utilisateur = afficher_menu()

    if choix_utilisateur == '1':
        mdp = entree_mdp()
        hashed_password = hash_password(mdp)
        enregistrer_mdp_hache(hashed_password)
        print("Mot de passe haché enregistré.")
    elif choix_utilisateur == '2':
        lire_mdp_haches()
    elif choix_utilisateur == '3':
        print("Fermeture du programme.")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")