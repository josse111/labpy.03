# labpy.03
#### Nama   = Zaki FAuzan Akhbari
#### Kelas  = TI.24.A4  
#### NIM    = 312410348  
#### Matkul = BAHASA PEMOGRAMAN

# LATIHAN 1:latihan1.py
# Program Angka Acak dengan Nilai Kurang dari 0.5

## Deskripsi
Program ini menghasilkan sejumlah `N` angka acak yang nilainya selalu kurang dari 0.5. Setiap angka acak ditampilkan secara berurutan dengan nomor urutannya. Program ini menggunakan kombinasi perulangan `for` dan `while` untuk memastikan bahwa setiap angka yang dihasilkan memenuhi kriteria yang ditentukan.

## Fitur Program
1. **Input Dinamis**: Pengguna dapat memasukkan nilai `N` (jumlah angka acak yang ingin dihasilkan) saat runtime.
2. **Pengulangan dan Seleksi**:
   - Menggunakan perulangan `for` untuk menghasilkan angka acak sebanyak `N` kali.
   - Menggunakan `while` untuk memastikan setiap angka yang dihasilkan selalu kurang dari 0.5.
3. **Fungsi Random**: Menggunakan fungsi `random()` dari modul `random` di Python untuk menghasilkan angka acak.

## Cara Menggunakan Program
1. Pastikan Python telah terinstal di komputer Anda.
2. Simpan program ini sebagai `latihan1.py`.
3. Buka terminal atau command prompt di lokasi penyimpanan file tersebut.
4. Jalankan perintah berikut:
   ```bash
   python3 latihan1.py
5. Masukkan nilai `N` sesuai jumlah angka acak yang ingin dihasilkan.

## Penjelasan Kode

### 1. Import Library Random
```python
from random import random
```
Kode ini mengimpor fungsi random() dari library random bawaan Python. Fungsi random() menghasilkan angka acak dalam rentang 0 hingga 1.

### 2. Input Nilai N
```python
n = int(input("Masukkan nilai N: "))
```
Program meminta pengguna memasukkan nilai integer N, yang menunjukkan berapa kali loop akan dijalankan. Nilai ini menentukan jumlah angka acak yang ingin dihasilkan.

### 3. Looping dan Generasi Angka Acak
```python
for i in range(1, n + 1):
```
Loop for ini berjalan dari 1 hingga N (inklusif). Pada setiap iterasi, variabel i akan menyimpan indeks iterasi saat ini.

### 4. Membuat Angka Acak
```python
angka_acak = random()
```
Pada setiap iterasi, sebuah angka acak dihasilkan menggunakan fungsi random() dan disimpan dalam variabel angka_acak.

### 5. Kondisi Pemilihan
```python
Salin kode
if angka_acak < 0.5:
    print(f"data ke: {i} => {angka_acak}")
else:
    while angka_acak >= 0.5:
        angka_acak = random()
   print(f"data ke: {i} => {angka_acak}")
