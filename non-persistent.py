import random
import time

propagation_delay = 0.01  
num_devices = 3 

def transmit_packet(device_id, packet_id):
    """Simulates sending a packet from a device."""
    print(f"Device {device_id} sends Packet {packet_id}.")
    time.sleep(propagation_delay)  
    print(f"Device {device_id} has finished sending Packet {packet_id}.")

def non_persistent_csma(device_id, packet_id):
    """Simulates Non-Persistent CSMA."""
    while True:
        channel_busy = random.choice([True, False])
        if not channel_busy:
            transmit_packet(device_id, packet_id)
            break  
        else:
            print(f"Device {device_id} found the channel busy (non-persistent).")
            time.sleep(random.uniform(0.1, 0.5)) 

if __name__ == "__main__":
    print("Starting Non-Persistent CSMA Simulation:")
    for device_id in range(num_devices):
        packet_id = random.randint(1, 10)
        non_persistent_csma(device_id, packet_id)
    print("Non-Persistent CSMA Simulation Complete.")
