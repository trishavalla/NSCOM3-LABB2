import random
import matplotlib.pyplot as plt

# Parameters
num_stations = 4           # Number of stations sending frames
simulation_time = 100      # Total simulation time in arbitrary units
frame_transmission_time = 1 # Time taken to send a frame (fixed for simplicity)

# Generate random transmission times for each station
transmissions = {}
for station in range(1, num_stations + 1):
    transmission_times = []
    time = 0
    while time < simulation_time:
        # Each station sends a frame at a random interval
        time += random.randint(1, 10)
        transmission_times.append(time)
    transmissions[station] = transmission_times

# Detect collisions
collision_times = []
for time in range(simulation_time):
    active_stations = [station for station, times in transmissions.items() if time in times]
    if len(active_stations) > 1:
        collision_times.append(time)  # Collision occurs if multiple stations send at the same time

# Visualization
plt.figure(figsize=(10, 6))

# Plot each station's frame transmissions
for station, times in transmissions.items():
    plt.scatter(times, [station] * len(times), label=f"Station {station}", s=100)

# Highlight collision times
for collision_time in collision_times:
    plt.axvspan(collision_time, collision_time + frame_transmission_time, color='red', alpha=0.3)

plt.xlabel("Time")
plt.ylabel("Station")
plt.title("Frames in Pure ALOHA Network")
plt.legend(loc="upper right")
plt.show()
