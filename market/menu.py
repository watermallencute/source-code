print("Selamat Datang di Pasar Buah\n")
fruit       = ["apple", "orange", "grape"]
stock       = [20, 15, 25]
price       = [10_000, 15_000, 20_000]

total_price = 0

fruit_cart  = []
qty_cart    = []
price_cart  = []

list_menu = print('1. Menampilkan Daftar Buah\n',
                  '2. Menambah buah\n',
                  '3. Menghapus buah\n',
                  '4. Membeli buah\n',
                  '5. Exit program')

menu = int(input("Masukkan angka Menu yang ingin dijalankan: "))

while True:
    if menu == 1:
        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in range(len(fruit)):
            print(f"{i:<6} | {fruit[i]:<6} | {stock[i]:<6} | {price[i]:<10}")

    elif menu == 2:
        new_fruit = input("Masukkan Nama Buah   : ")
        new_stock = input("Masukkan Stock Buah  : ")
        new_price = input("Masukkan Harga Buah  : ")

        fruit.append(new_fruit)
        stock.append(new_stock)
        price.append(new_price)

        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in range(len(fruit)):
            print(f"{i:<6} | {fruit[i]:<6} | {stock[i]:<6} | {price[i]:<10}")

    elif menu == 3:
        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in range(len(fruit)):
            print(f"{i:<6} | {fruit[i]:<6} | {stock[i]:<6} | {price[i]:<10}")
        
        index_delete = int(input("Masukkan index buah yang ingin dihapus: "))
        fruit.pop(index_delete)
        stock.pop(index_delete)
        price.pop(index_delete)

        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in range(len(fruit)):
            print(f"{i:<6} | {fruit[i]:<6} | {stock[i]:<6} | {price[i]:<10}")

    elif menu == 4:
        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in range(len(fruit)):
            print(f"{i:<6} | {fruit[i]:<6} | {stock[i]:<6} | {price[i]:<10}")

        total_cart = 0
        
        while True:
            index_buy = int(input("\nMasukkan index buah yang ingin dibeli: "))
            to_buy = int(input("Masukkan jumlah yang ingin dibeli: "))

            if to_buy > stock[index_buy]:
                print(f"Stock tidak cukup, stock {fruit[index_buy]} tinggal {stock[index_buy]}")
            
            else:
                if fruit[index_buy] in fruit_cart:
                    idx = fruit_cart.index(fruit[index_buy])
                    qty_cart[idx] += to_buy

                else:
                    fruit_cart.append(fruit[index_buy])
                    qty_cart.append(to_buy)
                    price_cart.append(price[index_buy])
                
            print("Isi Cart: ")
            print("Nama   | Qty    | Harga")
            for i in range(len(fruit_cart)):
                print(f"{fruit_cart[i]:<6} | {qty_cart[i]:<6} | {price_cart[i]}")

            buy_again = input("Mau beli yang lain (ya/tidak) = ")
            if buy_again == "ya":
                continue
            else:
                print("Daftar Belanja:")
                print("Nama   | Qty    | Harga | Total Harga")
                for i in range(len(fruit_cart)):
                    total_price = qty_cart[i] * price_cart[i]
                    total_cart += total_price
                    print(f"{fruit_cart[i]:<6} | {qty_cart[i]:<6} | {price_cart[i]} | {total_price}")

                print(f"Total Yang Harus Dibayar: = {total_cart}")

                while True: 
                    pay_amount = int(input("\nMasukkan jumlah uang: "))

                    if pay_amount < total_cart:
                        print(f"Uang anda kurang sebesar {(total_cart - pay_amount):,}")
                    elif pay_amount == total_cart:
                        print("Terimakasih")
                        break
                    else:
                        print("Terimakasih")
                        print(f"\nUang kembali anda: {(pay_amount - total_cart):,}")
                        break
                break

    elif menu == 5: 
        print("Keluar dari program.")

    else:
        break