# Angela Adytha Putri
# Python Variable, Data Types, and User Inputs
fruit = ["apple", "orange", "grape"]
stock = [5, 7, 6]
price = [10_000, 15_000, 20_000]
total_price = 0
cart = []

# Python Looping Statements & Conditional Statements
for i in range(len(fruit)):
    while True:
        qty = int(input(f"\nMasukkan jumlah {fruit[i]}: "))
        if qty <= stock[i]:
            break 
        else:
            print("Jumlah yang dimasukkan terlalu banyak")
            print(f"Stock {fruit[i]} tinggal: {stock[i]}") 
    total = qty * price[i]
    total_price += total
    cart.append((fruit[i], qty, price[i], total))

# lanjut Python Variable, Data Types, and User Inputs
print("\nDetail belanja: ")
for item in cart:
    name, qty, item_price, total = item
    print(f"{name}: {qty} x {item_price:,} = {total:,}")
print(f"\nTotal: {total_price:,}")

# Python Looping Statements & Conditional Statements
while True:
    pay_amount = int(input("\nMasukkan jumlah uang: "))

    if pay_amount < total_price:
        print(f"Uang anda kurang sebesar {(total_price - pay_amount):,}")
    elif pay_amount == total_price:
        print("Terimakasih")
        break
    else:
        print("Terimakasih")
        print(f"\nUang kembali anda: {(pay_amount - total_price):,}")
        break