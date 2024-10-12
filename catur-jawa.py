import os
import random as rn
import time

def clear():
    os.system("cls")

def dashboard():
    clear()
    print("x"*50)
    print("Selamat Datang di Catur Jawa")
    print("o"*50)
    
    print("1. Player vs Bot\n2. Player vs Player\n3. Cara Bermain\n4. Keluar dari program")
    while True:
        choice = input("Pilih menu: ")
        if choice == "1":
            playerAndBot()
        elif choice == "2":
            playerAndPlayer()
        elif choice == "3":
            rules()
        elif choice == "4":
            print("Terima kasih telah bermain")
            exit()
        else:
            print("Inputan salah")
            
def playerAndBot():
    clear()
    player = input("Masukkan nama: ")
    while True:
        choice = input("Pilih objek:[x/o] ")
        if choice == "x":
            (f"{player} sebagai giliran pertama" )
            playerAndBot_first(player)
        elif choice == "o":
            print(f"{player} sebagai giliran kedua")
            playerAndBot_second(player)
        else: 
            print("Objek tidak ada. Silahkan pilih lagi.")

def playerAndBot_first(pemain):
    papan = ["x", "x", "x",
            " ", " ", " ",
            "o","o","o"]
    
    print(f"{papan[0]} | {papan[1]} | {papan[2]}\n----------\n{papan[3]} | {papan[4]} | {papan[5]}\n----------\n{papan[6]} | {papan[7]} | {papan[8]}")
    urutan = 0
    while True:
        if urutan % 2 == 0:
            print(f"Giliran {pemain}")
            try:
                turn_1 = input("Pilih objek: ")   
            except ValueError:
                print("Maaf, inputan harus angka")
                continue
            finally:
                turn_1 = int(turn_1)
                turn_1 -= 1
            if "o" in papan[turn_1]:
                input("Objek yang dipilih salah. Enter untuk kembali")
                continue
            elif "x" not in papan[turn_1] :
                input("X tidak ada. Enter untuk kembali")
                continue
            else:
                place_1 = int(input("Akan dipindahkan ke: "))-1
                if "x" in papan[place_1]:
                    input("Ruangan telah terisi. Enter untuk kembali")
                    continue
                elif "o" in papan[place_1]:
                    input("Ruangan telah terisi. Enter untuk kembali")
                    continue
                else:
                    papan[turn_1] = " "
                    papan[place_1]= "x"
            clear()
            print(f"{papan[0]} | {papan[1]} | {papan[2]}\n----------\n{papan[3]} | {papan[4]} | {papan[5]}\n----------\n{papan[6]} | {papan[7]} | {papan[8]}")
    
        if urutan % 2 != 0:
            turn_2 = rn.randint(1,9)-1
            if "o" not in papan[turn_2]:
                continue
            elif "x" in papan[turn_2]:
                continue
            else:
                place_2 = rn.randint(1,9)-1
                if "x" in papan[place_2]:
                    continue
                elif "o" in papan[place_2]:
                    continue
                else:
                    papan[turn_2] = " "
                    papan[place_2] = "o"
            clear()
            print("Giliran BOT")
            print(f"{papan[0]} | {papan[1]} | {papan[2]}\n----------\n{papan[3]} | {papan[4]} | {papan[5]}\n----------\n{papan[6]} | {papan[7]} | {papan[8]}")    
            input("Enter untuk lanjut")
        if (papan[0] == papan[4] == papan[8] == "x"):
            input(f"{pemain} menang. Enter untuk kembali")
            dashboard()
        elif (papan[2] == papan[4] == papan[6] == "x"):
            input(f"{pemain} menang. Enter untuk kembali")
            dashboard()
        elif (papan[2] == papan[4] == papan[6] == "o"):
            input(f"BOT menang. Enter untuk kembali")
            dashboard()
        elif (papan[2] == papan[4] == papan[6] == "o"):
            input(f"BOT menang. Enter untuk kembali")
            dashboard()
        urutan += 1
    
def playerAndBot_second(pemain):
    papan = ["x", "x", "x",
            " ", " ", " ",
            "o","o","o"]
    
    print(f"{papan[0]} | {papan[1]} | {papan[2]}\n----------\n{papan[3]} | {papan[4]} | {papan[5]}\n----------\n{papan[6]} | {papan[7]} | {papan[8]}")
    urutan = 0
    
    while True:
        if urutan % 2 == 0:
            turn_1 = rn.randint(1,9)-1
            if "x" not in papan[turn_1]:
                continue
            elif "o" in papan[turn_1]:
                continue
            else:
                place_1 = rn.randint(1,9)-1
                if "x" in papan[place_1]:
                    continue
                elif "o" in papan[place_1]:
                    continue
                else:
                    papan[turn_1] = " "
                    papan[place_1] = "x"
            clear()
            print("Giliran BOT")
            print(f"{papan[0]} | {papan[1]} | {papan[2]}\n----------\n{papan[3]} | {papan[4]} | {papan[5]}\n----------\n{papan[6]} | {papan[7]} | {papan[8]}")    
            input("Enter untuk lanjut")
        
        if urutan % 2 != 0:
            print(f"Giliran {pemain}")
            try:
                turn_2 = input("Pilih objek: ")
            except ValueError:
                print("Maaf inputan harus angka")
                continue
            finally:
                turn_2 = int(turn_2)
                turn_2 -= 1
            if "o" not in papan[turn_2]:
                print("Maaf, objek tidak ada")
                continue
            elif "x" in papan[turn_2]:
                print("Maaf, objek anda salah")
                continue
            else:
                place_2 = int(input("Akan dipindahkan ke: "))-1
                if "x" in papan[place_2]:
                    print("Papan telah terisi")
                    continue
                elif "o" in papan[place_2]:
                    print("Papan telah terisi")
                else:
                    papan[turn_2] = " "
                    papan[place_2] = "o"
            clear()
            print(f"{papan[0]} | {papan[1]} | {papan[2]}\n----------\n{papan[3]} | {papan[4]} | {papan[5]}\n----------\n{papan[6]} | {papan[7]} | {papan[8]}")   
        if (papan[0] == papan[4] == papan[8] == "x"):
            input(f"BOT menang. Enter untuk kembali")
            dashboard()
        elif (papan[2] == papan[4] == papan[6] == "x"):
            input(f"BOT menang. Enter untuk kembali")
            dashboard()
        elif (papan[0] == papan[4] == papan[8] == "o"):
            input(f"{pemain} menang. Enter untuk kembali")
            dashboard()
        elif (papan[2] == papan[4] == papan[6] == "o"):
            input(f"{pemain} menang. Enter untuk kembali")
            dashboard()
        urutan += 1
        
