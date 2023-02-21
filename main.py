import requests
import tkinter as tk
def weather():
    global txt,ctx,final,desc,icon
    city = txt.get()
    country_code = ctx.get()
    api_id = "6a76d416c5800e9afbd2f4ba7747b2b8"
    try:
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_id}")
        js = res.json()
        dc = js['weather'][0]
        final.config(text=f"{dc['main']}")
        desc.config(text=f"{dc['description']}")
        icon.config(text=f"{dc['icon']}")
    except KeyError:
        final.config(text="Either City Code or City name is invalid")
app = tk.Tk()
app.config(padx=100,pady=100)
ct = tk.Label(text="Enter City name:")
ct.grid(row=0,column=0)
txt = tk.Entry()
txt.grid(row=0,column=1)
code = tk.Label(text="Enter the city code: ")
code.grid(row=1,column=0)
ctx = tk.Entry()
ctx.grid(row=1,column=1)
test = tk.Button(text="Get the weather",command=weather)
test.grid(row=2,column=1)
final = tk.Label()
final.grid(row=3,column=0)
desc = tk.Label()
desc.grid(row=4,column=0)
icon = tk.Label()
icon.grid(row=5,column=0)
app.mainloop()