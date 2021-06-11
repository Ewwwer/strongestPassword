import tkinter as tk
import password

print(password.result_psw)

def copy_text ():
    txt = txtbox1.get ()
    print (txt)
    ventana.clipboard_append (txt)

ventana = tk.Tk()
ventana.title ("Generateur mot de pass")
ventana.geometry("650x150")
greeting = tk.Label(ventana,text=password.result_psw, relief="flat",takefocus=0,highlightthickness=0)
greeting.config(font=("Courier", 80))
greeting.pack()

# button3 = tk.Button (ventana, text = "Copier le mot de pass", font = ("Meiryo UI", 18), command = copy_text)
# button3.pack (expand = 1)


ventana.mainloop()
