# Student-Performance-Predictions

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal memiliki reputasi baik dalam mencetak lulusan yang kompeten. Namun, dalam beberapa tahun terakhir, institusi menghadapi tantangan serius terkait tingginya angka mahasiswa yang tidak menyelesaikan studinya (dropout).


### Permasalahan Bisnis
Tingginya tingkat dropout menimbulkan kekhawatiran terhadap kualitas akademik dan reputasi institusi. Saat ini Jaya jaya institute ingin mendeteksi secepat mungkin siswa yang mungkin melakukan dropout agar dapat di beri bimbingan khusus, selain itu pihak institusi juga meminta untuk membuat dashboard analitik agar bisa di gunakan untuk memantau performa akademik dan risiko dropout mahasiswa secara real-time


### Cakupan Proyek
1. Mengidentifikasi faktor-faktor kunci yang berkontribusi terhadap risiko mahasiswa melakukan dropout dengan menganalisis data historis.
2. Membangun model prediktif untuk mengklasifikasikan kemungkinan seorang mahasiswa akan dropout.
3. Membuat dashboard interaktif yang dapat digunakan oleh pihak akademik dan manajemen untuk memantau performa mahasiswa dan melakukan intervensi dini terhadap mereka yang berisiko tinggi dropout.


### Persiapan

Sumber data: [Dataset Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)


## Setup Environment
1. Ekstrack Folder .zip

Ekstrak file student-performance-analysis.zip, berikut tampilan struktur folder setelah di ekstrack:

```
student_performance_predictions/
│
├── dashboard/
│   ├── prediction.py
│   ├── random_forest_model.joblib
│   └── requirements.txt
│
├── README.md
├── Student_Performance_Predictions.ipynb
├── clean_student_df.csv
├── daffa_suada_i9ug-dashboard.png
├── data.csv
├── link-dashboard.txt
└── requirements.txt                      
```
2. Buat setup environtment dan aktifkan dengan kode berikut :
```
conda create --name student-performance-env python=3.11
conda activate student-performance-env
```
> Note : Karena requirement.txt berada dalam student-performance-analysis maka :
```
cd student-performance-analysis
```
```
pip install -r requirements.txt
```

3. Jalankan notebook
```
Student_Performance_Predictions.ipynb
```

## Business Dashboard
Link : https://lookerstudio.google.com/reporting/7136b014-1612-47cd-b26d-3a2b1db0601a

<img width="566" alt="Screen Shot 2025-05-12 at 19 50 54" src="https://github.com/user-attachments/assets/6db2c72b-e673-4ad4-b9ff-8e4e0efbc787" />


## Menjalankan Sistem Machine Learning
Jalankan prediction di terminal dengan kode berikut:
1. Setelah berada di `student_performance_predictions`, maka harus berpindah ke `dashboard` maka :
```
cd dashboard
```
2. Jalankan dashboard prediction
```
streamlit run prediction.py
```
Note : Setelah menjalankan kode diatas, anda akan diarahkan ke dalam browser yang berjudul `Student Performance Prediction`. Broswer tersebut berisi cara penggunaannya.

Atau anda dapat mengakses langsung dashboard dengan tautan di bawah ini:

[StreamlitApp](https://student-performance-predictions-2apjx3i2qzd6vthpfsz4wb.streamlit.app)

## Conclusion

Dari infromasi yang telah saya paparkan, ada bebearapa kesimpulan yang dapat saya sampaikan. 
1. Dari total 4.424 mahasiswa, perempuan mendominasi dengan 2.868 orang, sedangkan laki-laki sebanyak 1.556. Meskipun jumlah perempuan lebih besar, jumlah dropout antara laki-laki (701) dan perempuan (720) hampir seimbang. Ini menunjukkan bahwa laki-laki memiliki proporsi dropout lebih tinggi (~45%) dibandingkan perempuan (~25%).
2. Mayoritas mahasiswa yang berhasil lulus berada dalam rentang usia 18–22 tahun, yang merupakan usia tipikal masuk kuliah langsung setelah pendidikan menengah. 
3. Siswa yang mendapatkan beasiswa lebih banyak graduate dari pada siswa yang dropout. Namun siswa yang tidak mendapatkan beasiswa mendapatkan hasil yang hampir mirip antara graduate dan dropout.
4. Mahasiswa yang graduate memiliki rata-rata nilai lebih tinggi dibandingkan mahasiswa yang dropout.
5. Dari jumlah course yang ada siswa terbanyak dari yang tertinggi berada pada course nursing, management, social service, veterinaty nursing, dan journalism and comminication. Namun dari data tersebut dapat di ambil kesimpulan bahwa nursing tetap menjadi yang tertinggi untuk keseluruhan siswa yang graduate dengan total 71.6% Social service 69.9%, dan journalism di angka 59.2% 

### Rekomendasi Action Items (Optional)

Berdasarkan kesimpulan di atas, berikut adalah beberapa rekomendasi yang dapat dilakukan oleh institut untuk mengurangi tingkat dropout:
1. Pihak institusi dapat melakukan mentoring terhadap para siswanya, terutama untuk siswa laki-laki dan siswa yang lebih tua karena siswa laki laki mempunyai rasio yang lebih tinggi untuk dropout sedangkan siswa yang lebih tua lebih berkecenderungan dropout.
2. Bagi siswa yang mendapat beasiswa pihak institute dapat memantau nilai mereka, jika bisa pihak institute dapat menambah quota beasiswa untuk siswa yang mempunyai nilai akademis yang baik.
3. Untuk nilai mahasiswa yang rendah. pihak institusi dapat melakukan pendeteksian awal, rekomendasi yang dapat di tawarkan adalah proses untuk remedial atau tutoring kepada siswa.
4. Memberikan dukungan ekstra untuk siswa dari latar belakang kurang mampu atau berpendidikan rendah.
5. Pihak institute harus melakukan pengkajian dan evaluasi terhadap course yang memiliki tingkat dropout yang tinggi.