```
Jika angka_acak kurang dari `0.5`, maka angka langsung dicetak dengan `format data ke: {i} => {angka_acak}`.
Jika angka_acak lebih besar atau sama dengan `0.5`, program akan masuk ke dalam loop while untuk terus menghasilkan angka acak baru hingga mendapatkan angka yang kurang dari `0.5`, lalu mencetak angka tersebut.

### 6. Akhir Program
```python
print("Selesai")
```
Setelah semua angka yang diinginkan berhasil dihasilkan dan ditampilkan, program mencetak "Selesai" sebagai tanda bahwa proses telah berakhir.

## Contoh Output
Jika pengguna memasukkan nilai `N = 5`, maka output yang dihasilkan mungkin terlihat seperti ini:

```python
Masukkan nilai N: 5
data ke: 1 => 0.3729648189127943
data ke: 2 => 0.12069084128885188
data ke: 3 => 0.12486530658774031
data ke: 4 => 0.4755389441515395
data ke: 5 => 0.4919317309126129
Selesai
```

## Berikut adalah hasin screenshot vsc

![Screenshot 2024-10-29 104430](https://github.com/user-attachments/assets/5ec24955-d8d6-4ac8-8984-1e8348906105)

## Penjelasan Kode
Import Modul Random: from random import random untuk mengimpor fungsi random() yang akan digunakan untuk menghasilkan angka acak.
Input Pengguna: `n = int(input("Masukkan nilai N: "))` meminta pengguna memasukkan jumlah angka yang akan dihasilkan.
Loop for: Menghasilkan angka acak sebanyak N kali.
Loop while: Memastikan setiap angka yang dihasilkan `kurang dari 0.5. Jika angka lebih besar atau sama dengan 0.5`, angka akan diacak kembali.
Output: Setiap angka acak ditampilkan dengan `format data ke: {nomor} => {angka}`.

# LATIHAN 2.latihan2.py
# Menghitung Laba Usaha selama 8 Bulan

## Deskripsi 

Program ini melakukan perhitungan laba bulanan dengan aturan sebagai berikut:
1. **Bulan 1 dan 2**: Belum mendapatkan laba (0%).
2. **Bulan 3 dan 4**: Mendapatkan laba sebesar 1% dari modal awal.
3. **Bulan 5, 6, dan 7**: Mendapatkan laba sebesar 5% dari modal awal.
4. **Bulan 8**: Mengalami penurunan laba menjadi 3% dari modal awal.

Program akan menghitung laba untuk setiap bulan dan menampilkan hasilnya. Setelah 8 bulan, program juga menampilkan total laba yang diakumulasi selama periode tersebut.
## Cara Menjalankan Program

1. Pastikan Python sudah terinstal di komputer Anda.
2. Simpan program ini sebagai latihan2.py.
3. Buka terminal atau command prompt di lokasi penyimpanan file tersebut.
4. Jalankan perintah berikut:
```bash
python3 latihan2.py
```

## Penjelasan Kode
### 1. Modal Awal dan Variabel Laba
```python
modal_awal = 100_000_000
total_laba = 0
```
   - `modal_awal: menyimpan modal awal pengusaha, yaitu 100 juta rupiah.`
   - `total_laba: akumulasi total laba dari bulan 1 hingga 8, dimulai dari 0.`

### 2. Lingkaran Perhitungan Laba per Bulan
```python
for bulan in range(1, 9):
    if bulan in [1, 2]:        # Bulan 1 dan 2 belum mendapatkan laba
        laba = 0
    elif bulan == 3:           # Bulan 3 mendapatkan laba 1%
        laba = 0.01 * modal_awal
    elif bulan == 4:           # Bulan 4 mendapatkan laba 1%
        laba = 0.01 * modal_awal
    elif bulan == 5:           # Bulan 5 mendapatkan laba 5%
        laba = 0.05 * modal_awal
    elif bulan in [6, 7]:      # Bulan 6 dan 7 mendapatkan laba 5%
        laba = 0.05 * modal_awal
    elif bulan == 8:           # Bulan 8 mendapatkan laba 3%
        laba = 0.03 * modal_awal
