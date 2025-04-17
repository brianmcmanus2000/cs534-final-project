import matplotlib.pyplot as plt
# X-axis: time scaling factors (your independent variable)
time_scales = [200, 400, 600, 800, 1000, 1200, 1300, 1400, 1500, 1600]

# Y-axis data (copy-pasted from Excel)
torus_latency = [39.3406, 40.1997, 40.5123, 40.7898, 41.3417, 42.408, 42.785, 44.7366, 58.3454, 204.982]
cmesh_latency = [43.4451, 43.7776, 43.9236, 44.6396, 45.2305, 48.2954, 70.2992, 338.044, None, None]

torus_power = [2.4583, 2.96121, 3.30363, 3.55315, 3.97467, 4.59908, 4.84421, 5.26336, 5.39624, 5.54755]
cmesh_power = [2.2602, 2.89617, 3.33036, 3.65126, 4.19163, 5.00371, 5.32301, 5.84963, None, None]

torus_flit_rate=[0.008416, 0.01512, 0.0189155, 0.0212084, 0.0263699, 0.0350486, 0.0382115, 0.0455285, 0.047956, 0.0506943]
cmesh_flit_rate = [0.008416, 0.01512, 0.0189155, 0.0212087, 0.0263703, 0.0350495, 0.0382184, 0.045276, None, None]

torus_fragmentation=[0.158, 0.181422, 0.184251, 0.238585, 0.540971, 0.525288, 0.527351, 0.567828, 0.608671, 0.614139]
cmesh_fragmentation=[2.82542, 2.72357, 2.69169, 3.03123, 3.10673, 3.42373, 3.49498, 3.53265, None, None]
# You can define a helper function for plotting
def plot_metric(y_torus, y_cmesh, ylabel, title):
    plt.figure()
    plt.plot(torus_flit_rate, y_torus, marker='o', label='Torus')
    plt.plot(cmesh_flit_rate, y_cmesh, marker='s', label='CMesh')
    plt.xlabel("Injection Rate")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

# Plot the metrics
plot_metric(torus_latency, cmesh_latency, "Avg Packet Latency (cycles)", "Packet Latency vs Flit Rate")
plt.savefig("latency.png",dpi=300)
plot_metric(torus_power, cmesh_power, "Total Power (W)", "Power vs Flit Rate")
plt.savefig("power.png",dpi=300)
plot_metric(torus_fragmentation, cmesh_fragmentation, "Average Fragmentation", "Fragmentation vs Flit Rate")
plt.savefig("fragmentation.png",dpi=300)