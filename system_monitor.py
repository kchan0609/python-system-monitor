
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


def main():
    print("SYSTEM PERFORMANCE MONITOR")
    print("--------------------------")
    print("1. Check System Performance Once")
    print("2. Monitor System Performance")

    choice = input("Select an option: ")

    if choice == "1":
        check_performance()

    elif choice == "2":
        readings = int(input("How many readings? "))

        if readings > 0:
            for i in range(readings):
                print("\nReading", i + 1, "of", readings)
                check_performance()

                if i < readings - 1:
                    time.sleep(4)
        else:
            print("Number of readings must be positive.")

    else:
        print("Invalid option.")


main()
