import tkinter as tk
import requests as rq
def weather(canvas):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid={api_key}3"
    json_data=rq.get(api).json()
    if json_data.get('cod') != 200:
                label1.config(text="City not found!")
                label2.config(text="")
                return
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    mintemp=int(json_data['main']['temp_min']-273.15)
    maxtemp=int(json_data['main']['temp_max']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    final_info=condition+'\n'+str(temp)+'°C'
    final_data='\n'+str(mintemp)+'°C'+'\n'+'MAX Temp:'+str(maxtemp)+'°C'+'\n'+'MIN Temp:'+str(mintemp)+'°C'+'\n'+'Presssure:'+str(pressure)+'Pa'+'\n'+'Humidity:'+str(humidity)+'%'+'\n'+'Wind speed:'+str(wind)+'m/s'
    label1.config(text=final_info)
    label2.config(text=final_data)
    if city not in history:
        history.append(city)
        update_dropdown()
def update_dropdown():
    menu=dropdown('menu')
    menu.delete(0,'end')
    for city in history:
        menu.addcommand(label=city,command=lambda c=city:select_city(c))
def select_city(city):
      textfield.delete(0,tk.END)   
      textfield.insert(0,city)
      weather()    
canvas=tk.Tk()
canvas.geometry('600x500')
canvas.title("Weather App")
t=('poppins',15,'bold')
f=('poppins',35,'bold')
textfield=tk.Entry(canvas,font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',weather)
history=[]
dropdown_var=tk.StringVar(canvas)
dropdown_var.set('Search history')
dropdown=tk.OptionMenu(canvas,dropdown_var,())
dropdown.pack(pady=10)
icon_label = tk.Label(canvas)
icon_label.pack()
label1=tk.Label(canvas,font=t)
label1.pack()
label2=tk.Label(canvas,font=f)
label2.pack()
canvas.mainloop()


