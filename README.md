# 📥 CLI Video Downloader

A lightweight, fast, and interactive command-line video and audio downloader built with Python. Powered by `yt-dlp` and styled with `rich`.

## 🚀 Features

- **Multi-Platform Support:** Automatically detects and downloads content from YouTube, TikTok, Instagram, and Twitter/X.
Disclaimer
This project is created strictly for educational purposes and personal offline media backup. Ensure you comply with the terms of service of the content platforms and copyright laws in your country.
- **Flexible Formats:**
  - `1`: Video only
  - `2`: Audio extraction (MP3 at 192 kbps)
  - `3`: Combined Video + Audio (Best available quality)
- **Clean Interface:** Modern CLI prompts, real-time download progress, and speed indicators.
- **Automatic Organization:** Saves downloaded media directly into a local `downloads/` directory.

## 🛠️ Prerequisites

This tool requires **FFmpeg** to process and merge media streams.

- **Windows (via Winget):**
  ```powershell
  winget install Gyan.FFmpeg

- Linux (Ubuntu/Debian):

sudo apt update && sudo apt install ffmpeg -y

- macOS (via Homebrew):

brew install ffmpeg

(Note: Restart your terminal after installation to update the PATH)


Installation : 
Clone the repository:

git clone [https://github.com/minddexst/downloads.git](https://github.com/minddexst/downloads.git)
cd nom-du-repo

Create and activate a virtual environment:

Windows:
PowerShell :
python -m venv venv
.\venv\Scripts\Activate.ps1

Linux / macOS:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the script:
windows: python main.py

Linux/MacOS : python3 main.py

License
Distributed under the MIT License. See LICENSE for more information.
