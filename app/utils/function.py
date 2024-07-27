from app.utils.query import make_table_mahasiswa, make_table_matakuliah_TI, make_table_mahasiswa_matakuliah, insert_query_matakuliah
from app.utils.data import mata_kuliah_TI, mata_kuliah_TI_Pilihan

def make_table(connection):
    cursor = connection.cursor()
    cursor.execute(make_table_mahasiswa)
    cursor.execute(make_table_matakuliah_TI)
    cursor.execute(make_table_mahasiswa_matakuliah)
    print("Tabel Mahasiswa, Matakuliah_TI, Mahasiswa_Matakuliah telah dibuat")

def matkul_TI_insert(connection):
    cursor = connection.cursor()
    check_query = "SELECT 1 FROM matakuliah_TI WHERE semester = %s AND nama_mata_kuliah = %s"

    for semester, mata_kuliah in enumerate(mata_kuliah_TI, start=1):
        for matkul in mata_kuliah:
            cursor.execute(check_query, (semester, matkul))
            result = cursor.fetchone()
            break

    if not result:
        for semester, mata_kuliah in enumerate(mata_kuliah_TI, start=1):
            for matkul_wajib in mata_kuliah:
                cursor.execute(insert_query_matakuliah, (semester, matkul_wajib, 'W'))

        for semester, mata_kuliah in enumerate(mata_kuliah_TI_Pilihan, start=1):
            for matkul_pilihan in mata_kuliah:
                cursor.execute(insert_query_matakuliah, (semester, matkul_pilihan, 'P'))
    
    if result:
        print("Data matakuliah_TI sudah ada")

    connection.commit()
    cursor.close()

def get_name_matakuliah(connection, semester, query):
    cursor = connection.cursor()
    cursor.execute(query, (semester, ))
    result = cursor.fetchall()
    cursor.close()
    return [baris[0] for baris in result]

def get_id(connection, query, params):
    cursor = connection.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result

def insert_data_get_id(connection, query, data):
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    return id

def insert_data(connection, query, data):
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    cursor.close()

def get_nama_matakuliah(connection, id_list, query):
    id_tuple = tuple(id_list)
    cursor = connection.cursor()
    cursor.execute(query, (id_tuple, ))
    result = cursor.fetchall()
    return [baris[1] for baris in result]