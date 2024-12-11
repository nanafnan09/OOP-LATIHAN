# view/mahasiswa.py

class DaftarMahasiswa:
    def __init__(self, data_mahasiswa):
        self.data_mahasiswa = data_mahasiswa

    def tampilkan_daftar(self):
        if not self.data_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            print("Daftar Mahasiswa:")
            for mahasiswa in self.data_mahasiswa:
                print(mahasiswa)

class DetailMahasiswa:
    def __init__(self, data_mahasiswa):
        self.data_mahasiswa = data_mahasiswa

    def tampilkan_detail(self, nim):
        mahasiswa = next((m for m in self.data_mahasiswa if m.nim == nim), None)
        if mahasiswa:
            print(f"Detail Mahasiswa untuk NIM {nim}:")
            print(mahasiswa)
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

# Contoh penggunaan
if __name__ == "__main__":
    from data.mahasiswa import Mahasiswa, DataMahasiswa

    # Membuat beberapa data mahasiswa untuk contoh
    data_mahasiswa = DataMahasiswa()
    data_mahasiswa.tambah_mahasiswa(Mahasiswa("001", "Budi", "Informatika"))
    data_mahasiswa.tambah_mahasiswa(Mahasiswa("002", "Siti", "Sistem Informasi"))

    # Tampilkan daftar mahasiswa
    daftar_mahasiswa = DaftarMahasiswa(data_mahasiswa.daftar_mahasiswa())
    daftar_mahasiswa.tampilkan_daftar()

    # Tampilkan detail mahasiswa
    detail_mahasiswa = DetailMahasiswa(data_mahasiswa.daftar_mahasiswa())
    detail_mahasiswa.tampilkan_detail("001")
