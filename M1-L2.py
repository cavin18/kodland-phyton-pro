import random   
characterspw = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("Masukkan panjang kata sandi yang diinginkan: "))
generated_password = " "

for i in range(password_length):
    generated_password += random.choice(characterspw)

print("Kata sandi yang dihasilkan:", generated_password)
