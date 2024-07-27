class Identitas:
    def __init__(self, nama=None, nim=None, fakultas=None, program_studi=None, semester=None, mata_kuliah_TI_Pilihan_Mahasiswa=None):
        self.nama = nama.upper() if nama is not None else None
        self.nim = nim
        self.fakultas = fakultas
        self.program_studi = program_studi
        self.semester = semester

fakultas = [                        #Daftar Fakultas dengan Array
    "Fakultas Ekonomi dan Bisnis",
    "Fakultas Komunikasi",
    "Fakultas Hukum",
    "Fakultas Psikologi",
    "Fakultas Teknik",
    "Fakultas Ilmu Komputer",
    "Fakultas Desain dan Industri Kreatif",
    "Fakultas Kesehatan",
    "Fakultas Fisioterapi",
    "Fakultas Keguruan dan Ilmu Pendidikan"
]

program_studi = [                   #Daftar Program studi dengan array 2 dimensi
    ["Manajemen", "Akuntansi"],
    ["Periklanan", "Jurnalistik", "Hubungan Masyarakat (Public Relations)", "Penyiaran (Broadcasting)"],
    ["Hukum"],
    ["Psikologi"],
    ["Perencanaan Wilayah & Kota", "Teknik Industri", "D3 Survei dan Pemetaan"],
    ["Sistem Informasi", "Teknik Informatika"],
    ["Desain Komunikasi Visual", "Desain Produk", "Desain Interior"],
    ["Kesehatan Masyarakat", "Ilmu Gizi", "D3 Rekam Medis", "Keperawatan", "Manajemen Informasi Kesehatan", "Bioteknologi", "Farmasi"],
    ["Fisioterapi"],
    ["Pendidikan Guru SD", "Pendidikan Bahasa Inggris"]
]

mata_kuliah_TI = [                  #Daftar mata kuliah Teknik Informatika
    ["Algoritma dan Pemrograman", "Dasar Sistem Informasi", "Aljabar Linier dan Matriks", "Bahasa Inggris 1", "Bahasa Indonesia dan PKN"],
    ["Bahasa Pemrograman", "Kalkulus 1", "Struktur Data", "Organisasi dan Manajemen", "Organisasi dan Arsitektur Komputer", "Matematika Diskrit"],
    ["Desain dan Analisis Algoritma", "Kalkulus 2", "Pemrograman Beriorientasi Objek", "Basis Data", "Sistem Operasi", "Rekayasa Perangkat Lunak", "Kewirausahawan"],
    ["Manajemen Proyek Perangkat Lunak", "Keamanan Informasi", "Pemrograman Web", "Jaringan Komputer", "Analisis dan Perangacangan Sistem Informasi", "Data Warehouse"],
    ["Kecerdasan Artificial", "Pemrograman Mobile", "Kriptografi", "Statistik", "Data Mining"],
    ["Isu Sosial dan Keprofesian Teknologi Informasi", "Metodologi Penelitian", "Interaksi Manusia Komputer"],
    ["Sistem Basis Data Terdistribusi", "Jaringan Komputer Lanjut", "Kapita Selekta Informatika", "Seminar Proposal"],
    ["Tugas Akhir"] 
]

mata_kuliah_TI_Pilihan = [
    [],
    [],
    [],
    ["Machine Learning", "Arsitektur berbasis layanan", "Internet of Things"],
    ["Pengolahan Citra", "Jaringan Mobile", "Pengembangan Perangkat Lunak", "Perancangan Aplikasi Mobile"],
    ["Arsitektur Enterprise", "Cyber Security", "Mobile Application and Technology", "Big Data", "Bahasa Inggris 2", "Kewirausahaan 2"],
    ["Software Quality Assurance", "Game Development" , "Bahasa Inggris 3", "Kewirausahaan 3"],
    []
]