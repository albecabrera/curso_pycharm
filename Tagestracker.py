import tkinter as tk
from tkinter import ttk
import datetime
import csv
import os
from tkcalendar import Calendar


class TagesTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Tages Tracker")
        self.root.geometry("1200x800")

        # Hauptdaten
        self.current_date = datetime.datetime.now()
        self.meals = {
            "morgens": "",
            "mittags": "",
            "abends": "",
            "snacks": ""
        }
        self.water_intake = 0
        self.workout_done = False
        self.sleep_hours = 0

        self.create_gui()
        self.load_data()

    def create_gui(self):
        # Hauptframe
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Tabs erstellen
        tab_control = ttk.Notebook(main_frame)

        # Tab 1: Täglicher Tracker
        daily_tab = ttk.Frame(tab_control)
        tab_control.add(daily_tab, text="Täglicher Tracker")

        # Tab 2: Ernährungsplan
        meal_tab = ttk.Frame(tab_control)
        tab_control.add(meal_tab, text="Ernährungsplan")

        # Tab 3: Aufgaben
        task_tab = ttk.Frame(tab_control)
        tab_control.add(task_tab, text="Meine Aufgaben")

        # Tab 4: Statistik
        stats_tab = ttk.Frame(tab_control)
        tab_control.add(stats_tab, text="Statistiken")

        tab_control.pack(fill=tk.BOTH, expand=True)

        # --- Tab 1: Täglicher Tracker ---
        # Datumsauswahl
        date_frame = ttk.LabelFrame(daily_tab, text="Datum", padding="10")
        date_frame.pack(fill=tk.X, padx=10, pady=5)

        self.cal = Calendar(date_frame, selectmode='day', date_pattern='dd.MM.yyyy')
        self.cal.pack(fill=tk.X)
        self.cal.bind("<<CalendarSelected>>", self.date_selected)

        # Mahlzeiten
        meal_frame = ttk.LabelFrame(daily_tab, text="Mahlzeiten", padding="10")
        meal_frame.pack(fill=tk.X, padx=10, pady=5)

        meals = ["morgens", "mittags", "abends", "snacks"]
        self.meal_entries = {}

        for i, meal in enumerate(meals):
            ttk.Label(meal_frame, text=f"{meal.capitalize()}:").grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            self.meal_entries[meal] = tk.Text(meal_frame, height=3, width=40)
            self.meal_entries[meal].grid(row=i, column=1, padx=5, pady=2)

        # Wasser
        water_frame = ttk.LabelFrame(daily_tab, text="Wasseraufnahme (ml)", padding="10")
        water_frame.pack(fill=tk.X, padx=10, pady=5)

        self.water_var = tk.StringVar(value="0")
        water_entry = ttk.Entry(water_frame, textvariable=self.water_var)
        water_entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(water_frame, text="+250ml", command=lambda: self.add_water(250)).pack(side=tk.LEFT, padx=2)
        ttk.Button(water_frame, text="+500ml", command=lambda: self.add_water(500)).pack(side=tk.LEFT, padx=2)

        # Workout
        workout_frame = ttk.LabelFrame(daily_tab, text="Workout", padding="10")
        workout_frame.pack(fill=tk.X, padx=10, pady=5)

        self.workout_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(workout_frame, text="Workout erledigt", variable=self.workout_var).pack(anchor=tk.W)

        # Schlaf
        sleep_frame = ttk.LabelFrame(daily_tab, text="Schlaf (Stunden)", padding="10")
        sleep_frame.pack(fill=tk.X, padx=10, pady=5)

        self.sleep_var = tk.StringVar(value="0")
        ttk.Spinbox(sleep_frame, from_=0, to=12, increment=0.5, textvariable=self.sleep_var).pack(fill=tk.X)

        # Speichern Button
        ttk.Button(daily_tab, text="Speichern", command=self.save_data).pack(pady=10)

        # --- Tab 2: Ernährungsplan ---
        # Wochenansicht für den Ernährungsplan
        for i in range(7):
            day = self.current_date + datetime.timedelta(days=i)
            day_name = day.strftime("%A")
            day_date = day.strftime("%d.%m.%Y")

            day_frame = ttk.LabelFrame(meal_tab, text=f"{day_name} - {day_date}", padding="10")
            day_frame.pack(fill=tk.X, padx=10, pady=5)

            for j, meal in enumerate(["morgens", "mittags", "abends", "snacks"]):
                ttk.Label(day_frame, text=f"{meal.capitalize()}:").grid(row=j, column=0, sticky=tk.W, padx=5, pady=2)
                meal_text = tk.Text(day_frame, height=2, width=40)
                meal_text.grid(row=j, column=1, padx=5, pady=2)

        # --- Tab 3: Aufgaben ---
        tasks = [
            "Tägliches Workout planen und durchführen (30-45 Minuten)",
            "Wochenmenü erstellen und Einkaufsliste vorbereiten",
            "Wasseraufnahme tracken (mindestens 2 Liter pro Tag)",
            "Schlafzeiten optimieren (7-8 Stunden pro Nacht)",
            "Wöchentliche Fortschritte dokumentieren und analysieren"
        ]

        self.task_vars = []

        for task in tasks:
            var = tk.BooleanVar(value=False)
            self.task_vars.append(var)
            ttk.Checkbutton(task_tab, text=task, variable=var).pack(anchor=tk.W, padx=10, pady=5)

        ttk.Button(task_tab, text="Aufgaben speichern", command=self.save_tasks).pack(pady=10)

        # --- Tab 4: Statistiken ---
        stats_frame = ttk.Frame(stats_tab, padding="10")
        stats_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(stats_frame, text="Wasseraufnahme der letzten Woche (ml)").pack(anchor=tk.W)

        # Einfaches Canvas für Statistik-Visualisierung
        self.stats_canvas = tk.Canvas(stats_frame, height=200, bg="white")
        self.stats_canvas.pack(fill=tk.X, pady=10)

        ttk.Button(stats_frame, text="Statistik aktualisieren", command=self.update_stats).pack()

    def date_selected(self, event=None):
        date_str = self.cal.get_date()
        selected_date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
        self.current_date = selected_date
        self.load_data()  # Daten für das ausgewählte Datum laden

    def add_water(self, amount):
        current = int(self.water_var.get() or 0)
        self.water_var.set(str(current + amount))

    def save_data(self):
        data = {
            "date": self.current_date.strftime("%Y-%m-%d"),
            "morgens": self.meal_entries["morgens"].get("1.0", tk.END).strip(),
            "mittags": self.meal_entries["mittags"].get("1.0", tk.END).strip(),
            "abends": self.meal_entries["abends"].get("1.0", tk.END).strip(),
            "snacks": self.meal_entries["snacks"].get("1.0", tk.END).strip(),
            "water": self.water_var.get(),
            "workout": "1" if self.workout_var.get() else "0",
            "sleep": self.sleep_var.get()
        }

        file_exists = os.path.isfile("tages_tracker.csv")

        with open("tages_tracker.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

        tk.messagebox.showinfo("Erfolg", f"Daten für {self.current_date.strftime('%d.%m.%Y')} gespeichert!")

    def load_data(self):
        if not os.path.isfile("tages_tracker.csv"):
            return

        date_str = self.current_date.strftime("%Y-%m-%d")

        with open("tages_tracker.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["date"] == date_str:
                    # Mahlzeiten
                    for meal in ["morgens", "mittags", "abends", "snacks"]:
                        self.meal_entries[meal].delete("1.0", tk.END)
                        self.meal_entries[meal].insert(tk.END, row[meal])

                    # Andere Werte
                    self.water_var.set(row["water"])
                    self.workout_var.set(row["workout"] == "1")
                    self.sleep_var.set(row["sleep"])
                    return

        # Wenn keine Daten gefunden wurden, Felder leeren
        for meal in self.meal_entries:
            self.meal_entries[meal].delete("1.0", tk.END)
        self.water_var.set("0")
        self.workout_var.set(False)
        self.sleep_var.set("0")

    def save_tasks(self):
        tasks = []
        for i, var in enumerate(self.task_vars):
            tasks.append("1" if var.get() else "0")

        with open("tasks.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(tasks)

        tk.messagebox.showinfo("Erfolg", "Aufgaben gespeichert!")

    def update_stats(self):
        # Einfache Statistikvisualisierung
        if not os.path.isfile("tages_tracker.csv"):
            return

        # Letzte 7 Tage
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=7)

        dates = []
        water_values = []

        with open("tages_tracker.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row_date = datetime.datetime.strptime(row["date"], "%Y-%m-%d")
                if start_date <= row_date <= end_date:
                    dates.append(row_date.strftime("%d.%m"))
                    water_values.append(int(row["water"] or 0))

        # Canvas löschen
        self.stats_canvas.delete("all")

        # Balkendiagramm zeichnen
        if water_values:
            max_value = max(water_values) if water_values else 1000
            width = self.stats_canvas.winfo_width() - 50
            bar_width = width / len(water_values) if water_values else 0
            scale_factor = 180 / max_value  # 180 für Canvas-Höhe

            for i, value in enumerate(water_values):
                x0 = 25 + i * bar_width
                y0 = 190 - value * scale_factor
                x1 = x0 + bar_width - 5
                y1 = 190

                self.stats_canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
                self.stats_canvas.create_text(x0 + bar_width / 2, y1 + 5, text=dates[i], anchor=tk.N)
                self.stats_canvas.create_text(x0 + bar_width / 2, y0 - 5, text=str(value), anchor=tk.S)


if __name__ == "__main__":
    root = tk.Tk()
    app = TagesTracker(root)
    root.mainloop()
