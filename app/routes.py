from flask import render_template, request, redirect, url_for
from app import app
from app import mysql
from app.utils.data import fakultas, program_studi, Identitas
from app.utils.query import query_select_matakuliah_TI_Wajib, query_select_matakuliah_TI_Pilihan, query_select_id_matakuliah_TI_Wajib, query_select_id_matakuliah_TI_Pilihan, insert_query_mahasiswa, insert_query_mahasiswa_matakuliah, query_select_matakuliah_TI_Pilihan_id
from app.utils.function import get_name_matakuliah, get_id, insert_data_get_id, insert_data, get_nama_matakuliah
import datetime as dt
import locale
import jinja2

@app.context_processor
def utility_processor():
    def zip_lists(a, b):
        return zip(a, b)
    return dict(zip_lists=zip_lists)

@app.route('/')

def home():
    return render_template('index.html', fakultas=fakultas, program_studi=program_studi)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nama = request.form.get('nama')
        nim = request.form.get('nim')
        fakultas_selected = request.form.get('fakultas')
        program_studi_selected = request.form.get('program_studi')
        semester = request.form.get('semester')

    mahasiswa = Identitas()

    mahasiswa.nama = nama
    mahasiswa.nim = nim
    mahasiswa.fakultas = fakultas_selected
    mahasiswa.program_studi = program_studi_selected
    mahasiswa.semester = semester
    
    print(mahasiswa.nama, mahasiswa.nim, mahasiswa.fakultas, mahasiswa.program_studi, mahasiswa.semester)

    if (mahasiswa.program_studi != 'Teknik Informatika'):
        return redirect(url_for('hasil', nama=mahasiswa.nama, nim=mahasiswa.nim, fakultas=mahasiswa.fakultas, program_studi=mahasiswa.program_studi, semester=mahasiswa.semester))
    else:
        return redirect(url_for('daftarmatkul', nama=mahasiswa.nama, nim=mahasiswa.nim, fakultas=mahasiswa.fakultas, program_studi=mahasiswa.program_studi, semester=mahasiswa.semester))


@app.route('/hasil')
def hasil():
    nama = request.args.get('nama')
    nim = request.args.get('nim')
    fakultas = request.args.get('fakultas')
    program_studi = request.args.get('program_studi')
    semester = request.args.get('semester')
    
    
    data_mahasiswa = (nama, nim, fakultas, program_studi, semester)
    mahasiswa_id = insert_data_get_id(mysql.connection, insert_query_mahasiswa, data_mahasiswa)
    print(mahasiswa_id)


    print(nama, nim, fakultas, program_studi, semester)

    locale.setlocale(locale.LC_ALL, 'id-ID')

    date = dt.datetime.now()
    formatted_date = date.strftime("%A, %d %B %Y, %I:%M:%S %p")

    return render_template('hasil.html', nama=nama, 
                           nim=nim, 
                           fakultas=fakultas, 
                           program_studi=program_studi, 
                           semester=semester,
                           date=formatted_date)


@app.route('/daftarmatkul')
def daftarmatkul():
    semester = request.args.get('semester')
    nama = request.args.get('nama')
    nim = request.args.get('nim')
    fakultas = request.args.get('fakultas')
    program_studi = request.args.get('program_studi')
    print(nama, nim, fakultas, program_studi, semester)

    mata_kuliah_wajib = get_name_matakuliah(mysql.connection, semester, query_select_matakuliah_TI_Wajib)
    mata_kuliah_pilihan = get_name_matakuliah(mysql.connection, semester, query_select_matakuliah_TI_Pilihan)

    return render_template('daftarmatkul.html',
                           nama=nama, nim=nim, fakultas=fakultas, program_studi=program_studi, 
                           semester=semester, mata_kuliah_wajib=mata_kuliah_wajib,
                           mata_kuliah_pilihan=mata_kuliah_pilihan)


@app.route("/getsemester", methods=['POST'])
def getsemester():
    nama = request.form.get('nama')
    nim = request.form.get('nim')
    fakultas = request.form.get('fakultas')
    program_studi = request.form.get('program_studi')
    semester = request.form.get('semester')
    return redirect(url_for('pilihmatkul', nama=nama, nim=nim, fakultas=fakultas, program_studi=program_studi, semester=semester))


