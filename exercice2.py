from flask import Flask, request, jsonify
from exercice1 import generate_key, encrypt, decrypt, hash_sha256, compare_hashes

app = Flask(__name__)


# POST /crypt — Chiffrer un texte
@app.route('/crypt', methods=['POST'])
def crypt():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Champ "text" manquant'}), 400

    key = generate_key()
    token = encrypt(data['text'], key)

    return jsonify({
        'token': token.decode(),
        'key':   key.decode()
    })


# GET /decrypt — Déchiffrer un texte
@app.route('/decrypt', methods=['GET'])
def decrypt_route():
    token = request.args.get('token')
    key   = request.args.get('key')

    if not token or not key:
        return jsonify({'error': 'Paramètres "token" et "key" requis'}), 400

    try:
        result = decrypt(token.encode(), key.encode())
        return jsonify({'decrypted_text': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# POST /hash — Calculer et comparer les hashes SHA-256
@app.route('/hash', methods=['POST'])
def hash_route():
    data = request.get_json()
    if not data or 'text1' not in data or 'text2' not in data:
        return jsonify({'error': 'Champs "text1" et "text2" requis'}), 400

    h1 = hash_sha256(data['text1'])
    h2 = hash_sha256(data['text2'])

    return jsonify({
        'hash1': h1,
        'hash2': h2,
        'match': compare_hashes(h1, h2)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
