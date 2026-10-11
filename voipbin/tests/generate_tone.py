#!/usr/bin/env python3
"""Generate the fixed-frequency test tone used by the VoIPBin recording
direction E2E monitoring test (voipbin/monorepo-monitoring,
sip-validator/test_sip_recording_direction.py).

Output: tone_1000hz_5s-mono_16bit_8khz_pcm.wav
  - 1000 Hz sine, 5.0 s, 8 kHz, mono, 16-bit PCM
  - amplitude 12000 (about -8.7 dBFS), 20 ms linear fade in/out

Deterministic: stdlib only, no randomness. Re-run to reproduce the file
byte for byte (written next to this script unless --output-dir is given):

    python3 generate_tone.py [--output-dir DIR]
"""
import argparse
import math
import os
import struct
import wave

FREQUENCY_HZ = 1000
DURATION_SEC = 5.0
SAMPLE_RATE = 8000
AMPLITUDE = 12000
FADE_SEC = 0.02
FILENAME = "tone_1000hz_5s-mono_16bit_8khz_pcm.wav"


def main():
    parser = argparse.ArgumentParser(description="Generate the 1000 Hz recording test tone.")
    parser.add_argument("--output-dir", default=os.path.dirname(os.path.abspath(__file__)),
                        help="directory to write the WAV into (default: next to this script)")
    args = parser.parse_args()

    total = int(SAMPLE_RATE * DURATION_SEC)
    fade = int(SAMPLE_RATE * FADE_SEC)
    frames = bytearray()
    for i in range(total):
        gain = 1.0
        if i < fade:
            gain = i / fade
        elif i >= total - fade:
            gain = (total - 1 - i) / fade
        value = int(round(AMPLITUDE * gain * math.sin(2 * math.pi * FREQUENCY_HZ * i / SAMPLE_RATE)))
        frames += struct.pack("<h", value)

    os.makedirs(args.output_dir, exist_ok=True)
    path = os.path.join(args.output_dir, FILENAME)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(bytes(frames))
    print(f"wrote {path} ({total} samples)")


if __name__ == "__main__":
    main()
