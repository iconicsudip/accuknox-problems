
# Problem Statement 1
# Cow wisdom web server

## Prerequisites

```
sudo apt install fortune-mod cowsay -y
```

## How to use?

1. Run `./wisecow.sh`
2. Point the browser to server port (default 4499)

## What to expect?
![wisecow](https://github.com/nyrahul/wisecow/assets/9133227/8d6bfde3-4a5a-480e-8d55-3fef60300d98)

# Problem Statement
Deploy the wisecow application as a k8s app

## Requirement
1. Create Dockerfile for the image and corresponding k8s manifest to deploy in k8s env. The wisecow service should be exposed as k8s service.
2. Github action for creating new image when changes are made to this repo
3. [Challenge goal]: Enable secure TLS communication for the wisecow app.

## Expected Artifacts
1. Github repo containing the app with corresponding dockerfile, k8s manifest, any other artifacts needed.
2. Github repo with corresponding github action.
3. Github repo should be kept private and the access should be enabled for following github IDs: nyrahul, SujithKasireddy

# Problem Statement 2
# System health monitor - 
This is a python script called `system_health.py` which helps to know the system health of any system and based on **THRESHOLD** it will give messages

## Explaination of code:
There is a class called `SystemHealth` which containes 6 methods which are explained below.
1. `get_all_usage` : Which will return CPU, Memory and Disk usages in percetage.
2. `get_all_stats` : Which will help user to know about the usages of CPU, Memory, Disk and Number of processes are running in the system.
3. `get_cpu_usage` : Which will help to know CPU usage, if usage is greater than CPU_THRESHOLD then it will show alert in console.
4. `get_memory_usage` : Which will help to know Memory usage, if usage is greater than MEMORY_THRESHOLD then it will show alert in console.
5. `get_disk_usage` : Which will help to know Disk usage, if usage is greater than DISK_THRESHOLD then it will show alert in console.
6. `get_running_processes` : Which will help to know number of processes are running in system.

**Note :** CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD are initially 80.

# Application health checker - 
This is a python script called `application_health.py` which helps to know the application health by using url and making requests and it will tell whether it is UP or Down.

## Explaination of code:
There is a class called `ApplicationHealth` which containes 2 methods which are explained below ApplicationHealth class will take url from user.
1. `check_application` : Which will request url and get the status code and based on the status code it will return application stauts.
2. `get_health` : Which will help user to know about the health of an application of given URL. By default the interval is 5 seconds. You can change interval accordingly by passing value in `get_health` as a parameter.