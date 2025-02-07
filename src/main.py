import argparse
from transcriber import MediaTranscriber

def main():
    parser = argparse.ArgumentParser(description='Media File Transcription Tool')
    parser.add_argument('input_dir', help='Input directory containing media files')
    parser.add_argument('output_dir', help='Output directory for transcriptions')
    parser.add_argument('--model', default='tiny', choices=['tiny', 'base', 'small', 'medium', 'large'],
                      help='Whisper model size to use (default: tiny)')
    
    args = parser.parse_args()
    
    # Initialize transcriber
    transcriber = MediaTranscriber(model_size=args.model)
    
    # Process files
    print(f"Starting transcription process...")
    print(f"Input directory: {args.input_dir}")
    print(f"Output directory: {args.output_dir}")
    print(f"Using model: {args.model}")
    
    results = transcriber.process_directory(args.input_dir, args.output_dir)
    
    # Print summary
    success_count = sum(1 for r in results if r['status'] == 'success')
    print("\nTranscription Summary:")
    print(f"Total files processed: {len(results)}")
    print(f"Successful transcriptions: {success_count}")
    print(f"Failed transcriptions: {len(results) - success_count}")

if __name__ == "__main__":
    main()