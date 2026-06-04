import tkinter as tk
import math
import MedicalCalculator







# PALETTE

BG      = "#0D0F14"
PANEL   = "#161A22"
BORDER  = "#252B38"
ACCENT  = "#00E5B0"
ACCENT2 = "#007AFF"
TEXT_HI = "#E8EDF5"
TEXT_LO = "#5A6478"
SUCCESS = "#00C97A"
WARNING = "#FFB830"
DANGER  = "#FF4560"






# WIDGETS

def _entry(parent, textvariable=None):
    return tk.Entry(
        parent,
        textvariable=textvariable,
        bg=PANEL, fg=TEXT_HI,
        insertbackground=ACCENT,
        relief="flat",
        font=("Courier New", 14),
        highlightthickness=1,
        highlightbackground=BORDER,
        highlightcolor=ACCENT,
    )

def _label(parent, text, size=10, color=TEXT_LO, bold=False):
    return tk.Label(
        parent, text=text,
        bg=parent.cget("bg"), fg=color,
        font=("Courier New", size, "bold" if bold else "normal"),
        anchor="w",
    )

def _button(parent, text, command):
    btn = tk.Button(
        parent, text=text, command=command,
        bg=ACCENT, fg=BG,
        activebackground=TEXT_HI, activeforeground=BG,
        relief="flat",
        font=("Courier New", 13, "bold"),
        cursor="hand2", padx=20, pady=10, bd=0,
    )
    btn.bind("<Enter>", lambda e: btn.config(bg=TEXT_HI))
    btn.bind("<Leave>", lambda e: btn.config(bg=ACCENT))
    return btn

def _card(parent):
    return tk.Frame(parent, bg=PANEL, padx=24, pady=20)

def _divider(parent):
    return tk.Frame(parent, bg=BORDER, height=1)

def _result_box(parent):
    box = tk.Text(
        parent,
        bg="#0A0C10", fg=ACCENT,
        font=("Courier New", 12),
        relief="flat", state="disabled",
        wrap="word", height=5,
        padx=14, pady=10,
        highlightthickness=1,
        highlightbackground=BORDER,
        cursor="arrow",
    )
    return box

def _set_result(box, text, color=ACCENT):
    box.config(state="normal")
    box.delete("1.0", "end")
    box.tag_configure("r", foreground=color)
    box.insert("end", text, "r")
    box.config(state="disabled")

def _back_button(parent, callback):
    btn = tk.Button(
        parent, text="← Back", command=callback,
        bg=BG, fg=TEXT_LO,
        activebackground=BG, activeforeground=ACCENT,
        relief="flat", font=("Courier New", 11),
        cursor="hand2", bd=0, pady=6,
    )
    btn.pack(anchor="w", padx=48, pady=(20, 0))

def _page_header(parent, icon, title, subtitle):
    tk.Label(parent, text=icon,     bg=BG, fg=ACCENT,   font=("Courier New", 36, "bold")).pack(pady=(8, 0))
    tk.Label(parent, text=title,    bg=BG, fg=TEXT_HI,  font=("Courier New", 20, "bold")).pack()
    tk.Label(parent, text=subtitle, bg=BG, fg=TEXT_LO,  font=("Courier New", 10)).pack(pady=(2, 20))
    _divider(parent).pack(fill="x", padx=48, pady=(0, 20))





# BASE PAGE

class Page(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG)




# HOME PAGE


