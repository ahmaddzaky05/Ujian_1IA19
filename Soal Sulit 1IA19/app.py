from flask import Flask, request, jsonify

app = Flask(__name__)

# Penyimpanan data buku
katalog_buku = {}

@app.route('/buku', methods=['POST'])
def tambah_buku():
    """Menambahkan buku baru ke katalog."""
    data = request.get_json()
    if not all(key in data for key in ("isbn", "judul", "penulis", "penerbit")):
        return jsonify({"error": "Data tidak lengkap"}), 400
    if data['isbn'] in katalog_buku:
        return jsonify({"error": "ISBN sudah ada di katalog"}), 409
    katalog_buku[data['isbn']] = {
        "judul": data["judul"],
        "penulis": data["penulis"],
        "penerbit": data["penerbit"]
    }
    return jsonify(katalog_buku[data['isbn']]), 201

@app.route('/buku', methods=['GET'])
def semua_buku():
    """Mengambil semua buku dari katalog."""
    return jsonify(list(katalog_buku.values())), 200

@app.route('/buku/<isbn>', methods=['GET'])
def detail_buku(isbn):
    """Mengambil data buku berdasarkan ISBN."""
    buku = katalog_buku.get(isbn)
    if not buku:
        return jsonify({"error": "Buku tidak ditemukan"}), 404
    return jsonify({"isbn": isbn, **buku}), 200

@app.route('/buku/<isbn>', methods=['PUT'])
def perbarui_buku(isbn):
    """Memperbarui data buku berdasarkan ISBN."""
    buku = katalog_buku.get(isbn)
    if not buku:
        return jsonify({"error": "Buku tidak ditemukan"}), 404
    data = request.get_json()
    if not all(key in data for key in ("judul", "penulis", "penerbit")):
        return jsonify({"error": "Data tidak lengkap"}), 400
    buku.update({
        "judul": data["judul"],
        "penulis": data["penulis"],
        "penerbit": data["penerbit"]
    })
    return jsonify({"isbn": isbn, **buku}), 200

@app.route('/buku/<isbn>', methods=['DELETE'])
def hapus_buku(isbn):
    """Menghapus buku dari katalog berdasarkan ISBN."""
    buku = katalog_buku.pop(isbn, None)
    if not buku:
        return jsonify({"error": "Buku tidak ditemukan"}), 404
    return jsonify({"isbn": isbn, **buku}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)