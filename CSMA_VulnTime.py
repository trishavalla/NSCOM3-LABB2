import random
import time

propagation_delay = 0.01
vulnerable_time = 2 * propagation_delay
num_devices = 3

def transmit_packet(device_id, packet_id, start_time):
    print(f"Device {device_id} is attempting to send Packet {packet_id}...")
    time.sleep(random.uniform(0, 0.5))
    current_time = time.time() - start_time
    print(f"Device {device_id} sends Packet {packet_id} at time {current_time:.3f}s.")
    print(f"Vulnerable Time for this packet: {vulnerable_time:.3f}s.")
    time.sleep(propagation_delay)
    print(f"Device {device_id} has finished sending Packet {packet_id}.")

if __name__ == "__main__":
    start_time = time.time()
    for device_id in range(num_devices):
        packet_id = random.randint(1, 10)
        transmit_packet(device_id, packet_id, start_time)
        time.sleep(1)
