import hashlib,sys,time,os
from datetime import datetime
from tabulate import tabulate
from colorama import Fore,Style

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 200)
#==================== MD5 END ====================
def md5_Crack():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y / ')
        counter = 1
        # Mendapatkan direktori skrip saat ini
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Path absolut ke file wordlist
        fileWordList = os.path.join(current_directory,"wordlist_password.txt")

        _Input_md5Hash = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN NILAI HASH]
└─➣  """)))

        if not _Input_md5Hash.strip():
            Tanya = input(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!\n ULANG LAGI?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue  # Lakukan loop untuk meminta input ulang
            else:
                exit(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!" + Style.BRIGHT + Style.RESET_ALL)
        break

    wordlist = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN PATH WORDLIST]
└─➣  """)))
    if not wordlist:
        wordlist = fileWordList
    try:
        
        wordlist_pswd = open(wordlist,"r",encoding="cp437",errors='ignore')
    except:
        exit(Fore.RED+"FILE TIDAK DI TEMUKAN...!!!"+Style.BRIGHT+Style.RESET_ALL)

    try:
        for paswd in wordlist_pswd:
            md5 = hashlib.md5()
            md5.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] MEMPROSES BRUTE_FORCE : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                slowprint("\n════════════════ Interrupt By User ════════════════")
                exit()
            if _Input_md5Hash.strip() == md5.hexdigest():
                table = [['NILAI HASH MD5',f'{_Input_md5Hash}'],
                ['PASSWORD DI TEMUKAN',f'{paswd.strip()} '],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             PASSWORD TIDAK DITEMUKAN                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()
    wordlist_pswd.close()
#==================== MD5 END ====================
#==================== SHA1 START ====================

def sha1_Crack():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y / ')
        counter = 1
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist_password.txt")
        _Input_sha1Hash = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN NILAI HASH]
└─➣  """)))

        if not _Input_sha1Hash.strip():
            Tanya = input(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!\n ULANG LAGI?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue  # Lakukan loop untuk meminta input ulang
            else:
                exit(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!" + Style.BRIGHT + Style.RESET_ALL)
        break
    wordlist = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN PATH WORDLIST]
└─➣  """)))
    if not wordlist:
        wordlist = fileWordList
    try:
        wordlist_pswd = open(wordlist,"r",encoding="cp437",errors='ignore')
    except:
        exit(Fore.RED+"FILE TIDAK DI TEMUKAN...!!!"+Style.BRIGHT+Style.RESET_ALL)
    try:
        for paswd in wordlist_pswd:
            sha1 = hashlib.sha1()
            sha1.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] MEMPROSES BRUTE_FORCE : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                slowprint("\n════════════════ Interrupt By User ════════════════")
                exit()
            if _Input_sha1Hash.strip() == sha1.hexdigest():
                table = [['NILAI HASH MD5',f'{_Input_sha1Hash}'],
                ['PASSWORD DI TEMUKAN',f'{paswd.strip()} '],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             PASSWORD TIDAK DITEMUKAN                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()
    wordlist_pswd.close()

#==================== SHA1 END ====================
#==================== SHA224 START ====================

def sha224_Crack():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y / ')
        counter = 1        
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist_password.txt")
        _Input_sha224Hash = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN NILAI HASH]
└─➣  """)))
        if not _Input_sha224Hash.strip():
            Tanya = input(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!\n ULANG LAGI?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue  # Lakukan loop untuk meminta input ulang
            else:
                exit(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!" + Style.BRIGHT + Style.RESET_ALL)
        break
    wordlist = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN PATH WORDLIST]
└─➣  """)))
    if not wordlist:
        wordlist = fileWordList
    try:
        wordlist_pswd = open(wordlist,"r",encoding="cp437",errors='ignore')
    except:
        exit(Fore.RED+"FILE TIDAK DI TEMUKAN...!!!"+Style.BRIGHT+Style.RESET_ALL)
    try:
        for paswd in wordlist_pswd:
            sha224 = hashlib.sha224()
            sha224.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] MEMPROSES BRUTE_FORCE : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                slowprint("\n════════════════ Interrupt By User ════════════════")
                exit()
            if _Input_sha224Hash.strip() == sha224.hexdigest():
                table = [['NILAI HASH MD5',f'{_Input_sha224Hash}'],
                ['PASSWORD DI TEMUKAN',f'{paswd.strip()} '],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             PASSWORD TIDAK DITEMUKAN                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()
    wordlist_pswd.close()
#==================== SHA224 END ====================

#==================== SHA256 START ====================

def sha256_Crack():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y / ')
        counter = 1
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist_password.txt")
        _Input_sha256Hash = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN NILAI HASH]
