catatan = []


def tambah_catatan():
    """Minta input dari pengguna dan tambahkan satu catatan ke list `catatan`.

    Struktur catatan adalah dict sederhana:
    {'mapel': str, 'topik': str, 'durasi': int}
    """
    # Input mapel (wajib diisi)
    mapel = input("🌟🌷 Masukkan nama mata pelajaran (mis: Matematika): ").strip()
    while not mapel:
        print("Ups, jangan kosong yaa 💌✨. Tulis nama mapelnya kecil ya~")
        mapel = input("🌟🌷 Masukkan nama mata pelajaran (mis: Matematika): ").strip()

    # Input topik (wajib diisi)
    topik = input("✨🌼 Masukkan topik yang dipelajari (contoh: Limit, Bab 1): ").strip()
    while not topik:
        print("Wah, topiknya kosong nih 😅🌈. Tulis sedikit yaa, kamu bisa! 💕")
        topik = input("✨🌼 Masukkan topik yang dipelajari (contoh: Limit, Bab 1): ").strip()

    # Input durasi (harus angka > 0)
    while True:
        durasi_input = input("⏱️✨ Kamu belajar berapa menit? (angka saja, mis: 45): ").strip()
        if durasi_input.isdigit() and int(durasi_input) > 0:
            durasi = int(durasi_input)
            break
        else:
            print("Mmm, masukkan angka positif yaa 😊✨ (mis: 45).")

    # Simpan catatan sebagai dict sederhana
    catatan_baru = {
        'mapel': mapel,
        'topik': topik,
        'durasi': durasi
    }
    catatan.append(catatan_baru)
    print(f"✨ Yeay! Catatan untuk {mapel} ({topik}, {durasi} menit) udah tersimpan. Kamu keren! 💪🌸")


def lihat_catatan():
    """Tampilkan semua catatan yang tersimpan dalam format tabel rapi.

    Jika belum ada data, tampilkan pesan yang sesuai.
    """
    if not catatan:
        print("Belum ada catatan belajar nih 😴🌼. Yuk mulai catat, tekan '1' ya! 💌🌟")
        return

    # Hitung lebar kolom secara dinamis berdasarkan isi
    no_w = max(len(str(len(catatan))), len("No"))
    mapel_w = max(len("Mapel"), max(len(c['mapel']) for c in catatan))
    topik_w = max(len("Topik"), max(len(c['topik']) for c in catatan))
    durasi_w = max(len("Durasi"), max(len(f"{c['durasi']} menit") for c in catatan))

    # Header
    header = f"{'No':>{no_w}}  {'Mapel':<{mapel_w}}  {'Topik':<{topik_w}}  {'Durasi':>{durasi_w}}"
    separator = '-' * len(header)

    print("\n🌸✨ --- Daftar Catatan Belajar (Aesthetic) --- ✨🌸")
    print(header)
    print(separator)

    # Baris data
    for i, c in enumerate(catatan, start=1):
        dur_str = f"{c['durasi']} menit"
        print(f"{i:>{no_w}}.  {c['mapel']:<{mapel_w}}  {c['topik']:<{topik_w}}  {dur_str:>{durasi_w}} 💖✨")

    print(separator)
    print(f"🌟 Total catatan: {len(catatan)} — kamu luar biasa! 🎉💖")


def total_waktu():
    """Hitung total durasi dari semua catatan dan tampilkan hasilnya."""
    if not catatan:
        print("Total waktu belajar: 0 menit — belum ada waktu dicatat nih, yuk mulai! 🌱")
        return

    total = sum(c['durasi'] for c in catatan)
    jam = total // 60
    menit = total % 60
    if jam:
        print(f"⏱️ Total waktu belajar: {total} menit ({jam} jam {menit} menit) — hebat, jalan terus! 🚀")
    else:
        print(f"⏱️ Total waktu belajar: {total} menit — keren banget! ✨")


def daftar_mapel():
    """Kembalikan daftar nama mapel unik, terurut alfabet."""
    return sorted({c['mapel'] for c in catatan})


