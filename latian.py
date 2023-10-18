class mobil:
    def __init__(self,model,harga,):
        self.model = model
        self.harga = harga

    def tampilan_mobil(self):
        print(f'model: {self.model}')
        print(f'harga: {self.harga}\n')

    def tampilan_tipe():
        print("Silahkan pilih tipe: ")
        print('1. Tipe MPV')
        print('2. Tipe SUV')
        print('3. Tipe HATCBACK')
        print('4. Tipe SEDAN')
        print('5. Tipe SPORT')
        print('6. Tipe COMMERCIAL')

    #def tampilan_veloz

mobil.tampilan_tipe()
tipe = input("Masukkan Nomor Tipe Anda : ")

if tipe == '1':
    print("Silahkan Memilih Tipe MPV: ")
    print("1.All New Veloz")
    print("2.All New Avanza")
    print("3. New Calya")
    print("4. New Alphard")
    print("5. New Vellfire")
    print("6. All New Foxy")
    print("7. All New Innova Zenix")
    pilih_mpv = input("Masukkan nomor MPV: ")
    if pilih_mpv == '1':
        #All New Veloz
        mpva1 = mobil("VELOZ 1.5 M/T (Non Premium Color)","288.700.000")
        mpva2 = mobil("VELOZ 1.5 M/T (Premium Color)", "290.200.000")
        mpva3 = mobil("VELOZ 1.5 Q CVT (Non Premium Color)", "313.300.000")
        mpva4 = mobil("VELOZ 1.5 Q CVT (Premium Color)", "314.800.000")
        mpva5 = mobil("VELOZ 1.5 Q CVT TSS (Non Premium Color)", "335.300.000")
        mpva6 = mobil("VELOZ 1.5 Q CVT TSS (Premium Color)","336.800.000")
        print("\nAll New Veloz")
        mpva1.tampilan_mobil()
        mpva2.tampilan_mobil()
        mpva3.tampilan_mobil()
        mpva4.tampilan_mobil()
        mpva5.tampilan_mobil()
        mpva6.tampilan_mobil()
    elif pilih_mpv == '2':
        #All New Avanza
        mpvb1 = mobil("AVANZA E M/T","233.100.000")
        mpvb2 = mobil('AVANZA E CVT','247.800.000')
        mpvb3 = mobil('AVANZA G M/T','257.800.000')
        mpvb4 = mobil('AVANZA G CVT',"272.500.000")
        mpvb5 = mobil('AVANZA G CVT TSS','298.500.000')
        print("\nAll New Avanza")
        mpvb1.tampilan_mobil()
        mpvb2.tampilan_mobil()
        mpvb3.tampilan_mobil()
        mpvb4.tampilan_mobil()
        mpvb5.tampilan_mobil()
    elif pilih_mpv == '3':
        # New Calya
        mpvc1 = mobil('CALYA 1.2 E MT STD','164.700.000')
        mpvc2 = mobil('CALYA 1.2 E MT','167.600.000')
        mpvc3 = mobil('CALYA 1.2 G MT','173.200.000')
        mpvc4 = mobil('CALYA 1.2 G AT','187.400.000')
        print("New Calya")
        mpvc1.tampilan_mobil()
        mpvc2.tampilan_mobil()
        mpvc3.tampilan_mobil()
        mpvc4.tampilan_mobil()
    elif pilih_mpv == '4':
        # #New Alphard
        mpvd1 = mobil('ALPHARD 2.5 G AT','1.385.000.000')
        print("New Alphard")
        mpvd1.tampilan_mobil()
    elif pilih_mpv == '5':
        # #New Vellfire
        mpve1 = mobil('VELLFIRE 2.5 AT','1.399.800.000')
        print('New Vellfire')
        mpve1.tampilan_mobil()
    elif pilih_mpv == '6':
        # #All New Foxy
        mpvf1 = mobil('ALL NEW VOXY 2.0 CVT','592.700.000')
        print('All New Foxy')
        mpvf1.tampilan_mobil()
    elif pilih_mpv == '7':
        # #All New Innova Zenix
        mpvg1 = mobil('ZENIX 2.0 G CVT','423.000.000')
        mpvg2 = mobil('ZENIX 2.0 V CVT',"471.000.000")
        mpvg3 = mobil('ZENIX 2.0 G HV CVT','469.000.000')
        mpvg4 = mobil('ZENIX 2.0 V HV CVT','543.000.000')
        mpvg5 = mobil('ZENIX 2,0 Q HV CVT','622.000.000')
        print("All New Innova Zenix")
        mpvg1.tampilan_mobil()
        mpvg2.tampilan_mobil()
        mpvg3.tampilan_mobil()
        mpvg4.tampilan_mobil()
        mpvg5.tampilan_mobil()

    else:
        print("Tolong masukkan tipe yang valid")
    
    if tipe == '2':
        print("Silahkan Memilih Tipe SUV: ")
        print("1.New Rush")
        print("2.All New Raize")
        print("3. New Fortuner")
        print("4. All New Corolla Cross")
        pilih_suv = input("Masukkan nomor SUV: ")
        if pilih_suv == '1':
            #All New Veloz
        mpva1 = mobil("VELOZ 1.5 M/T (Non Premium Color)","288.700.000")
        mpva2 = mobil("VELOZ 1.5 M/T (Premium Color)", "290.200.000")
        mpva3 = mobil("VELOZ 1.5 Q CVT (Non Premium Color)", "313.300.000")
        mpva4 = mobil("VELOZ 1.5 Q CVT (Premium Color)", "314.800.000")
        mpva5 = mobil("VELOZ 1.5 Q CVT TSS (Non Premium Color)", "335.300.000")
        mpva6 = mobil("VELOZ 1.5 Q CVT TSS (Premium Color)","336.800.000")
        print("\nAll New Veloz")
        mpva1.tampilan_mobil()
        mpva2.tampilan_mobil()
        mpva3.tampilan_mobil()
        mpva4.tampilan_mobil()
        mpva5.tampilan_mobil()
        mpva6.tampilan_mobil()
        elif pilih_suv == '2':
            print
        elif pilih_suv == '3':
            print
        elif pilih_suv == '4':
            print


















    


    



#print("New Alphard")
#mpvd1.tampilan_mobil()