class HomePage(Page):
    def __init__(self, parent, show_page_cb):
        super().__init__(parent)
        self._show = show_page_cb
        self._build()

    def _build(self):
        tk.Frame(self, bg=BG, height=40).pack()

        header = tk.Frame(self, bg=BG)
        header.pack(fill="x", padx=48)
        tk.Label(header, text="✚",                              bg=BG, fg=ACCENT,  font=("Courier New", 48, "bold")).pack()
        tk.Label(header, text="MEDICAL CALCULATOR",             bg=BG, fg=TEXT_HI, font=("Courier New", 22, "bold")).pack(pady=(4, 0))
        tk.Label(header, text="clinical health metrics · at a glance", bg=BG, fg=TEXT_LO, font=("Courier New", 11)).pack(pady=(2, 32))

        _divider(self).pack(fill="x", padx=48, pady=(0, 32))

        for code, title, sub, key in [
            ("01", "BMI Calculator",          "Body Mass Index from height & weight", "bmi"),
            ("02", "Blood Pressure",          "Mean Arterial Pressure from readings",  "bp"),
            ("03", "Cardiovascular Fitness",  "VO₂ Max from distance, age & gender",   "cardio"),
        ]:
            self._tile(code, title, sub, key)

    def _tile(self, code, title, subtitle, key):
        outer = tk.Frame(self, bg=BG, padx=48)
        outer.pack(fill="x", pady=6)

        card = tk.Frame(outer, bg=PANEL, padx=24, pady=18, cursor="hand2")
        card.pack(fill="x")

        bar = tk.Frame(card, bg=ACCENT, width=3)
        bar.pack(side="left", fill="y", padx=(0, 16))

        tk.Label(card, text=code, bg=PANEL, fg=TEXT_LO, font=("Courier New", 10)).pack(side="left", anchor="n", pady=(2, 0))

        txt = tk.Frame(card, bg=PANEL)
        txt.pack(side="left", fill="x", expand=True, padx=12)
        tk.Label(txt, text=title,    bg=PANEL, fg=TEXT_HI, font=("Courier New", 15, "bold"), anchor="w").pack(fill="x")
        tk.Label(txt, text=subtitle, bg=PANEL, fg=TEXT_LO, font=("Courier New", 10),         anchor="w").pack(fill="x")

        tk.Label(card, text="→", bg=PANEL, fg=ACCENT, font=("Courier New", 18, "bold")).pack(side="right")

        def _click(e, k=key): self._show(k)
        def _enter(e, c=card, b=bar):
            c.config(bg="#1E2430")
            for w in c.winfo_children():
                try: w.config(bg="#1E2430")
                except: pass
            b.config(bg=TEXT_HI)
        def _leave(e, c=card, b=bar):
            c.config(bg=PANEL)
            for w in c.winfo_children():
                try: w.config(bg=PANEL)
                except: pass
            b.config(bg=ACCENT)

        for w in [card, bar, txt] + list(card.winfo_children()) + list(txt.winfo_children()):
            w.bind("<Button-1>", _click)
        card.bind("<Enter>", _enter)
        card.bind("<Leave>", _leave)



# BMI PAGE


class BMIPage(Page):
    def __init__(self, parent, show_page_cb):
        super().__init__(parent)
        self._show = show_page_cb
        self._build()

    def _build(self):
        _back_button(self, lambda: self._show("home"))
        _page_header(self, "⚖", "BMI CALCULATOR", "body mass index")

        card = _card(self)
        card.pack(fill="x", padx=48, pady=(0, 16))

        _label(card, "HEIGHT  (metres, e.g. 1.75)").grid(row=0, column=0, sticky="w", pady=(0, 4))
        self.height_var = tk.StringVar()
        _entry(card, self.height_var).grid(row=1, column=0, sticky="ew", ipady=6, pady=(0, 16))

        _label(card, "WEIGHT  (kilograms)").grid(row=2, column=0, sticky="w", pady=(0, 4))
        self.weight_var = tk.StringVar()
        _entry(card, self.weight_var).grid(row=3, column=0, sticky="ew", ipady=6, pady=(0, 20))

        card.columnconfigure(0, weight=1)
        _button(card, "CALCULATE BMI", self._on_calculate).grid(row=4, column=0, sticky="ew", ipady=4)

        self.result_box = _result_box(self)
        self.result_box.pack(fill="x", padx=48, pady=(8, 0))

        self.gauge = tk.Canvas(self, bg=BG, height=70, highlightthickness=0)
        self.gauge.pack(fill="x", padx=48, pady=(12, 0))
        self.after(100, self._draw_gauge)

    def _draw_gauge(self, bmi=None):
        c = self.gauge
        c.delete("all")
        W = c.winfo_width() or 520
        zones = [(10, 18.5, "#4FC3F7"), (18.5, 25, SUCCESS), (25, 30, WARNING), (30, 45, DANGER)]
        mn, mx = 10, 45
        tw = W - 40
        def xv(v): return 20 + (v - mn) / (mx - mn) * tw
        for lo, hi, col in zones:
            c.create_rectangle(xv(lo), 28, xv(hi), 44, fill=col, outline="")
        for v, lbl in [(18.5, "18.5"), (25, "25"), (30, "30")]:
            c.create_line(xv(v), 22, xv(v), 50, fill=BORDER)
            c.create_text(xv(v), 58, text=lbl, fill=TEXT_LO, font=("Courier New", 8))
        if bmi is not None:
            px = xv(min(max(bmi, mn), mx))
            c.create_polygon(px, 22, px - 7, 12, px + 7, 12, fill=ACCENT)
            c.create_text(px, 7, text=str(bmi), fill=ACCENT, font=("Courier New", 9, "bold"))

    def _on_calculate(self):
        try:
            height = float(self.height_var.get())
            weight = float(self.weight_var.get())
        except ValueError:
            _set_result(self.result_box, "⚠  Please enter valid numbers.", DANGER)
            return

        # Call your backend file
        bmi, category, advice = MedicalCalculator.BMICalculator(height, weight)
        
        # Match up UI design colors
        if category == "Normalweight":
            colour = SUCCESS
        elif category in ["Underweight", "Overweight"]:
            colour = WARNING
        else:
            colour = DANGER
        
        # Output results directly to the UI elements
        _set_result(self.result_box, f"BMI: {bmi} ({category})\n\n{advice}", colour)
        self.after(50, lambda: self._draw_gauge(bmi))

