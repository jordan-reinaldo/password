import hashlib
import json
import random

# Fonction qui vérifie la sécurité du mot de passe
def valid_password(password):
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

# fonction pour générer un mot de passe aléatoire
def generer_mdp_aleatoire():
    #réer des listes pour les différents types de caractères
    majuscules = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3)]
    minuscules = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3)]
    chiffres = [random.choice('0123456789') for _ in range(2)]
    speciaux = [random.choice('!@#$%^&*') for _ in range(2)]

    # construire le mot de passe en combinant les listes
    password_chars = majuscules + minuscules + chiffres + speciaux
    # mélanger les caractères pour que le mot de passe soit aléatoire
    random.shuffle(password_chars)
    # joindre les caractères pour former le mot de passe
    password = ''.join(password_chars)

    return password


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

    if mdp_hache in data.values():
        print("Ce mot de passe est déjà utilisé.")
        return False

    index = str(len(data) + 1)
    data[index] = mdp_hache

    with open(chemin_fichier, 'w') as fichier:
        json.dump(data, fichier, indent=4)
    return True

# fonction pour lire et afficher les mots de passe hachés
def lire_mdp_haches(chemin_fichier='mdp.json'):
    try:
        with open(chemin_fichier, 'r') as fichier:
            data = json.load(fichier)
            print("Mots de passe hachés :")
            for index, mdp_hache in data.items():
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

# Programme principal
def main():
    while True:
        choix_utilisateur = afficher_menu()

        if choix_utilisateur == '1':
            mdp = input("Choisissez un mot de passe : ")
            erreurs_détectées = valid_password(mdp)
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

# Appel de la fonction main pour exécuter le programme
main()