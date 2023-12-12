import hashlib

# fonction qui permet de tester la si la sécurité du mdp est conforme aux éxigences
def is_valid_password(password):
    # liste pour stocker en string les erreurs que l'on a obtenu
    erreurs = []

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

    # Affichez toutes les erreurs
    if erreurs:
        print("Erreurs dans le mot de passe :")
        for i in erreurs:
            print(i)
        return False
    return True

# Fonction pour demander à l'utilisateur d'entrer un mot de passe
def get_user_password():
    while True:
        user_password = input("Choisissez un mot de passe : ")
        if is_valid_password(user_password):
            return user_password
        else:
            print("Veuillez réessayer.")

# Fonction pour hacher le mot de passe avec SHA-256
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Demandez à l'utilisateur d'entrer un mot de passe valide
user_password = get_user_password()

# Hachez le mot de passe et affichez le résultat
hashed_password = hash_password(user_password)
print(f"Mot de passe haché : {hashed_password}")