# BLOOD PRESSURE PAGE

class BPPage(Page):
    def __init__(self, parent, show_page_cb):
        super().__init__(parent)
        self._show = show_page_cb
        self._anim = False
        self._step = 0
        self._build()

    def _build(self):
        _back_button(self, lambda: self._show("home"))
        _page_header(self, "❤", "BLOOD PRESSURE", "mean arterial pressure")

        card = _card(self)
        card.pack(fill="x", padx=48, pady=(0, 16))

        _label(card, "SYSTOLIC  (mmHg)").grid(row=0, column=0, sticky="w", pady=(0, 4))
        self.sys_var = tk.StringVar()
        _entry(card, self.sys_var).grid(row=1, column=0, sticky="ew", ipady=6, pady=(0, 16))

        _label(card, "DIASTOLIC  (mmHg)").grid(row=2, column=0, sticky="w", pady=(0, 4))
        self.dia_var = tk.StringVar()
        _entry(card, self.dia_var).grid(row=3, column=0, sticky="ew", ipady=6, pady=(0, 20))

        card.columnconfigure(0, weight=1)
        _button(card, "CALCULATE MAP", self._on_calculate).grid(row=4, column=0, sticky="ew", ipady=4)

        self.result_box = _result_box(self)
        self.result_box.pack(fill="x", padx=48, pady=(8, 0))

        self.pulse_canvas = tk.Canvas(self, bg=BG, height=60, highlightthickness=0)
        self.pulse_canvas.pack(fill="x", padx=48, pady=(12, 0))

    def _animate_pulse(self):
        if not self._anim:
            return
        c = self.pulse_canvas
        c.delete("all")
        W = c.winfo_width() or 520
        pts = []
        for i in range(120):
            x = i / 120 * W
            phase = (i + self._step * 3) % 120
            y = 30 - 26 * math.exp(-0.05 * (phase - 40) ** 2) * math.sin(math.pi * (phase - 30) / 20) if 30 < phase < 50 else 30
            pts.extend([x, y])
        if len(pts) >= 4:
            c.create_line(pts, fill=ACCENT, width=2, smooth=True)
        self._step += 1
        self.after(40, self._animate_pulse)

    def _on_calculate(self):
        try:
            systolic  = int(self.sys_var.get())
            diastolic = int(self.dia_var.get())
        except ValueError:
            _set_result(self.result_box, "⚠  Please enter valid integers.", DANGER)
            return

        # Call your backend file
        map_value, status, advice = MedicalCalculator.BloodPressureCalculator(systolic, diastolic)
        
        if status == "Normal":
            colour = SUCCESS
        elif status == "High":
            colour = WARNING
        else:
            colour = DANGER
            
        _set_result(self.result_box, f"Mean Arterial Pressure: {map_value} mmHg\nStatus: {status}\n\n{advice}", colour)

        
        self._anim = True
        self._animate_pulse()
        self.after(4000, lambda: setattr(self, "_anim", False))

# CARDIOVASCULAR PAGE

