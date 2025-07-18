import os
import subprocess
import logging
from pathlib import Path

# ========== CONFIGURATION ==========
INPUT_DIR = "flv_files"          # Folder containing .flv files
OUTPUT_DIR = "mp4_output"        # Where .mp4 files will be stored
THUMBNAIL_DIR = "thumbnails"     # Where thumbnails will be stored
LOG_FILE = "conversion.log"      # Log file path
FFMPEG_PATH = "C:\\ffmpeg\\bin\\ffmpeg.exe"  # Use full path if ffmpeg not in PATH
# ===================================

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def convert_flv_to_mp4(input_path, output_path):
    try:
        # FFmpeg command to convert FLV to MP4
        command = [
            FFMPEG_PATH,
            "-i", str(input_path),
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "23",
            "-c:a", "aac",
            "-b:a", "128k",
            "-y",
            str(output_path)
        ]
        subprocess.run(command, check=True)
        logging.info(f"Successfully converted: {input_path} -> {output_path}")
        print(f"✅ Converted: {input_path.name}")

    except subprocess.CalledProcessError as e:
        logging.error(f"FFmpeg failed for {input_path}: {e}")
        print(f"❌ Failed: {input_path.name}")

def generate_thumbnail(input_path, thumbnail_path):
    try:
        # FFmpeg command to generate thumbnail at 5 seconds
        command = [
            FFMPEG_PATH,
            "-ss", "00:00:05",
            "-i", str(input_path),
            "-vframes", "1",
            "-q:v", "2",
            "-y",
            str(thumbnail_path)
        ]
        subprocess.run(command, check=True)
        logging.info(f"Thumbnail created: {thumbnail_path}")
        print(f"🖼️  Thumbnail created: {thumbnail_path.name}")

    except subprocess.CalledProcessError as e:
        logging.error(f"Thumbnail generation failed for {input_path}: {e}")
        print(f"⚠️  Thumbnail failed: {input_path.name}")

def batch_convert():
    input_dir = Path(INPUT_DIR)
    output_dir = Path(OUTPUT_DIR)
    thumbnail_dir = Path(THUMBNAIL_DIR)

    output_dir.mkdir(parents=True, exist_ok=True)
    thumbnail_dir.mkdir(parents=True, exist_ok=True)

    flv_files = list(input_dir.glob("*.flv"))

    if not flv_files:
        print("No .flv files found.")
        return

    print(f"Found {len(flv_files)} FLV files. Starting conversion...\n")

    for flv_file in flv_files:
        output_file = output_dir / f"{flv_file.stem}.mp4"
        thumbnail_file = thumbnail_dir / f"{flv_file.stem}.jpg"

        convert_flv_to_mp4(flv_file, output_file)
        generate_thumbnail(flv_file, thumbnail_file)

    print("\n🎉 All conversions and thumbnails completed!")

if __name__ == "__main__":
    batch_convert()

    # Remove all .flv files after conversion
    flv_files = list(Path(INPUT_DIR).glob("*.flv"))
    for flv_file in flv_files:
        flv_file.unlink()