def ringkasan_mapel(mapel):
    """Tampilkan ringkasan (jumlah catatan + total durasi) untuk sebuah mapel."""
    notes = [c for c in catatan if c['mapel'] == mapel]
    if not notes:
        print(f"Hmmm, {mapel} belum punya catatan nih 🌱. Ayo tambahkan satu, kamu pasti bisa! 💪✨")
        return
    count = len(notes)
    total = sum(c['durasi'] for c in notes)
    jam = total // 60
    menit = total % 60
    if jam:
        waktu_str = f"{total} menit ({jam} jam {menit} menit)"
    else:
        waktu_str = f"{total} menit"

    print(f"\n✨🌹 Ringkasan manis untuk {mapel}:")
    print(f"- Jumlah catatan: {count} 📝💕")
    print(f"- Total waktu: {waktu_str} ⏰🌟")
    print("Wah hebat! Terus semangat, kamu bisa! 💪💖")


def tambah_catatan(mapel_default=None):
    """Minta input dari pengguna dan tambahkan satu catatan ke list `catatan`.

    Jika `mapel_default` diberikan, gunakan sebagai nilai awal (mis. saat menambah dari tampilan per-mapel).
    Setelah menambah, tampilkan ringkasan untuk mapel tersebut dengan gaya lucu.
    """
    # Input mapel (wajib diisi) - jika ada default, gunakan dan konfirmasi
    if mapel_default:
        mapel = mapel_default.strip()
        if not mapel:
            mapel = input("🌟 Masukkan nama mata pelajaran: ").strip()
    else:
        mapel = input("🌟 Masukkan nama mata pelajaran: ").strip()
    while not mapel:
        print("Nama mata pelajaran tidak boleh kosong. 😊")
        mapel = input("🌟 Masukkan nama mata pelajaran: ").strip()

    # Input topik (wajib diisi)
    topik = input("✨🌼 Masukkan topik yang dipelajari (mis: Limit, Bab 1): ").strip()
    while not topik:
        print("Wah, topiknya kosong nih 😅🌈. Tulis sedikit ya~")
        topik = input("✨🌼 Masukkan topik yang dipelajari (mis: Limit, Bab 1): ").strip()

    # Input durasi (harus angka > 0)
    while True:
        durasi_input = input("⏱️ Masukkan durasi belajar (menit): ").strip()
        if durasi_input.isdigit() and int(durasi_input) > 0:
            durasi = int(durasi_input)
            break
        else:
            print("Masukkan angka positif untuk durasi (mis: 45). 💫")

    # Simpan catatan sebagai dict sederhana
    catatan_baru = {
        'mapel': mapel,
        'topik': topik,
        'durasi': durasi
    }
    catatan.append(catatan_baru)
    print(f"✨ Yeay! Catatan untuk {mapel} ({topik}, {durasi} menit) udah tersimpan. Kamu keren! 💪🌸")

    # Tampilkan ringkasan untuk mapel tersebut
    ringkasan_mapel(mapel)     


def edit_catatan(global_index):
    """Edit catatan berdasarkan indeks global (1-based).

    Pengguna bisa mengubah topik dan durasi. Kosongkan input untuk membiarkan nilai lama.
    """
    if not (1 <= global_index <= len(catatan)):
        print("Indeks catatan tidak valid. 😿")
        return
    item = catatan[global_index - 1]
    print(f"🔧✏️ Yuk edit catatan: {item['mapel']} - {item['topik']} ({item['durasi']} menit) 💖✨")

    new_topik = input("Masukkan topik baru (kosong = tetap) — biarkan kosong kalau mau tetap: ").strip()
    if new_topik:
        item['topik'] = new_topik

    while True:
        new_dur = input("Masukkan durasi baru (menit, kosong = tetap): ").strip()
        if not new_dur:
            break
        if new_dur.isdigit() and int(new_dur) > 0:
            item['durasi'] = int(new_dur)
            break
        else:
            print("Masukkan angka positif ya (mis: 45) atau kosong untuk tetap 😊✨")

    print("🎉 Berhasil! Perubahan tersimpan 💾✨💕")
    ringkasan_mapel(item['mapel'])


