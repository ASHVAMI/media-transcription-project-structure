# Media Transcription Tool

A Python tool for batch transcription of audio and video files using OpenAI's Whisper model.

## Features

- Recursive directory scanning for media files
- Support for multiple audio/video formats
- Configurable Whisper model size
- JSON output format with timestamps
- Progress tracking with tqdm
- Error handling and reporting

## Requirements

- Python 3.8+
- FFmpeg (system requirement)
- Dependencies listed in requirements.txt

## Installation

1. Install FFmpeg on your system:
   - Ubuntu/Debian: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`
   - Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html)

2. Install Python dependencies:
   pip install -r requirements.txt

## Usage

Run the script from the command line:
python src/main.py /path/to/input/directory /path/to/output/directory --model tiny

Arguments:
- `input_dir`: Directory containing media files to transcribe
- `output_dir`: Directory where transcription files will be saved
- `--model`: Whisper model size (tiny, base, small, medium, large)

## Output Format

Transcriptions are saved as JSON files with the following structure:

{
  "text": "Complete transcription text",
  "segments": [
    {
      "start": 0.0,
      "end": 2.5,
      "text": "Segment text"
    }
  ],
  "timestamp": "2024-02-29T12:00:00"
}

## Testing

Run the test suite:

python -m unittest discover tests

## Limitations

- Processing time depends on the model size and file length
- Large files may require significant memory
- GPU acceleration recommended for larger models

## License

MIT License


Developed by Ashvani S !!!!!
