import torch
print("CUDA Available:", torch.cuda.is_available())
print("CUDA Version:", torch.version.cuda)
print("Device Name:", torch.cuda.get_device_name() if torch.cuda.is_available() else "No CUDA")
