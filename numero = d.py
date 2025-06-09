import tkinter as tk
from tkinter import messagebox
import os

# Paleta de colores y texturas
BG_COLOR = "#7A7A7A"
BTN_COLOR = "#353535"
BTN_HOVER = "#2B2B2B"
ENTRY_BG = "#121629"
ENTRY_FG = "#fffffe"
TEXT_COLOR = "#FAFFED"
RESULT_BG = "#1d3546"
CARD_BG = "#284b63"
SHADOW = "#474747"
SEPARATOR = "#4b7794"
ACCENT = "#FAFFED"

USUARIOS_FILE = "usuarios.txt"
usuarios = {}

def cargar_usuarios():
    if os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if "|" in line:
                    usuario, contraseña = line.strip().split("|", 1)
                    usuarios[usuario] = contraseña

def guardar_usuarios():
    with open(USUARIOS_FILE, "w", encoding="utf-8") as f:
        f.write("Usuario|Contraseña\n")
        for usuario, contraseña in usuarios.items():
            f.write(f"{usuario}|{contraseña}\n")

class ModernApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contador de Caracteres")
        self.geometry("500x500")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        self.usuario_actual = None
        cargar_usuarios()
        self.inicio()

    def _clear(self):
        for widget in self.winfo_children():
            widget.destroy()


    def inicio(self):
            self._clear()
            shadow = tk.Frame(self, bg=SHADOW)
            shadow.place(relx=0.5, rely=0.16, anchor="n", width=440, height=285)
            card = tk.Frame(self, bg=CARD_BG, bd=0, highlightthickness=2, highlightbackground=SEPARATOR)
            card.place(relx=0.5, rely=0.18, anchor="n", width=420, height=260)

            tk.Label(card, text="Contador de Caracteres", font=("Segoe UI", 24, "bold"), fg=ACCENT, bg=CARD_BG).pack(pady=(30, 10))
            tk.Frame(card, bg=SEPARATOR, height=2).pack(fill="x", padx=30, pady=(0, 20))
            tk.Label(
                card,
                text="Sistema experimental enfocado en contar la cantidad de caracteres de una frase",
                font=("Segoe UI", 14),
                fg=TEXT_COLOR,
                bg=CARD_BG,
                wraplength=360,
                justify="center"
            ).pack(pady=(0, 20))
            

            btn_frame = tk.Frame(card, bg=CARD_BG)
            btn_frame.pack(pady=10)
            self._modern_button(btn_frame, "Continuar", self._build_login_register).pack(fill="x", pady=(0, 10))
        


    def _build_login_register(self):
        self._clear()
        shadow = tk.Frame(self, bg=SHADOW)
        shadow.place(relx=0.5, rely=0.16, anchor="n", width=420, height=260 + 25)
        card = tk.Frame(self, bg=CARD_BG, bd=0, highlightthickness=2, highlightbackground=SEPARATOR)
        card.place(relx=0.5, rely=0.18, anchor="n", width=400, height=260)

        tk.Label(card, text="Bienvenido", font=("Segoe UI", 24, "bold"), fg=ACCENT, bg=CARD_BG).pack(pady=(30, 10))
        tk.Frame(card, bg=SEPARATOR, height=2).pack(fill="x", padx=30, pady=(0, 20))

        btn_frame = tk.Frame(card, bg=CARD_BG)
        btn_frame.pack(pady=10)
        self._modern_button(btn_frame, "Iniciar Sesión", self._login_window).pack(fill="x", pady=(0, 10))
        self._modern_button(btn_frame, "Registrar", self._register_window).pack(fill="x")

    def _register_window(self):
        self._clear()
        shadow = tk.Frame(self, bg=SHADOW)
        shadow.place(relx=0.5, rely=0.11, anchor="n", width=420, height=340 + 15)
        card = tk.Frame(self, bg=CARD_BG, bd=0, highlightthickness=2, highlightbackground=SEPARATOR)
        card.place(relx=0.5, rely=0.13, anchor="n", width=400, height=330)

        # Botón flecha volver arriba
        self._arrow_button(card, self._build_login_register).place(x=10, y=10)

        tk.Label(card, text="Registro", font=("Segoe UI", 20, "bold"), fg=ACCENT, bg=CARD_BG).pack(pady=(25, 10))
        tk.Frame(card, bg=SEPARATOR, height=2).pack(fill="x", padx=30, pady=(0, 15))

        user_var = tk.StringVar()
        pass_var = tk.StringVar()
        msg_var = tk.StringVar()

        self._modern_entry(card, "Usuario", user_var).pack(pady=10)
        self._modern_entry(card, "Contraseña", pass_var, show="*").pack(pady=10)

        def registrar():
            usuario = user_var.get().strip()
            contraseña = pass_var.get()
            if not usuario or not contraseña or usuario == "Usuario" or contraseña == "Contraseña":
                msg_var.set("Debe completar ambos campos.")
                self.after(2500, lambda: msg_var.set(""))
                return
            if usuario in usuarios:
                msg_var.set("El usuario ya existe.")
                self.after(2500, lambda: msg_var.set(""))
                return
            usuarios[usuario] = contraseña
            guardar_usuarios()
            self.usuario_actual = usuario
            msg_var.set("¡Registrado exitosamente!")
            self.after(700, self._main_app)

        self._modern_button(card, "Registrar", registrar).pack(pady=15)
        tk.Label(card, textvariable=msg_var, font=("Segoe UI", 11), fg=ACCENT, bg=CARD_BG).pack()
        # Botón volver abajo (opcional, puedes quitarlo si solo quieres la flecha)
        # self._modern_button(card, "Volver", self._build_login_register).pack(pady=5)

    def _login_window(self):
        self._clear()
        shadow = tk.Frame(self, bg=SHADOW)
        shadow.place(relx=0.5, rely=0.11, anchor="n", width=420, height=340 + 15)
        card = tk.Frame(self, bg=CARD_BG, bd=0, highlightthickness=2, highlightbackground=SEPARATOR)
        card.place(relx=0.5, rely=0.13, anchor="n", width=400, height=330)

        # Botón flecha volver arriba
        self._arrow_button(card, self._build_login_register).place(x=10, y=10)

        tk.Label(card, text="Inicio de Sesión", font=("Segoe UI", 20, "bold"), fg=ACCENT, bg=CARD_BG).pack(pady=(25, 10))
        tk.Frame(card, bg=SEPARATOR, height=2).pack(fill="x", padx=30, pady=(0, 15))

        user_var = tk.StringVar()
        pass_var = tk.StringVar()
        msg_var = tk.StringVar()

        self._modern_entry(card, "Usuario", user_var).pack(pady=10)
        self._modern_entry(card, "Contraseña", pass_var, show="*").pack(pady=10)

        def iniciar():
            usuario = user_var.get().strip()
            contraseña = pass_var.get()
            if not usuario or usuario not in usuarios or usuario == "Usuario":
                msg_var.set("Usuario no encontrado.")
                self.after(2500, lambda: msg_var.set(""))
                return
            if usuarios[usuario] != contraseña:
                msg_var.set("Contraseña incorrecta.")
                self.after(2500, lambda: msg_var.set(""))
                return
            self.usuario_actual = usuario
            self._main_app()

        self._modern_button(card, "Iniciar Sesión", iniciar).pack(pady=15)
        tk.Label(card, textvariable=msg_var, font=("Segoe UI", 11), fg=ACCENT, bg=CARD_BG).pack()
        # Botón volver abajo (opcional, puedes quitarlo si solo quieres la flecha)
        # self._modern_button(card, "Volver", self._build_login_register).pack(pady=5)

    def _main_app(self):
        self._clear()
        
        # Crear un contorno alrededor de 'card' usando un Frame con borde visible
        # Ajustar la posición vertical para que no se corte arriba
        shadow = tk.Frame(self, bg=SHADOW)
        shadow.place(relx=0.5, rely=0.11, anchor="n", width=440, height=495)

        card = tk.Frame(self, bg=CARD_BG, bd=0, highlightthickness=2, highlightbackground=SEPARATOR)
        card.place(relx=0.5, rely=0.13, anchor="n", width=420, height=470)


        tk.Label(card, text=f"Bienvenido, {self.usuario_actual}", font=("Segoe UI", 18, "bold"), fg=ACCENT, bg=CARD_BG).pack(pady=(25, 10))
        tk.Frame(card, bg=SEPARATOR, height=2).pack(fill="x", padx=30, pady=(0, 15))
        tk.Label(card, text="Digite una frase:", font=("Segoe UI", 14), fg=TEXT_COLOR, bg=CARD_BG).pack(pady=10)

        entry_var = tk.StringVar()
        entry = tk.Entry(card, textvariable=entry_var, font=("Segoe UI", 14), bg=ENTRY_BG, fg=ENTRY_FG, bd=0, relief="flat", highlightthickness=2, highlightbackground=BTN_COLOR, insertbackground=ENTRY_FG)
        entry.pack(ipady=8, ipadx=8, pady=10, padx=40, fill="x")

        resultado = tk.Label(card, text="", font=("Segoe UI", 14), fg=TEXT_COLOR, bg=RESULT_BG, bd=0, relief="flat")
        resultado.pack(pady=20, ipadx=10, ipady=10)

        def contar_caracteres():
            frase = entry_var.get()
            ncaracteres = sum(1 for letra in frase if letra != " ")
            resultado.config(text=f"La frase tiene {ncaracteres} caracteres (sin contar espacios).")

        self._modern_button(card, "Contar caracteres", contar_caracteres).pack(pady=10)
        self._modern_button(card, "Cerrar sesión", self._build_login_register).pack(pady=5)

    def _modern_button(self, parent, text, command):
        btn = tk.Button(parent, text=text, font=("Segoe UI", 12, "bold"), fg=ACCENT, bg=BTN_COLOR,
                        activebackground=BTN_HOVER, activeforeground=BG_COLOR, bd=0, relief="flat",
                        command=command, cursor="hand2")
        btn.configure(highlightthickness=0)
        btn.pack_propagate(False)
        btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BTN_COLOR))
        btn.config(height=2, width=18)
        btn.config(borderwidth=0, highlightbackground=BTN_COLOR)
        return btn

    def _arrow_button(self, parent, command):
        btn = tk.Button(parent, text="🡸", font=("Segoe UI", 15, "bold"), fg=ACCENT, bg=BTN_COLOR,
                        activebackground=BTN_HOVER, activeforeground=BG_COLOR, bd=0, relief="flat",
                        command=command, cursor="hand2", width=2, height=1)
        btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BTN_COLOR))
        return btn

    def _modern_entry(self, parent, placeholder, textvar, show=None):
        frame = tk.Frame(parent, bg=CARD_BG)
        entry = tk.Entry(frame, textvariable=textvar, font=("Segoe UI", 12), bg=ENTRY_BG, fg=ENTRY_FG,
                         bd=0, relief="flat", insertbackground=ENTRY_FG, show=show)
        entry.pack(ipady=8, ipadx=8, fill="x")
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e: self._clear_placeholder(entry, placeholder))
        entry.bind("<FocusOut>", lambda e: self._add_placeholder(entry, placeholder))
        return frame

    def _clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=ENTRY_FG, show=entry.cget("show") if entry.cget("show") else "")

    def _add_placeholder(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg="#888", show="")

if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()