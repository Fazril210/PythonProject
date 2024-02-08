data_product = {
    1:"Laptop",
    2:"Mouse ",
    3:"Monitor",
    4:"MousePad",
    5:"Charger"
}

daftar_harga = {
    1: 17000000,
    2: 2000000,
    3: 4500000,
    4: 8000000,
    5: 1500000
}

dict_trx = {}
daftar_metode_pembayaran = {
    1:"Transfer Bank",
    2:"Virtual Account",
    3:"Cash On Delivery",
    4:"Kartu Kredit"
}

print("=================Daftar Produk=================")
for i in data_product:
    print("Id Produk :",i,"\t Nama Produk : ",data_product[i],"\t Harga Produk : ",daftar_harga[i])

pilih_id = int(input("Pilih Id Produk : "))
if pilih_id in  data_product :
    pilih_beli = input("Ingin Beli ? (Y/N): ")
    if pilih_beli == "Y" or pilih_beli == "y":
        nama_penerima    = input("Nama Penerima    : ")
        alamat_penerima  = input("Alamat Penerima  : ")
        telepon          = input("No HP            : ")
        kurir_pengiriman = input("Kurir Pengiriman : ")
        dict_trx = {
            "nama penerima":nama_penerima,
            "alamat penerima":alamat_penerima,
            "No HP":telepon,
            "Kurir Pengiriman":kurir_pengiriman,
            "product id":data_product, 
        }
    else:
        pass
    if len (dict_trx) > 0 :
        print("========================== Metode Pembayaran ==========================")
    for i in daftar_metode_pembayaran:
        print("Id : ", i, "\t Metode Pembayaran : ", daftar_metode_pembayaran[i])
    pilih_metode = int(input("Pilih ID Metode Pembayaran : "))
    if pilih_metode in daftar_metode_pembayaran :
        print("Nama Penerima : ", dict_trx["nama penerima"])
        print("Alamat Penerima : ", dict_trx["alamat penerima"])
        print("No HP : ", dict_trx["No HP"])
        print("Kurir Pengiriman : ", dict_trx["Kurir Pengiriman"])
        print("Produk : ", data_product["pilih_id"])
        print("Harga : ", daftar_harga["pilih_id"])
        print("Metode Pembayaran", daftar_metode_pembayaran[pilih_metode])
        konfirmasi = input("Apakah Anda Yakin ingin melakukan pembayaran? (Y/N) :")
        if konfirmasi == "Y" or konfirmasi == "y":
            print("Anda sudah berhasil melakukan pembayaran")
        else : 
            pass
    else:
        print("Id metode pembayaran tidak tersedia")
else:
    print("Id produk tidak tersedia")