def lihat_per_mapel():
    """Tampilkan daftar mapel, ringkasan per mapel, dan memungkinkan melihat/detail/edit per mapel."""
    if not catatan:
        print("Belum ada catatan belajar nih 😴🌷. Yuk mulai, aku dukung kamu! 💌✨")
        return

    while True:
        mapels = daftar_mapel()
        print("\n🌟🌸 --- Daftar Mapel Aesthetic --- 🌸✨")
        for i, m in enumerate(mapels, start=1):
            notes = [c for c in catatan if c['mapel'] == m]
            total = sum(c['durasi'] for c in notes)
            print(f"{i}. {m} - {len(notes)} catatan, {total} menit ⏰🌈💫")
        print("b. Kembali 🔙✨")

        pilihan = input("Pilih mapel (nomor) untuk lihat detail / ketik 'b' untuk balik: ").strip()
        if pilihan.lower() == 'b':
            return
        if not (pilihan.isdigit() and 1 <= int(pilihan) <= len(mapels)):
            print("Ups, pilihan nggak valid, coba lagi yaa 😊")
            continue

        sel_mapel = mapels[int(pilihan) - 1]

        # Tampilkan catatan untuk mapel yang dipilih
        filtered = [(i, c) for i, c in enumerate(catatan, start=1) if c['mapel'] == sel_mapel]
        if not filtered:
            print(f"Hmmm, belum ada catatan untuk mapel {sel_mapel}. Yuk tambahkan satu! 🌱🌷")
            continue

        # Lebar kolom dinamis
        no_w = max(len(str(len(filtered))), len("No"))
        mapel_w = max(len("Mapel"), max(len(c['mapel']) for _, c in filtered))
        topik_w = max(len("Topik"), max(len(c['topik']) for _, c in filtered))
        durasi_w = max(len("Durasi"), max(len(f"{c['durasi']} menit") for _, c in filtered))

        header = f"{'No':>{no_w}}  {'Mapel':<{mapel_w}}  {'Topik':<{topik_w}}  {'Durasi':>{durasi_w}}"
        separator = '-' * len(header)

        print(f"\n🌸✨ — Catatan untuk {sel_mapel} — 🌸💫")
        print(header)
        print(separator)
        for local_idx, (global_idx, c) in enumerate(filtered, start=1):
            dur_str = f"{c['durasi']} menit"
            print(f"{local_idx:>{no_w}}.  {c['mapel']:<{mapel_w}}  {c['topik']:<{topik_w}}  {dur_str:>{durasi_w}} 💖✨")
        print(separator)

        # Opsi dalam view mapel
        print("1. 🌱✨ Tambah catatan pada mapel ini 💖")
        print("2. ✏️🌈 Edit catatan pada mapel ini")
        print("3. 🔙 Kembali ke daftar mapel")
        aksi = input("Pilih aksi (1/2/3): ").strip()
        if aksi == '1':
            tambah_catatan(sel_mapel)
        elif aksi == '2':
            pilih_edit = input("Pilih nomor catatan untuk di-edit: ").strip()
            if not (pilih_edit.isdigit() and 1 <= int(pilih_edit) <= len(filtered)):
                print("Ups, pilihan nggak valid, coba lagi yaa 😊")
            else:
                # ambil global index dari filtered list
                global_idx = filtered[int(pilih_edit) - 1][0]
                edit_catatan(global_idx)
        elif aksi == '3':
            continue
        else:
            print("Ups, aksinya nggak valid, coba lagi yaa 😅")


def menu():
    print("\n✨🌸🌈📚 Study Log App - Catatan Belajar Aesthetic ✨🌟")
    print("1. 🌱✨💕 Tambah catatan belajar (tumbuh sedikit tiap hari!)")
    print("2. 📝🌼 Lihat semua catatan (cek usaha kerennya)")
    print("3. 📚🎯 Lihat per mapel (filter & ringkasan)")
    print("4. ✏️💖 Edit catatan (ubah kalau perlu)")
    print("5. ⏱️🌟 Total waktu belajar (lihat progress)")
    print("6. 💖🌙 Keluar (sampai jumpa, semangat terus!)")


while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        lihat_per_mapel()
    elif pilihan == "4":
        # Edit global
        if not catatan:
            print("Belum ada catatan yang bisa diedit nih 😿. Tambahkan dulu ya! 💕✨")
        else:
            print("\n--- Pilih catatan untuk diedit ---")
            lihat_catatan()
            pilih = input("Masukkan nomor catatan yang ingin diedit (atau 'b' untuk kembali): ").strip()
            if pilih.lower() == 'b':
                continue
            if pilih.isdigit() and 1 <= int(pilih) <= len(catatan):
                edit_catatan(int(pilih))
            else:
                print("Pilihan tidak valid. Kembali ke menu utama ❤️")
    elif pilihan == "5":
        total_waktu()
    elif pilihan == "6":
        print("Terima kasih, terus semangat belajar! 🌟💖🎀✨")
        break
    else:
        print("Pilihan tidak valid. Coba lagi ya~ 😺✨")
