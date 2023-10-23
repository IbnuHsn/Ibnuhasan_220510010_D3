print("program menghitung luas dan volume tabung")
"""
Programmer : Ibnu Hasan
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

# Nilai
jariJariTabung = 10
tinggi = 20

# Rumus
luasSelimutTabung = 2 * 3.14 *jariJariTabung **2 * tinggi
luasPermukaanTabung = luasSelimutTabung + 2 * 3.14 * jariJariTabung **2
volumeTabung = (3.14 * jariJariTabung) * tinggi
# Output
print("jariJariTabung =",jariJariTabung)
print("tinggi =",tinggi)
print("luasSelimutTabung =",luasSelimutTabung)
print("luas permukaan tabung =", luasPermukaanTabung)
print("volume permukaan tabung =", volumeTabung)