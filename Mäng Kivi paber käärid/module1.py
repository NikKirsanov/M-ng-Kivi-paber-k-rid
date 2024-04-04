K = int(input("Sisestage kogus kotlette: "))
M = int(input("Sisestage, mitu kotletit mahub ühele pannile: "))

pannid = 0

while K > 0:
    K -= M
    pannid += 1

kotletid = M + K if K < 0 else M - K

print("Täislõunaid on vaja:", pannid - 1)
print("Ülejäänud kotlette viimasel pannil:", abs(kotletid))


