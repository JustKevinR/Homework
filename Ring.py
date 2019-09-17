import math

r = float(input("Sisesta raadius "))
c = r * 2 * math.pi
s = math.pi * r * r
print ("Raadius on " + str(r) + " ümbermõõt on " + str(round(c, 2)) + " pindala on " + str(round(s, 2)))