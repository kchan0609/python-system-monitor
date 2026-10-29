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

main()