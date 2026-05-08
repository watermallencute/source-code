print("Selamat Datang di Pasar Buah\n")
fruit = {
    0  : {"name" : "apple" , "stock" : 20, "price" : 10_000},
    1  : {"name" : "orange", "stock" : 15, "price" : 15_000},
    2  : {"name" : "grape" , "stock" : 25, "price" : 20_000}
}

cart = {
    "name" : [],
    "qty"   : [],
    "price" : []
}

total_price = 0

while True:
    print(' 1. Menampilkan Daftar Buah\n',
          '2. Menambah Buah\n',
          '3. Menghapus Buah\n',
          '4. Membeli Buah\n',
          '5. Exit Program')
    menu = int(input("Masukkan angka Menu yang ingin dijalankan: "))

    # Menampilkan Daftar Buah
    if menu == 1:
        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in fruit:
            print(f"{i:<6} | {fruit[i]["name"]:<6} | {fruit[i]["stock"]:<6} | {fruit[i]["price"]:<10}")

    # Menambah Buah
    elif menu == 2:
        new_name  = input("\nMasukkan Nama Buah   : ")
        new_stock = int(input("Masukkan Stock Buah  : "))
        new_price = int(input("Masukkan Harga Buah  : "))

        new_index = len(fruit)
        fruit[new_index] = {
            "name" : new_name,
            "stock": new_stock,
            "price": new_price
        }

        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in fruit:
            print(f"{i:<6} | {fruit[i]["name"]:<6} | {fruit[i]["stock"]:<6} | {fruit[i]["price"]:<10}")

        confirm_msg = input("Mau lanjut tambah buah (ya/tidak): ")
        if confirm_msg != "ya":
            print("\nDaftar buah")
            print("Index  | Nama   | Stock  | Harga")
            for i in fruit:
                print(f"{i:<6} | {fruit[i]["name"]:<6} | {fruit[i]["stock"]:<6} | {fruit[i]["price"]:<10}")
            
    # Menghapus Buah
    elif menu == 3:
        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in fruit:
            print(f"{i:<6} | {fruit[i]["name"]:<6} | {fruit[i]["stock"]:<6} | {fruit[i]["price"]:<10}")
        
        index_delete = int(input("Masukkan index buah yang ingin dihapus: "))
        if index_delete in fruit:
            fruit.pop(index_delete)
            # del fruit[index_delete]

        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        for i in fruit:
            print(f"{i:<6} | {fruit[i]["name"]:<6} | {fruit[i]["stock"]:<6} | {fruit[i]["price"]:<10}")
        break

    # Membeli Buah
    elif menu == 4:
        print("Daftar buah")
        print("Index  | Nama   | Stock  | Harga")
        # Menampilkan index, nama, stock, dan harga buah sesuai index
        for i in fruit:
            print(f"{i:<6} | {fruit[i]["name"]:<6} | {fruit[i]["stock"]:<6} | {fruit[i]["price"]:<10}")

        total_cart = 0
        
        while True:
            index_buy = int(input("\nMasukkan index buah yang ingin dibeli: "))
            to_buy = int(input("Masukkan jumlah yang ingin dibeli: "))

            name_buy  = fruit[index_buy]["name"]
            stock_buy = fruit[index_buy]["stock"]
            price_buy = fruit[index_buy]["price"]

            name_cart  = cart["name"]
            qty_cart   = cart["qty"]
            price_cart = cart["price"]

            # Kalo yang mau dibeli lebih BANYAK daripada stok yang ada
            if to_buy > stock_buy:
                print(f"Stock tidak cukup, stock {name_buy} tinggal {stock_buy}")
            
            # Kalo yang mau dibeli lebih SEDIKIT daripada stok yang ada
            else:
                # Jika menambah buah yang sama pada transaksi yang beda, cart langsung jadi satu baris dengan nambahin qty
                # Tidak perlu append karena tidak mau nambahin nilai baru
                ## Kalo buah udah pernah masuk cart
                if name_buy in name_cart:
                    # Cari posisi index di cart
                    idx = name_cart.index(name_buy)
                    # Nambahin qty dari buah yang sama
                    qty_cart[idx] += to_buy

                # Kalo buah belum pernah masuk cart
                else:
                    name_cart.append(name_buy)
                    qty_cart.append(to_buy)
                    price_cart.append(price_buy)
                
            # Print isi cart yang mau dibeli
            print("Isi Cart: ")
            print("Nama   | Qty    | Harga")
            for i in range(len(name_cart)):
                print(f"{name_cart[i]:<6} | {qty_cart[i]:<6} | {price_cart[i]}")

            # Conditional statement mau beli yang lain/tidak
            buy_again = input("Mau beli yang lain (ya/tidak): ")
            if buy_again == "ya":
                continue
            # Jika tidak
            else:
                print("Daftar Belanja:")
                print("Nama   | Qty    | Harga | Total Harga")
                for i in range(len(name_cart)):
                    # total harga per buah
                    total_price = qty_cart[i] * price_cart[i]
                    # total harga seluruh belanjaan
                    total_cart += total_price
                    # print
                    print(f"{name_cart[i]:<6} | {qty_cart[i]:<6} | {price_cart[i]} | {total_price}")

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
        break

    else:
        print("Pilihan tidak ada di dalam menu.")