#ROUTE UNTUK MEMILIH MATKUL
@app.route('/pilihmatkul')
def pilihmatkul():
    nama = request.args.get('nama')
    nim = request.args.get('nim')
    fakultas = request.args.get('fakultas')
    program_studi = request.args.get('program_studi')
    semester = request.args.get('semester')
    print(semester)

    #Data yang akan ditampilkan ke html
    mata_kuliah_wajib = get_name_matakuliah(mysql.connection, semester, query_select_matakuliah_TI_Wajib)
    mata_kuliah_pilihan = get_name_matakuliah(mysql.connection, semester, query_select_matakuliah_TI_Pilihan)

    #Data yang akan disimpan dalam database
    id_matakuliah_wajib_tuples = get_id(mysql.connection, query_select_id_matakuliah_TI_Wajib, (semester, ))
    id_matakuliah_pilihan_tuples = get_id(mysql.connection, query_select_id_matakuliah_TI_Pilihan, (semester, ))

    id_matakuliah_wajib = [id[0] for id in id_matakuliah_wajib_tuples]
    id_matakuliah_pilihan = [id[0] for id in id_matakuliah_pilihan_tuples]

    return render_template('pilihmatkul.html', nama=nama, nim=nim, fakultas=fakultas, program_studi=program_studi, semester=semester, 
                           mata_kuliah_wajib=mata_kuliah_wajib, 
                           mata_kuliah_pilihan=mata_kuliah_pilihan,
                           id_matakuliah_wajib=id_matakuliah_wajib,
                           id_matakuliah_pilihan=id_matakuliah_pilihan)

@app.route('/submitmatakuliah', methods=['POST'])
def submitmatakuliah():
    nama = request.form.get('nama')
    nim = request.form.get('nim')
    fakultas = request.form.get('fakultas')
    program_studi = request.form.get('program_studi')
    semester = request.form.get('semester')

    matakuliah_wajib_id = request.form.getlist('matkul_wajib')
    matakuliah_pilihan_id = request.form.getlist('matkul_pilihan')

    nama_matakuliah_wajib = get_nama_matakuliah(mysql.connection, matakuliah_wajib_id, query_select_matakuliah_TI_Pilihan_id)
    nama_matakuliah_pilihan = get_nama_matakuliah(mysql.connection, matakuliah_pilihan_id, query_select_matakuliah_TI_Pilihan_id)

    print(nama_matakuliah_wajib)
    print(nama_matakuliah_pilihan)

    print(matakuliah_wajib_id)
    print(matakuliah_pilihan_id)

    #Masukan Identitas Mahasiswa ke database lalu ambil idnya
    data_mahasiswa = (nama, nim, fakultas, program_studi, semester)
    mahasiswa_id = insert_data_get_id(mysql.connection, insert_query_mahasiswa, data_mahasiswa)
    print(mahasiswa_id)

    #Masukan Data ID Mata Kuliah Wajib
    for id_matkul in matakuliah_wajib_id:
        data_matakuliah_wajib = (mahasiswa_id, id_matkul)
        insert_data(mysql.connection, insert_query_mahasiswa_matakuliah, data_matakuliah_wajib)

    #Masukan Data ID Mata Kuliah Pilihan
    for id_matkul in matakuliah_pilihan_id:
        data_matakuliah_pilihan = (mahasiswa_id, id_matkul)
        insert_data(mysql.connection, insert_query_mahasiswa_matakuliah, data_matakuliah_pilihan)


    return redirect(url_for('hasilti', nama=nama, nim=nim, fakultas=fakultas, program_studi=program_studi, semester=semester,
                            nama_matakuliah_wajib=nama_matakuliah_wajib, nama_matakuliah_pilihan=nama_matakuliah_pilihan))

@app.route('/hasilti')
def hasilti():
    nama = request.args.get('nama')
    nim = request.args.get('nim')
    fakultas = request.args.get('fakultas')
    program_studi = request.args.get('program_studi')
    semester = request.args.get('semester')
    
    matakuliah_wajib = request.args.getlist('nama_matakuliah_wajib')
    matakuliah_pilihan = request.args.getlist('nama_matakuliah_pilihan')
    print(matakuliah_wajib)
    print(matakuliah_pilihan)

    locale.setlocale(locale.LC_ALL, 'id-ID')

    date = dt.datetime.now()
    formatted_date = date.strftime("%A, %d %B %Y, %I:%M:%S %p")

    return render_template('hasilti.html', nama=nama, 
                           nim=nim, 
                           fakultas=fakultas, 
                           program_studi=program_studi, 
                           semester=semester,
                           matakuliah_wajib=matakuliah_wajib,
                           matakuliah_pilihan=matakuliah_pilihan,
                           date=formatted_date)