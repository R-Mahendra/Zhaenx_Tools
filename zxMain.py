import subprocess,sys,time
from zhaenx_Package import Banner
from zhaenx_Package.zhaenx_CrackHash import *



def clearSys():
    sis = sys.platform
    if sis == "win32":
        subprocess.run("cls", shell=True)
    elif sis == "linux" or sis == "darwin":
        subprocess.run("clear", shell=True)
clearSys()
Banner.zxHeader()
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 300)
        
def zhaenx_MainCrack():
    _Options_MenuHacks = """
    ╔═══════════════╦═══════════════════════════════════════════════════════════════════════╗
    ║               ║                                                                       ║
    ║               ║ [ 1 ] Cracking [Hash_MD5]         [ 5 ] Cracking [Hash_SHA384]        ║
    ║               ║                                                                       ║
    ║               ║ [ 2 ] Cracking [Hash_SHA1]        [ 6 ] Cracking [Hash_SHA512]        ║
    ║  [ OPTIONS ]  ║                                                                       ║
    ║               ║ [ 3 ] Cracking [Hash_SHA224]      [ 7 ] Check type Hashing            ║
    ║               ║                                                                       ║
    ║               ║ [ 4 ] Cracking [Hash_SHA256]      [ 0 ] BACK                          ║
    ║               ║                                                                       ║  
    ╚═══════════════╩═══════════════════════════════════════════════════════════════════════╝"""
    print(_Options_MenuHacks)
    try:
        MenuHacks = input(
            (
                (
                    """
┌──[𝙯HaEN✘]-[PILIH ANGKA OPSI MENU]
└─➣  """
                )
            )
        )
        if MenuHacks == "1":
            zhaenx_Crackx.md5_Crack()
        elif MenuHacks == "2":
            zhaenx_Crackx.sha1_Crack()
        elif MenuHacks == "3":
            zhaenx_Crackx.sha224_Crack()
        elif MenuHacks == "4":
            zhaenx_Crackx.sha256_Crack()
        elif MenuHacks == "5":
            zhaenx_Crackx.sha384_Crack()
        elif MenuHacks == "6":
            zhaenx_Crackx.sha512_Crack()
        elif MenuHacks == "7":
            zhaenx_Crackx._CheckTypeHas()
        elif MenuHacks == "0":
            clearSys()
            Banner.zxHeader()
            zhaenx_MainApp()
        else:
            print("Opsi Yang Anda Masukan Salah...!!!")
            Tanya = input("Ulang Lagi...(y/n)? ")
            if Tanya == "y" or Tanya == "Y":
                clearSys()
                Banner.zxHeader()
                zhaenx_MainCrack()
            else:
                slowprint("════════════════ Keluar Program ════════════════")
                exit()
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()

    


def zhaenx_MainHack():
    _Options_MenuHack = """
    ╔═══════════════╦═══════════════════════════════════════════════════════════════╗
    ║               ║                                                               ║
    ║               ║ [ 1 ] TRACK INFO WEBSITE      [ x ] TRACK SUBDOMAIN           ║
    ║               ║                                                               ║
    ║               ║ [ 2 ] PORT SCANNER            [ x ] TRACK PANEL LOGIN ADMIN   ║
    ║  [ OPSION ]   ║                                                               ║
    ║               ║ [ 3 ] TRACK EMAIL WEBSITE     [ 6 ] TRACK HYPER LINK WEBSTIE  ║
    ║               ║                                                               ║
    ║               ║ [ 0 ] BACK                    [ 7 ] WORDLIST GENERATED        ║
    ║               ║                                                               ║
    ╚═══════════════╩═══════════════════════════════════════════════════════════════╝"""
    print(_Options_MenuHack)
    try:
        MenuHacks = input(
            (
                (
                    """
┌──[𝙯HaEN✘]-[PILIH ANGKA OPSI MENU]
└─➣  """
                )
            )
        )
        if MenuHacks == "1":
            pass
        elif MenuHacks == "2":
            pass
        elif MenuHacks == "3":
            pass
        elif MenuHacks == "4":
            pass
        elif MenuHacks == "5":
            pass
        elif MenuHacks == "6":
            pass
        elif MenuHacks == "7":
            pass
        elif MenuHacks == "0":
            clearSys()
            Banner.zxHeader()
            zhaenx_MainApp()
        else:
            print("Opsi Yang Anda Masukan Salah...!!!")
            Tanya = input("Ulang Lagi...(y/n)? ")
            if Tanya == "y" or Tanya == "Y":
                clearSys()
                Banner.zxHeader()
                zhaenx_MainCrack()
            else:
                slowprint("════════════════ Keluar Program ════════════════")
                exit()
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()

def zhaenx_MainApp():
    MainAPP ="""
    ┌═════════════════════════╦═════════════════════════════════┐
    █                         ║                                 █
    █                         ║   [1] ZX-CRACK                  █
    █                         ║                                 █   ♦ Version 2.5
    █      [ OPSTIONS ]       ║   [2] ZX-HACKX                  █   ♦ Date 10-10-2022
    █                         ║                                 █   ♦ Code By 𝙯HaEN✘
    █                         ║   [3] EXIT                      █
    █                         ║                                 █
    └═════════════════════════╩═════════════════════════════════┘ """
    print(MainAPP)
    try:
        MenuHacks = input(
        (
            (
                """
┌──[𝙯HaEN✘]-[PILIH OPSI MENU]
└─➣  """
            )
        )
    )
        if MenuHacks == "1" or MenuHacks == "zx-Crack" or MenuHacks == "ZX-CRACK":
            clearSys()
            Banner.zxHeader()
            zhaenx_MainCrack()
        elif MenuHacks == "2" or MenuHacks == "zx-Hackx" or MenuHacks == "ZX-HACKX":
            clearSys()
            Banner.zxHeader()
            zhaenx_MainHack()
        elif MenuHacks == "3" or MenuHacks == "exit" or MenuHacks == "EXIT":
            slowprint("════════════════ Keluar Program ════════════════")
            exit()
        else:
            print("Opsi Yang Anda Masukan Salah...!!!")
            Tanya = input("Ulang Lagi...(y/n)? ")
            if Tanya == "y" or Tanya == "Y":
                clearSys()
                Banner.zxHeader()
                zhaenx_MainApp()
            else:
                slowprint("════════════════ Keluar Program ════════════════")
                exit()
    except KeyboardInterrupt:
        slowprint("\n════════════════ Interrupt By User ════════════════")
        exit()