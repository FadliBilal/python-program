class Remote:
    def __init__(self, jarakvolume):
        self.power = False
        self.mute = False
        self.channels = ["Korsel TV", "Korut TV", "Indonesia TV", "Jepang TV", "Korea TV", "German TV", "Brazil TV", "Australia TV", "Cina TV"]
        self.channel_awal = 5
        self.volume = 5
        self.jarakvolume = jarakvolume

    def tombol_power(self):
        self.power = not self.power
        if self.power:
            print("POWER TV ON")
        else:
            print("POWER TV OFF")

    def tombol_mute(self):
        self.mute = not self.mute
        if self.mute:
            print("TV telah di muted")
        else:
            print("TV telah di un-mute")

    def ganti_volume(self, direction):
        if direction == "naikinvol":
            if self.volume < self.jarakvolume[1]:
                self.volume += 1
                print(f"Volume telah naik jadi volume {self.volume}")
            else:
                print("Volume TV sudah paling keras")
        elif direction == "turuninvol":
            if self.volume > self.jarakvolume[0]:
                self.volume -= 1
                print(f"Volume sekarang Turun jadi Volume {self.volume}")
            else:
                print("Volume TV sudah paling kecil")

    def ganti_channel(self, direction):
        if direction == "tekankanan":
            if self.channel_awal < len(self.channels):
                self.channel_awal += 1
                print(f"Channel sekarang adalah {self.channels[self.channel_awal - 1]}")
            else:
                print("Gaada channel lagi")
        elif direction == "tekankiri":
            if self.channel_awal > 1:
                self.channel_awal -= 1
                print(f"Channel sekarang adalah {self.channels[self.channel_awal - 1]}")
            else:
                print("Gaada channel lagi")

    def pilih_channel(self, channel):
        if channel in self.channels:
            self.channel_awal = self.channels.index(channel) + 1
            print(f"Channel kamu sekarang ganti {channel}")
        else:
            print("Channel tidak ditemukan")

    def info_settings_TV(self):
        print(f"============ INFO TV NEGARA ============")
        print(f"Power TV : {'ON' if self.power else 'OFF'}")
        print(f"Mute TV sedang : {'aktif' if self.mute else 'tidak aktif'}")
        print(f"Channel yang diliat sekarang : {self.channels[self.channel_awal - 1]}")
        print(f"Volume anda sekarang : {self.volume}")
        print(f"========================================")

#kode dibawah ini buat range volume
remote_tv = Remote((0, 10))

#Tempat buat action output program - Fadli
remote_tv.tombol_power()
remote_tv.tombol_power()
remote_tv.ganti_volume("turuninvol")
remote_tv.ganti_volume("turuninvol")

#Volume default saya setting 5
#Channel default saya setting Korea TV
#untuk ganti channel pakai direction = tekankanan dan tekankiri
#untuk ganti volume pakai direction = naikinvol dan turuninvol

#Tugas Program Remote Fadli Bilal Afifuddin NIM 1482300040