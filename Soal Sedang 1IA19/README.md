# 🎓 Soal Pemrograman Cerita: Verifikasi Status Akademik Mahasiswa

## 📖 Latar Belakang Cerita

Bagian kemahasiswaan sebuah universitas sedang membuka pendaftaran beasiswa. Salah satu syarat utama adalah mahasiswa harus berstatus "Aktif" dengan IPK di atas 3.5. Staf harus memverifikasi ratusan pendaftar, dan proses manual dengan membuka sistem informasi akademik (SIAKAD) satu per satu sangat tidak efisien.

Anda sebagai programmer di unit IT universitas ditugaskan untuk membuat **klien verifikasi massal** yang mampu:

- Melakukan verifikasi status untuk banyak Nomor Induk Mahasiswa (NIM) secara **concurrent (paralel)**.
- **Menangani kemungkinan error**, seperti NIM tidak terdaftar, server SIAKAD sedang *down*, atau koneksi jaringan yang lambat.
- Memberikan output yang jelas dan ringkas untuk membantu staf membuat keputusan.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_verifikasi_mahasiswa_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API status akademik.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil verifikasi ke konsol secara terstruktur per thread (per verifikator).