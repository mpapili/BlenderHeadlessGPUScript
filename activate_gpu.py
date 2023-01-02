import bpy


def enable_gpus(device_type, use_cpus=False):
    preferences = bpy.context.preferences
    cycles_preferences = preferences.addons["cycles"].preferences
    cycles_preferences.refresh_devices()
    cuda_devices, opencl_devices = cycles_preferences.devices

    if device_type == "CUDA":
        devices = cuda_devices
        print("Setting to use CUDA Devices")
    elif device_type == "OPENCL":
        devices = opencl_devices
        print("Setting to use OpenCL Devices")
    else:
        raise RuntimeError("Unsupported device type")

    try:
        iter(devices)
    except TypeError:
        print("Single GPU Detected")
        devices = [devices]
    print("f{len(devices)} devices detected")
    activated_gpus = []

    for device in devices:
        if device.type == "CPU":
            device.use = use_cpus
        else:
            device.use = True
            activated_gpus.append(device.name)

    cycles_preferences.compute_device_type = device_type
    bpy.context.scene.cycles.device = "GPU"

    return activated_gpus

enable_gpus("CUDA")

