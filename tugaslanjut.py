class mobil:
    def __init__(self,nama,model,harga,):
        self.nama = nama
        self.model = model
        self.harga = harga

    def menu(self):
        print(self.nama)

    def cek_tipe(self):
        if self.nama == "All New Veloz":
            print("Tipe Mobil ini MPV")
        elif self.nama == "All New Avanza":
            print("Tipe Mobil ini MPV")
        elif self.nama == "New Rush":
            print("Tipe Mobil ini SUV")
        elif self.nama == "New Fortuner":
            print("Tipe Mobil ini SUV")
        elif self.nama == "New Agya":
            print("Tipe Mobil ini HATCBACK")
        elif self.nama == "New Yaris":
            print("Tipe Mobil ini HATCHBACK")
        elif self.nama == "All New Camry":
            print("Tipe Mobil ini Sedan")
        elif self.nama == "All New Vios":
            print("Tipe Mobil ini Sedan")
        elif self.nama == "All New Hiace Premio":
            print("Tipe Mobil ini Commercial")
        elif self.nama == "NEW HILUX D CAB":
            print("Tipe Mobil ini Commercial")
        else:
            print("Tipe Mobil yang anda masukkan tidak ada")
    
    def choice(self):
        print("1. Kredit Perorangan")
        print("2. Kredit Perusahaan")
        choice = int(input("Silahkan Pilih tipe Kredit anda = "))
        if choice == 1:
            print("""Syarat pengajuan kredit perorangan adalah:

                    1.KTP Suami + Istri
                    2.Kartu Keluarga
                    3.NPWP
                    4.PBB / AJB Rumah
                    5.Rekening tabungan 3 bulan terakhir
                    6.Slip gaji bila bekerja""")
        elif choice == 2:
            print("""Kredit Perusahaan:

                    1.Fotocopy akte pendirian & perubahannya
                    2.Fotocopy pengesahan kehakiman
                    3.Fotocopy SIUP, NPWP, SITU / Domisili, TDP
                    4.Fotocopy Rek. Koran 3 bulan terakhir
                    5.Fotocopy KTP direksi & komisaris""")
            
        terpenuhi = input("Apa semua syaratnya terpenuhi YA/TIDAK : ")
        if terpenuhi == 'YA' or terpenuhi == 'Ya' or terpenuhi == 'y' or terpenuhi == 'ya':
            print("Kredit Anda Disetujui")
        else:
            print("Kredit Anda Ditolak") 
            
print('\tDAFTAR TIPE-TIPE MOBIL')    
tes = mobil("All New Veloz",'VELOZ 1.5 M/T (Non Premium Color)','288.700.000')
tes1 = mobil("All New Avanza","AVANZA G CVT TSS","298.500.000")
tes2 = mobil("New Rush",'RUSH 1.5 GR AT','303.600.000')
tes3 = mobil("New Fortuner","FORTUNER 2.8 VRZ GR (4X4)","715.350.000")
tes4 = mobil("New Agya","AGYA 1.2 GR AT","181.500.000")
tes5 = mobil("New Yaris","YARIS 1.5 CVT GR 7 AIRBAGS","327.250.000")
tes6 = mobil("All New Camry","ALL NEW CAMRY 2.5 AT HYBRID","937.400.000")
tes7 = mobil("All New Vios","VIOS 1.5 G CVT TSS","376.400.000")
tes8 = mobil("All New Hiace Premio","PREMIO MT","630.000.000")
tes9 = mobil("NEW HILUX D CAB","HILUX 2.4 V AT 4X4 DIESEL","513.600.000")

tes.menu()
tes1.menu()
tes2.menu()
tes3.menu()
tes4.menu()
tes5.menu()
tes6.menu()
tes7.menu()
tes8.menu()
tes9.menu()

model = input("Masukkan Model mobil: ")
if model == "All New Veloz":
    tes.cek_tipe()
elif model == "All New Avanza":
    tes1.cek_tipe()
elif model == "New Rush":
    tes2.cek_tipe()
elif model == "New Fortuner":
    tes3.cek_tipe()
elif model == "New Agya":
    tes4.cek_tipe()
elif model == "New Yaris":
    tes5.cek_tipe()
elif model == "All New Camry":
    tes6.cek_tipe()
elif model == "All New Vios":
    tes7.cek_tipe()
elif model == "All New Hiace Premio":
    tes8.cek_tipe()
elif model == "NEW HILUX D CAB":
    tes9.cek_tipe()

tes.choice()
    
