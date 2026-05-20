from inventaris_kantin import Makanan, Minuman

daftar_barang = []
riwayat = []

def tambah_makanan():

    nama = input(
        "nama makanan : "
    )

    harga = int(
        input("harga : ")
    )

    stok = int(
        input("stok : ")
    )

    tanggal = int(
        input(
            "tanggal expired : "
        )
    )

    bulan = int(
        input(
            "bulan expired : "
        )
    )

    tahun = int(
        input(
            "tahun expired : "
        )
    )

    barang = Makanan(
        nama,
        harga,
        stok,
        tanggal,
        bulan,
        tahun
    )

    daftar_barang.append(
        barang
    )

    print(
        "makanan berhasil ditambahkan"
    )


def tambah_minuman():

    nama = input(
        "nama minuman : "
    )

    harga = int(
        input("harga : ")
    )

    stok = int(
        input("stok : ")
    )

    suhu = int(
        input(
            "suhu minuman : "
        )
    )

    barang = Minuman(
        nama,
        harga,
        stok,
        suhu
    )

    daftar_barang.append(
        barang
    )

    print(
        "minuman berhasil ditambahkan"
    )


def lihat_barang():

    if len(
        daftar_barang
    ) == 0:

        print(
            "barang kosong"
        )

    else:

        for i, barang in enumerate(
            daftar_barang,
            start=1
        ):

            print(f"""
===== data barang =====

nomor : {i}
nama : {barang.nama}
harga : Rp {barang.get_harga()}
stok : {barang.get_stok()}
status : {barang.layak()}
""")


def beli_barang():

    if len(
        daftar_barang
    ) == 0:

        print(
            "barang kosong"
        )

    else:

        print("""
===== daftar barang =====
""")

        for i, barang in enumerate(
            daftar_barang,
            start=1
        ):

            print(
                f"{i}. {barang.nama}"
            )

        index = int(
            input(
                "pilih barang : "
            )
        ) - 1

        nama_pembeli = input(
            "nama pembeli : "
        )

        jumlah = int(
            input(
                "jumlah beli : "
            )
        )

        if jumlah > daftar_barang[
            index
        ].get_stok():

            print(
                "stok tidak cukup"
            )

        else:

            harga_awal = (
                daftar_barang[
                    index
                ].get_harga() * jumlah
            )

            total = daftar_barang[
                index
            ].hitung_total(
                jumlah
            )

            diskon = (
                harga_awal - total
            )

            print(f"""
===== rincian harga =====

harga awal :
Rp {harga_awal}

diskon :
Rp {diskon}

total bayar :
Rp {total}
""")

            bayar = (int(
                input(
                    "uang bayar : "
                ))
            )

            if bayar < total:

                kurang = (
                    total - bayar
                )

                print(f"""
uang kurang :
Rp {kurang}
""")

            else:

                kembalian = (
                    bayar - total
                )

                stok_baru = (
                    daftar_barang[
                        index
                    ].get_stok() - jumlah
                )

                daftar_barang[
                    index
                ].set_stok(
                    stok_baru
                )

                riwayat.append(
                    {
                        "pembeli":
                        nama_pembeli,

                        "barang":
                        daftar_barang[
                            index
                        ].nama,

                        "jumlah":
                        jumlah,

                        "harga_awal":
                        harga_awal,

                        "diskon":
                        diskon,

                        "total":
                        total,

                        "bayar":
                        bayar,

                        "kembalian":
                        kembalian
                    }
                )

                print(f"""
===== struk pembelian =====

nama pembeli :
{nama_pembeli}

barang :
{daftar_barang[index].nama}

jumlah :
{jumlah}

harga awal :
Rp {harga_awal}

diskon :
Rp {diskon}

total bayar :
Rp {total}

uang bayar :
Rp {bayar}

kembalian :
Rp {kembalian}
""")

                print("""
===== riwayat pembelian =====
""")

                for data in riwayat:

                    print(f"""
nama pembeli :
{data["pembeli"]}

barang :
{data["barang"]}

jumlah :
{data["jumlah"]}

total :
Rp {data["total"]}

bayar :
Rp {data["bayar"]}

kembalian :
Rp {data["kembalian"]}
""")


while True:

    print("""
======== kantin SMKN 11 BANDUNG ========

1. tambah makanan
2. tambah minuman
3. lihat barang
4. beli barang
5. keluar
""")

    pilih = input(
        "pilih menu : "
    )

    if pilih == "1":

        tambah_makanan()

    elif pilih == "2":

        tambah_minuman()

    elif pilih == "3":

        lihat_barang()

    elif pilih == "4":

        beli_barang()

    elif pilih == "5":

        print(
            "program selesai"
        )

        break

    else:

        print(
            "menu tidak tersedia"
        )