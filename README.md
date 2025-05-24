# Proyek Akhir : Aplikasi Prediksi Dropout Siswa
## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

## Permasalahan Business
- Tingginya angka dropout siswa pada institusi Jaya jaya

## Persiapan
Sumber Data:
Dataset dapat ada unduh pada  [tautan berikut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)
Setup Environment
1. Buka Anaconda Prompt atau terminal
2. Jalankan perintah di bawah ini
    ```
    conda create --name student_pred python=3.10
    ```
3. aktifkan environment yang telah dibuat sebelumnya dengan menjalankan perintah di bawah ini
    ```
    conda activate student_pred
    ```
4. Install semua library yang dibutuhkan dengan menjalankan perintah di bawah ini
    ```
    pip install -r requirements.txt
    ```

## Businnes Dashboard
Analisis HR Dashboard merupakan dashboard yang dibuat dengan tujuan agar memberikan insight ke HR perusahaan Edutech Jaya Jaya Maju dengan berupa visualisasi data yang dapat membantu dalam memantau tingkat attrition dari perusahaan dan mengetahui faktor-faktor apa saja yang dapat menyebabkan tingginya attrition di perusahaan.
Fitur utama dalam dashboard ini :
- Key Performance Index (KPI) : KPI ini menyoroti dari mulai jumlah total keseluruhan siswa yang ada di institusi, lalu total siswa yang dropout dengan siswa yang lulus dan ada percentage dropout siswa pada institusi jaya jaya ini.
- Gender : Perbandingan total mahasiswa laki-laki dengan mahasiswi perempuan dengan menggunakana visualisasi donut chart
- Nacionality : Berisikan sumber informasi mengenai mahasiswa berasal dari negara  mana saja
- Marital Status : Berisikan informasi mengenai status para mahasiswa di institusi jaya jaya
- Application mode : visualisasi yang memberikan informasi mahasiswa ini mendaftar ke institusi melalui jalur apa saja
- Course : visualisasi course yang dipilih oleh mahasiswa saat diinstitusi
- Scholarship holder : visualisasi perbandingan yang menerima beasiswa atau tidak pada saat bersekolah di jaya jaya
- Educational Special Needs : Visualisasi perbandingan antara mahasiswa berkebutuhan khusus dengan yang tidak
- Fees UptoDate : Visualisasi perbandingan antara mahasiswa melakukan pembayaran yang tepat waktu dengan yang terlambat
- Debtor : Visualisai perbandingan antara mahasiswa yang mengandalkan pembayaran dengan cash ataupun hasil pinjaman
- Displaced : Visualisasi perbandingan antara mahasiswa yang seorang pengungsi dengan yang tidak
- International : Visualisasi perbandingan antara mahasiswa yang mengambil kelas international denga yang tidak.

Tools yang digunakan :
```
Tableau
```
Dashboard dapat diakses [di sini](https://public.tableau.com/views/JayaJayaMaju_17460798610090/JayaJayaMaju?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Menjalankan Aplikasi
1. Pastikan sudah buat environment sebelumnya dan install semua kebutuhan library dengan mengikuti langkah langkah pada bagian setup environment sebelumnya
2. Clone repository  ini ke penyimpanan kalian dengan menjalankan perintah di bawah ini
    ```
    [git clone https://github.com/DeniPriyadi18/JayaJayaInstitut.git]
    ```
3. Masuk ke directory project dengan menjalankan perintah di bawah ini
    ```
    cd JayaJayaInstitut
    ```
4. Jalankan perintah berikut pada terminal 
     ```
    run streamlit app.py
    ```

## Alternatif akses aplikasi
Kalian dapat mengakses aplikasi dengan mengklik [di sini]()


## Conclusion
Berdasarkan hasil yang didapatkan dari dashboard dapat ditarik kesimpulan sebagai berikut :
1. Total siswa berjumlah 4.424 dengan mahasiswa yang telah dropout pada institusi ini adalah 42,54% dari jumlah keseluruhan. Angka yang besar untuk jumlah dropout dengan rata-rata usia di sekitar 23 tahunan
2. Mahasiswa yang masuk ke dalam kategori seorang mahasiswa terlantar dalam artian tidak memiliki tempat tinggal atau merupakan seorang pengungsi, lalu tidak menerima beasiswa, pembayarannya terlambat serta dari jurusan Management. Mahasiswa tersebut dapat langsung diberikan bimbingan konseling untuk menghindari mahasiswa yang masuk dalam kategori tersebut dropout.

## Rekomendasi Action Items
Berikut beberapa rekomendasi yang dapat dilakukan untuk mengatasi tingkat attrition yang tinggi :
1. Perbanyak lagi beasiswa yang dapat diberikan kepada mahasiswa agar mahasiswa dapat menyelesaikan pembelajaran hingga lulus di institusi ini
2. Buat sebuah hunian tempat tinggal untuk seorang mahasiswa yang tidak memiliki tempat tinggal agar mahasiswa tidak perlu  pusing pindah-pindah tempat atau memikirkan biaya sewa tempat tinggal, agar mahasiswa itu fokus belajar.
