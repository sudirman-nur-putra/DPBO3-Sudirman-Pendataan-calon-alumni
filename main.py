""" 
    Saya Sudirman Nur Putra mengerjakan Tugas Praktkm 3 dalam Praktikum Desain dan Pemrograman Berorientasi Objek untuk
    keberkahan-Nya maka saya tidak melakukan kecurangan yang seperti yang telah dispesifikasikan. Aamiin
"""
# mengimfor library
from Biodata import Biodata
from tkinter import *

data = []

# tkinter untuk tampilan GUI
root = Tk()
root.title("PENDATAAN CALON ALUMNI")
# menampilkan semua data calon alumni
def semuaData():
    prof = Toplevel()
    prof.title("DATA CALON ALUMNI")

    p_frame = LabelFrame(prof, text="Data calon alumni", padx=15, pady=10)
    p_frame.pack(padx=15, pady=10)

    prof_nama = Label(p_frame, text="Data Semua Calon Alumni", anchor="w").grid(row=0, column=0, sticky="w")
# body untuk tampilan
body = LabelFrame(root, borderwidth=0)
body.grid(column=0, row=0)
# untuk form inputan
masuk = LabelFrame(body, padx=10, pady=10, borderwidth=0)
masuk.pack(padx=10, pady=10)
masuk.grid(column=0, row=0)
# untuk tampilan navigasi 
navigasi = LabelFrame(masuk, padx=5, borderwidth=0, pady=3, width=50)
navigasi.grid(column = 0, row = 0)
# untuk menampilkan semua data calon alumni
b_alumni = Button(navigasi, text="Calon alumni", command=lambda: semuaData())
b_alumni.grid(row=0, column=0)
# menghapus semua data calon
b_haspu = Button(navigasi, text="Hapus Semua")
b_haspu.grid(row=0, column=2)
# menampilkan tentang pembuat perangkat
def Profil():
	# tampilan baru
    prof = Toplevel()
    prof.title("Profil Pembuat")
    # data mahasiswa
    p_frame = LabelFrame(prof, text="Data mahasiswa", padx=15, pady=10)
    p_frame.pack(padx=15, pady=10)
    # data yang ditampilkan
    prof_nama = Label(p_frame, text="Nama   : Sudirman Nur Putra", anchor="w").grid(row=0, column=0, sticky="w")
    prof_nim = Label(p_frame, text="NIM    : 1900457", anchor="w").grid(row=1, column=0, sticky="w")
    prof_kelas = Label(p_frame, text="Kelas   : C1", anchor="w").grid(row=2, column=0, sticky="w")
# untuk menampilkan tentang pembuat
b_simpan = Button(navigasi, text="Tentang Perangkat",  command=lambda: Profil())
b_simpan.grid(row=0, column=4)
# keluar dari aplikasi
b_simpan = Button(navigasi, text="Keluar",  command=root.quit)
b_simpan.grid(row=0, column=6)
# variabel untuk inputan
nama = StringVar()
alamat = StringVar()
var1 = "Olahraga"
var2 = "Seni"
var3 = "Travel"
var4 = "Keilmuan"
var5 = "dll"
var = StringVar()
options = StringVar()
kesan = StringVar()
pesan = StringVar()
# mengambil data
# def getValue():
# 	prof = Toplevel()
#     prof.title("data input")
#     # data mahasiswa
#     p_frame = LabelFrame(prof, text="Data mahasiswa", padx=15, pady=10)
#     p_frame.pack(padx=15, pady=10)
#     prof_nama = Label(p_frame, text= nama.get(), anchor="w").grid(row=0, column=0, sticky="w")
#     prof_nama = Label(p_frame, text= alamat.get(), anchor="w").grid(row=0, column=0, sticky="w")
#     prof_nama = Label(p_frame, text= kesan.get(), anchor="w").grid(row=0, column=0, sticky="w")
#     prof_nama = Label(p_frame, text= pesan.get(), anchor="w").grid(row=0, column=0, sticky="w")


# bungkusan form input calon alumni
frame = LabelFrame(masuk, text="CALON ALUMNI", padx=5, pady=3, width=50)
frame.grid(column = 0, row = 1)
# bungkusan untuk tombol
frame_b = LabelFrame(masuk, padx=5, pady=3, width=50, borderwidth=0)
frame_b.grid(column = 0, row = 3)

# opts = LabelFrame(root, padx=10, pady=10)
# opts.pack(padx=10, pady=10)

# label dan inputan untuk nama
label = Label(frame, text="Nama ", pady=5, width = 20)
label.grid(column=0, row=0)
namaEntered = Entry(frame, width = 30, textvariable = nama)
namaEntered.grid(column = 2, row = 0)
# label dan inputan untuk alamat
label = Label(frame, text="Alamat ", pady=5, width = 20)
label.grid(column=0, row=1)
alamatEntered = Entry(frame, width = 30, textvariable = alamat)
alamatEntered.grid(column = 2, row = 1)
# label dan inputan untuk hobi berupa checkbox
label = Label(frame, text="Hobi ", pady=5, width = 20)
label.grid(column=0, row=2)
check = LabelFrame(frame, padx=5, pady=3, width=50, borderwidth=0)
check.grid(column = 2, row = 2)
check1 = Checkbutton(check, text='Olahraga',variable=var1, onvalue=1, offvalue=0).grid(column=0, row=0)
check2 = Checkbutton(check, text='Seni',variable=var2, onvalue=1, offvalue=0).grid(column=1, row=0)
check3 = Checkbutton(check, text='Travel',variable=var3, onvalue=1, offvalue=0).grid(column=2, row=0)
check4 = Checkbutton(check, text='Keilmuan',variable=var4, onvalue=1, offvalue=0).grid(column=0, row=1)
check5 = Checkbutton(check, text='lainnya',variable=var5, onvalue=1, offvalue=0).grid(column=1, row=1)
# label dan inputan untuk jenis kelamin
label = Label(frame, text="Jenis Kelamin ", pady=5, width = 20)
label.grid(column=0, row=3)
radio = LabelFrame(frame, padx=5, pady=3, width=50, borderwidth=0)
radio.grid(column = 2, row = 3)
R1 = Radiobutton(radio, text="Laki-laki", variable=var, value="Laki-laki")
R1.grid(column=0, row=0)
R2 = Radiobutton(radio, text="Perempuan", variable=var, value="Perempuan")
R2.grid(column=1, row=0)
# label dan inputan untuk kelas
label = Label(frame, text="Kelas ", pady=5, width = 20)
label.grid(column=0)
options.set("Kelas") # default value
om1 = OptionMenu(frame, options, "RPL","TKJ", "Telin", "Farmasi", "TMO", "TKRO")
om1.grid(row=4,column=2) 
# label dan inputan untuk kesan
label = Label(frame, text="Kesan ", pady=5, width = 20)
label.grid(column=0, row=5)
kesanEntered = Entry(frame, width = 30, textvariable = kesan)
kesanEntered.grid(column = 2, row = 5)
# label dan intpuan untuk pesan
label = Label(frame, text="Pesan ", pady=5, width = 20)
label.grid(column=0, row=6)
pesanEntered = Entry(frame, width = 30, textvariable = pesan)
pesanEntered.grid(column = 2, row = 6)
# tombol untuk tambah gambar, mesi tidak bisa di tambahkan gambar
b_add = Button(frame_b, text="Tambah Foto", width=40)
b_add.grid(row=0, column=0)
# tombol untuk menyimpan data
b_simpan = Button(frame_b, text="Simpan", width=40)
b_simpan.grid(row=1, column=0)

root.mainloop()