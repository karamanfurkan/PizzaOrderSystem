import datetime
import csv

# Menü ve fiyatları
menu = {1: "Klasik", 2: "Margarita", 3: "TürkPizza", 4: "Sade Pizza"}
menu_prices = {1: 20, 2: 25, 3: 30, 4: 15}
sauces = {11: "Zeytin", 12: "Mantarlar", 13: "Keçi Peyniri", 14: "Et", 15: "Soğan", 16: "Mısır"}
sauce_prices = {11: 5, 12: 4, 13: 6, 14: 8, 15: 3, 16: 2}

# Sipariş bilgilerini
print("Lütfen bir pizza seçin:")
for key, value in menu.items():
    print(f"{key}: {value} ({menu_prices[key]} TL)")
pizza_choice = int(input("Pizza seçiminiz (1-4 arası bir sayı giriniz.): "))

print("Lütfen bir sos seçiniz:")
for key, value in sauces.items():
    print(f"{key}: {value} ({sauce_prices[key]} TL)")
sauce_choice = int(input("Sos seçiminiz (11-16 arası bir sayı giriniz.): "))

# Toplam fiyatı hesaplayın
total_price = menu_prices[pizza_choice] + sauce_prices[sauce_choice]

# Kullanıcı bilgilerini alın
name = input("Lütfen adınızı ve soyadınızı girin: ")
credit_card = input("Lütfen kredi kartı numaranızı girin: ")

# Sipariş bilgilerini Orders_Database.csv dosyasına kaydetme yeri
now = datetime.datetime.now()
with open("Orders_Database.csv", "a") as file:
    file.write(f"{name},{menu[pizza_choice]},{sauces[sauce_choice]},{total_price} TL ,{credit_card},{now}\n")

# Kullanıcıya sipariş onayı verin
print("Siparişiniz başarıyla alındı!")
print(f"{menu[pizza_choice]} pizzası {sauces[sauce_choice]} sosuyla birlikte toplamda {total_price} TL tutarındadır.")
