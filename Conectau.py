import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class Estudiante:
    def __init__(self, nombre, carrera, materia, horario, whatsapp):
        self.nombre = nombre
        self.carrera = carrera
        self.materia = materia
        self.horario = horario
        self.whatsapp = whatsapp
class ConectaU:
    def __init__(self, root):
        self.root = root
        self.root.title("CONECTAU")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#EAF2F8")
        self.estudiantes = []
        # Estilo de la tabla
        style = ttk.Style()
        style.configure("Treeview", rowheight=28,font=("Segoe UI", 10))
        style.configure("Treeview.Heading",font=("Segoe UI", 10, "bold"))
        # Título
        titulo = tk.Label(root,text="CONECTAU", font=("Segoe UI", 24, "bold"),bg="#EAF2F8",fg="#1F618D") 
        titulo.pack(pady=(20, 5))
        subtitulo = tk.Label(root,text="Plataforma para Formación de Equipos Universitarios",font=("Segoe UI", 11),bg="#EAF2F8")
        subtitulo.pack(pady=(0, 15))
        # Contador
        self.lbl_contador = tk.Label(root,text="Estudiantes registrados: 0",font=("Segoe UI", 10, "bold"),bg="#EAF2F8",fg="#117A65")        
        self.lbl_contador.pack()
        # Frame principal
        frame = tk.LabelFrame( root,text="Registro de Estudiantes",padx=10,pady=10,font=("Segoe UI", 10, "bold"))
        frame.pack(fill="x", padx=10, pady=10)
        # Nombre
        tk.Label(frame, text="Nombre").grid(row=0,column=0,padx=5,pady=5)
        self.nombre = tk.Entry(frame, width=25)
        self.nombre.grid(row=0, column=1)
        # Carrera
        tk.Label(frame, text="Carrera").grid(row=0,column=2,padx=5,pady=5)
        self.carrera = tk.Entry(frame, width=25)
        self.carrera.grid(row=0, column=3)
        # Materia
        tk.Label(frame, text="Materia").grid(row=1,column=0,padx=5,pady=5)
        self.materia = tk.Entry(frame, width=25)
        self.materia.grid(row=1, column=1)
        # Horario
        tk.Label(frame, text="Horario").grid(row=1,column=2,padx=5,pady=5)
        self.horario = ttk.Combobox(frame,values=["Mañana", "Tarde", "Noche"],state="readonly",width=22)
        self.horario.grid(row=1, column=3)
        # WhatsApp
        tk.Label(frame, text="WhatsApp").grid(row=2,column=0,padx=5,pady=5)
        self.whatsapp = tk.Entry(frame, width=25)
        self.whatsapp.grid(row=2, column=1)
        # Botones
        tk.Button(frame,text="Registrar",bg="#2E86C1",fg="white",width=15,command=self.registrar).grid(row=3, column=0, pady=10)
        tk.Button(frame,text="Buscar Carrera",bg="#17A589",fg="white",width=15,command=self.buscar_carrera).grid(row=3, column=1)
        tk.Button(frame,text="Buscar Materia",bg="#AF7AC5",fg="white",width=15,command=self.buscar_materia).grid(row=3, column=2)
        tk.Button(frame,text="Mostrar Todos",bg="#5D6D7E",fg="white",width=15,command=self.mostrar_todos).grid(row=3, column=3)
        tk.Button(frame,text="Eliminar",bg="#C0392B",fg="white",width=15,command=self.eliminar_estudiante).grid(row=3, column=4)
        # Tabla
        self.tabla = ttk.Treeview( root, columns=("Nombre","Carrera","Materia","Horario","WhatsApp"),show="headings" )
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Carrera", text="Carrera")
        self.tabla.heading("Materia", text="Materia")
        self.tabla.heading("Horario", text="Horario")
        self.tabla.heading("WhatsApp", text="WhatsApp")

        self.tabla.column("Nombre", width=180)
        self.tabla.column("Carrera", width=180)
        self.tabla.column("Materia", width=180)
        self.tabla.column("Horario", width=120)
        self.tabla.column("WhatsApp", width=180)
        self.tabla.pack(fill="both",expand=True,padx=10,pady=10)
        self.cargar_datos()
    def actualizar_contador(self):self.lbl_contador.config(text=f"Estudiantes registrados: {len(self.estudiantes)}" )
    def guardar_datos(self):
        datos = []
        for estudiante in self.estudiantes:
            datos.append({"nombre": estudiante.nombre,"carrera": estudiante.carrera,"materia": estudiante.materia,"horario": estudiante.horario,"whatsapp": estudiante.whatsapp })
        with open("estudiantes.json","w",encoding="utf-8" ) as archivo: json.dump(datos,archivo,ensure_ascii=False,indent=4)
    def cargar_datos(self):
        if not os.path.exists("estudiantes.json"):
            return
        with open("estudiantes.json","r",encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for e in datos:
                estudiante = Estudiante(e["nombre"],e["carrera"],e["materia"],e["horario"],e["whatsapp"])
                self.estudiantes.append(estudiante)
                self.tabla.insert("","end",values=(estudiante.nombre,estudiante.carrera,estudiante.materia,estudiante.horario,estudiante.whatsapp ))
        self.actualizar_contador()
    def registrar(self):
        nombre = self.nombre.get().strip()
        carrera = self.carrera.get().strip()
        materia = self.materia.get().strip()
        horario = self.horario.get().strip()
        whatsapp = self.whatsapp.get().strip()
        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error","El nombre solo debe contener letras.")
            return
        if not carrera.replace(" ", "").isalpha():
            messagebox.showerror("Error","La carrera solo debe contener letras.")
            return
        if not materia.replace(" ", "").isalpha():
            messagebox.showerror("Error","La materia solo debe contener letras.")
            return
        if horario not in ["Mañana", "Tarde", "Noche"]:
            messagebox.showerror("Error","Seleccione un horario válido.")
            return
        if not whatsapp.isdigit():
            messagebox.showerror("Error","WhatsApp solo debe contener números.")
            return
        estudiante = Estudiante(nombre,carrera,materia,horario,whatsapp)
        self.estudiantes.append(estudiante)
        self.tabla.insert("","end", values=(nombre,carrera,materia,horario,whatsapp))
        self.guardar_datos()
        self.actualizar_contador()
        messagebox.showinfo("Correcto","Estudiante registrado correctamente." )
        self.limpiar()
    def eliminar_estudiante(self):
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Aviso","Seleccione un estudiante.")
            return
        item = seleccionado[0]
        valores = self.tabla.item(item)["values"]
        nombre = valores[0]
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                self.estudiantes.remove(estudiante)
                break
        self.tabla.delete(item)
        self.guardar_datos()
        self.actualizar_contador()
        messagebox.showinfo("Correcto","Estudiante eliminado.")
    def limpiar(self):
        self.nombre.delete(0, tk.END)
        self.carrera.delete(0, tk.END)
        self.materia.delete(0, tk.END)
        self.whatsapp.delete(0, tk.END)
        self.horario.set("")
    def mostrar_todos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for estudiante in self.estudiantes:
            self.tabla.insert("","end",values=(estudiante.nombre,estudiante.carrera,estudiante.materia,estudiante.horario,estudiante.whatsapp))
    def buscar_carrera(self):
        carrera = self.carrera.get().strip()
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        encontrados = False
        for estudiante in self.estudiantes:
            if estudiante.carrera.lower() == carrera.lower():
                self.tabla.insert("","end",values=(estudiante.nombre,estudiante.carrera,estudiante.materia,estudiante.horario,estudiante.whatsapp))
                encontrados = True
        if not encontrados:
            messagebox.showinfo("Búsqueda","No se encontraron compañeros.")
    def buscar_materia(self):
        materia = self.materia.get().strip()
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        encontrados = False
        for estudiante in self.estudiantes:
            if estudiante.materia.lower() == materia.lower():
                self.tabla.insert("","end",values=(estudiante.nombre,estudiante.carrera,estudiante.materia,estudiante.horario,estudiante.whatsapp))
                encontrados = True
        if not encontrados:
            messagebox.showinfo("Búsqueda","No se encontraron compañeros.")
root = tk.Tk()
app = ConectaU(root)
root.mainloop()