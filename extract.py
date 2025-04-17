import re

def extract_stats(file_path):
    # Define the patterns to match
    patterns = {
        "avg_packet_latency": r"Overall average packet latency = ([\d\.eE+-]+)",
        "avg_network_latency": r"Overall average network latency = ([\d\.eE+-]+)",
        "avg_flit_latency": r"Overall average flit latency = ([\d\.eE+-]+)",
        "avg_fragmentation": r"Overall average fragmentation = ([\d\.eE+-]+)",
        "avg_injected_packet_rate": r"Overall average injected packet rate = ([\d\.eE+-]+)",
        "avg_injected_flit_rate": r"Overall average injected flit rate = ([\d\.eE+-]+)",
        "avg_hops": r"Overall average hops = ([\d\.eE+-]+)",
        "total_power": r"- Total Power:\s+([\d\.eE+-]+)",
        "total_area": r"- Total Area:\s+([\d\.eE+-]+)",
    }

    results = {}

    with open(file_path, "r") as f:
        content = f.read()

    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            results[key] = float(match.group(1))
        else:
            results[key] = None  # could not find value

    return results

# Example usage
if __name__ == "__main__":
    stats = extract_stats("output.txt")  # or any output file

    for key, value in stats.items():
        print(f"{value}")