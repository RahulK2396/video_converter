# Video Converter

A simple tool to convert `.flv` video files to `.mp4` format.

## Features

- Converts FLV video files to MP4 format
- Easy to use
- Lightweight and fast

## Requirements

- Python 3.x
- [ffmpeg](https://ffmpeg.org/) installed and accessible in your system's PATH

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RahulK2396/video_converter.git
   cd video_converter
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install any required dependencies:

   *(Add if there is a requirements.txt file, otherwise skip)*

   ```bash
   pip install -r requirements.txt
   ```

4. Make sure `ffmpeg` is installed:

   - [Download ffmpeg](https://ffmpeg.org/download.html) and follow installation instructions for your OS.
   - Confirm installation by running:
     ```bash
     ffmpeg -version
     ```

## Usage

By default, this tool converts `.flv` files to `.mp4`. Assuming you have a script (e.g., `convert.py`) in this repo:

```bash
python convert.py input.flv output.mp4
```

Replace `convert.py` with the actual script name if different.

## Example

```bash
python convert.py sample.flv sample.mp4
```

## License

This project is licensed under the MIT License.

---

*Feel free to contribute or open issues for suggestions and bug reports!*