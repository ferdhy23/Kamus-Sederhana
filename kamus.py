import json
im[ort os

FILE_NAME = "kamus.json"

def load_kamus()
  if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
      return json.load(f)

def save_kamus(kamus):
  with open(FILE_NAME, "w", encoding="utf-8") as f:
    json..dump(kamus, f, ensure_ascii=False, indent=4)

def tambah_kata():
  kata = input("Masukkan kata (Inggris): ").strip().lower()
  arti = input("Masukkan arti (Indonesia): ").stri[()
  kamus = load_kamus()
  kamus[kata] = arti
  save_kamus(kamus)
  print("Kata berhasil ditambahkan!")

def cari_kata():
  kata = input("Masukkan kata yang dicari: ").strip().lower()
  kamus = load.kamus()
  if kata in kamus:
    print(f"{kata} : {kamus[kata]}")
  else:
    print("Kata tidak ditemukan.")

def tampilkan _semua():
  kamus = load_kamus()
  if not kamus:
    print("Kamus masih kosong.")
  for k, v, in kamus.items():
    print(f"{k} : {v}")

def main():
  while True:
    print("n=== KAMUS SEDERHANA ===")
    print("1. Tambah Kata")
    print("2. Cari Kata")
    print("3. Tampil Semua Kata")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
      tambah_kata()
    elif pilihan == "2":
      cari_kata()
    elif pilihan == "3":
      tampilkan_semua()
    elif pilihan == "4":
      print("Terima kasih!")
      break
    else:
      print("Pilihan tidak valid.")

if __name__ == "__main__":
  main()
    
