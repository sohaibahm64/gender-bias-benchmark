# run_benchmark.py
# Gender Bias Benchmark — AI in Education
# Author: Sohaib Ahmad
#
# USAGE:
#   1. Install Ollama from https://ollama.com
#   2. In Command Prompt run:  ollama pull llama3
#   3. In Command Prompt run:  ollama serve
#   4. Open a NEW Command Prompt and run:  python run_benchmark.py
#
# No API key needed. Completely free.

import os
import json
import urllib.request
from datetime import datetime
from prompts import PROMPTS

# ── Settings ──────────────────────────────────────────────────────────────────

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

# ── Setup ─────────────────────────────────────────────────────────────────────

os.makedirs("outputs", exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"\nGender Bias Benchmark — starting at {timestamp}")
print(f"Model: {MODEL_NAME} via Ollama (free, local)")
print(f"Total prompts to run: {len(PROMPTS)}\n")

# ── Helper function ───────────────────────────────────────────────────────────

def ask_ollama(prompt_text):
    """Send a prompt to Ollama and return the response text."""
    data = json.dumps({
        "model": MODEL_NAME,
        "prompt": prompt_text,
        "stream": False
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=300) as response:
        result = json.loads(response.read().decode("utf-8"))
        return result["response"].strip()

# ── Run prompts ───────────────────────────────────────────────────────────────

results = []

for i, (label, prompt_text) in enumerate(PROMPTS, start=1):
    filename = f"{label}.txt"
    filepath = os.path.join("outputs", filename)

    print(f"[{i}/{len(PROMPTS)}] Running: {label}")

    try:
        output_text = ask_ollama(prompt_text)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"LABEL:  {label}\n")
            f.write(f"PROMPT: {prompt_text}\n")
            f.write(f"MODEL:  {MODEL_NAME}\n")
            f.write(f"DATE:   {timestamp}\n")
            f.write("-" * 60 + "\n\n")
            f.write(output_text)

        results.append({
            "label": label,
            "prompt": prompt_text,
            "filename": filename,
            "status": "OK",
            "preview": output_text[:80].replace("\n", " ") + "..."
        })

        print(f"        ✓ Saved to outputs/{filename}")

    except Exception as e:
        results.append({
            "label": label,
            "prompt": prompt_text,
            "filename": filename,
            "status": f"ERROR: {e}",
            "preview": ""
        })
        print(f"        ✗ Error: {e}")
        print(f"          Make sure Ollama is running: open Command Prompt and type 'ollama serve'")

# ── Write summary file ────────────────────────────────────────────────────────

summary_path = os.path.join("outputs", "summary.txt")

with open(summary_path, "w", encoding="utf-8") as f:
    f.write("GENDER BIAS BENCHMARK — SUMMARY\n")
    f.write(f"Run at: {timestamp}\n")
    f.write(f"Model: {MODEL_NAME}\n")
    f.write(f"Total prompts: {len(PROMPTS)}\n")
    f.write("=" * 60 + "\n\n")

    for r in results:
        f.write(f"[{r['status']}] {r['label']}\n")
        f.write(f"  Prompt:   {r['prompt']}\n")
        f.write(f"  File:     outputs/{r['filename']}\n")
        if r["preview"]:
            f.write(f"  Preview:  {r['preview']}\n")
        f.write("\n")

# ── Write analysis template ───────────────────────────────────────────────────

analysis_path = os.path.join("outputs", "analysis_template.md")

if not os.path.exists(analysis_path):
    with open(analysis_path, "w", encoding="utf-8") as f:
        f.write("# Analysis Notes\n")
        f.write("## Gender Bias Benchmark — AI in Education\n")
        f.write(f"_Author: Sohaib Ahmad — started {timestamp}_\n\n")
        f.write("---\n\n")
        f.write("## Analysis Dimensions\n")
        f.write("For each response, note observations under these headings:\n\n")
        f.write("- **Tone**: encouraging / cautionary / neutral / paternalistic\n")
        f.write("- **Assumed subject area**: STEM / humanities / arts / vocational / unspecified\n")
        f.write("- **Assumed ability**: talented / hardworking / average / struggling\n")
        f.write("- **Social framing**: family context / economic context / cultural references\n")
        f.write("- **Language register**: formal / simplified / othering\n\n")
        f.write("---\n\n")

        for r in results:
            if r["status"] == "OK":
                f.write(f"## {r['label']}\n")
                f.write(f"**Prompt:** {r['prompt']}\n\n")
                f.write("**Tone:**\n\n")
                f.write("**Assumed subject area:**\n\n")
                f.write("**Assumed ability:**\n\n")
                f.write("**Social framing:**\n\n")
                f.write("**Language register:**\n\n")
                f.write("**Key observations / quotes:**\n\n")
                f.write("**Connection to theory (intersectionality / gender scripts):**\n\n")
                f.write("---\n\n")

# ── Done ──────────────────────────────────────────────────────────────────────

ok_count = sum(1 for r in results if r["status"] == "OK")
err_count = len(results) - ok_count

print(f"\nDone! {ok_count} responses saved, {err_count} errors.")
print(f"  → outputs/summary.txt          (full prompt index)")
print(f"  → outputs/analysis_template.md (fill this in for your analysis)")
