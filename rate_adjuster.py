input_file = "../booksim/forward_activation_trace.txt"

for scale in range(300, 1900, 200):
    output_path = f"../booksim/activation_files/activation_trace_{scale}.txt"
    with open(input_file, "r") as infile, open(output_path, "w") as outfile:
        for raw in infile:
            if not (line := raw.strip()):
                continue
            ts, src, dst, typ = line.split()
            ts_scaled = int(ts) // scale
            outfile.write(f"{ts_scaled} {src} {dst} {typ}\n")
# special case if needed
# output_file = f"different_rates/DNNMark_1300.txt"
# with open(output_file, "w") as outfile:
#     for line in lines:
#         if not line.strip():  # skip blank lines
#             continue
#         ts, src, dst, typ = line.strip().split()
#         ts_scaled = int(int(ts) // 1300)
#         outfile.write(f"{ts_scaled} {src} {dst} {typ}\n")