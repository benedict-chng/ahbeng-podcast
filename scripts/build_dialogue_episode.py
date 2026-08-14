#!/usr/bin/env python3
"""Two-host dialogue TTS builder (Kokoro: Jessica af_jessica + Echo am_echo).

Usage:
  PIP_BREAK_SYSTEM_PACKAGES=1 python3 build_dialogue_episode.py <script.json> <output.mp3>

script.json = [{"s": "MAYA"|"GUY", "t": "line text", "gap": 0.0-0.4}, ...]
  MAYA = Jessica (af_jessica), GUY = Echo (am_echo)

Output: 64kbps mono mp3 (podcast standard).
"""
import json, subprocess, os, sys, tempfile

import soundfile as sf
import numpy as np
from kokoro import KPipeline

pipeline = KPipeline(lang_code='a')  # American English

VOICES = {"MAYA": "af_jessica", "GUY": "am_echo"}

script_path, out_path = sys.argv[1], sys.argv[2]

with open(script_path) as f:
    lines = json.load(f)

workdir = tempfile.mkdtemp(prefix="kokoro_ep_")
os.chdir(workdir)
files = []
for i, line in enumerate(lines):
    wav = f"kok_{i:03d}.wav"
    chunks = []
    for gs, ps, audio in pipeline(line["t"], voice=VOICES[line["s"]], speed=1.05):
        chunks.append(audio if isinstance(audio, np.ndarray) else audio.numpy())
    full = np.concatenate(chunks)
    sf.write(wav, full, 24000)
    files.append(wav)
    ms = int(line.get("gap", 0.15) * 1000)
    if ms > 0:
        sil = f"ksil_{i:03d}.wav"
        sf.write(sil, np.zeros(int(24000 * ms / 1000), dtype=np.float32), 24000)
        files.append(sil)
    print(f"line {i+1}/{len(lines)}: {line['s']} {len(full)/24000:.1f}s", flush=True)

with open("klist.txt", "w") as f:
    for fn in files:
        f.write(f"file '{fn}'\n")

subprocess.run(["/home/benedict/.local/bin/ffmpeg", "-y", "-v", "error",
                "-f", "concat", "-safe", "0", "-i", "klist.txt",
                "-c:a", "libmp3lame", "-b:a", "64k", "-ar", "44100", "-ac", "1",
                out_path], check=True)
dur = subprocess.run(["/home/benedict/.local/bin/ffprobe", "-v", "error",
                      "-show_entries", "format=duration", "-of", "csv=p=0", out_path],
                     capture_output=True, text=True).stdout.strip()
print(f"DONE {out_path} ({os.path.getsize(out_path)/1e6:.1f} MB, {float(dur):.0f}s)")
