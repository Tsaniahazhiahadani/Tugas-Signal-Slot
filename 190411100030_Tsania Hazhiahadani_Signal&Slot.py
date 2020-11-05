import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Membuat fungsi utk menentukan layout window
# Memecah fungsi menjadi beberapa bagian, TopLayout merupakan fungsi untuk tampilan bagian atas

def topLayout(window):
    # Membuat Judul Dibagian Atas
    lb = QLabel(" Menghitung Skala dan Jarak Peta")
    # Mensetting Align nya agar berada Ditengah
    lb.setAlignment(Qt.AlignCenter)
    # Membuat Vertical Layout Dan Menambahkan Widget ya
    layout1 = QVBoxLayout()
    layout1.addWidget(lb)
    # Mereturn/mengembalikan nilai layout nya karena kita butuh layoutnya untuk ditambahkan ke gridLayout nya
    return layout1

def hitungSkala(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Menghitung Skala", window)
    # Membuat Widget Label
    labelJP = QLabel("Jarak pada peta: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global JP
    labelJS = QLabel("Jarak Sebenarnya: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global JS
    # Membuat Widget Inputan
    JP = QLineEdit()
    JS = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Hitung")
    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(hitskala)
    # Membuat Form Layout Dan Menambahkan widget
    layout = QVBoxLayout()
    layout1 = QGridLayout()
    layout1.addWidget(labelJP)
    layout1.addWidget(JP)
    layout2 = QGridLayout()
    layout2.addWidget(labelJS)
    layout2.addWidget(JS)
    layout.addLayout(layout1)
    layout.addLayout(layout2)
    layout.addWidget(btn)
    groupbox.setLayout(layout)
    return groupbox

def hitskala():
    try:
        RJP = JP.text()
        RJS = JS.text()
        hSkala = int(RJP) / int(RJS)
        hasilSkala.setText(str(hSkala))
        JP.setText("")
        JS.setText("")
    except ValueError:
        pass
    
# Rumus Perhitungan
def jarakPeta(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Menghitung Jarak pada Peta", window)
    # Membuat Widget Label
    labelJarSebenarnya = QLabel("Jarak Sebenarnya: ")
    labelSkala = QLabel("Skala: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global jarsebenarnya, skala
    # Membuat Widget Inputan
    jarsebenarnya = QLineEdit()
    skala = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Hitung")
    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(Peta)
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QGridLayout()
    layout1.addWidget(labelJarSebenarnya,0,0)
    layout1.addWidget(jarsebenarnya,0,1)
    layout1.addWidget(labelSkala,1,0)
    layout1.addWidget(skala,1,1)
    layout1.addWidget(btn,2,0,1,0)
    groupbox.setLayout(layout1)
    return groupbox

def Peta():
    try:
        RJS = jarsebenarnya.text()
        RSkal = skala.text()
        hJarakPeta = int (RJS) * int (RSkal)
        hasilJarakPeta.setText(str(hJarakPeta))
        jarsebenarnya.setText("")
        skala.setText("")
    except ValueError:
        pass
    
def Tampil(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Hasil Operasi", window)
    # Membuat Widget Label
    labelSkala = QLabel("Skala: ")
    labelJarakPeta = QLabel("Jarak pada Peta: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global hasilSkala,hasilJarakPeta
    # Membuat Widget Inputan
    hasilSkala = QLineEdit()
    hasilSkala.setReadOnly(True)
    hasilJarakPeta = QLineEdit()
    hasilJarakPeta.setReadOnly(True)
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QFormLayout()
    layout1.addRow(labelSkala,hasilSkala)
    layout1.addRow(labelJarakPeta,hasilJarakPeta)
    groupbox.setLayout(layout1)
    return groupbox

def window_go():
    #inisialisasi pyqt
    app = QApplication(sys.argv)
    window = QWidget()
    # Menginisiasi GridLayout
    GLayout = QGridLayout()
    # Menambahkan Widget GroupBox Ke gridLayout
    GLayout.addLayout(topLayout(window),0,0,1 ,2)
    GLayout.addWidget(hitungSkala(window), 2, 0,1,0)
    GLayout.addWidget(jarakPeta(window), 3, 0,1,0)
    GLayout.addWidget(Tampil(window), 4, 0,1,0)
    # Menset agar jarak tidak terlalu renggang
    GLayout.setRowStretch(2,1)
    GLayout.setRowStretch(3,1)
    # Menset Layout Utama Ke GridLayout
    window.setLayout(GLayout)
    # Mensetting Ukuran Aplikasinya
    window.setGeometry(100,100,500,500)
    # Menset Judul Aplikasi
    window.setWindowTitle("Menghitung Skala dan Jarak Peta")
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    window_go()