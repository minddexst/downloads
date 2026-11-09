# 📥 CLI Video Downloader

A lightweight, fast, and interactive command-line video and audio downloader built with Python. Powered by `yt-dlp` and styled with `rich`.

## 🚀 Features

- **Multi-Platform Support:** Automatically detects and downloads content from YouTube, TikTok, Instagram, and Twitter/X.
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