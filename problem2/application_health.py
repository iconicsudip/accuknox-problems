import time
import requests

class ApplicationHealth:
    def __init__(self, url):
        self.url = url
    def check_application(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return "Application is UP"
            else:
                return "Application is DOWN"
        except requests.ConnectionError:
            return "Connection Error: Application is DOWN"
        except requests.Timeout:
            return "Timeout Error: Application is DOWN"
    
    def get_health(self, interval=5):
        try:
            while True:
                result = self.check_application()
                print(f"Status - {time.strftime('%Y-%m-%d %H:%M:%S')} - {result}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Exiting...")
            exit()


def main():
    url = input("Enter the URL of the application to check: ")
    applicationHealth = ApplicationHealth(url)
    applicationHealth.get_health()

if __name__ == '__main__':
    main()