# 🔐 Sécurité Informatique Chiffrement & Hachage

## 📁 Structure du projet

```
security/
├── exercice1.py          # Fonctions crypto (console + module réutilisable)
├── exercice2.py          # API REST Flask (importe exercice1)
├── requirements.txt      # Dépendances Python
├── Dockerfile            # Image Docker
├── docker-compose.yml    # Orchestration Docker
└── README.md
```

---

## ⚙️ Fonctionnalités

| Fonctionnalité                        | Exercice 1 (Console) | Exercice 2 (API) |
|---------------------------------------|:---------------------:|:-----------------:|
| Chiffrer un texte (Fernet)            | ✅                    | ✅ `POST /crypt`  |
| Déchiffrer un texte                   | ✅                    | ✅ `GET /decrypt`  |
| Calculer le hash SHA-256              | ✅                    | ✅ `POST /hash`    |
| Comparer deux hashes (intégrité)      | ✅                    | ✅ `POST /hash`    |

---

## 🚀 Installation & Lancement

### Prérequis

- Python 3.10+ **ou** Docker

### Option 1 — Sans Docker

```bash
pip install -r requirements.txt

# Lancer en mode console
python exercice1.py

# Lancer l'API Flask
python exercice2.py
```

Le serveur démarre sur **http://localhost:5000**

### Option 2 — Avec Docker

```bash
# Avec Docker Compose
docker-compose up --build

# Ou manuellement
docker build -t security-api .
docker run -p 5000:5000 security-api
```

---

## 📡 Endpoints de l'API

### 1. `POST /crypt` — Chiffrer un texte

**Request :**
```http
POST http://localhost:5000/crypt
Content-Type: application/json

{
    "text": "Hello word"
}
```

**Response :**
```json
{
    "token": "gAAAAABp5o54dCgwao7-DoOk...",
    "key": "GmTHnJ61WGwgTTHMZRgGOdn..."
}
```

---

### 2. `GET /decrypt` — Déchiffrer un texte

**Request :**
```http
GET http://localhost:5000/decrypt?token=<TOKEN>&key=<KEY>
```

**Response :**
```json
{
    "decrypted_text": "Hello word"
}
```

> ⚠️ Utiliser le `token` et la `key` obtenus depuis `POST /crypt`.

---

### 3. `POST /hash` — Calculer et comparer les SHA-256

**Request :**
```http
POST http://localhost:5000/hash
Content-Type: application/json

{
    "text1": "hello",
    "text2": "hello"
}
```

**Response (textes identiques) :**
```json
{
    "hash1": "2cf24dba5fb0a30e26e83b2ac5b9e29e...",
    "hash2": "2cf24dba5fb0a30e26e83b2ac5b9e29e...",
    "match": true
}
```

**Response (textes différents) :**
```json
{
    "hash1": "2cf24dba5fb0a30e...",
    "hash2": "b94d27b9934d3e08...",
    "match": false
}
```

---

## 🧪 Tester avec Postman

1. Lancer le serveur (`python exercice2.py` ou `docker-compose up`)
2. Ouvrir Postman
3. Pour les routes **POST** : onglet **Body** → **raw** → **JSON**
4. Pour la route **GET** : onglet **Params** → ajouter `token` et `key`

---

## 📚 Concepts de sécurité utilisés

### Chiffrement symétrique (Fernet)
- Une seule clé sert à **chiffrer** et **déchiffrer**
- L'algorithme Fernet utilise AES-128-CBC avec HMAC pour garantir la confidentialité et l'intégrité
- Sans la clé, il est impossible de retrouver le texte original

### Hachage SHA-256
- Fonction **irréversible** : on ne peut pas retrouver le texte à partir du hash
- Produit une empreinte de **256 bits** (64 caractères hexadécimaux)
- **Effet d'avalanche** : un seul caractère modifié change totalement le hash
- Utilisé pour vérifier l'**intégrité** des données (détecter toute modification)

---

## 🛠️ Technologies

- **Python 3.12**
- **Flask** — Framework web léger
- **cryptography** — Bibliothèque de chiffrement (Fernet)
- **hashlib** — Module standard Python (SHA-256)
- **Docker** — Conteneurisation
