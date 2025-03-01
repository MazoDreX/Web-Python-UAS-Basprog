# Web-Python-UAS-Basprog

## Memulai

Sebelum mencoba aplikasi ini,ada beberapa langkah untuk menginstall depedencies yang diperlukan seperti packages dari python dan npm untuk asset static yang saya gunakan yaitu tailwindcss 

### Prasyarat
Pastikan komputer anda terinstall python@3 dan npm untuk package tailwindcss.

### Instalasi

1. Clone repo
   ```sh
   git clone https://github.com/MazoDreX/Web-Python-UAS-Basprog.git
   ```

2. Buat virtual environment dengan python
    ```py
    python -m venv venv
    ```
    Ini akan membuat folder untuk virtual environment yang akan diinstall dengan package python

3. Install package python dengan pip
    ```py
    pip install -r requirements.txt
    ```
    ini akan menginstall semua packages yang dibutuhkan di requirements.txt

4. Install tailwindcss
   ```sh
   npm install
   ```

5. Pada folder app, buat folder `static/dist/css` untuk menampung build tailwindcss

6. Buat file `.env` dari `.env.example` untuk menaruh informasi sensitif dari database
    

### Memulai Aplikasi
1.  Nyalakan virtual environment anda
    ```sh
    # In cmd.exe
    venv\Scripts\activate.bat
    # In PowerShell
    venv\Scripts\Activate.ps1
    ```

2. Jalankan run.py
    ```py
    python run.py
    ```

3. Build tailwindcss (GUNAKAN TERMINAL BERBEDA)
    ```sh
    npm run build:css
    ```

### CATATAN UNTUK TAILWINDCSS
Jika anda ingin mengubah class tailwind atau melihat perubahan tailwind secara live anda harus menjalankan <b>npm run build:css</b> di terminal berbeda