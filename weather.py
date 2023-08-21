import tkinter as tk
import requests
def getwheatherdata(canvas):
    city=text.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b15f186ed5da500b5913bbbf53bc921a"
    json_data=requests.get(api).json()
    condition =json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    temp_max=int(json_data['main']['temp_max']-273.15)
    temp_min=int(json_data['main']['temp_min']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    final_info=" condition:"+ condition+"\n" +"temperature :"+str(temp)+"^C"
    final_data="max_temp :"+str(temp_max)+"\nmin_temp :"+str(temp_min)+"\npressure :"+str(pressure)+"\nhumidity :"+str(humidity)
    label1.config(text =final_info)
    label2.config(text=final_data)
canvas = tk.Tk()
canvas.attributes("-toolwindow")
canvas.title("weather app")
f=("poppins",15,"bold")
t=("poppins",25,"bold")
text=tk.Entry(canvas,font=f)
text.pack(pady =20)
text.focus()
text.bind("<Return>",getwheatherdata)
label1=tk.Label(canvas,font=t)
label1.pack()
label2=tk.Label(canvas,font=f)
label2.pack()
canvas.mainloop()


