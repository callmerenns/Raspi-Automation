# Raspberry Pi Automation dengan Ansible

Repository ini berisi program **automation Raspberry Pi 5** menggunakan **Ansible**.  
Automation dijalankan dari komputer lokal untuk mengelola dan mengeksekusi perintah ke beberapa Raspberry Pi melalui koneksi **SSH**.

---

## Prasyarat

Pastikan komputer lokal Anda sudah memenuhi persyaratan berikut:

- Python 3
- Ansible
- Sistem operasi Linux (Ubuntu/Debian direkomendasikan)
- Akses SSH ke Raspberry Pi (Local Network atau Tailscale)

---

## Cara Download & Instalasi

1. Pastikan **Ansible** dan **Python 3** sudah terinstall di komputer lokal.

2. Tentukan atau buat folder kerja untuk menjalankan program automation.

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


