# Tugas Pertemuan 1 - Algoritma dan Pemrograman

**Nama:** [Ahmad Ismut Thoriequddin] 
**NIM:** [2225250011]  
**Kelas:** [3A]  
**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** Pendidikan Matematika  

---

## 1. Deskripsi Masalah
Lingkaran merupakan salah satu bangun datar dasar dalam matematika. Untuk menghitung luas dan kelilingnya, diperlukan nilai jari-jari (r) serta konstanta pi. Program ini dibuat menggunakan bahasa Python untuk membantu menghitung luas dan keliling lingkaran secara otomatis, tepat, dan cepat berdasarkan input jari-jari yang dimasukkan pengguna.

---

## 2. Identifikasi Input - Proses - Output

* **INPUT:** 
  * Jari-jari lingkaran (`r`)
* **PROSES:** 
  * Luas = pi * r^2
  * Keliling = 2 * pi * r
* **OUTPUT:** 
  * Nilai Luas Lingkaran
  * Nilai Keliling Lingkaran

---

## 3. Pseudocode

```text
DECLARE
    r, luas, keliling : FLOAT
    PI : CONSTANT FLOAT = 3.14159

IMPLEMENTATION
    INPUT r
    
    luas = PI * r * r
    keliling = 2 * PI * r
    
    OUTPUT "Jari-jari: ", r
    OUTPUT "Luas Lingkaran: ", luas
    OUTPUT "Keliling Lingkaran: ", keliling
END

