input_file = "DNNMark_trace_master.txt"

with open(input_file, "r") as infile:
    lines = infile.readlines()  # read all lines once into memory

# for i in range(200, 1800, 200):
#     output_file = f"different_rates/DNNMark_{i}.txt"
#     with open(output_file, "w") as outfile:
#         for line in lines:
#             if not line.strip():  # skip blank lines
#                 continue
#             ts, src, dst, typ = line.strip().split()
#             ts_scaled = int(int(ts) // i)
#             outfile.write(f"{ts_scaled} {src} {dst} {typ}\n")

# special case if needed
output_file = f"different_rates/DNNMark_1300.txt"
with open(output_file, "w") as outfile:
    for line in lines:
        if not line.strip():  # skip blank lines
            continue
        ts, src, dst, typ = line.strip().split()
        ts_scaled = int(int(ts) // 1300)
        outfile.write(f"{ts_scaled} {src} {dst} {typ}\n")