pilihan="Ya"
while pilihan=="Ya":
    print("""
    ==============================
    
    Angel Share Tavern
          
    List Menu Minuman :
    ==============================
    A. Wolfhook Juice : Rp 13.000
    B. Berry Mint Burst : Rp 15.000
    C. Apple Cider : Rp 11.000
    D. Sparkling Berry : Rp 15.000
    E. Wine Khusus Venti : Rp 75.000
    ==============================
    """)
    pesan=str(input("masukkan list abjad menu ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "A":
        listnama= "Wolfhook Juice"
        harga=(13000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "B":
        listnama= "Berry Mint Burst"
        harga = (15000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "C":
        listnama= "Apple Cider"
        harga=int(11000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "D":
        listnama= "Sparkling Berry"
        harga=int(15000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    elif pesan == "E":
        listnama= "Wine Khusus Venti"
        harga=int(75000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Ya/Tidak =")
 
    print("===============Bukti Pembayaran=============")

    print("Angel Share Tavern")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)

    print("=====Terima Kasih Telah Berbelanja di Toko Kami=====")
    
    pilihan=input("apakah anda ingin order kembali Ya/Tidak =")