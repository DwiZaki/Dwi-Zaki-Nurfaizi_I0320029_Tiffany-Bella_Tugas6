data_nilai = []

n = int(input('Masukkan banyaknya data nilai: '))

for i in range (n):
    nilai = float(input('Masukkan nilai ke-{} :'.format (i+1)))
    data_nilai.append (nilai)

print ('Hasil nilai total adalah : {:.2f}'.format (sum(data_nilai)))
print ('Hasil rata-rata adalah : {:.2f}'.format (sum(data_nilai)/n))