```
Program menggunakan loop fordari bulan 1 hingga 8. Di setiap iterasi, program menentukan besarnya laba berdasarkan kondisi:
   - Bulan 1 dan 2 : laba 0%.
   - Bulan 3 dan 4 : laba 1% dari modal awal.
   - Bulan 5, 6, dan 7 : laba 5% dari modal awal.
   - Bulan 8 : laba 3% dari modal awal.

### 3. Menambahkan Laba ke Total Laba dan Menampilkan Laba per Bulan

```python
total_laba += laba
print(f"laba bulan ke- {bulan} sebesar: {laba}")
```
Setiap laba bulanan yang dihitung akan ditambahkan ke total_laba. Selain itu, program menampilkan laba yang diperoleh pada bulan tersebut.

### 4. Akhir Program: Menampilkan Total Laba

```python
print(f"Total laba adalah: {total_laba}")
```
Setelah loop selesai, program menampilkan total laba yang diperoleh selama 8 bulan.

## Contoh Output
Jika Anda menjalankan program ini, outputnya mungkin akan terlihat seperti berikut:

```python
laba bulan ke- 1 sebesar: 0
laba bulan ke- 2 sebesar: 0
laba bulan ke- 3 sebesar: 1000000.0
laba bulan ke- 4 sebesar: 1000000.0
laba bulan ke- 5 sebesar: 5000000.0
laba bulan ke- 6 sebesar: 5000000.0
laba bulan ke- 7 sebesar: 5000000.0
laba bulan ke- 8 sebesar: 3000000.0
Total laba adalah: 19000000.0
```
## Berikut adalah hasin screenshot vsc

![Screenshot 2024-10-29 122748](https://github.com/user-attachments/assets/09c598d6-d230-4b32-96c8-bb08dd0a744b)

# LATIHAN 3.latihan3.py
# Simulasi Mesin ATM Sederhana

## Deskripsi
Program ini adalah simulasi mesin ATM sederhana yang memungkinkan pengguna untuk melakukan penarikan uang dengan saldo awal sebesar Rp 1.000.000. Pengguna dapat memilih untuk menarik uang atau keluar dari sistem.

## Fitur Program
1. **Menampilkan Saldo** - Program akan selalu menampilkan saldo saat ini.
2. **Penarikan Uang** - Pengguna dapat melakukan penarikan uang dengan nominal tertentu.
3. **Validasi Saldo** - Program akan mengecek apakah saldo mencukupi sebelum memproses penarikan.
4. **Keluar dari Program** - Pengguna dapat memilih untuk keluar dari program.

## Cara Menggunakan Program

 1. **Menjalankan Program**: 
   - Pastikan Anda memiliki Python 3 terinstal di komputer Anda.
   - Simpan file kode ini sebagai `latihan3.py`.
   - Buka terminal atau command prompt, navigasikan ke folder tempat file `latihan3.py` disimpan, dan jalankan perintah berikut:
     ```bash
     python3 latihan3.py
     ```

2. **Interaksi dengan Program**:
   - **Menu Tarik Uang**: Masukkan "1" dan kemudian masukkan jumlah penarikan. Program akan memvalidasi saldo dan mengurangi saldo sesuai dengan jumlah penarikan.
   - **Menu Keluar**: Masukkan "2" untuk keluar dari program. Program akan menampilkan pesan perpisahan sebelum keluar.

## Penjelasan Kode

### 1. Inisialisasi Saldo
```python
saldo = 1000000
```
Saldo awal pengguna diatur sebesar Rp 1.000.000.

### 2. Fungsi tampilkan_menu
```python
def tampilkan_menu():
    print("\nSaldo saat ini: Rp", saldo)
    print("1. Tarik Uang")
    print("2. Keluar")
```
Fungsi ini menampilkan saldo pengguna dan dua opsi: Tarik Uang dan Keluar.

### 3. Loop Utama
Program menggunakan loop while yang berjalan terus-menerus hingga pengguna memilih untuk keluar.

- Pilihan 1 (Tarik Uang):
   Program meminta jumlah uang yang ingin ditarik.
   Jika jumlah yang diminta lebih besar dari saldo, program menampilkan pesan bahwa saldo tidak mencukupi.
   Jika saldo mencukupi, saldo dikurangi sesuai jumlah penarikan dan ditampilkan pesan "Penarikan berhasil!".
- Pilihan 2 (Keluar):
   Program akan menampilkan pesan terima kasih dan menghentikan loop, sehingga program berakhir.

- Input Tidak Valid:
   Jika pengguna memasukkan pilihan selain "1" atau "2", program akan menampilkan pesan error dan meminta pengguna untuk memasukkan pilihan yang valid.

## Contoh Output
Berikut adalah contoh tampilan saat program berjalan:
```python
Saldo saat ini: Rp 1000000
1. Tarik Uang
2. Keluar
Pilih menu (1/2): 1
Masukkan jumlah penarikan: 500000
Penarikan berhasil!

Saldo saat ini: Rp 500000
1. Tarik Uang
2. Keluar
Pilih menu (1/2): 2
Terima kasih telah menggunakan ATM!
```
- Pada contoh ini:
   Pengguna memilih opsi "Tarik Uang" dan memasukkan jumlah penarikan Rp 500.000. Program berhasil melakukan penarikan dan mengurangi saldo.
   Pengguna kemudian memilih opsi "Keluar" untuk mengakhiri program.

## Berikut adalah hasin screenshot vsc

![image](https://github.com/user-attachments/assets/6ae16950-df3c-45e4-8c2f-7eb9d71b9f00)



