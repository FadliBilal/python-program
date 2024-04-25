class KartuStack:
    def __init__(self):
        self.stack = []

    def push(self, kartu):
        self.stack.append(kartu)
        self.stack.sort()

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def cari_kartu(self, kartu):
        for i, stack_kartu in enumerate(reversed(self.stack), 1):
            nomor_stack, jenis_stack = stack_kartu.split()
            nomor_kartu, jenis_kartu = kartu.split()
            if nomor_kartu == nomor_stack and jenis_kartu == jenis_stack:
                return len(self.stack) - i + 1
        return "Kartu tidak ditemukan"

    def ambil_kartu(self, card):
        # Looping melalui setiap kartu dalam tumpukan dimulai dari atas
        for i, stack_card in enumerate(reversed(self.stack), 1):
            # Misahin nomor dan jenis kartu dari kartu dalam tumpukan dan kartu yang dicari
            nomor_stack, jenis_stack = stack_card.split()
            nomor_card, jenis_card = card.split()
            # Meriksa apakah kartu dalam tumpukan cocok dengan kartu yang dicari
            if nomor_stack == nomor_card and jenis_stack == jenis_card:
                # Jika cocok, siapkan kartu-kartu yang akan dipop dari tumpukan
                cards_to_pop = self.stack[-i:]
                taken_card = self.pop()  # Ambil kartu yang sesuai dari tumpukan
                # Pop kartu-kartu lain dari tumpukan, kecuali yang sudah diambil
                for _ in range(len(cards_to_pop) - 1):
                    self.pop()
                # Push kartu-kartu yang sudah dipop kembali ke tumpukan
                for card in cards_to_pop[1:]:
                    self.push(card)
                return taken_card  # Kembalikan kartu yang sudah diambil
        # Jika kartu tidak ditemukan dalam tumpukan, kembalikan None
        return None

    def info_tumpukan(self):
        print("Tumpukan kartu:")
        print(' | '.join(self.stack))


def main():
    kartu = KartuStack()

    while True:
        input_kartu = input("Masukkan urutan kartu (selesai untuk berhenti): ")
        if input_kartu.lower() == "selesai":
            break
        kartu.push(input_kartu)

    # Menampilkan tumpukan kartu setelah selesai memasukkan urutan kartu
    kartu.info_tumpukan()

    # Cari urutan kartu ada di tumpukan ke berapa
    input_cari_kartu = input("Masukkan urutan kartu untuk dicari: ")
    posisi_kartu = kartu.cari_kartu(input_cari_kartu)
    print(f"Urutan kartu {input_cari_kartu} ada di tumpukan ke-{posisi_kartu}")

    # Mengambil urutan kartu tertentu
    input_ambil_kartu = input("Masukkan urutan kartu yang ingin diambil : ")
    kartu_terambil = kartu.ambil_kartu(input_ambil_kartu)
    if kartu_terambil:
        print(f"Kartu yang diambil: {kartu_terambil}")

    kartu.info_tumpukan()


main()
