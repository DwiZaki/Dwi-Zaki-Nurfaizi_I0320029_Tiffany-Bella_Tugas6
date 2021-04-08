start = 10
stop = 25

for angka in range (start, stop):
    if angka > 1:
        for i in range (2, angka):
            if (angka % i) == 0:
                print(angka,'bukan bilangan prima')
                break
        else:
            print(angka, 'adalah bilangan prima')
    else:
        print(angka, 'bukan bilangan prima')