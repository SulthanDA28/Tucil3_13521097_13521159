# Tucil3_13521097_13521159
## Pencarian Rute Terdekat pada Map dengan Menggunakan ALgoritma A* dan UCS

<br>

## Author
1. Shidqi Indy Izhari 13521097
2. Sulthan Dzaky Alfaro

<br>

## Penjelasan Singkat Algoritma UCS dan A*
<br>
Dalam kehidupan sehari-hari, kita tidak mungkin tidak menggunakan sebauh peta. Peta digunakan untuk mengetahui tempat dimana kita berada pada bumi ini dan digunakan untuk menemukan jalur ke tempat yang lain. Tentunya ada banyak jalur yang bisa kita lalui untuk mencapai tujuan kita. Dalam tugas kecil ini, kami menggunakan algoritma UCS dan A* untuk mencari rute terbaik ke tujuan yang kita tentukan. Berikut penjelasan algoritma UCS dan A*
<br>
<br>
Algoritma Uniform Cost Search (UCS) adalah salah satu metode pencarian jalur terpendek dalam graf berbobot yang menghitung biaya dari suatu rute dengan menjumlahkan bobot dari setiap edge yang dilewati. Algoritma ini bekerja dengan cara memperluas node yang memiliki biaya path terendah terlebih dahulu dan membandingkan biaya path dari setiap node yang dicapai dengan biaya path dari node sebelumnya. UCS akan terus memperluas node yang memiliki biaya path terendah hingga menemukan solusi terpendek. Dasar dari UCS adalah struktur data priority queue.
<br>
<br>
Algoritma A* merupakan algoritma pencarian untuk menemukan rute paling optimal dan terpendek. Algoritma ini biasa digunakan dalam pencarian rute pada peta untuk mencari rute terpendek.  Algoritma A* mencari jalur yang lebih pendek terlebih dahulu, sehingga menjadikannya algoritma yang optimal dan lengkap. Algoritma ini menggunakan graph berbobot dalam pengolahan datanya. Ini berarti, algoritma ini mengambil jalur yang paling minimum dari segi jarak maupun waktu. Kelemahan algoritma ini adalah kompleksitas waktu yang cukup tinggi, dengan kompleksitas waktu O(b^d) dengan b adalah faktor percabangan dan d adalah jumlah node pada jalur yang dihasilkan. Cara kerja algoritma ini, yaitu hampir sama dengan UCS, algoritma akan mencari jarak yang paling minimum antar node yang akan dikunjungi, perbedaannya A* mempertimbangkan jarak heuristik yaitu jarak “euclidean” (disini kami menggunakan metode haversine) antara node dengan node tujuan.
<br>
<br>

## Requirement Spesifikasi
Adapun spesifikasi yang diperlukan untuk menjalankan program ini yaitu:
1. Pastikan sudah menginstall python
2. Pastikan sudah menginstall library python, antara lain, networkx,matplotlib, dan tkinter. Apabila belum menginstall, dapat diinstall dengan menuliskan command berikut pada cmd
<br>

```
pip install networkx
pip install tkinter
pip install matplotlib
```

<br> 

## Cara Menjalankan Program
1. Clone repository ini.
2. Lalu buka folder src dan buka file GUI.py di dalam Visual Studio Code
3. Jalankan file GUI.py
4. Lalu pilih file txt yang nanti dijadikan sebagai peta. Urutan penulisan pada file txt yaitu, pada baris pertama terdiri nama nama titik yang akan dipetakan(misal sebanyak n). Lalu pada baris berikutnya sebanyak n baris berisi matriks berbobot yang isinya jarak antar titik sebanyak nxn. Lalu baris selanjutnya sebanyak n berisi koordinat dari setiap titik. Koordinat berurutan sesuai urutan nama titik. Contoh file input sebagai berikut.
<img width="215" alt="Screenshot 2023-04-12 181127" src="https://user-images.githubusercontent.com/110533939/231440519-e45181f3-c7fa-4ceb-9e62-d392d6429cbd.png">

5. Selanjutnya, program akan menampilkan peta yang telah diinputkan beserta pilihan titik titik yang tersedia.
6. Lalu pilih titik awal dan titik tujuan untuk mencari rute dari titik tersebut.
7. Selanjutnya klik tombol algoritma sesuai yang diinginkan. Program akan menampilkan hasil rute pada peta dengan garis berwarna biru serta ada hasil tertulis dan jarak tempuh pada bagian bawah aplikasi. 
