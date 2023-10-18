class mahasiswa:
    def informasi_mahasiswa(self,nama,nim,email,prodi,kelas):
        self.nama = nama
        self.nim = nim
        self.email = email
        self.prodi = prodi
        self.kelas = kelas
        self.matkul = {}


    def tambah_matkul(self,matkul,nilai,sks):
        if nilai == 'a' or nilai == "A":
            nilai = 4
            nilai = 3.7 
        elif nilai == 'b+' or nilai == 'B+':
            nilai = 3.3
        elif nilai == 'b' or nilai == 'B':
            nilai = 3
        elif nilai == 'b-' or nilai == 'B-':
            nilai = 2.7
        elif nilai == 'c+' or nilai == 'C+':
            nilai = 2.3
        elif nilai == 'c' or nilai == 'C':
            nilai = 2
        elif nilai == 'd' or nilai == 'D':
            nilai = 1
        elif nilai == 'e' or nilai == 'E':
            nilai = 0
        else:
            print('Invalid')
            return 

        self.matkul[matkul] = nilai, sks

    def tampilan_informasi(self):
        print(f'Nama: {self.nama}')
        print(f'NIM: {self.nim}')
        print(f'Email: {self.email}')
        print(f'Prodi: {self.prodi}')
        print(f'Kelas: {self.kelas}')
        for matkul,[nilai,sks] in self.matkul.items():
            print(f"- {matkul} : nilai = {nilai}, sks = {sks}")

    def jumlah_ipk(self):
        Total_nilai = 0 
        Total_sks = 0
        for nilai,sks in self.matkul.values():
            Total_nilai += nilai
            Total_sks += sks
            return Total_nilai * 2 / Total_sks

mahasiswa1 = mahasiswa() 
mahasiswa1.informasi_mahasiswa("Muammar Zain",2207421010,"Muammar.zain.tik22@mhsw.pnj.ac.id","Teknik Multimedia & Jaringan","TMJ 3 A")
mahasiswa1.tambah_matkul("Infrastruktur Jaringan","B+",2)
mahasiswa1.tambah_matkul("Keamanan Komputer","A",2)
mahasiswa1.tambah_matkul('Rekayasa Perangkat Lunak',"A-",2)
mahasiswa1.tambah_matkul('Pemrograman Berorientasi Objek',"B+",2)
mahasiswa1.tambah_matkul('Sistem Embeded','A',2)
mahasiswa1.tambah_matkul('English',"A-",2)
mahasiswa1.tambah_matkul('Pemrograman Web',"B+",2)
mahasiswa1.tambah_matkul('Metode Numerik',"A-",2)
mahasiswa1.tambah_matkul('Organisasi & Arsitektur Komputer',"B+",2)
mahasiswa1.tampilan_informasi()
print(mahasiswa1.jumlah_ipk())

mahasiswa2 = mahasiswa() 
mahasiswa2.informasi_mahasiswa("Harsdyka Wibisono",2207421023,"Harsdyka.wibisono.tik22@mhsw.pnj.ac.id","Teknik Multimedia & Jaringan","TMJ 3 A")
mahasiswa2.tambah_matkul("Infrastruktur Jaringan","C",2)
mahasiswa2.tambah_matkul("Keamanan Komputer","B-",2)
mahasiswa2.tambah_matkul('Rekayasa Perangkat Lunak',"D",2)
mahasiswa2.tambah_matkul('Pemrograman Berorientasi Objek',"E",2)
mahasiswa2.tambah_matkul('Sistem Embeded','A',2)
mahasiswa2.tambah_matkul('English',"A",2)
mahasiswa2.tambah_matkul('Pemrograman Web',"B",2)
mahasiswa2.tambah_matkul('Metode Numerik',"B",2)
mahasiswa2.tambah_matkul('Organisasi & Arsitektur Komputer',"B-",2)
mahasiswa2.tampilan_informasi()
print(mahasiswa2.jumlah_ipk())




    