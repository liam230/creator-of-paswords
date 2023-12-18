import random
codigos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("¿que tan grande quieres que sea la contraseña?"))
pw = ""
for i in range(longitud):
    pw = pw + random.choice(codigos)
print(pw)
