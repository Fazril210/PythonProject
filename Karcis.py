ulangin="y"
while ulangin=="y":
    print("""
-----------------------------------------------------------------------
SELAMAT DATANG DI TAMAN WISATA FAZRIL
TEMPAT BERBAGAI MACAM WAHANA BERMAIN DAN SPOT FOTO
-----------------------------------------------------------------------
    silahkan masukkan user dan password
    user admin
    pass admin
        """)
    
        user=input("Masukkan username :")
    
        password=input("Masukkan password :")
        if user=="admin" and password=="admin":
            ngulang="y"
            while ngulang=="y":
                print("""
-----------------------------------------------------------------------
SELAMAT DATANG DI TAMAN WISATA FAZRIL
TEMPAT BERBAGAI MACAM WAHANA BERMAIN DAN SPOT FOTO
-----------------------------------------------------------------------
silahkan pilih pembelian tiket 

a. Tiket Masuk Taman Wisata Fazril
b. Wahana Bermain
c. Spot Foto
d. Log Out
-----------------------------------------------------------------------
                """)
                pilihtiket = input("Silahkan pilih pembelian tiket dengan memasukkan abjad dari list di atas :")
# START FUNGSI A
            if pilihtiket == "a" or pilihtiket =="A":
                ulangtikettamanwisatafazril = "y"
                while ulangtikettamanwisatafazril == "y":
                    print("""
                    
                    
                    """)
                