class CardioPage(Page):
    def __init__(self, parent, show_page_cb):
        super().__init__(parent)
        self._show = show_page_cb
        self._build()

    def _build(self):
        _back_button(self, lambda: self._show("home"))
        _page_header(self, "🏃", "CARDIOVASCULAR", "VO₂ max fitness rating")

        card = _card(self)
        card.pack(fill="x", padx=48, pady=(0, 16))

        _label(card, "DISTANCE RAN  (metres)").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 4))
        self.dist_var = tk.StringVar()
        _entry(card, self.dist_var).grid(row=1, column=0, columnspan=2, sticky="ew", ipady=6, pady=(0, 16))

        _label(card, "GENDER").grid(row=2, column=0, sticky="w", pady=(0, 4))
        _label(card, "AGE").grid(row=2, column=1, sticky="w", padx=(16, 0), pady=(0, 4))

        self.gender_var = tk.StringVar(value="M")
        gf = tk.Frame(card, bg=PANEL)
        gf.grid(row=3, column=0, sticky="w", pady=(0, 16))
        for val, lbl in [("M", "Male"), ("F", "Female")]:
            rb = tk.Radiobutton(
                gf, text=lbl, variable=self.gender_var, value=val,
                bg=PANEL, fg=TEXT_HI, selectcolor=BG,
                activebackground=PANEL, activeforeground=ACCENT,
                font=("Courier New", 12),
                indicatoron=0, relief="flat",
                padx=14, pady=6, cursor="hand2",
            )
            rb.pack(side="left", padx=(0, 8))

        self.age_var = tk.StringVar(value="25")
        _entry(card, self.age_var).grid(row=3, column=1, sticky="ew", ipady=6, padx=(16, 0), pady=(0, 16))

        card.columnconfigure(0, weight=1)
        card.columnconfigure(1, weight=1)
        _button(card, "CALCULATE VO₂ MAX", self._on_calculate).grid(row=4, column=0, columnspan=2, sticky="ew", ipady=4)

        self.result_box = _result_box(self)
        self.result_box.pack(fill="x", padx=48, pady=(8, 0))

        self.meter = tk.Canvas(self, bg=BG, height=80, highlightthickness=0)
        self.meter.pack(fill="x", padx=48, pady=(12, 0))
        self.after(100, self._draw_meter)

    def _draw_meter(self, category=None):
        c = self.meter
        c.delete("all")
        W = c.winfo_width() or 520
        zones = [("LOW", DANGER, 0), ("NORMAL", SUCCESS, 1), ("HIGH", ACCENT2, 2)]
        zw = (W - 40) / 3
        for lbl, col, idx in zones:
            x0 = 20 + idx * zw
            filled = category and lbl == category.upper()
            c.create_rectangle(x0, 26, x0 + zw - 4, 46, fill=col if filled else BORDER, outline="")
            c.create_text(x0 + zw / 2 - 2, 60, text=lbl, fill=col if filled else TEXT_LO,
                          font=("Courier New", 9, "bold" if filled else "normal"))
        if category:
            idx_map = {"LOW": 0, "NORMAL": 1, "HIGH": 2}
            idx = idx_map.get(category.upper(), 1)
            cx = 20 + (idx + 0.5) * zw
            c.create_polygon(cx, 20, cx - 7, 10, cx + 7, 10, fill=ACCENT)

    def _on_calculate(self):
        try:
            distance = float(self.dist_var.get())
            age      = int(self.age_var.get())
        except ValueError:
            _set_result(self.result_box, "⚠  Please enter valid values.", DANGER)
            return

        gender = self.gender_var.get()

        # Call your backend file
        vo2, category = MedicalCalculator.CardiovascularFitness(distance, gender, age)
        
        if category == "Normal":
            colour = SUCCESS
        elif category == "High":
            colour = ACCENT2
        else:
            colour = DANGER
            
        _set_result(self.result_box, f"VO₂ Max: {vo2} ml/kg/min\nFitness Level: {category.upper()}", colour)
        self.after(50, lambda: self._draw_meter(category))

# APP

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Calculator")
        self.configure(bg=BG)
        self.geometry("520x680")
        self.minsize(440, 560)

        x = (self.winfo_screenwidth()  - 520) // 2
        y = (self.winfo_screenheight() - 680) // 2
        self.geometry(f"520x680+{x}+{y}")

        container = tk.Frame(self, bg=BG)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self._pages = {}
        for name, cls in [
            ("home",   HomePage),
            ("bmi",    BMIPage),
            ("bp",     BPPage),
            ("cardio", CardioPage),
        ]:
            p = cls(container, self._show_page)
            self._pages[name] = p
            p.grid(row=0, column=0, sticky="nsew")

        self._show_page("home")

    def _show_page(self, name):
        self._pages[name].tkraise()

if __name__ == "__main__":
    App().mainloop()