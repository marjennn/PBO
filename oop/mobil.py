class Mobil():
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