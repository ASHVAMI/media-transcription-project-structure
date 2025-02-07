import os
import json
from datetime import datetime
import whisper
from tqdm import tqdm

class MediaTranscriber:
    def __init__(self, model_size="tiny"):
        """Initialize the transcriber with the specified model size."""
        self.model = whisper.load_model(model_size)
        self.supported_formats = ('.mp3', '.mp4', '.wav', '.m4a', '.wma', '.aac')

    def is_media_file(self, filename):
        """Check if the file is a supported media format."""
        return filename.lower().endswith(self.supported_formats)

    def scan_directory(self, input_dir):
        """Recursively scan directory for media files."""
        media_files = []
        for root, _, files in os.walk(input_dir):
            for file in files:
                if self.is_media_file(file):
                    full_path = os.path.join(root, file)
                    media_files.append(full_path)
        return media_files

    def transcribe_file(self, file_path):
        """Transcribe a single media file."""
        try:
            result = self.model.transcribe(file_path)
            return {
                'text': result['text'],
                'segments': result['segments'],
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def save_transcription(self, transcription, file_path, output_dir):
        """Save transcription results to JSON file."""
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}_transcription.json")
        
        os.makedirs(output_dir, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(transcription, f, ensure_ascii=False, indent=2)
        
        return output_path

    def process_directory(self, input_dir, output_dir):
        """Process all media files in the input directory."""
        media_files = self.scan_directory(input_dir)
        results = []
        
        print(f"Found {len(media_files)} media files to process")
        
        for file_path in tqdm(media_files, desc="Processing files"):
            print(f"\nTranscribing: {file_path}")
            transcription = self.transcribe_file(file_path)
            output_path = self.save_transcription(transcription, file_path, output_dir)
            results.append({
                'input_file': file_path,
                'output_file': output_path,
                'status': 'error' if 'error' in transcription else 'success'
            })
        
        return results