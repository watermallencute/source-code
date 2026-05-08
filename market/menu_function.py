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

def view_menu(): # kalo bikin fungsi TANPA input, pas dipanggil di main menu harus TANPA input
    print("\nDaftar Menu")
    print(' 1. Menampilkan Daftar Buah\n',
          '2. Menambah Buah\n',
          '3. Menghapus Buah\n',
          '4. Membeli Buah\n',
          '5. Exit Program')
    menu = int(input("Masukkan angka Menu yang ingin dijalankan: "))
    return menu

def get_product(data): # Menampilkan index, nama, stock, dan harga buah sesuai index
    print("\nDaftar buah")
    print("Index  | Nama   | Stock  | Harga")
    for i in data:
        fruit_name = fruit[i]["name"]
        fruit_stock = fruit[i]["stock"]
        fruit_price = fruit[i]["price"]
        print(f"{i:<6} | {fruit_name:<6} | {fruit_stock:<6} | {fruit_price:<10,}")

def search_product(search_fruit_name): # kalo bikin fungsi DENGAN input, pas dipanggil di main menu harus DENGAN input
    search_result = []
    for i in fruit:
        fruit_name = fruit[i]["name"]
        if search_fruit_name.lower() in fruit_name.lower():
            search_result.append(i)
    get_product(search_result)

def add_fruit(fruit_name, fruit_stock = 0, fruit_price = 0):
    new_index = len(fruit)

    new_fruit = {
        "name"  : fruit_name,
        "stock" : fruit_stock,
        "price" : fruit_price
    }   

    print(new_fruit)
    confirm = input("Yakin untuk menambah buah (ya/tidak): ")
    if confirm.lower() == "ya":
        fruit[new_index] = new_fruit
        print("Produk baru berhasil ditambahkan!")
    else:
        print("Produk baru gagal ditambahkan.")

# def other_menu():
#     menu_again = input("\nApakah mau memilih menu lain (ya/tidak)? ")
#     if menu_again == "tidak":
#         break
    
while True:
    menu = view_menu()
    # Menampilkan Daftar Buah
    if menu == 1:
        print("\nSub-Menu Lihat daftar Buah")
        print(" 1. Lihat semua daftar buah\n",
              "2. Cari buah\n",
              "3. Kembali")
        
        sub_menu = input("Masukkan angka Sub-Menu yang ingin dijalankan: ")
        if sub_menu == "1":
            get_product(fruit)
        elif sub_menu == "2":
            search = input("Masukkan nama buah: ")
            search_product(search)

        menu_again = input("\nApakah mau memilih menu lain (ya/tidak)? ")
        if menu_again == "tidak":
            break

    # Menambah Buah
    elif menu == 2:
        while True:
            print("Tambah Daftar Buah")
            new_name  = input("\nMasukkan Nama Buah   : ")
            new_stock = int(input("Masukkan Stock Buah  : "))
            new_price = int(input("Masukkan Harga Buah  : "))

            add_fruit(new_name, new_stock, new_price)

            get_product(fruit)

            confirm_msg = input("Mau lanjut tambah buah (ya/tidak): ")
            if confirm_msg != "ya":
                break

        menu_again = input("\nApakah mau memilih menu lain (ya/tidak)? ")
        if menu_again == "tidak":
            break
            
    # Menghapus Buah
    elif menu == 3:
        while True: 
            get_product(fruit)
            
            index_delete = int(input("Masukkan index buah yang ingin dihapus: "))
            if index_delete in fruit:
                fruit.pop(index_delete)

            get_product(fruit)
            break

        menu_again = input("\nApakah mau memilih menu lain (ya/tidak)? ")
        if menu_again == "tidak":
            break

    # Membeli Buah
    elif menu == 4:
        while True: 
            get_product(fruit)

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

        menu_again = input("\nApakah mau memilih menu lain (ya/tidak)? ")
        if menu_again == "tidak":
            break

    # Exit Program
    elif menu == 5: 
        print("\nKeluar dari program.")
        break

    else:
        print("Pilihan tidak ada di dalam menu.")