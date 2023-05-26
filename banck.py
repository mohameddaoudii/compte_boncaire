# import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import sqlite3

conn = sqlite3.connect("banck.db")
cr = conn.cursor()


class homepageemploye(tk.Tk):
    def __init__(self, data):
        super().__init__()
        self.data = data
        print(data)

        self.title("Home")
        self.geometry("550x500")
        self.config(bg="#355070")
        #
        self.titer = tk.Label(
            self,
            text="Welcom To Your A Counte ",
            font=("Arial", 18, "bold"),
            bg="#355070",
            fg="#9bf6ff",
        )
        self.titer.place(x=100, y=40)
        # name
        self.namelabel = tk.Label(
            self,
            text="Name : ",
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#9bf6ff",
        )

        self.namelabel.place(x=100, y=130)
        self.name = tk.Label(
            self,
            text=data[0].capitalize(),
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#f4f4f4",
        )
        self.name.place(x=240, y=130)

        # prenom

        self.prenomlabel = tk.Label(
            self,
            text="Prenom : ",
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#9bf6ff",
        )
        self.prenomlabel.place(x=100, y=190)

        self.prenom = tk.Label(
            self,
            text=data[1].capitalize(),
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#f4f4f4",
        )
        self.prenom.place(x=240, y=190)
        # identifiant

        self.idenlabel = tk.Label(
            self,
            text="Identifiant : ",
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#9bf6ff",
        )
        self.idenlabel.place(x=100, y=250)
        self.identifaint = tk.Label(
            self,
            text=data[2],
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#f4f4f4",
        )
        self.identifaint.place(x=240, y=250)

        # password
        self.passwordlabe = tk.Label(
            self,
            text="Password : ",
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#9bf6ff",
        )
        self.passwordlabe.place(x=100, y=310)

        self.password = tk.Label(
            self,
            text=data[3],
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#f4f4f4",
        )
        self.password.place(x=240, y=310)

        # sold
        self.soldlabe = tk.Label(
            self,
            text="Sold : ",
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#9bf6ff",
        )
        self.soldlabe.place(x=100, y=370)
        self.soldlabe = tk.Label(
            self,
            text=f"{data[4]} DH",
            font=("Arial", 15, "bold"),
            bg="#355070",
            fg="#f4f4f4",
        )
        self.soldlabe.place(x=240, y=370)

        self.btretier = tk.Button(
            self,
            text="Retier",
            font=("", 12, "bold"),
            bg="#00afef",
            padx=18,
            pady=8,
            fg="#f4f4f4",
            command=self.retires,
        )
        self.btretier.place(x=100, y=430)

    def retires(self):
        self.destroy()
        interf = retirer(self.data)


class retirer(tk.Tk):
    def __init__(self, montantexist):
        super().__init__()
        self.montantexist = montantexist
        self.title("Employe")
        self.geometry("300x300")
        self.config(bg="#355070")
        self.title("Retirer L'argent")
        self.titer = tk.Label(
            self,
            text="Retirer L'argent",
            font=("Arial", 25, "bold"),
            bg="#355070",
            fg="#9bf6ff",
        )
        self.titer.place(x=20, y=100)

        self.argent = ttk.Label(
            self,
            text="La valeur du montant que vous souhaitez retirer",
            # bg="#355070",
            background="#355070",
            foreground="#fff",
        )
        self.argent.place(x=20, y=150)
        self.montant = ttk.Entry(self, width=40)
        # self.password.config(height=2)
        self.montant.place(x=20, y=180)
        self.button = ttk.Button(self, text="retirer", padding=5, command=self.retir)
        self.button.place(x=20, y=230)
        self.status = ttk.Label(
            self, background="#355070", foreground="red", font=("Arial", 14, "bold")
        )
        self.status.place(x=20, y=270)

    def retir(self):
        montant = int(self.montant.get())
        montex = "SELECT sold FROM client WHERE identifiant = ?"
        datae = (int(self.montantexist[2]),)
        cr.execute(montex, datae)
        resulta = cr.fetchall()

        if len(resulta) >= 1:
            print(resulta)
            resulta = int(resulta[0][0])

        if resulta >= montant:
            re = resulta - int(self.montant.get())
            self.status.config(text="operation is pass", foreground="blue")
            sql = "UPDATE client SET sold = ? WHERE identifiant = ? and password = ?"
            data = (re, int(self.montantexist[2]), int(self.montantexist[3]))
            print(self.montantexist[2])
            print(self.montantexist[3])

            cr.execute(sql, data)
            conn.commit()
        else:
            self.status.config(
                text="this montant is beg to the montant you have",
                font=("Arial", 10, "bold"),
                foreground="red",
            )