└─➣  """)))
        if not _Input_sha256Hash.strip():
            Tanya = input(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!\n ULANG LAGI?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue  # Lakukan loop untuk meminta input ulang
            else:
                exit(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!" + Style.BRIGHT + Style.RESET_ALL)
        break
    wordlist = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN PATH WORDLIST]
└─➣  """)))
    if not wordlist:
        wordlist = fileWordList
    try:
        wordlist_pswd = open(wordlist,"r",encoding="cp437",errors='ignore')
    except:
        exit(Fore.RED+"FILE TIDAK DI TEMUKAN...!!!"+Style.BRIGHT+Style.RESET_ALL)
    try:
        for paswd in wordlist_pswd:
            sha256 = hashlib.sha256()
            sha256.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] MEMPROSES BRUTE_FORCE : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                slowprint("\n════════════════ Interrupt By User ════════════════")
                exit()
            if _Input_sha256Hash.strip() == sha256.hexdigest():
                table = [['NILAI HASH MD5',f'{_Input_sha256Hash}'],
                ['PASSWORD DI TEMUKAN',f'{paswd.strip()} '],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             PASSWORD TIDAK DITEMUKAN                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()
    wordlist_pswd.close()

#==================== SHA256 END ====================

#==================== SHA384 START ====================

def sha384_Crack():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y / ')
        counter = 1
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist_password.txt")
        _Input_sha384Hash = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN NILAI HASH]
└─➣  """)))
        if not _Input_sha384Hash.strip():
            Tanya = input(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!\n ULANG LAGI?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue  # Lakukan loop untuk meminta input ulang
            else:
                exit(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!" + Style.BRIGHT + Style.RESET_ALL)
        break
    wordlist = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN PATH WORDLIST]
└─➣  """)))
    if not wordlist:
        wordlist = fileWordList
    try:
        wordlist_pswd = open(wordlist,"r",encoding="cp437",errors='ignore')
    except:
        exit(Fore.RED+"FILE TIDAK DI TEMUKAN...!!!"+Style.BRIGHT+Style.RESET_ALL)
    try:
        for paswd in wordlist_pswd:
            sha384 = hashlib.sha384()
            sha384.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] MEMPROSES BRUTE_FORCE : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                slowprint("\n════════════════ Interrupt By User ════════════════")
                exit()
            if _Input_sha384Hash.strip() == sha384.hexdigest():
                table = [['NILAI HASH MD5',f'{_Input_sha384Hash}'],
                ['PASSWORD DI TEMUKAN',f'{paswd.strip()} '],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             PASSWORD TIDAK DITEMUKAN                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()
    wordlist_pswd.close()

#==================== SHA384 END ====================

#==================== SHA512 START ====================

def sha512_Crack():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y / ')
        counter = 1
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist_password.txt")
        _Input_sha512Hash = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN NILAI HASH]
└─➣  """)))
        if not _Input_sha512Hash.strip():
            Tanya = input(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!\n ULANG LAGI?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue  # Lakukan loop untuk meminta input ulang
            else:
                exit(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!" + Style.BRIGHT + Style.RESET_ALL)
        break
    wordlist = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN PATH WORDLIST]
└─➣  """)))
    if not wordlist:
        wordlist = fileWordList
    try:
        wordlist_pswd = open(wordlist,"r",encoding="cp437",errors='ignore')
    except:
        exit(Fore.RED+"FILE TIDAK DI TEMUKAN...!!!"+Style.BRIGHT+Style.RESET_ALL)
    try:
        for paswd in wordlist_pswd:
            sha512 = hashlib.sha512()
            sha512.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] MEMPROSES BRUTE_FORCE : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                slowprint("\n════════════════ Interrupt By User ════════════════")
                exit()
            if _Input_sha512Hash.strip() == sha512.hexdigest():
                table = [['NILAI HASH MD5',f'{_Input_sha512Hash}'],
                ['PASSWORD DI TEMUKAN',f'{paswd.strip()} '],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             PASSWORD TIDAK DITEMUKAN                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()
    wordlist_pswd.close()
#==================== SHA512 END ====================

def _CheckTypeHas():
# Contoh penggunaan
    try:
        hash_value = input((("""
┌──[𝙯HaEN✘]-[MASUKKAN NILAI HASH]
└─➣  """)))  # Contoh hash MD5 "test">> 098f6bcd4621d373cade4e832627b4f6
        hash_type = zhaenxCheck_typeHash(hash_value)

        # Menampilkan hasil jenis hash
        if hash_type:
            _Table =[[f"JUMLAH CHARACTER HASH ➣  {len(hash_value)}"],
                     [f"{'TIPE HASH':22}➣  {hash_type}".upper()],
                     [f"{'nilai has':22}➣  {hash_value}".upper()]]
            print(tabulate(_Table, tablefmt="double_grid"))
        else:
            print("Tipe hash tidak ditemukan".upper())

        Tanya = str(input("Ulang Lagi (Y/n)? "))
        if Tanya == "y" or Tanya == "Y":
            _CheckTypeHas()
        else:
            slowprint("════════════════ Keluar Program ════════════════")
            exit()
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()

    # Fungsi untuk memeriksa jenis hash
def zhaenxCheck_typeHash(hash_value):
    # Mendapatkan algoritma hash yang tersedia
    hash_algorithms = hashlib.algorithms_guaranteed

    # Melakukan iterasi pada setiap algoritma hash
    for algorithm in hash_algorithms:
        try:
            # Memeriksa apakah algoritma hash ini dapat digunakan
            hashlib.new(algorithm, b'').digest_size
        except ValueError:
            continue

        # Membuat objek hash dengan algoritma yang sedang diperiksa
        hash_obj = hashlib.new(algorithm)

        # Memeriksa panjang hash yang cocok dengan panjang objek hash
        if len(hash_value) == hash_obj.digest_size * 2:
            return algorithm

    return None