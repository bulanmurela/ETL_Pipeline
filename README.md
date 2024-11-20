# End-To-End Data Engineering: Analisis Performa Penjualan Buku Kategori Anak dan Remaja Pada NYTimes Books Berdasarkan Rating Goodreads

Kelompok :
- Tsania Galuh Banggash (22/500322/TK/54832)
- Bulan Aprilia Putri Murela (22/500326/TK/54834)

# Link

Video Presentasi: https://drive.google.com/drive/folders/170rb-OFfdNHrAW2QNo-ES2KXsWirhFLX

Blog Notion: https://safe-swing-bc6.notion.site/End-to-End-Data-Engineering-Analisis-Performa-Penjualan-Buku-Kategori-Anak-dan-Remaja-Pada-NYTimes--143e45f3dc3680a09a83f34fb7ab5135?pvs=4

### Solusi untuk masalah yang mungkin terjadi pada Docker
1. Setelah Airflow berstatus running di running di Docker, masuk ke bash di container dengan command di terminal:
   docker exec -it airflow bash
2. Lakukan instalasi:
   pip install nbconvert
   pip install ipykernel
3. Setelah python terinstal, jalankan perintah:
   python -m ipykernel install --user
4. Restart container
