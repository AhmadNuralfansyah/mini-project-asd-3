class ReviewFilm:
    def __init__(self, judul, genre, tahun, rating, komentar):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun
        self.rating = rating
        self.komentar = komentar


class Node:
    def __init__(self, review):
        self.data = review
        self.next = None


class DatabaseReview:
    def __init__(self):
        self.head = None

    def tambah_review_awal(self, review):
        new_node = Node(review)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.next = temp

    def tambah_review_akhir(self, review):
        new_node = Node(review)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def tambah_review_diantara(self, review, judul_sebelumnya):
        new_node = Node(review)
        prev = None
        temp = self.head
        while temp:
            if temp.data.judul.lower() == judul_sebelumnya.lower():
                if not prev:
                    self.head = new_node
                else:
                    prev.next = new_node
                new_node.next = temp
                print(f"Review telah ditempatkan antaran film '{judul_sebelumnya}'")
                return
            prev = temp
            temp = temp.next
        print(f"Review film '{judul_sebelumnya}' tidak ditemukan.")

    def tampilkan_semua_review(self):
        if not self.head:
            print("Belum ada review film.")
        else:
            temp = self.head
            while temp:
                print(f"\n===Review Film:===\n"
                    f"Judul: {temp.data.judul}\n"
                    f"Genre: {temp.data.genre}\n"
                    f"Tahun: {temp.data.tahun}\n"
                    f"Rating: {temp.data.rating}\n"
                    f"Komentar: {temp.data.komentar}")
                temp = temp.next

    def cari_review_by_judul(self, judul):
        temp = self.head
        while temp:
            if temp.data.judul.lower() == judul.lower():
                return temp.data
            temp = temp.next
        return None

    def update_review(self, judul, review_baru):
        review = self.cari_review_by_judul(judul)
        if review:
            review.rating = review_baru.rating
            review.komentar = review_baru.komentar
            print(f"Review film '{judul}' berhasil diperbarui.")
        else:
            print(f"Review film '{judul}' tidak ditemukan.")

    def hapus_review_diantara(self, judul):
        prev = None
        temp = self.head
        while temp:
            if temp.data.judul.lower() == judul.lower():
                if not prev:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                print(f"Review film '{judul}' berhasil dihapus.")
                return
            prev = temp
            temp = temp.next
        print(f"Review film '{judul}' tidak ditemukan.")

    def hapus_review_awal(self):
        if not self.head:
            print("Belum ada review film.")
        else:
            self.head = self.head.next

    def hapus_review_akhir(self):
        if not self.head:
            print("Belum ada review film.")
        else:
            prev = None
            temp = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            if not prev:
                self.head = None
            else:
                prev.next = None

    def merge_sort(self, array, key, reverse):
        if len(array) <= 1:
            return array

        # Splitting the array into halves
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        # Recursive calls to merge_sort for both halves
        left_half = self.merge_sort(left_half, key, reverse)
        right_half = self.merge_sort(right_half, key, reverse)

        return self.merge(left_half, right_half, key, reverse)

    def merge(self, left, right, key, reverse):
        merged = []
        left_index = 0
        right_index = 0

        
        while left_index < len(left) and right_index < len(right):
            if reverse:
                if getattr(left[left_index].data, key) > getattr(right[right_index].data, key):
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1
            else:
                if getattr(left[left_index].data, key) < getattr(right[right_index].data, key):
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1

        
        merged += left[left_index:]
        merged += right[right_index:]

        return merged

    def urutkan_review(self, key, reverse=False):
        reviews = []
        temp = self.head
        while temp:
            reviews.append(temp)
            temp = temp.next

        sorted_reviews = self.merge_sort(reviews, key, reverse)

        if not reverse:
            print("Urutan ascending:")
        else:
            print("Urutan descending:")

        for review in sorted_reviews:
            print(f"\n===Review Film:===\n"
                f"Judul: {review.data.judul}\n"
                f"Genre: {review.data.genre}\n"
                f"Tahun: {review.data.tahun}\n"
                f"Rating: {review.data.rating}\n"
                f"Komentar: {review.data.komentar}")

database_review = DatabaseReview()


