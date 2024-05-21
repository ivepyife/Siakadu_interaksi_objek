class Mahasiswa:

    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.nilai = {}

    def tampilkan_nama_nim(self):
        print(f"Nama: {self.nama}, NIM: {self.npm}")

    def tambah_nilai(self, mata_kuliah, nilai):
        if mata_kuliah.nama in self.nilai:
            self.nilai[mata_kuliah.nama] += nilai
        else:
            self.nilai[mata_kuliah.nama] = nilai

    def kurangi_nilai(self, mata_kuliah, nilai):
        if mata_kuliah.nama in self.nilai:
            self.nilai[mata_kuliah.nama] -= nilai
            if self.nilai[mata_kuliah.nama] < 0:
                self.nilai[mata_kuliah.nama] = 0

    def tampilkan_nilai(self):
        print(f"Nilai untuk {self.nama} (NIM: {self.npm}):")
        for mata_kuliah, nilai in self.nilai.items():
            print(f"{mata_kuliah}: {nilai}")

class Dosen:

    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip

    def tampilkan_nama_nip(self):
        print(f"Nama: {self.nama}, NIP: {self.nip}")

    def tambah_nilai_mahasiswa(self, mahasiswa, mata_kuliah, nilai):
        print(f"{self.nama} menambahkan nilai {nilai} untuk {mata_kuliah.nama} pada mahasiswa {mahasiswa.nama}")
        mahasiswa.tambah_nilai(mata_kuliah, nilai)

    def kurangi_nilai_mahasiswa(self, mahasiswa, mata_kuliah, nilai):
        print(f"{self.nama} mengurangi nilai {nilai} untuk {mata_kuliah.nama} pada mahasiswa {mahasiswa.nama}")
        mahasiswa.kurangi_nilai(mata_kuliah, nilai)

class MataKuliah:

    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks

    def tampilkan_info(self):
        print(f"Mata Kuliah: {self.nama}, SKS: {self.sks}")

ai = MataKuliah('AI', 3)
pbo = MataKuliah('PBO', 4)

mahasiswa1 = Mahasiswa('Adit', '2215061039')
mahasiswa2 = Mahasiswa('Arifin', '2255061008')
mahasiswa3 = Mahasiswa('Fadhil', '2215061019')

dosen1 = Dosen('Pak PUPUT', '12344444')

dosen1.tambah_nilai_mahasiswa(mahasiswa1, ai, 80)
dosen1.tambah_nilai_mahasiswa(mahasiswa2, ai, 85)
dosen1.tambah_nilai_mahasiswa(mahasiswa3, ai, 70)
dosen1.tambah_nilai_mahasiswa(mahasiswa1, pbo, 70)
dosen1.tambah_nilai_mahasiswa(mahasiswa2, pbo, 75)
dosen1.tambah_nilai_mahasiswa(mahasiswa3, pbo, 0)
print("\n")
dosen1.kurangi_nilai_mahasiswa(mahasiswa3, ai, 60)
dosen1.kurangi_nilai_mahasiswa(mahasiswa1, pbo, 20)
print("\n")
mahasiswa1.tampilkan_nilai()
mahasiswa2.tampilkan_nilai()
mahasiswa3.tampilkan_nilai()
