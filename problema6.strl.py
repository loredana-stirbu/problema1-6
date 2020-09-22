n=9467
a=n//1000
b=n//100%10
c=n//10%10
d=n%10
s=a+b+c+d
print("Ultima cifra a acestui numar este:", d)
print("Penultima cifra a acestui numar este:", c)
print("Restul si citul impartirii acestui numar la 9 este:", n%9, "si", n//9)
print("Suma cifrelor acestui numar este:", s)
print("Rasturnatul acestui numar este:", d,c,b,a,sep="")