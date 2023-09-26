import os 
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    

while (True):
    match sistem_operasi:
        case 'posix': os.system('clear')
        case 'nt': os.system('cls')

    print('SELAMAT DATANG DI PROGRAM')
    print('DATABASE PERPUSTAKAAN DIGITAL')
    print('='*20)

    print(f"1. Read Data")
    print(f"2. Add Data")
    print(f"3. Update Data")
    print(f"4. Delete Data")

    user_option = input("Masukkan opsi: ")
    print('\n', '='*20, '\n')
    match user_option:
        case '1': print(f"1. Read Data")
        case '2': print(f"2. Add Data")
        case '3': print(f"3. Update Data")
        case '4': print(f"4. Delete Data")

    print('\n', '='*20, '\n')
    isCountinue = input("Apakah ingin dilanjutkan? (y/n) : ")
    if isCountinue == 'n':
        print("Program telah berakhir, Terimakasih :)")
        break
    



