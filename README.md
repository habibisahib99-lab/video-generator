# Video Generator

A Python-based tool to create videos from images with various effects and transitions.

## Features

- Convert static images to videos
- Add effects and transitions
- Customize video duration and frame rate
- Simple command-line interface

## Installation

### Prerequisites
- Python 3.8 or higher
- FFmpeg

### Setup

1. Clone the repository:
```bash
git clone https://github.com/habibisahib99-lab/video-generator.git
cd video-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python main.py --input image.jpg --output video.mp4 --duration 5
```

### Options

- `--input` or `-i`: Input image file path (required)
- `--output` or `-o`: Output video file path (default: output.mp4)
- `--duration` or `-d`: Video duration in seconds (default: 5)
- `--fps` or `-f`: Frames per second (default: 30)
- `--effect` or `-e`: Effect to apply (zoom, pan, fade, etc.)

### Examples

```bash
# Create a 10-second video with zoom effect
python main.py -i photo.jpg -o result.mp4 -d 10 -e zoom

# Create a video with pan effect
python main.py -i image.png -o video.mp4 -e pan -d 8
```

## Project Structure

```
video-generator/
├── main.py              # Main entry point
├── video_generator/     # Core module
│   ├── __init__.py
│   ├── generator.py     # Video generation logic
│   └── effects.py       # Effect definitions
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
