import random
import time

propagation_delay = 0.01
num_devices = 3
collision_detected = False

def transmit_packet(device_id, packet_id):
    print(f"Device {device_id} sends Packet {packet_id}.")
    time.sleep(propagation_delay)
    print(f"Device {device_id} has finished sending Packet {packet_id}.")

def csma_cd(device_id, packet_id):
    global collision_detected
    while True:
        channel_busy = random.choice([True, False])
        if not channel_busy:
            print(f"Device {device_id} is attempting to transmit Packet {packet_id}.")
            if collision_detected:
                print(f"Collision detected! Device {device_id} will back off.")
                time.sleep(random.uniform(0.1, 0.5))
                collision_detected = False
                continue
            transmit_packet(device_id, packet_id)
            break
        else:
            print(f"Device {device_id} found the channel busy. Waiting...")
            time.sleep(0.1)

if __name__ == "__main__":
    print("Starting CSMA/CD Simulation")
    
    for device_id in range(num_devices):
        packet_id = random.randint(1, 10)
        if device_id < 2:
            collision_detected = True
        csma_cd(device_id, packet_id)
    
    print("CSMA/CD Simulation Complete.")
