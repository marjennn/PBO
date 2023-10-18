class kredit(): 
    def __init__(self,kredit):
        self.kredit = kredit

    def tampilkredit(self):
        print(self.kredit)

    def pilih_kredit(self):
        print("1. Kredit Perorangan")
        print("2. Kredit Perusahaan")
        choice = int(input("Silahkan Pilih tipe Kredit anda = "))
        if choice == 1:
            self.kredit = "Kredit Perorangan"
            print("""Syarat pengajuan kredit perorangan adalah:

                    1.KTP Suami + Istri
                    2.Kartu Keluarga
                    3.NPWP
                    4.PBB / AJB Rumah
                    5.Rekening tabungan 3 bulan terakhir
                    6.Slip gaji bila bekerja""")
        elif choice == 2:
            self.kredit = "Kredit Perusahaan"
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