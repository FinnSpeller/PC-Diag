import psutil
import platform
import pygame

pc_name = platform.node()


os_name = platform.system()
os_version = platform.version()
os_info = (os_name+" "+str(os_version))

cpu_name = platform.processor()
cpu_usage = psutil.cpu_percent()


ram = psutil.virtual_memory()
ram_total = ram.total / (1024 ** 3)
ram_used = ram.used / (1024 ** 3) 
ram_percent = ram.percent
ram_data=(f"RAM: {ram_total:.2f} GB ({ram_used:.2f} GB in usage, {ram_percent}%)")


disk = psutil.disk_usage('/')
disk_total = disk.total / (1024 ** 3) # in GB
disk_used = disk.used / (1024 ** 3) # in GB
disk_percent = disk.percent
disk_data=(f"Disk: {disk_total:.2f} GB ({disk_used:.2f} GB used, {disk_percent}%)")

battery = psutil.sensors_battery()

def systemdatago():
    print(f"PC'S Name: {pc_name}")
    print(f"OS: {os_info}")
    print(f"CPU: {cpu_name} ({cpu_usage}%)")
    print(ram_data)
    print(disk_data)
    print("Battery Percentage: "+ str(battery.percent) + "%")

while True:
    print (input("Say Anything you want and the system will print: "))
    systemdatago()