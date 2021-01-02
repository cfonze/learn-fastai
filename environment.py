# An example Python script to check environment/platform information

import torch
import psutil
import platform
from datetime import datetime

# converts large number of bytes into a scaled format 
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# Torch GPU information
print("="*40, "Torch CUDA GPU Info", "="*40)
print(f"How many GPUs? {torch.cuda.device_count()}")
print(f"Which GPU Is The Current GPU? {torch.cuda.current_device()}")
print(f"Name of the current GPU: {torch.cuda.get_device_name(torch.cuda.current_device())}")
print(f"Is PyTorch using a GPU? {torch.cuda.is_available()}")
print(f"Torch CUDA version: {torch.version.cuda}")
print(f"Torch CUDNN version: {torch.backends.cudnn.version()}")
print(f"Torch CUDA NCCL version: {torch.cuda.nccl.version()}")

# Platform information
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

# CPU Information
print("="*40, "CPU Info", "="*40)
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")

# Memory Information
print("="*40, "Memory Information", "="*40)
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")



