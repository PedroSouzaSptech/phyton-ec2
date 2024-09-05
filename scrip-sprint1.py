import psutil
import time

# CPU - percentuais de uso
cpu_percent = psutil.cpu_percent(interval=1)

# Memória RAM - total, disponível e usada
mem = psutil.virtual_memory()
total_ram = mem.total
used_ram = mem.used
free_ram = mem.available

# Armazenamento - total e usado
disk = psutil.disk_usage('/')
total_storage = disk.total
used_storage = disk.used
free_storage = disk.free

# Rede - latência (Ping para Google DNS)
def get_network_latency():
    try:
        # Enviando um ping para o servidor DNS do Google
        start_time = time.time()
        psutil.net_connections(kind='inet')
        end_time = time.time()
        latency = (end_time - start_time) * 1000  # Convertendo para milissegundos
        return latency
    except Exception as e:
        return None

# Latência de rede
network_latency = get_network_latency()

# Imprimindo os resultados
print(f"CPU usada: {cpu_percent}%")
print(f"Total de RAM: {total_ram / (1024 ** 3):.2f} GB")
print(f"RAM usada: {used_ram / (1024 ** 3):.2f} GB")
print(f"RAM livre: {free_ram / (1024 ** 3):.2f} GB")
print(f"Armazenamento total: {total_storage / (1024 ** 3):.2f} GB")
print(f"Armazenamento usado: {used_storage / (1024 ** 3):.2f} GB")
print(f"Armazenamento livre: {free_storage / (1024 ** 3):.2f} GB")
if network_latency is not None:
    print(f"Latência de rede: {network_latency:.2f} ms")
else:
    print("Não foi possível calcular a latência de rede.")