def tambah_review(self=None):
    judul = input("Masukkan judul film: ")
    genre = input("Masukkan genre film: ")
    tahun = int(input("Masukkan tahun film: "))
    rating = int(input("Masukkan rating film (1-10): "))
    komentar = input("Masukkan komentar film: ")

    review_baru = ReviewFilm(judul, genre, tahun, rating, komentar)

    while True:
        print("\n")
        print("===Pilih Posisi Penambahan===")
        print("1. Tambah di Awal")
        print("2. Tambah di Akhir")
        print("3. Tambah di Antara")
        print("0. Kembali")

        pilihan_tambah = int(input("Masukkan pilihan: "))

        if pilihan_tambah == 1:
            database_review.tambah_review_awal(review_baru)
            print(f"Review film '{judul}' berhasil ditambahkan di awal.")
            break

        elif pilihan_tambah == 2:
            database_review.tambah_review_akhir(review_baru)
            print(f"Review film '{judul}' berhasil ditambahkan di akhir.")
            break

        elif pilihan_tambah == 3:
            judul_sebelumnya = input("Masukkan judul film sebagai referensi: ")
            database_review.tambah_review_diantara(review_baru, judul_sebelumnya)
            break

        elif pilihan_tambah == 0:
            break

        else:
            print("Pilihan tidak valid.")

database_review = DatabaseReview()


while True:
    print("\n")
    print("==Menu Review Film==")
    print("1. Tambah Review")
    print("2. Tampilkan Semua Review")
    print("3. Cari Review")
    print("4. Update Review")
    print("5. Hapus Review")
    print("6. Urutkan Review")
    print("0. Keluar")

    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        tambah_review()

    elif pilihan == 2:
        database_review.tampilkan_semua_review()

    elif pilihan == 3:
        judul = input("Masukkan judul film yang ingin dicari: ")
        review = database_review.cari_review_by_judul(judul)

        if review:
            print(f"Review film '{judul}' ditemukan:")
            print(review)
        else:
            print(f"Review film '{judul}' tidak ditemukan.")

    elif pilihan == 4:
        judul = input("Masukkan judul film yang ingin diupdate: ")
        review = database_review.cari_review_by_judul(judul)

        if review:
            rating_baru = int(input("Masukkan rating baru (1-10): "))
            komentar_baru = input("Masukkan komentar baru: ")

            review_baru = ReviewFilm(judul, review.genre, review.tahun, rating_baru, komentar_baru)
            database_review.update_review(judul, review_baru)
        else:
            print(f"Review film '{judul}' tidak ditemukan.")

    elif pilihan == 5:
        while True:
                print("\n")
                print("===Pilih Posisi Penghapusan===")
                print("1. Hapus di Awal")
                print("2. Hapus di Akhir")
                print("3. Hapus di Antara")
                print("0. Kembali")

                pilihan_hapus = int(input("Masukkan pilihan: "))

                if pilihan_hapus == 1:
                    database_review.hapus_review_awal()
                    print("Review film pertama berhasil dihapus.")
                    break

                elif pilihan_hapus == 2:
                    database_review.hapus_review_akhir()
                    print("Review film terakhir berhasil dihapus.")
                    break

                elif pilihan_hapus == 3:
                    judul = input("Masukkan judul film sebagai referensi: ")
                    database_review.hapus_review_diantara(judul)
                    break

                elif pilihan_hapus == 0:
                    break

                else:
                    print("Pilihan tidak valid.")

    elif pilihan == 6:
        while True:
            print("\n")
            print("===Pilih Jenis Pengurutan===")
            print("1. Urutkan Ascending")
            print("2. Urutkan Descending")
            print("0. Kembali")

            pilihan_sorting = int(input("Masukkan pilihan: "))

            if pilihan_sorting == 1:
                key = input("Masukkan atribut untuk pengurutan(judul/tahun/rating): ")
                database_review.urutkan_review(key)
                break

            elif pilihan_sorting == 2:
                key = input("Masukkan atribut untuk pengurutan(judul/tahun/rating): ")
                database_review.urutkan_review(key, reverse=True)
                break

            elif pilihan_sorting == 0:
                break

            else:
                print("Pilihan tidak valid.")

    elif pilihan == 0:
        break

    else:
        print("Pilihan tidak valid.")
