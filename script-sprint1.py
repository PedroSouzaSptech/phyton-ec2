import psutil
import time
import subprocess

atualizador = 2  

i = 0

while i < atualizador:
    
    cpu_percent = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    total_ram = mem.total
    used_ram = mem.used
    free_ram = mem.available

    disk = psutil.disk_usage('/')
    total_storage = disk.total
    used_storage = disk.used
    free_storage = disk.free

    print(f"CPU usada: {cpu_percent}%")
    print(f"Total de RAM: {total_ram / (1024 ** 3):.2f} GB")
    print(f"RAM usada: {used_ram / (1024 ** 3):.2f} GB")
    print(f"RAM livre: {free_ram / (1024 ** 3):.2f} GB")
    print(f"Armazenamento total: {total_storage / (1024 ** 3):.2f} GB")
    print(f"Armazenamento usado: {used_storage / (1024 ** 3):.2f} GB")
    print(f"Armazenamento livre: {free_storage / (1024 ** 3):.2f} GB")
    print("-------------------------------------------------------------")

    time.sleep(5)
   
