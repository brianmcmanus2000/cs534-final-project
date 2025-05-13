import os
import subprocess

# === Configuration ===
BASE_DIR        = os.getcwd()  # Assuming you run this script from the top-level booksim/ folder
EXAMPLES_DIR    = os.path.join(BASE_DIR, "examples")
BOOKSIM_BIN     = os.path.join(BASE_DIR, "booksim2", "booksim")
GEN_CFG_DIR     = os.path.join(BASE_DIR, "generated_configs")
RESULTS_DIR     = os.path.join(BASE_DIR, "results")

# Create output directories
os.makedirs(GEN_CFG_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# Symlink the trace file into generated_configs/
trace_src  = os.path.join(EXAMPLES_DIR, "forward_pool_trace.txt")
trace_link = os.path.join(GEN_CFG_DIR, "forward_pool_trace.txt")
if not os.path.exists(trace_link):
    os.symlink(os.path.relpath(trace_src, GEN_CFG_DIR), trace_link)

# Read the template config
template_path = os.path.join(EXAMPLES_DIR, "project_torus.cfg")
with open(template_path, "r") as f:
    template_lines = f.readlines()

# Parameters to sweep
scales             = list(range(100, 2001, 100))  # 100, 200, ..., 2000
routing_functions  = ["dor"]  # add more routing functions here

def update_workload_line(line: str, scale: int) -> str:
    """Replace the 5th trace argument (scale) in a workload=trace(...) line."""
    indent = line[:len(line) - len(line.lstrip())]
    if not line.strip().startswith("workload=trace"):
        return line

    # Find the outer braces
    start = line.find("{", line.find("trace("))
    end   = line.find("});", start)
    if start < 0 or end < 0:
        return line

    interior = line[start+1:end]
    # Split on commas at brace-depth 0
    parts, buf, depth = [], "", 0
    for ch in interior:
        if ch == "{":
            depth += 1; buf += ch
        elif ch == "}":
            depth -= 1; buf += ch
        elif ch == "," and depth == 0:
            parts.append(buf); buf = ""
        else:
            buf += ch
    parts.append(buf)

    # Replace 5th element with new scale
    if len(parts) >= 5:
        parts[4] = str(scale)

    new_interior = ",".join(parts)
    return f"{indent}workload=trace({{{new_interior}}});\n"

# Generate configs, run BookSim, collect outputs
for scale in scales:
    for func in routing_functions:
        cfg_name = f"project_torus_scale_{scale}_{func}.cfg"
        cfg_path = os.path.join(GEN_CFG_DIR, cfg_name)

        # Write modified config
        with open(cfg_path, "w") as out_cfg:
            for line in template_lines:
                if line.strip().startswith("workload=trace"):
                    out_cfg.write(update_workload_line(line, scale))
                elif line.strip().startswith("routing_function"):
                    indent = line[:len(line) - len(line.lstrip())]
                    out_cfg.write(f"{indent}routing_function = {func};\n")
                else:
                    out_cfg.write(line)

        # Execute BookSim
        proc = subprocess.run(
            [BOOKSIM_BIN, cfg_name],
            cwd=GEN_CFG_DIR,
            capture_output=True,
            text=True
        )

        # Save stdout to results folder
        result_file = os.path.join(RESULTS_DIR, f"scale_{scale}_{func}.txt")
        with open(result_file, "w") as out_f:
            out_f.write(proc.stdout)

print("Done: configs in 'generated_configs/', outputs in 'results/'.")
