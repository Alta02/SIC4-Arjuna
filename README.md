# SIC4-Arjuna

![Made with Raspberry Pi](https://img.shields.io/badge/-Raspberry%20Pi-C51A4A?logo=Raspberry%20Pi&logoColor=white&labelColor=C51A4A)
![IoT Platform - Ubidots](https://img.shields.io/badge/IoT%20Platform-Ubidots-00ACD7.svg)

## Overview

Proyek ini bertujuan untuk mengembangkan sistem penimbangan berat keripik tempe menggunakan Raspberry Pi 4 dan sensor berat HX711. Sistem ini akan memungkinkan pengguna untuk mengukur berat keripik tempe dengan akurasi tinggi dan mengirim data berat ke platform IoT Ubidots untuk pemantauan dan analisis.

## Flowchart

![Flowchart](link_ke_flowchart)

## List Hardware

- Raspberry Pi 4
- Kabel Jumper 
- (Opsional) LCD Display

## List Sensor Mandatory

- Sensor berat HX711

## List Technology Mandatory

- Ubidots

## Instalasi dan Penggunaan

Berikut adalah langkah-langkah untuk menginstal dan menggunakan proyek ini:

1. Pastikan Raspberry Pi 4 Anda telah terpasang dengan sistem operasi yang sesuai.
2. Hubungkan sensor berat HX711 dengan Raspberry Pi menggunakan kabel penghubung yang sesuai.
3. (Opsional) Hubungkan LCD display dengan Raspberry Pi jika ingin menampilkan informasi berat secara visual.
4. Instal library HX711 pada Raspberry Pi untuk membaca data dari sensor berat.
5. Buat akun Ubidots dan dapatkan API key untuk mengirim data berat ke platform IoT.
6. Salin kode proyek ini ke Raspberry Pi Anda.
7. Atur konfigurasi seperti API key Ubidots pada kode proyek.
8. Jalankan program dan sistem akan mulai mengukur dan mengirim data berat keripik tempe ke Ubidots.
