import math

def luas_permukaan_kubus(sisi):
    return 6 * sisi ** 2

def luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

def luas_permukaan_bola(jari_jari):
    return 4 * math.pi * jari_jari ** 2

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def luas_permukaan_kerucut(jari_jari, tinggi):
    return math.pi * jari_jari * (jari_jari + tinggi)
