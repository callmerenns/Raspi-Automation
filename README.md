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

   ip-raspi dapat berupa IP lokal atau IP dari Tailscale.

---

## Cara Menjalankan Program

1. Test koneksi ke semua Raspberry Pi menggunakan Ansible.

   ```bash
   ansible all -i inventory/hosts.ini -m ping

   Jika berhasil, setiap Raspberry Pi akan membalas dengan status pong.

2. Jalankan program automation berdasarkan playbook yang tersedia.

   ```bash
   ansible-playbook -i inventory/hosts.ini playbooks/nama_playbook.yml

## Struktur Folder & Keterangan
    ###ansible.cfg
    File konfigurasi utama Ansible.

    ###tasks/
    Berisi task-task Ansible untuk mengeksekusi perintah ke Raspberry Pi.

    ###library/
    Berisi custom Ansible library/module untuk automation, seperti memodifikasi file
    settings.yaml di Raspberry Pi.

    ###roles/collect_dataset/
    Role Ansible yang berisi:

    -tasks/

    -library/

    ###playbooks/
    Berisi playbook untuk mengelompokkan dan menjalankan program automation.

    ###group_vars/
    Berisi konfigurasi global, seperti:

    -path folder di Raspberry Pi

    -format zip

    -nama folder

    -konfigurasi lainnya

    ###inventory/
    Berisi file hosts.ini untuk konfigurasi:

    -hostname Raspberry Pi

    -alamat IP

    -jenis Raspberry Pi

    -pengaturan SSH dan parameter lainnya
