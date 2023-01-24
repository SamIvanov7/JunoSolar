from tkinter import *
from tkinter import messagebox

import customtkinter
import jinja2
import pdfkit

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("500x550")
app.title("Juno Solar Application")

jinko_solar = 1000
phono_solar = 2000
heckert_solar = 3000

battery_5_kwh = 1500
battery_10_kwh = 2500
battery_15_kwh = 3500


def op_1_callback(selection):
    print(selection)


def op_2_callback(selection):
    print(selection)


def pdf_create():

    vorname = entry_1.get()
    nachname = entry_2.get()
    strasse = entry_3.get()
    stadt = entry_4.get()
    modultyp = optionmenu_1.get()
    context = {
        "vorname": entry_1.get(),
        "nachname": nachname,
        "strasse": strasse,
        "stadt": stadt,
        "modultyp": modultyp,
        "jinko_solar": jinko_solar,
        "phono_solar": phono_solar,
        "heckert_solar": heckert_solar,
        "sum": sum,
    }
    print(sum)
    if not vorname:
        messagebox.showerror(title="Error", message="Please enter Vorname")

    if not nachname:
        messagebox.showerror(title="Error", message="Please enter Nachname")

    if not strasse:
        messagebox.showerror(title="Error", message="Please enter Strasse")

    if not stadt:
        messagebox.showerror(title="Error", message="Please enter Stadt")

    template_loader = jinja2.FileSystemLoader("./")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template("my-basic-html-template.html")
    output_text = template.render(context)

    pdfkit_config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    pdfkit.from_string(
        output_text, f"{vorname} {nachname}.pdf", configuration=pdfkit_config
    )


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=15, padx=40, fill="both", expand=True)

frame_2 = customtkinter.CTkFrame(master=app)
frame_2.pack(pady=15, padx=40, fill="both", expand=True)

frame_3 = customtkinter.CTkFrame(master=app)
frame_3.pack(pady=15, padx=40, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)


entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Vorname")
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Nachname")
entry_2.pack(pady=10, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Straße")
entry_3.pack(pady=10, padx=10)

entry_4 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Stadt")
entry_4.pack(pady=10, padx=10)

vorname = entry_1.get()
nachname = entry_2.get()
strasse = entry_3.get()
stadt = entry_4.get()

modultyp = ["Jinko Solar", "Phono Solar", "Heckert Solar"]

optionmenu_1 = customtkinter.CTkOptionMenu(
    frame_2,
    values=modultyp,
    command=op_1_callback,
)
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Modultyp")

batteriespeicher = ["5 kWh", "10 kWh", "15 kWh"]

optionmenu_2 = customtkinter.CTkOptionMenu(frame_2, values=batteriespeicher)
optionmenu_2.pack(pady=10, padx=10)
optionmenu_2.set("Batteriespeicher")


sum = op_1_callback

button_1 = customtkinter.CTkButton(master=frame_3, command=pdf_create)
button_1.pack(pady=10, padx=10)


app.mainloop()
