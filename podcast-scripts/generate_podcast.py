#!/usr/bin/env python3
"""Generate podcast MP3 from dialog JSON using edge-tts Python API."""

import json, sys, os, asyncio
import edge_tts

VOICES = {
    "host": "zh-CN-YunyangNeural",
    "cohost": "zh-CN-XiaoxiaoNeural",
}

async def synthesize(text, voice, out_file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(out_file)

async def generate_episode(dialog_file, output_mp3):
    with open(dialog_file) as f:
        lines = json.load(f)

    tmp_dir = os.path.join(os.path.dirname(output_mp3), "tmp_segments")
    os.makedirs(tmp_dir, exist_ok=True)

    segments = []
    for i, line in enumerate(lines):
        speaker = line["speaker"]
        text = line["text"]
        voice = VOICES.get(speaker, VOICES["cohost"])
        seg_file = os.path.join(tmp_dir, f"seg_{i:04d}.mp3")

        print(f"  [{i+1}/{len(lines)}] {speaker}: {text[:60]}...")
        try:
            await synthesize(text, voice, seg_file)
            segments.append(seg_file)
        except Exception as e:
            print(f"  FAILED: {e}")
            continue

    print(f"  Merging {len(segments)} segments...")
    with open(output_mp3, "wb") as out:
        for seg in segments:
            with open(seg, "rb") as f:
                out.write(f.read())

    for seg in segments:
        os.remove(seg)
    for f in os.listdir(tmp_dir):
        os.remove(os.path.join(tmp_dir, f))
    os.rmdir(tmp_dir)

    size_mb = os.path.getsize(output_mp3) / 1024 / 1024
    print(f"  Done: {output_mp3} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_podcast.py <dialog.json> <output.mp3>")
        sys.exit(1)
    asyncio.run(generate_episode(sys.argv[1], sys.argv[2]))
