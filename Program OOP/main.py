# main.py

from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import DaftarMahasiswa, DetailMahasiswa

def tampilkan_menu():
    print("Menu Utama:")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Daftar Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Modifikasi Mahasiswa")
    print("6. Keluar")

def main():
    data_mahasiswa = DataMahasiswa()
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            form = InputForm()
            data = form.input_mahasiswa()
            mahasiswa = Mahasiswa(data['nim'], data['nama'], data['jurusan'])
            data_mahasiswa.tambah_mahasiswa(mahasiswa)
            print("Mahasiswa berhasil ditambahkan!")
        
        elif pilihan == "2":
            daftar = DaftarMahasiswa(data_mahasiswa.daftar_mahasiswa())
            daftar.tampilkan_daftar()
        
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
            detail = DetailMahasiswa(data_mahasiswa.daftar_mahasiswa())
            detail.tampilkan_detail(nim)
        
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
            if data_mahasiswa.hapus_mahasiswa(nim):
                print("Mahasiswa berhasil dihapus!")
            else:
                print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
        
        elif pilihan == "5":
            nim = input("Masukkan NIM mahasiswa yang ingin dimodifikasi: ")
            nama = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
            jurusan = input("Masukkan jurusan baru (kosongkan jika tidak ingin mengubah): ")
            if data_mahasiswa.modifikasi_mahasiswa(nim, nama, jurusan):
                print("Data mahasiswa berhasil dimodifikasi!")
            else:
                print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
        
        elif pilihan == "6":
            print("Terima kasih! Program berakhir.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
