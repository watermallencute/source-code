print("Selamat Datang di Pasar Buah\n")
fruit       = ["apple", "orange", "grape"]
stock       = [20, 15, 25]
price       = [10_000, 15_000, 20_000]

total_price = 0

fruit_cart  = []
qty_cart    = []
price_cart  = []

list_menu = print('1. Menampilkan Daftar Buah\n',
                  '2. Menambah Buah\n',
                  '3. Menghapus Buah\n',
                  '4. Membeli Buah\n',
                  '5. Exit Program')

menu = int(input("Masukkan angka Menu yang ingin dijalankan: "))

while True:
    # Menampilkan Daftar Buah
    if menu == 1:
        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in range(len(fruit)):
            print(f"{i:<6} | {fruit[i]:<6} | {stock[i]:<6} | {price[i]:<10}")

    # Menambah Buah
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

    # Menghapus Buah
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

    # Membeli Buah
    elif menu == 4:
        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        # Menampilkan index, nama, stock, dan harga buah sesuai index
        for i in range(len(fruit)):
            print(f"{i:<6} | {fruit[i]:<6} | {stock[i]:<6} | {price[i]:<10}")

        total_cart = 0
        
        while True:
            index_buy = int(input("\nMasukkan index buah yang ingin dibeli: "))
            to_buy = int(input("Masukkan jumlah yang ingin dibeli: "))

            # Kalo yang mau dibeli lebih BANYAK daripada stok yang ada
            if to_buy > stock[index_buy]:
                print(f"Stock tidak cukup, stock {fruit[index_buy]} tinggal {stock[index_buy]}")
            
            # Kalo yang mau dibeli lebih SEDIKIT daripada stok yang ada
            else:
                # Jika menambah buah yang sama pada transaksi yang beda, cart langsung jadi satu baris dengan nambahin qty
                # Tidak perlu append karena tidak mau nambahin nilai baru
                ## Kalo buah udah pernah masuk cart
                if fruit[index_buy] in fruit_cart:
                    # Cari posisi index di cart
                    idx = fruit_cart.index(fruit[index_buy])
                    # Nambahin qty dari buah yang sama
                    qty_cart[idx] += to_buy

                # Kalo buah belum pernah masuk cart
                else:
                    fruit_cart.append(fruit[index_buy])
                    qty_cart.append(to_buy)
                    price_cart.append(price[index_buy])
                
            # Print isi cart yang mau dibeli
            print("Isi Cart: ")
            print("Nama   | Qty    | Harga")
            for i in range(len(fruit_cart)):
                print(f"{fruit_cart[i]:<6} | {qty_cart[i]:<6} | {price_cart[i]}")

            # Conditional statement mau beli yang lain/tidak
            buy_again = input("Mau beli yang lain (ya/tidak) = ")
            if buy_again == "ya":
                continue
            # Jika tidak
            else:
                print("Daftar Belanja:")
                print("Nama   | Qty    | Harga | Total Harga")
                for i in range(len(fruit_cart)):
                    # total harga per buah
                    total_price = qty_cart[i] * price_cart[i]
                    # total harga seluruh belanjaan
                    total_cart += total_price
                    # print
                    print(f"{fruit_cart[i]:<6} | {qty_cart[i]:<6} | {price_cart[i]} | {total_price}")

                print(f"Total Yang Harus Dibayar: = {total_cart}")

                # 'While True' dipakai agar program terus nanya jumlah uang sampe jumlah uang nya pas/lebih
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
        break

    # Exit Program
    elif menu == 5: 
        print("Keluar dari program.")

    else:
        break