#QUERY Untuk membuat tabel jika tidak ada
make_table_mahasiswa = """CREATE TABLE IF NOT EXISTS mahasiswa(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255),
    nim VARCHAR(255),
    fakultas VARCHAR(255),
    prodi VARCHAR(255),
    semester INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

make_table_matakuliah_TI = """CREATE TABLE IF NOT EXISTS matakuliah_TI(
    id INT AUTO_INCREMENT PRIMARY KEY,
    semester INT,
    nama_mata_kuliah VARCHAR(255),
    sifat CHAR(1) DEFAULT 'W'
)
"""

make_table_mahasiswa_matakuliah = """CREATE TABLE IF NOT EXISTS mahasiswa_matakuliah(
    id INT AUTO_INCREMENT PRIMARY KEY,
    mahasiswa_id INT,
    matakuliah_id INT,
    FOREIGN KEY (mahasiswa_id) REFERENCES mahasiswa(id),
    FOREIGN KEY (matakuliah_id) REFERENCES matakuliah_TI(id)
)
"""

#QUERY untuk memasukan data
insert_query_mahasiswa = "INSERT INTO mahasiswa (nama, nim, fakultas, prodi, semester) VALUES (%s, %s, %s, %s, %s)"
insert_query_mahasiswa_matakuliah = "INSERT INTO mahasiswa_matakuliah (mahasiswa_id, matakuliah_id) VALUES (%s, %s)"

insert_query_matakuliah = "INSERT INTO matakuliah_ti (semester, nama_mata_kuliah, sifat) VALUES (%s, %s, %s)"


#QUERY untuk memilih data atau mengambil data dari database
query_select_matakuliah_TI_Wajib = "SELECT nama_mata_kuliah FROM matakuliah_ti WHERE semester = %s AND sifat = 'W'"
query_select_matakuliah_TI_Pilihan = "SELECT nama_mata_kuliah FROM matakuliah_ti WHERE semester = %s AND sifat = 'P'"
query_select_matakuliah_TI_Pilihan_id = "SELECT id, nama_mata_kuliah FROM matakuliah_ti WHERE id IN %s"

query_select_id_matakuliah_TI_Wajib = "SELECT id FROM matakuliah_ti WHERE semester = %s AND sifat = 'W'"
query_select_id_matakuliah_TI_Pilihan = "SELECT id FROM matakuliah_ti WHERE semester = %s AND sifat = 'P'"