def playerAndPlayer():
    clear()
    player_1 = input("Masukkan nama: ") 
    player_2 = input("Masukkan nama: ")
    clear()
    papan = ["x", "x", "x",
            " ", " ", " ",
            "o","o","o"]
    
    print(f"{papan[0]} | {papan[1]} | {papan[2]}\n----------\n{papan[3]} | {papan[4]} | {papan[5]}\n----------\n{papan[6]} | {papan[7]} | {papan[8]}")
    urutan = 0
    while True:
        if urutan % 2 == 0:
            print(f"Giliran {player_1}")
            try:
                turn_1 = input("Pilih objek: ")   
            except ValueError:
                input("Inputan harus angka")
                continue
            finally:
                turn_1 = int(turn_1)
                turn_1 -= 1
            if "o" in papan[turn_1]:
                input("Objek yang dipilih salah. Enter untuk kembali")
                continue
            elif "x" not in papan[turn_1] :
                input("X tidak ada. Enter untuk kembali")
                continue
            else:
                place_1 = int(input("Akan dipindahkan ke: "))-1
                if "x" in papan[place_1]:
                    input("Ruangan telah terisi. Enter untuk kembali")
                    continue
                elif "o" in papan[place_1]:
                    input("Ruangan telah terisi. Enter untuk kembali")
                    continue
                else:
                    papan[turn_1] = " "
                    papan[place_1]= "x"
            clear()
            print(f"{papan[0]} | {papan[1]} | {papan[2]}\n----------\n{papan[3]} | {papan[4]} | {papan[5]}\n----------\n{papan[6]} | {papan[7]} | {papan[8]}")
            
        
        if urutan % 2 != 0:
            print(f"Giliran {player_2}")
            try:
                turn_2 = input("Pilih objek: ")   
            except ValueError:
                input("Inputan harus angka. Enter untuk kembali")
                continue
            finally:
                turn_2 = int(turn_2)
                turn_2 -= 1
            if "x" in papan[turn_2]:
                input("Objek yang dipilih salah. Enter untuk kembali")
                continue
            elif "o" not in papan[turn_2] :
                input("O tidak ada. Enter untuk kembali")
                continue
            else:
                place_2 = int(input("Akan dipindahkan ke: "))-1
                if "x" in papan[place_2]:
                    input("Ruangan telah terisi. Enter untuk kembali")
                    continue
                elif "o" in papan[place_2]:
                    input("Ruangan telah terisi. Enter untuk kembali")
                    continue
                else:
                    papan[turn_2] = " "
                    papan[place_2]= "o"
            clear()
            print(f"{papan[0]} | {papan[1]} | {papan[2]}\n----------\n{papan[3]} | {papan[4]} | {papan[5]}\n----------\n{papan[6]} | {papan[7]} | {papan[8]}")
        if (papan[0] == papan[4] == papan[8] == "x"):
            input(f"{player_1} menang. Enter untuk kembali")
            dashboard()
        elif (papan[2] == papan[4] == papan[6] == "x"):
            input(f"({player_1} menang. Enter untuk kembali")
            dashboard()
        elif (papan[0] == papan[4] == papan[8] == "o"):
            input(f"{player_2} menang. Enter untuk kembali")
            dashboard()
        elif (papan[2] == papan[4] == papan[6] == "o"):
            input(f"{player_1} menang. Enter untuk kembali")
            dashboard()
        urutan += 1

def rules():
    clear()
    print("x"*50)
    print("Cara Bermain")
    print("o"*50)

    print("Di permainan ini, konsepnya hampir sama seperti tic tac toe hanya saja ada sedikit modifikasi di mana ada unsur catur di dalamnya. Pemain 1 (x) akan memulai permainan terlebih dahulu baru dilanjut dengan Pemain 2 (o). Pemain harus berusaha untuk membuat pola pada setiap objek yang dimiliki agar bisa membentuk pola diagonal ke kiri atau ke kanan. Barangsiapa telah memmbentuk pola diagonal, maka akan ditemukan pemenangnya. Pemain tidak bisa menimpa objek dengan objek lain yang ada di kotak yang telah terisi sehingga pemain harus mencari kotak kosong untuk diberi objek. Selamat bermain")

    input("Enter untuk kembali")
    dashboard()

dashboard()