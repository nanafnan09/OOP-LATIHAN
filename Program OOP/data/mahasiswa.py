# data/mahasiswa.py

class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"{self.nim} - {self.nama} ({self.jurusan})"


class DataMahasiswa:
    def __init__(self):
        self.mahasiswas = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswas.append(mahasiswa)

    def cari_mahasiswa(self, nim):
        for mahasiswa in self.mahasiswas:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    def hapus_mahasiswa(self, nim):
        mahasiswa = self.cari_mahasiswa(nim)
        if mahasiswa:
            self.mahasiswas.remove(mahasiswa)
            return True
        return False

    def modifikasi_mahasiswa(self, nim, nama=None, jurusan=None):
        mahasiswa = self.cari_mahasiswa(nim)
        if mahasiswa:
            if nama:
                mahasiswa.nama = nama
            if jurusan:
                mahasiswa.jurusan = jurusan
            return True
        return False

    def daftar_mahasiswa(self):
        return self.mahasiswas
