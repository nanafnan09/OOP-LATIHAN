# view/input_form.py

class InputForm:
    def __init__(self):
        self.data = {}

    def input_mahasiswa(self):
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        self.data = {'nim': nim, 'nama': nama, 'jurusan': jurusan}
        return self.data

    def tampilkan_form(self):
        print("Form Input Data Mahasiswa")
        data = self.input_mahasiswa()
        print(f"Data yang diinput: NIM={data['nim']}, Nama={data['nama']}, Jurusan={data['jurusan']}")

# Contoh penggunaan
if __name__ == "__main__":
    form = InputForm()
    form.tampilkan_form()
