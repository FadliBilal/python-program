class RemoteTv:
    def __init__(self, volume_suara):
        self.power = "off"
        self.mute = False
        self.channels = ["Metro TV", "Global TV", "Kompas TV", "TVONE", "News TV"]
        self.default_channel = 3
        self.volume = 0
        self.volume_suara = volume_suara

    def power_on(self):
        self.power = "on"
        print("TV telah dinyalakan")

    def power_off(self):
        self.power = "off"
        print("TV kamu dimatikan kalo mau nyalain TV re-run program ini")
        return True

    def toggle_mute(self):
        self.mute = not self.mute
        if self.mute:
            print("TV telah dimuted")
        else:
            print("TV telah di un-mute")

    def change_volume(self, direction):
        if direction == "naikkan":
            if self.volume < self.volume_suara[1]:
                self.volume += 1
                print(f"Volume sekarang Naik jadi volume {self.volume}")
            else:
                print("Volume TV sudah maksimal nanti telinga kamu sakit")
        elif direction == "turunkan":
            if self.volume > self.volume_suara[0]:
                self.volume -= 1
                print(f"Volume sekarang Turun jadi Volume {self.volume}")
            else:
                print("Volume TV sudah paling kecil")

    def change_channel(self, direction):
        if direction == "naik":
            if self.default_channel < len(self.channels):
                self.default_channel += 1
                print(f"Channel sekarang adalah {self.channels[self.default_channel - 1]}")
            else:
                print("Gaada channel lagi klik 5 untuk kechannel tadi")
        elif direction == "turun":
            if self.default_channel > 1:
                self.default_channel -= 1
                print(f"Channel sekarang adalah {self.channels[self.default_channel - 1]}")
            else:
                print("Gaada channel lagi klik 4 untuk kechannel tadi")

    def select_channel(self, channel):
        if channel in self.channels:
            self.default_channel = self.channels.index(channel) + 1
            print(f"Channel kamu sekarang ganti {channel}")
        else:
            print("Channel tidak ditemukan")

    def get_current_settings(self):
        print(f"============ INFO SETTING TV ============")
        print(f"Power TV : {self.power}")
        print(f"Mute TV sedang : {'hidup' if self.mute else 'tidak hidup'}")
        print(f"Channel Yang Diliat : {self.channels[self.default_channel - 1]}")
        print(f"Volume Sekarang : {self.volume}")
        print(f"========================================")

# Inisialisasi remote TV
volume_range = (0, 10)
remote_tv = RemoteTv(volume_range)

# Program utama
print("\nRemote TV Menu:")
print("1. Power On")
choice = input("Masukkan Angka 1 untuk menyalakan TV : ")

if choice == '1':
    remote_tv.power_on()
    while remote_tv.power == "on":
        print("\nRemote TV Menu:")
        print("1. Tombol Mute")
        print("2. Naikkan Volume")
        print("3. Turunkan Volume")
        print("4. Channel Kanan")
        print("5. Channel Kiri")
        print("6. Pilih Channel")
        print("7. Dapatkan Info")
        print("8. Power Off")
        sub_choice = input("Masukkan pilihanmu: ")
        if sub_choice == '1':
            remote_tv.toggle_mute()
        elif sub_choice == '2':
            remote_tv.change_volume("naikkan")
        elif sub_choice == '3':
            remote_tv.change_volume("turunkan")
        elif sub_choice == '4':
            remote_tv.change_channel("naik")
        elif sub_choice == '5':
            remote_tv.change_channel("turun")
        elif sub_choice == '6':
            channel = input("Masukkan channel yang kamu cari: ")
            remote_tv.select_channel(channel)
        elif sub_choice == '7':
            remote_tv.get_current_settings()
        elif sub_choice == '8':
            if remote_tv.power_off():
                break
        else:
            print("masukkan pilihan yang benar.")
else:
    print("Pilihan tidak valid.")