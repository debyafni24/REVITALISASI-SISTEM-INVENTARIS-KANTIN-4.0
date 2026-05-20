from abc import ABC, abstractmethod
from datetime import datetime


class Layak(ABC):

    @abstractmethod
    def layak(self):
        pass


class Produk(ABC):

    def __init__(self, nama, harga, stok):

        self.nama = nama
        self.__harga = harga
        self.__stok = stok

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def set_stok(self, stok_baru):

        if stok_baru >= 0:
            self.__stok = stok_baru

        else:
            print("stok tidak valid")

    @abstractmethod
    def hitung_total(self, jumlah):
        pass


class Makanan(
    Produk,
    Layak
):

    def __init__(
        self,
        nama,
        harga,
        stok,
        tanggal,
        bulan,
        tahun
    ):

        super().__init__(
            nama,
            harga,
            stok
        )

        self.exp = datetime(
            tahun,
            bulan,
            tanggal
        )

    def layak(self):

        sekarang = datetime.now()

        selisih = (self.exp - sekarang).days

        if selisih < 0:

            return ("makanan tidak layak jual")

        elif selisih <= 2:

            return ("makanan hampir expired")

        else:

            return ("makanan layak jual")

    def hitung_total(
        self,
        jumlah
    ):

        harga_awal = (
            self.get_harga() * jumlah
        )

        sekarang = datetime.now()

        selisih = (self.exp - sekarang).days

        if selisih <= 2:

            diskon = (harga_awal * 0.10)
            total = (harga_awal - diskon)

        else:

            total = harga_awal

        return total


class Minuman(
    Produk,
    Layak
):

    def __init__(
        self,
        nama,
        harga,
        stok,
        suhu
    ):

        super().__init__(
            nama,
            harga,
            stok
        )

        self.suhu = suhu

    def layak(self):

        if self.suhu > 10:

            return ("minuman kurang dingin")

        else:

            return ("minuman dingin")

    def hitung_total(self,jumlah):

        total = (self.get_harga() * jumlah)
        return total