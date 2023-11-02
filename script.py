import evdev
from evdev import ecodes
from evdev import resolve_ecodes
from typing import List

def get_devices(names: List[str]):
    matching = []
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if device.name in names:
            print(device.path, device.name, device.phys)
            matching.append(device)
    return matching

def get_device(name: str):
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if device.name == name:
            print(device.path, device.name, device.phys)
            return device

# First name is for wired devices, second for unwired
controller_name = "Valve Software Steam Controller"
wired_name = "Valve Software Wired Controller"
# steam_controller_devices = get_devices([controller_name, wired_name])
# print(steam_controller_devices)

controller: evdev.InputDevice = get_device(controller_name)

for event in controller.read_loop():
    if event.type == ecodes.EV_KEY:
        try:
            key_event = evdev.categorize(event)
            key = ecodes.KEY[event.code]
            print(
                    f"Event: {key_event}\t"
                    #f"Type: {event.type}\t"
                    #f"Code: {event.code}\t"
                    f"Key: {key}\t"
                    #f"Value: {event.value}\t"
                    #f"Timestamp: {event.timestamp}\t"
            )
        except Exception as e:
            print(e)
    #else:
    #    print(f"Unknown event: {str(event)}")


