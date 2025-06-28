

import requests
import time

BASE_URL = "http://127.0.0.1:5001/buku"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Katalog Buku...")

    buku_baru_1 = {"isbn": "978-0321765723", "judul": "The C++ Programming Language", "penulis": "Bjarne Stroustrup", "penerbit": "Addison-Wesley"}
    buku_baru_2 = {"isbn": "978-0132350884", "judul": "Clean Code", "penulis": "Robert C. Martin", "penerbit": "Prentice Hall"}
    buku_tidak_lengkap = {"isbn": "978-1449355739", "judul": "Fluent Python"}

    print_response(requests.post(BASE_URL, json=buku_baru_1), "Create Buku 1 (C++)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=buku_baru_2), "Create Buku 2 (Clean Code)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=buku_baru_1), "Create Buku 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=buku_tidak_lengkap), "Create Buku Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Buku (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/978-0321765723"), "Get Buku C++")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/999-9999999999"), "Get Buku Fiktif (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_cpp = {"judul": "The C++ Programming Language (4th Edition)", "penulis": "B. Stroustrup", "penerbit": "Addison-Wesley Professional"}
    update_data_tidak_lengkap = {"penulis": "Uncle Bob"}

    print_response(requests.put(f"{BASE_URL}/978-0321765723", json=update_data_cpp), "Update Buku C++")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/978-0132350884", json=update_data_tidak_lengkap), "Update Buku Clean Code Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/999-9999999999", json=update_data_cpp), "Update Buku Fiktif (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/978-0321765723"), "Get Buku C++ (Setelah Update)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/978-0132350884"), "Delete Buku Clean Code")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/999-9999999999"), "Delete Buku Fiktif (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/978-0132350884"), "Get Buku Clean Code (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Buku (Setelah Delete)")

    print("\nPengujian Selesai.")