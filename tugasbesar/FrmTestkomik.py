import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Testkomik import Testkomik
from tkcalendar import Calendar, DateEntry
class FormTestkomik:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar) 
        self.update_main_window = update_main_window
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # int 
        Label(mainFrame, text='ID Pelanggan:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox IDPELANGGAN
        self.txtIDPELANGGAN = Entry(mainFrame) 
        self.txtIDPELANGGAN.grid(row=0, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='Nama Pelanggan:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMAPELANGGAN
        self.txtNAMAPELANGGAN = Entry(mainFrame) 
        self.txtNAMAPELANGGAN.grid(row=1, column=1, padx=5, pady=5)
                
         # enum 
        Label(mainFrame, text='Judul Komik:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtJUDULKOMIK = StringVar()
        CboJUDULKOMIK = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJUDULKOMIK) 
        CboJUDULKOMIK.grid(row=2, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboJUDULKOMIK['values'] = ('Naruto','Jujutsu Kaisen','My Hero Academia','Hunter x Hunter','One Piece','Boruto','Dragon Ball','Bleach','Inuyasha','Kingdom','Demon Slayer','Monster')
        CboJUDULKOMIK.current()
        
         # date 
        Label(mainFrame, text='Waktu Peminjaman:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Date Input WAKTUPEMINJAMAN
        self.txtWAKTUPEMINJAMAN = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtWAKTUPEMINJAMAN.grid(row=3, column=1, padx=5, pady=5)
                    
         # date 
        Label(mainFrame, text='Waktu Pengembalian:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Date Input WAKTUPENGEMBALIAN
        self.txtWAKTUPENGEMBALIAN = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtWAKTUPENGEMBALIAN.grid(row=4, column=1, padx=5, pady=5)
                    
         # int 
        Label(mainFrame, text='Tarif:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Textbox TARIF
        self.txtTARIF = Entry(mainFrame) 
        self.txtTARIF.grid(row=5, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','idpelanggan','namapelanggan','judulkomik','waktupeminjaman','waktupengembalian','tarif')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('idpelanggan', text='idpelanggan')
        self.tree.column('idpelanggan', width="100")
        self.tree.heading('namapelanggan', text='namapelanggan')
        self.tree.column('namapelanggan', width="100")
        self.tree.heading('judulkomik', text='judulkomik')
        self.tree.column('judulkomik', width="100")
        self.tree.heading('waktupeminjaman', text='waktupeminjaman')
        self.tree.column('waktupeminjaman', width="100")
        self.tree.heading('waktupengembalian', text='waktupengembalian')
        self.tree.column('waktupengembalian', width="100")
        self.tree.heading('tarif', text='tarif')
        self.tree.column('tarif', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtIDPELANGGAN.delete(0,END)
        self.txtIDPELANGGAN.insert(END,"")
                                
        self.txtNAMAPELANGGAN.delete(0,END)
        self.txtNAMAPELANGGAN.insert(END,"")
                                
        self.txtJUDULKOMIK.set("")
            
        self.txtTARIF.delete(0,END)
        self.txtTARIF.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data testkomik
        obj = Testkomik()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        self.txt.get()
        obj = Testkomik()
        res = obj.getBy()
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        self.txt.get()
        obj = Testkomik()
        res = obj.getBy()
            
        self.txtIDPELANGGAN.delete(0,END)
        self.txtIDPELANGGAN.insert(END,obj.idpelanggan)
                                
        self.txtNAMAPELANGGAN.delete(0,END)
        self.txtNAMAPELANGGAN.insert(END,obj.namapelanggan)
                                
        self.txtJUDULKOMIK.set(obj.judulkomik)
            
        self.txtWAKTUPEMINJAMAN.delete(0,END)
        self.txtWAKTUPEMINJAMAN.insert(END,obj.waktupeminjaman)
                                
        self.txtWAKTUPENGEMBALIAN.delete(0,END)
        self.txtWAKTUPENGEMBALIAN.insert(END,obj.waktupengembalian)
                                
        self.txtTARIF.delete(0,END)
        self.txtTARIF.insert(END,obj.tarif)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        idpelanggan = self.txtIDPELANGGAN.get()
        namapelanggan = self.txtNAMAPELANGGAN.get()
        judulkomik = self.txtJUDULKOMIK.get()
        waktupeminjaman = self.txtWAKTUPEMINJAMAN.get()
        waktupengembalian = self.txtWAKTUPENGEMBALIAN.get()
        tarif = self.txtTARIF.get()       
        obj = Testkomik()
        obj.idpelanggan = idpelanggan
        obj.namapelanggan = namapelanggan
        obj.judulkomik = judulkomik
        obj.waktupeminjaman = waktupeminjaman
        obj.waktupengembalian = waktupengembalian
        obj.tarif = tarif
        if(self.ditemukan==True):
            res = obj.updateBy()
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        self.txt.get()
        obj = Testkomik()
    
        if(self.ditemukan==True):
            res = obj.deleteBy()
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormTestkomik(root, "Aplikasi Rental Komik" , update_main_window) 
    root.mainloop() 