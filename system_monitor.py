import psutil

def main():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("C:\\").percent

    print("SYSTEM PERFORMANCE MONITOR")
    print("--------------------------")
    print("CPU Usage:", cpu, "%")
    print("RAM Usage:", ram, "%")
    print("Disk Usage:", disk, "%")

    print("--------------------------")

    if cpu >= 80:
        print("CPU Status: High Usage!")
    elif cpu >= 50:
        print("CPU Status: Moderate")
    else:
        print("CPU Status: Normal")

    if ram >= 80:
        print("RAM Status: High Usage!")
    elif ram >= 50:
        print("RAM Status: Moderate")
    else:
        print("RAM Status: Normal")

    if disk >= 80:
        print("Disk Status: High Usage!")
    elif disk >= 50:
        print("Disk Status: Moderate")
    else:
        print("Disk Status: Normal")
main()