import tkinter as tk
from functools import partial

def pertambahan(labelHasil, bil1, bil2):
b1 = int(bil1.get())
b2 = int(bil2.get())
hasil = bl + b2
# config digunakan untuk mengakses object atribut setelah inj
labelHasil.config(text=hasil)
return

root = th.Tk()

# 400x200 adalah lebar dan tinggi window
# 500 adalah posisi secara horizontal

# 200 odelah posisi secars vertikal
root. geometry ('460x200+500+200' )

# mengubah font
root.option_add('font', ('Verdana', 10, 'normal'))

# untuk tampilkan title di window border
root. title('Aritnatika')

# configure untuk mengubah tampilan warna
#root. configure (bg="#FFFFFF")

labelBilangani = tk.Label(root. text="Masukkan Bilangen 1")
labelBilanganl.grid(row=8, column=e, padx=(19,20))
labelBilangan2 = tk.Label(root, text="Masukkan Bilangan 2")
1abelBilangan2.grid(row=1, column=8, padx=(16,20))

# Stringvar() digunakan untuk menampung inputan tipe String
bilangani = tk.Stringvar()

bilangan2 = tk.Stringvar()

inputBilanganl = tk.Entry(root, textvariable=bilangani)
inputBilanganl.grid(row=e, column=1)
inputBilangan2 = tk.Entry(root, textvariable=bilangan2)
inputBilangan2.grid(row=1, column=1)

labelHasil = tk.Label(root)
1abelHasil.grid(row=2, column=1)

# Functools.partial untuk membuat fungsi baru atau fungsi versi baru dengan argumen
pertambahan = partial(pertambanan, labeldasil, bilangani, bilanganz)
tombolTambah = tk.Button(root, text="Tambah", command=pertambahan)

# sticky digunakan untuk penyesuaian widget di dalam cell

# sticky="W" yang artinya West adalah posisi widget di kiri (di dalam cell)
# sticky="E" yang artinya East adaleh posisi widget di kanen (di dalam cell)
# sticky="WE" artinya memenuhi cell atau alignment rata penuh

# padx adalah padding horizontal

# pady adalah padding vertikal

tombolTambah.grid(row-2, column-0, sticky-"WE", pads-(10,20), pady-(5,0))
tombolTambah. configure(bg="400@", fg="#FFF")

root.mainloop()