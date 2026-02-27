thislistnilai = [75,80,65,90,85]

thislistnilai.append(95)
thislistnilai.remove(65)
thislistnilai.sort()

print(thislistnilai)
print(max(thislistnilai))
print(min(thislistnilai))
print(len(thislistnilai))

rata_rata = sum(thislistnilai) / len(thislistnilai)
print(rata_rata)

print(thislistnilai)


thisdosen = ("D001","dr.andi","struktur data",12)
print(thisdosen[1 : 3])
thisdosen = ("D001","dr.andi","struktur data",12)
for x in thisdosen :
    print(x)

thisdosen = ("D001","dr.andi","struktur data",14)
print(thisdosen)
#sks nya berubah menjadi 14 sks

#tuple meyimpan elemen dengan cara berurutan sedangkan set tidak

mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80}
}

for mahasiswa in mahasiswa:
    if mahasiswa["prodi"] == "Informatika" and mahasiswa["ipk"] >= 3.5:
        print(mahasiswa["nama"])





mahasiswa ={
    "nim":"m004",
    "nama":"unibakwan",
    "prodi":"teknik informatika",
    "ipk":3.75




}
print(mahasiswa)