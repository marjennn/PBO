class TipeMobil:
    @staticmethod
    def cek_tipe(nama):
        tipe_mobil = {
            "All New Veloz": "MPV",
            "All New Avanza": "MPV",
            "New Rush": "SUV",
            "New Fortuner": "SUV",
            "New Agya": "HATCHBACK",
            "New Yaris": "HATCHBACK",
            "All New Camry": "Sedan",
            "All New Vios": "Sedan",
            "All New Hiace Premio": "Commercial",
            "NEW HILUX D CAB": "Commercial"
        }
        return tipe_mobil.get(nama, "Tipe Mobil yang anda masukkan tidak ada")