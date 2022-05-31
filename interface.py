from tkinter import *
from Data import *
# window parameter
point = Tk()

point.geometry('300x300')
point.title('Ou&Ta supermarket')

# labels parameters
label1 = Label(point, text='id')
label2 = Label(point, text='nom complet')
label3 = Label(point, text='password')
label1.grid(row=0, column=0)
label2.grid(row=2, column=0)
label3.grid(row=4, column=0)

# inputs parameters
id = StringVar()
nom = StringVar()
passwd = StringVar()
et1 = Entry(point, textvariable=id)
et1.grid(row=0, column=8)
et2 = Entry(point, textvariable=nom)
et2.grid(row=2, column=8)
et3 = Entry(point, textvariable=passwd)
et3.grid(row=4, column=8)

# button parameters


def se_connecter():
    idgestionnaire = id.get()
    nomgestionnaire = nom.get()
    passwdgestionnaire = passwd.get()
    cursor, db = get_connection()
    request = f"SELECT * FROM gestionnaire WHERE idgestionnaire = '{idgestionnaire}'"
    cursor.execute(request)
    x= 0
    for row in cursor:
        x=1
        if row is not None:
            n_id = row[0]
            n_nom = row[1]
            n_tele = row[2]
            n_address = row[3]
            n_email = row[4]
            n_passwd = row[5]
            if n_passwd == passwdgestionnaire:
                point2 = Tk()
                point2.geometry('300x300')
                point2.title('Opération réussie')
                label2 = Label(point2, text='opération réussie')
                label2.grid(row=5, column=5)
                point2.mainloop()
            else:
                point3 = Tk()
                point3.geometry('300x300')
                point3.title('Opération échouée')
                label3 = Label(point3, text='mot de pass incorrect')
                label3.grid(row=5, column=5)
                point3.mainloop()
    if x == 0:
        point1 = Tk()
        point1.geometry('300x300')
        point1.title('Opération échouée')
        label1 = Label(point1, text='id ou nom incorrect incorrect')
        label1.grid(row=5, column=5)
        point1.mainloop()
"""
    if cursor.fetchone() is not None:
        row = cursor.fetchall()

        n_id = row[0]
        n_nom = row[1]
        n_tele = row[2]
        n_address = row[3]
        n_email = row[4]
        n_passwd = row[5]
        print(0)
        if n_passwd == passwdgestionnaire:
            point2 = Tk()
            point2.geometry('300x300')
            point2.title('Opération réussie')
            label2 = Label(point2, text='opération réussie')
            label2.grid(row=5, column=5)
            point2.mainloop()
        else:
            point3 = Tk()
            point3.geometry('300x300')
            point3.title('Opération échouée')
            label3 = Label(point3, text='mot de pass incorrect')
            label3.grid(row=5, column=5)
            point3.mainloop()
    else:
        point1 = Tk()
        point1.geometry('300x300')
        point1.title('Opération échouée')
        label1 = Label(point1, text='id ou nom incorrect incorrect')
        label1.grid(row=5, column=5)
        point1.mainloop()
"""



button = Button(point, text='calculer', command=se_connecter)
button.grid(row=8, column=8)

point.mainloop()