class employe(tk.Tk):
    def __init__(
        self,
    ):
        super().__init__()
        # self.cr = cr
        self.title("Employe")
        self.geometry("550x500")
        self.config(bg="#355070")
        self.titte = tk.Label(
            self,
            text="Accédez à Vos Comptes",
            font=("Arial", 16),
            bg="#355070",
            fg="#f4f4f4",
        )
        self.titte.place(x=150, y=100)
        # identifiant
        self.identifiant = tk.Entry(
            self, font=("Arial", 16), bg="#f4f4f4", fg="#87878f"
        )
        self.identifiant.place(x=150, y=150)
        self.identifiant.insert(0, "Identifiant")
        self.identifiant.bind("<FocusIn>", self.onclick)
        self.identifiant.bind("<FocusOut>", self.onfocus)

        # password
        self.passowrd = tk.Entry(
            self,
            font=("Arial", 16),
            bg="#f4f4f4",
            fg="#87878f",
        )
        self.passowrd.place(x=150, y=200)
        self.passowrd.insert(0, "password")
        self.passowrd.bind("<FocusIn>", self.onclickp)
        self.passowrd.bind("<FocusOut>", self.onfocusp)

        self.login = tk.Button(
            self,
            text="Connexion",
            font=("", 12, "bold"),
            bg="#00afef",
            padx=18,
            pady=8,
            fg="#f4f4f4",
            command=self.verification,
        )
        self.login.place(x=210, y=250)
        self.status = tk.Label(
            self,
            bg="#355070",
            fg="red",
            font=(
                "Arial",
                12,
            ),
        )
        self.status.place(x=150, y=320)

    def onclick(self, event):
        if self.identifiant.get() == "Identifiant":
            self.identifiant.delete(0, tk.END)

    def onfocus(self, event):
        if self.identifiant.get() == "":
            self.identifiant.insert(0, "Identifiant")

    def onclickp(self, event):
        if self.passowrd.get() == "password":
            self.passowrd.delete(0, tk.END)

    def onfocusp(self, event):
        if self.passowrd.get() == "":
            self.passowrd.insert(0, "password")

    def verification(self):
        sql = "SELECT * FROM client WHERE identifiant = ?  AND password = ?"
        data = (int(self.identifiant.get()), int(self.passowrd.get()))

        cr.execute(sql, data)
        resulta = cr.fetchall()
        if len(resulta) >= 1:
            self.destroy()
            inter = homepageemploye(resulta[0])
        else:
            # print("you are not existe in banck ")
            self.status.config(text="identifiant or password not correct !!")


class admin(tk.Tk):
    def __init__(
        self,
    ):
        super().__init__()
        # self.cr = cr
        self.title("Admin")
        self.geometry("550x500")
        self.config(bg="#355070")
        self.titte = tk.Label(
            self,
            text="Accédez à Vos Comptes Admin",
            font=("Arial", 16),
            bg="#355070",
            fg="#9bf6ff",
        )
        self.titte.place(x=120, y=100)
        # identifiant
        self.identifiant = tk.Entry(
            self, font=("Arial", 16), bg="#f4f4f4", fg="#87878f"
        )
        self.identifiant.place(x=150, y=150)
        self.identifiant.insert(0, "Identifiant")
        self.identifiant.bind("<FocusIn>", self.onclick)
        self.identifiant.bind("<FocusOut>", self.onfocus)

        # password
        self.passowrd = tk.Entry(
            self,
            font=("Arial", 16),
            bg="#f4f4f4",
            fg="#87878f",
        )
        self.passowrd.place(x=150, y=200)
        self.passowrd.insert(0, "password")
        self.passowrd.bind("<FocusIn>", self.onclickp)
        self.passowrd.bind("<FocusOut>", self.onfocusp)

        self.login = tk.Button(
            self,
            text="Connexion",
            font=("", 12, "bold"),
            bg="#00afef",
            padx=18,
            pady=8,
            fg="#f4f4f4",
            command=self.verification,
        )
        self.login.place(x=210, y=250)
        self.status = tk.Label(
            self,
            bg="#355070",
            fg="red",
            font=(
                "Arial",
                12,
            ),
        )
        self.status.place(x=150, y=320)

    def onclick(self, event):
        if self.identifiant.get() == "Identifiant":
            self.identifiant.delete(0, tk.END)

    def onfocus(self, event):
        if self.identifiant.get() == "":
            self.identifiant.insert(0, "Identifiant")

    def onclickp(self, event):
        if self.passowrd.get() == "password":
            self.passowrd.delete(0, tk.END)

    def onfocusp(self, event):
        if self.passowrd.get() == "":
            self.passowrd.insert(0, "password")

    def verification(self):
        sql = "SELECT * FROM admin WHERE identifiant = ?  AND password = ?"
        data = (int(self.identifiant.get()), int(self.passowrd.get()))

        cr.execute(sql, data)
        resulta = cr.fetchall()
        if len(resulta) >= 1:
            self.destroy()
            # inter =
            # (resulta[0])
        else:
            # print("you are not existe in banck ")
            self.status.config(text="identifiant or password not correct !!")


