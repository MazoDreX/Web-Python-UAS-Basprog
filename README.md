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

5. Pada folder app, buat folder `static/dist/css` dan `static/src`. Pada `static/src`, buat file input.css lalu masukan kode berikut
    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

6. Install tailwind
    ```sh
    npm run build:css
    ```

3. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```