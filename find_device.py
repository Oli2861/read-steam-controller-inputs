import pyudev
from evdev import InputDevice, categorize, ecodes
from typing import List

def find_event_paths_of_device(vendor_id: str, model_ids: List[str]) -> List[str]:
    context = pyudev.Context()
    event_paths: List[str] = []
    print("Found devices:")
    for device in context.list_devices(subsystem="input"):
        if device.get("ID_VENDOR_ID") == vendor_id and device.get("ID_MODEL_ID") in model_ids:
            print(f"Name: {device.get('NAME')} Event path: {device.device_node}")
            if device.device_node != None:
                event_paths.append(device.device_node)
    print(f"Valid event paths: {event_paths}")
    return event_paths

valve_vendor_id = "28de"
steam_controller_model_ids = ["1102", "1142"]
event_paths = find_event_paths_of_device(valve_vendor_id, steam_controller_model_ids)

def print_capabilities(event_paths: List[str]):
    for event_path in event_paths:
        device = InputDevice(event_path)
        print(f"Event path: {event_path}\nDevice: {device}\n Capabilities:{device.capabilities(verbose=True)}")

print_capabilities(event_paths)
