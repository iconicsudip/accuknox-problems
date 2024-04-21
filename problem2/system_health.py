import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

class SystemHealth:
    def __init__(self):
        self.cpu = psutil.cpu_percent(interval=1)
        self.memory = psutil.virtual_memory().percent
        self.disk = psutil.disk_usage('/').percent
        self.processes = psutil.pids()

    def get_all_usage(self):
        return self.cpu, self.memory, self.disk

    def get_all_stats(self):
        self.get_cpu_usage()
        self.get_memory_usage()
        self.get_disk_usage()
        self.get_running_processes()

    def get_cpu_usage(self):
        if(self.cpu > CPU_THRESHOLD):
            print(f"CPU usage is {self.cpu}%, which is above the threshold of {CPU_THRESHOLD}% - Alert!")
        else:
            print(f"CPU usage is {self.cpu}%")

    def get_memory_usage(self):
        if(self.memory > MEMORY_THRESHOLD):
            print(f"Memory usage is {self.memory}%, which is above the threshold of {MEMORY_THRESHOLD}% - Alert!")
        else:
            print(f"Memory usage is {self.memory}%")

    def get_disk_usage(self):
        if(self.disk > DISK_THRESHOLD):
            print(f"Disk usage is {self.disk}%, which is above the threshold of {DISK_THRESHOLD}% - Alert!")
        else:
            print(f"Disk usage is {self.disk}%")
    
    def get_running_processes(self):
        number_of_processes = len(self.processes)
        print(f"Number of running processes: {number_of_processes}")

def main():
    print("Current system health:")
    system_health = SystemHealth()
    system_health.get_all_stats()

if __name__ == '__main__':
    main()