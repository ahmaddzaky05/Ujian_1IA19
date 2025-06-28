## Skenario: Manajemen Pelanggan CRM

Anda adalah seorang backend developer di "HubungBaik CRM", sebuah perusahaan software. Anda ditugaskan untuk membuat API service sederhana untuk sistem Customer Relationship Management (CRM) yang akan mengelola data pelanggan. Data pelanggan akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data pelanggan:

### Data Pelanggan:

Setiap pelanggan akan memiliki atribut berikut:

- `id_pelanggan` (string, unik, contoh: "CUST-001")
- `nama_perusahaan` (string)
- `kontak_person` (string)
- `email` (string)

### Penyimpanan Data:

Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data pelanggan.

### Endpoint API yang Harus Diimplementasikan:

**`POST /pelanggan`**

- **Fungsi**: Menambahkan pelanggan baru.
- **Request Body (JSON)**: `{ "id_pelanggan": "...", "nama_perusahaan": "...", "kontak_person": "...", "email": "..." }`
- **Respons Sukses (201 Created)**: JSON data pelanggan yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `id_pelanggan` sudah ada.

**`GET /pelanggan`**

- **Fungsi**: Mengambil seluruh data pelanggan.
- **Respons Sukses (200 OK)**: JSON array berisi semua data pelanggan.

**`GET /pelanggan/<id_pelanggan>`**

- **Fungsi**: Mengambil data pelanggan spesifik.
- **Respons Sukses (200 OK)**: JSON data pelanggan yang dicari.
- **Respons Error (404 Not Found)**: Jika `id_pelanggan` tidak ditemukan.

**`PUT /pelanggan/<id_pelanggan>`**

- **Fungsi**: Memperbarui data pelanggan spesifik.
- **Request Body (JSON)**: `{ "nama_perusahaan": "...", "kontak_person": "...", "email": "..." }`
- **Respons Sukses (200 OK)**: JSON data pelanggan yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `id_pelanggan` tidak ditemukan.

**`DELETE /pelanggan/<id_pelanggan>`**

- **Fungsi**: Menghapus data pelanggan.
- **Respons Sukses (200 OK)**: JSON data pelanggan yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `id_pelanggan` tidak ditemukan.
