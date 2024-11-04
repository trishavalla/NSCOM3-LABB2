import random
import time

propagation_delay = 0.01
num_devices = 3

def transmit_packet(device_id, packet_id):
    print(f"Device {device_id} sends Packet {packet_id}.")
    time.sleep(propagation_delay)
    print(f"Device {device_id} has finished sending Packet {packet_id}.")

def one_persistent_csma(device_id, packet_id):
    while True:
        channel_busy = random.choice([True, False])
        if not channel_busy:
            transmit_packet(device_id, packet_id)
            break
        else:
            print(f"Device {device_id} found the channel busy (1-persistent).")
            time.sleep(0.1)

if __name__ == "__main__":
    print("Starting 1-Persistent CSMA Simulation:")
    for device_id in range(num_devices):
        packet_id = random.randint(1, 10)
        one_persistent_csma(device_id, packet_id)
    print("1-Persistent CSMA Simulation Complete.")
