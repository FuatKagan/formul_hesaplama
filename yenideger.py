deger = []

a = ['0', '0', '0', '0.6', '1.3', '2.6', '4', '5.5', '7.3', '8.8', '10.9', '13', '15.2', '19.4', '21.9', '24.9', '26', '27.2', '27.6', '27', '25.5', '22.8', '20.7', '17.7', '15.9', '15.2', '11.5', '9.1', '6.7', '4.8', '3.2', '1.8', '0.8', '0.2', '0', '0', '0', '0']

for i in range(0,38):
    a[i] = float(a[i])/32.60
    deger.append(a[i])

print(deger)