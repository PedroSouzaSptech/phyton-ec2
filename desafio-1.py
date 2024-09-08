import psutil
import time 
from datetime import datetime

print('Monitorando memoria swap...')

i = 0
contador = 20  

data_e_hora_atuais = datetime.now()
dt= data_e_hora_atuais.strftime("%d/%m/%Y")
dthora = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

a = "Total GB"
b = "Avaible"
c = "Percent %"
e = "Used GB"
f = "Data e Hora"

while i < contador:
    i += 1
    mem = psutil.virtual_memory()
    total_ram = mem.total
    avaible_ram = mem.available
    percent_ram = mem.percent
    used_ram = mem.used

    total = "{:.2f}".format(total_ram/ (1024 ** 3))
    avaible = "{:.2f}".format(avaible_ram/ (1024 ** 3))
    percent = percent_ram
    used = "{:.2f}".format(used_ram/ (1024 ** 3)) 


    biblioteca = {a : total , b : avaible, c : percent, e : used, f : dthora }
  
    print(biblioteca)
    time.sleep(2)
    




 



