a=input("Masukan Nilai a: ")
b=input("Masukan Nilai b: ")
print("variable a=",a)
print("variable b=",b)
print("Hasil penggabungan {1}&{0}= %d".format(a,b) %(a+b)) #%d = dianggap sebagai bilangan bulat desimal

#konversi nilai variable
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}= %d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}= %d".format(a,b) %(a/b))
