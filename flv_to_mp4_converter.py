import os
import subprocess
import logging
from pathlib import Path

# ========== CONFIGURATION ==========
INPUT_DIR = "flv_files"          # Folder containing .flv files
OUTPUT_DIR = "mp4_output"        # Where .mp4 files will be stored
LOG_FILE = "conversion.log"      # Log file path
FFMPEG_PATH = "C:\\ffmpeg\\bin\\ffmpeg.exe"
          # Use full path if ffmpeg not in PATH
# ===================================

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def convert_flv_to_mp4(input_path, output_path):
    try:
        # Build ffmpeg command
        command = [
            FFMPEG_PATH,
            "-i", str(input_path),
            "-c:v", "libx264",        # Use H.264 video codec
            "-preset", "fast",        # Speed/quality trade-off
            "-crf", "23",             # Constant Rate Factor (lower = better quality)
            "-c:a", "aac",            # Use AAC audio codec
            "-b:a", "128k",           # Audio bitrate
            "-y",                     # Overwrite output files without asking
            str(output_path)
        ]

        subprocess.run(command, check=True)
        logging.info(f"Successfully converted: {input_path} -> {output_path}")
        print(f"✅ Converted: {input_path.name}")

    except subprocess.CalledProcessError as e:
        logging.error(f"FFmpeg failed for {input_path}: {e}")
        print(f"❌ Failed: {input_path.name}")

def batch_convert():
    input_dir = Path(INPUT_DIR)
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    flv_files = list(input_dir.glob("*.flv"))

    if not flv_files:
        print("No .flv files found.")
        return

    print(f"Found {len(flv_files)} FLV files. Starting conversion...\n")

    for flv_file in flv_files:
        output_file = output_dir / f"{flv_file.stem}.mp4"
        convert_flv_to_mp4(flv_file, output_file)

    print("\n🎉 All conversions completed!")
    

if __name__ == "__main__":
    batch_convert()
