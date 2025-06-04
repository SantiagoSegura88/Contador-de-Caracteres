import tkinter as tk
from tkinter import messagebox

# Paleta de colores y texturas
BG_COLOR = "#232946"
BTN_COLOR = "#eebbc3"
BTN_HOVER = "#d4939d"
ENTRY_BG = "#121629"
ENTRY_FG = "#fffffe"
TEXT_COLOR = "#b8c1ec"
RESULT_BG = "#393e60"
CARD_BG = "#2a2d43"
SHADOW = "#181a2b"
SEPARATOR = "#44476a"
ACCENT = "#f6c177"

usuarios = {}

class ModernApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contador de Caracteres")
        self.geometry("600x600")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        self.usuario_actual = None
        self._build_login_register()

    def _clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def _build_login_register(self):
        self._clear()
        # Sombra y tarjeta principal
        shadow = tk.Frame(self, bg=SHADOW)
        shadow.place(relx=0.5, rely=0.18, anchor="n", width=410, height=260)
        card = tk.Frame(self, bg=CARD_BG, bd=0, highlightthickness=2, highlightbackground=SEPARATOR)
        card.place(relx=0.5, rely=0.16, anchor="n", width=400, height=250)

        tk.Label(card, text="Bienvenido", font=("Segoe UI", 24, "bold"), fg=ACCENT, bg=CARD_BG).pack(pady=(30, 10))
        tk.Frame(card, bg=SEPARATOR, height=2).pack(fill="x", padx=30, pady=(0, 20))

        btn_frame = tk.Frame(card, bg=CARD_BG)
        btn_frame.pack(pady=10)
        self._modern_button(btn_frame, "Iniciar Sesión", self._login_window).pack(side="left", padx=20)
        self._modern_button(btn_frame, "Registrar", self._register_window).pack(side="left", padx=20)

    def _register_window(self):
        self._clear()
        shadow = tk.Frame(self, bg=SHADOW)
        shadow.place(relx=0.5, rely=0.13, anchor="n", width=410, height=340)
        card = tk.Frame(self, bg=CARD_BG, bd=0, highlightthickness=2, highlightbackground=SEPARATOR)
        card.place(relx=0.5, rely=0.11, anchor="n", width=400, height=330)

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
            if not usuario or not contraseña:
                msg_var.set("Debe completar ambos campos.")
                self.after(2500, lambda: msg_var.set(""))
                return
            if usuario in usuarios:
                msg_var.set("El usuario ya existe.")
                self.after(2500, lambda: msg_var.set(""))
                return
            usuarios[usuario] = contraseña
            self.usuario_actual = usuario
            msg_var.set("¡Registrado exitosamente!")
            self.after(1200, self._main_app)

        self._modern_button(card, "Registrar", registrar).pack(pady=15)
        tk.Label(card, textvariable=msg_var, font=("Segoe UI", 11), fg=ACCENT, bg=CARD_BG).pack()
        self._modern_button(card, "Volver", self._build_login_register).pack(pady=5)

    def _login_window(self):
        self._clear()
        shadow = tk.Frame(self, bg=SHADOW)
        shadow.place(relx=0.5, rely=0.13, anchor="n", width=410, height=340)
        card = tk.Frame(self, bg=CARD_BG, bd=0, highlightthickness=2, highlightbackground=SEPARATOR)
        card.place(relx=0.5, rely=0.11, anchor="n", width=400, height=330)

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
            if not usuario or usuario not in usuarios:
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
        self._modern_button(card, "Volver", self._build_login_register).pack(pady=5)

    def _main_app(self):
        self._clear()
        # Fondo con textura (líneas horizontales)
        for y in range(0, 600, 40):
            tk.Frame(self, bg=SEPARATOR, height=1, width=600).place(x=0, y=y)
        shadow = tk.Frame(self, bg=SHADOW)
        shadow.place(relx=0.5, rely=0.13, anchor="n", width=430, height=340)
        card = tk.Frame(self, bg=CARD_BG, bd=0, highlightthickness=2, highlightbackground=SEPARATOR)
        card.place(relx=0.5, rely=0.11, anchor="n", width=420, height=330)

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
        btn = tk.Button(parent, text=text, font=("Segoe UI", 12, "bold"), fg=BG_COLOR, bg=BTN_COLOR,
                        activebackground=BTN_HOVER, activeforeground=BG_COLOR, bd=0, relief="flat",
                        command=command, cursor="hand2")
        btn.configure(highlightthickness=0)
        btn.pack_propagate(False)
        btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BTN_COLOR))
        btn.config(height=2, width=18)
        btn.config(borderwidth=0, highlightbackground=BTN_COLOR)
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
