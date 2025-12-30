# Raspberry Pi Automation with Ansible

![Ansible](https://img.shields.io/badge/Ansible-Automation-red?logo=ansible)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-5-C51A4A?logo=raspberrypi)

Repository ini berisi program **automation untuk Raspberry Pi 5** menggunakan **Ansible**.  
Automation dijalankan dari **komputer lokal** untuk mengelola dan mengeksekusi perintah ke beberapa Raspberry Pi melalui koneksi **SSH**.

---

## 📋 Prasyarat

Pastikan komputer lokal Anda memenuhi persyaratan berikut:

- **Python 3**
- **Ansible**
- Sistem operasi **Linux** (Ubuntu/Debian direkomendasikan)
- Akses **SSH** ke Raspberry Pi  
  (melalui Local Network atau **Tailscale**)

---

## 🚀 Cara Download & Instalasi

1️⃣ Pastikan **Ansible** dan **Python 3** sudah terinstall di komputer lokal.

2️⃣ Tentukan atau buat folder kerja untuk menjalankan program automation.

3. Clone repository dari GitHub menggunakan **SSH**  
   (pastikan SSH key sudah dibuat dan didaftarkan ke akun GitHub).

   ```bash
   git clone git@github.com:username/nama-repo.git

4. Masuk ke folder repository.

    ```bash
    cd raspi-automation

5. Install library Python dan dependency yang dibutuhkan.

    ```bash
    sudo apt install python3-yaml -y
    sudo apt install python3-ruamel.yaml -y
    sudo pip3 install jsonpointer
    sudo apt install rsync -y

6. Buat koneksi SSH dari komputer lokal ke semua Raspberry Pi
   agar Ansible dapat mengakses Raspberry Pi tanpa password.

   Jalankan perintah berikut untuk setiap Raspberry Pi:

   ```bash
   ssh-copy-id -i ~/.ssh/id_rsa.pub user-raspi@ip-raspi
   ```

   ip-raspi dapat berupa IP lokal atau IP dari Tailscale.

---

## Cara Menjalankan Program

1. Test koneksi ke semua Raspberry Pi menggunakan Ansible.

   ```bash
   ansible all -i inventory/hosts.ini -m ping
   ```

   Jika berhasil, setiap Raspberry Pi akan membalas dengan status pong.

2. Jalankan program automation berdasarkan playbook yang tersedia.

   ```bash
   ansible-playbook -i inventory/hosts.ini playbooks/nama_playbook.yml

## 📁 Struktur Folder 
   
   ```text
   .
   ├── ansible.cfg
   ├── tasks/
   ├── library/
   ├── roles/
   │   └── collect_dataset/
   │       ├── tasks/
   │       └── library/
   ├── playbooks/
   ├── group_vars/
   └── inventory/
   ```

## Keterangan Struktur

   #### ansible.cfg

   - File konfigurasi utama Ansible.

   #### tasks/

   - Berisi task-task Ansible untuk mengeksekusi perintah ke Raspberry Pi.

   #### library/

   - Berisi custom Ansible library/module untuk automation,
     misalnya untuk memodifikasi file settings.yaml di Raspberry Pi.

   #### roles/collect_dataset/

   ***Role Ansible untuk proses pengumpulan dataset, terdiri dari:***

   - tasks/ — task spesifik role

   - library/ — custom module untuk role

   #### playbooks/

   - Berisi playbook Ansible untuk mengelompokkan dan menjalankan automation.

   #### group_vars/

   ***Berisi konfigurasi global, seperti:***

   - Path folder di Raspberry Pi

   - Format zip

   - Nama folder

   - Konfigurasi lainnya

   #### inventory/

   ***Berisi file hosts.ini untuk konfigurasi:***

   - Hostname Raspberry Pi

   - Alamat IP

   - Jenis Raspberry Pi

   - Pengaturan SSH dan parameter lainnya

## 📝 Catatan

   Pastikan setiap Raspberry Pi dapat diakses melalui SSH dan terdaftar dengan benar di file inventory sebelum menjalankan playbook.