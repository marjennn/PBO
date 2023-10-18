from mobil import Mobil
from kredit import kredit
class combine():
    def __init__(self,mobil):
        self.mobil = mobil

    def tampil(self):
        self.mobil.menu()

print('\tDAFTAR TIPE-TIPE MOBIL')    
tes = Mobil("All New Veloz",'VELOZ 1.5 M/T (Non Premium Color)','288.700.000')
tes1 = Mobil("All New Avanza","AVANZA G CVT TSS","298.500.000")
tes2 = Mobil("New Rush",'RUSH 1.5 GR AT','303.600.000')
tes3 = Mobil("New Fortuner","FORTUNER 2.8 VRZ GR (4X4)","715.350.000")
tes4 = Mobil("New Agya","AGYA 1.2 GR AT","181.500.000")
tes5 = Mobil("New Yaris","YARIS 1.5 CVT GR 7 AIRBAGS","327.250.000")
tes6 = Mobil("All New Camry","ALL NEW CAMRY 2.5 AT HYBRID","937.400.000")
tes7 = Mobil("All New Vios","VIOS 1.5 G CVT TSS","376.400.000")
tes8 = Mobil("All New Hiace Premio","PREMIO MT","630.000.000")
tes9 = Mobil("NEW HILUX D CAB","HILUX 2.4 V AT 4X4 DIESEL","513.600.000")

c1 = combine(tes)
c2 = combine(tes1)
c3 = combine(tes2)
c4 = combine(tes3)
c5 = combine(tes4)
c6 = combine(tes5)
c7 = combine(tes6)
c8 = combine(tes7)
c9 = combine(tes8)
c10 = combine(tes9)

c1.tampil();c2.tampil();c3.tampil();c4.tampil();c5.tampil();c6.tampil();c7.tampil();c8.tampil();
c9.tampil();c10.tampil();

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

amar = kredit("")
amar.pilih_kredit()
amar.tampilkredit()