class homepageadmin(tk.Tk):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.title("Home_Page_Admin")
        self.geometry("550x500")
        self.config(bg="#355070")

        self.titles = tk.Label(
            self,
            text="Welcom To Page  The Admin",
            fg="#9bf6ff",
            bg="#355070",
            font=("Arial", 20),
        )
        self.titles.place(x=100, y=60)
        # addadmin
        self.addadmin = tk.Button(
            self,
            text="Add Admin",
            padx=19,
            pady=8,
            bg="#9bf6ff",
            fg="#6d597a",
            font=("Arial", 10, "bold"),
            # command=self.admin,
        )
        self.addadmin.place(x=100, y=150)
        # addclient
        self.addclient = tk.Button(
            self,
            text="Add Clinet",
            padx=19,
            pady=8,
            bg="#9bf6ff",
            fg="#6d597a",
            font=("Arial", 10, "bold"),
            # command=self.admin,
        )
        self.addclient.place(x=100, y=240)

        # show clinet
        self.showclient = tk.Button(
            self,
            text="Show Clinet",
            padx=19,
            pady=8,
            bg="#9bf6ff",
            fg="#6d597a",
            font=("Arial", 10, "bold"),
            # command=self.admin,
        )
        self.showclient.place(x=350, y=150)

        # delet clinet
        self.deltclinet = tk.Button(
            self,
            text="Delet Clinet",
            padx=19,
            pady=8,
            bg="#9bf6ff",
            fg="#6d597a",
            font=("Arial", 10, "bold"),
            # command=self.admin,
        )
        self.deltclinet.place(x=350, y=240)
        self.currentadmin = tk.Label(
            self,
            text="Name Admin : ",
            fg="#9bf6ff",
            bg="#355070",
            font=("Arial", 13),
        )
        self.currentadmin.place(x=200, y=340)
        self.nameadmin = tk.Label(
            self,
            text=data[0].capitalize(),
            fg="#9bf6ff",
            bg="#355070",
            font=("Arial", 13),
        )
        self.nameadmin.place(x=350, y=340)

        # identifiant
        self.idtfiant = tk.Label(
            self,
            text="Identifiant Admin : ",
            fg="#9bf6ff",
            bg="#355070",
            font=("Arial", 13),
        )
        self.idtfiant.place(x=200, y=400)

        self.currentadmin.place(x=200, y=340)
        self.idefadmin = tk.Label(
            self,
            text=data[1].capitalize(),
            fg="#9bf6ff",
            bg="#355070",
            font=("Arial", 13),
        )
        self.idefadmin.place(x=350, y=400)


class banck(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("banck")
        self.geometry("550x500")
        self.config(bg="#355070")

        self.titles = tk.Label(
            self,
            text="Welcom To This Banck",
            fg="#9bf6ff",
            bg="#355070",
            font=("Arial", 20),
        )
        self.titles.place(x=160, y=100)
        self.employe = tk.Button(
            self,
            text="Employe",
            padx=17,
            pady=8,
            bg="#9bf6ff",
            fg="#6d597a",
            font=("Arial", 10, "bold"),
            command=self.employ,
        )
        self.employe.place(x=200, y=200)
        self.Admin = tk.Button(
            self,
            text="Admin",
            padx=19,
            pady=8,
            bg="#9bf6ff",
            fg="#6d597a",
            font=("Arial", 10, "bold"),
            command=self.admin,
        )
        self.Admin.place(x=310, y=200)

    def employ(self):
        self.destroy()
        intef = employe()

    def admin(self):
        self.destroy()
        intef = admin()


datae = ("mohamed", "daoudi", 123072, 1234, 0)
objec = banck()
objec.mainloop()
conn.close()
