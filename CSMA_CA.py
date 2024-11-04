import random
import time

num_devices = 3
max_retries = 3
channel_busy = True

def transmit_data(device_id, packet_id):
    print(f"Device {device_id} sends Packet {packet_id}.")
    time.sleep(0.5)
    print(f"Device {device_id} has finished sending Packet {packet_id}.")

def csma_ca(device_id, packet_id, retries):
    global channel_busy
    while retries >= 0:
        if not channel_busy:
            print(f"Device {device_id} is sending RTS for Packet {packet_id}.")
            time.sleep(0.1)
            print(f"Device {device_id} received CTS for Packet {packet_id}.")
            transmit_data(device_id, packet_id)
            break
        else:
            print(f"Device {device_id} found the channel busy. Waiting...")
            time.sleep(0.5)
        
        retries -= 1
        if retries < 0:
            print(f"Device {device_id} has exhausted all retries for Packet {packet_id}.")

if __name__ == "__main__":
    print("Starting CSMA/CA Simulation with Exhausted Retries:")
    
    for device_id in range(num_devices):
        packet_id = random.randint(1, 10)
        retries = max_retries
        
        if device_id == 0:
            channel_busy = True
        else:
            channel_busy = random.choice([True, False])
            
        csma_ca(device_id, packet_id, retries)
    
    print("CSMA/CA Simulation Complete.")
