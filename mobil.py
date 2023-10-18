class Mobil:
    def __init__(self, nama, model, harga):
        self.nama = nama
        self.model = model
        self.harga = harga

    def menu(self):
        print('nama : ',self.nama)

    from mobil import Mobil

print('\tDAFTAR TIPE-TIPE MOBIL')
tes = Mobil("All New Veloz", 'VELOZ 1.5 M/T (Non Premium Color)', '288.700.000')
tes.menu()

model = input("Masukkan Model mobil: ")
tipe = TipeMobil.cek_tipe(model)
print(f"Tipe Mobil ini: {tipe}")

Kredit.choice()