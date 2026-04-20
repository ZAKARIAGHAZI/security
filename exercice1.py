
import hashlib
from cryptography.fernet import Fernet


def generate_key():     
    return Fernet.generate_key()


def encrypt(text, key):
    fernet = Fernet(key)
    return fernet.encrypt(text.encode())


def decrypt(token, key):
    fernet = Fernet(key)
    return fernet.decrypt(token).decode()


def hash_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def compare_hashes(hash1, hash2):
    return hash1 == hash2


if __name__ == "__main__":
    # 1. Chiffrement
    print("--- Chiffrement et Déchiffrement ---")
    texte = input("Entrez le texte à chiffrer : ")
    key = generate_key()
    token = encrypt(texte, key)
    print(f"Texte chiffré : {token}\n")

    # 2. Déchiffrement
    texte_dechiffre = decrypt(token, key)
    print(f"Texte déchiffré : {texte_dechiffre}\n")

    # 3. Hachage SHA-256
    print("--- Hachage SHA-256 ---")
    texte_a_hacher = input("Entrez un texte pour calculer son hash : ")
    h1 = hash_sha256(texte_a_hacher)
    print(f"Hash SHA-256 : {h1}\n")

    # 4. Comparaison
    texte_recu = input("Entrez le texte reçu (à comparer) : ")
    h2 = hash_sha256(texte_recu)
    print(f"Hash reçu    : {h2}")
    if compare_hashes(h1, h2):
        print("-> Intégrité vérifiée !")
    else:
        print("-> ALERTE ! Le texte a été modifié.")