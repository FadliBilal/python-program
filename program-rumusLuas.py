class HitungLuas:
    def __init__(rumus, sisi=None, alas=None, tinggi=None, panjang=None, lebar=None, jari_jari=None):
        rumus.sisi = sisi
        rumus.alas = alas
        rumus.tinggi = tinggi
        rumus.panjang = panjang
        rumus.lebar = lebar
        rumus.jari_jari = jari_jari

    def luas_persegi(rp):
        return rp.sisi ** 2

    def luas_segitiga(rs):
        return 0.5 * rs.alas * rs.tinggi

    def luas_persegi_panjang(rpp):
        return rpp.panjang * rpp.lebar

    def luas_lingkaran(rl):
        return 3.14 * (rl.jari_jari ** 2)


# Contoh pemanggilan fungsi-fungsi di atas dengan inisialisasi nilai
hitung1 = HitungLuas(sisi=2)
print("Luas Persegi:", hitung1.luas_persegi())

hitung2 = HitungLuas(alas=4, tinggi=5)
print("Luas Segitiga:", hitung2.luas_segitiga())

hitung3 = HitungLuas(panjang=3, lebar=6)
print("Luas Persegi Panjang:", hitung3.luas_persegi_panjang())

hitung4 = HitungLuas(jari_jari=2)
print("Luas Lingkaran:", hitung4.luas_lingkaran())