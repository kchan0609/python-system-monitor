
import psutil
import time


def check_performance():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("C:\\").percent

    print("\nSYSTEM PERFORMANCE MONITOR")
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

    # Save measurements to a text file
    log = open("performance_log.txt", "a")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    log.write(
        f"{timestamp} | CPU: {cpu}% | "
        f"RAM: {ram}% | Disk: {disk}%\n"
    )
    log.close()

    return cpu, ram


def main():
    print("SYSTEM PERFORMANCE MONITOR")
    print("--------------------------")
    print("1. Check System Performance Once")
    print("2. Monitor System Performance")

    choice = input("Select an option: ")

    if choice == "1":
        readings = 1
    elif choice == "2":
        readings = int(input("How many readings? "))
    else:
        print("Invalid option.")
        return

    if readings <= 0:
        print("Number of readings must be positive.")
        return

    cpu_history = []
    ram_history = []

    for i in range(readings):
        print("\nReading", i + 1, "of", readings)

        cpu, ram = check_performance()

        cpu_history.append(cpu)
        ram_history.append(ram)

        if i < readings - 1:
            time.sleep(4)

    avg_cpu = sum(cpu_history) / len(cpu_history)
    avg_ram = sum(ram_history) / len(ram_history)

    print("\n--------------------------")
    print("PERFORMANCE SUMMARY")
    print("--------------------------")
    print("Average CPU Usage:", round(avg_cpu, 2), "%")
    print("Average RAM Usage:", round(avg_ram, 2), "%")
    print("\nPerformance data saved successfully!")


main()
