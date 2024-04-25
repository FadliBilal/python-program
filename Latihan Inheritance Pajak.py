class PPH:
    def tampilPPH(self):
        print("Pilihan PPH yang dipakai buat menghitung : ")
        print("1. pph21")
        print("2. pph22")

    def hitungPPH(self, pilihan):
        if pilihan == 1:
            objekpph = pph21()
        elif pilihan == 2:
            objekpph = pph22()
        else:
            print("Pilihan tidak ada, cuma ada 1 dan 2")
            return

        objekpph.hitung_tarif_pph()  # kalo udah milih maka lanjut ngitung sesuai pilihannya

class pph21(PPH):
    def hitung_tarif_pph(self):
        pemasukan = float(input("Masukkan nominal untuk menghitung pph21: "))
        tarif_pph = 0.10  # tarif pph21 itu 10%
        tax = pemasukan * tarif_pph
        total = pemasukan - tax
        print(f"Nominal Anda: Rp {pemasukan:.0f}")
        print(f"Pajak pph21 ({tarif_pph * 100:.0f}%): Rp {tax:.0f}")
        print(f"Total penerimaan: Rp {total:.0f}")

class pph22(PPH):
    def hitung_tarif_pph(self):
        pemasukan = float(input("Masukkan nominal untuk menghitung pph22: "))
        tarif_pph = 0.02  # tarif pph22 2%
        if pemasukan <= 50000000:
            tax = pemasukan * tarif_pph
        else:
            tax = 1000000 + (pemasukan - 50000000) * 0.05
        total = pemasukan - tax
        print(f"Nominal: Rp {pemasukan:.0f}")
        print(f"Pajak pph22 ({tarif_pph * 100:.0f}%): Rp {tax:.0f}")
        print(f"Total penerimaan: Rp {total:.0f}")

def mulai_program():
    main_obj = PPH()
    main_obj.tampilPPH()

    pilihan = int(input("Masukkan pilihan Anda: "))
    main_obj.hitungPPH(pilihan)

mulai_program()