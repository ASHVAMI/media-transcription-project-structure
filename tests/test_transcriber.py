import unittest
import os
import tempfile
import shutil
from src.transcriber import MediaTranscriber

class TestMediaTranscriber(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.output_dir = tempfile.mkdtemp()
        self.transcriber = MediaTranscriber()

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        shutil.rmtree(self.output_dir)

    def test_is_media_file(self):
        self.assertTrue(self.transcriber.is_media_file('test.mp3'))
        self.assertTrue(self.transcriber.is_media_file('test.MP3'))
        self.assertTrue(self.transcriber.is_media_file('test.wav'))
        self.assertFalse(self.transcriber.is_media_file('test.txt'))

    def test_scan_directory(self):
        # Create test files
        test_files = ['test1.mp3', 'test2.wav', 'test3.txt']
        for file in test_files:
            with open(os.path.join(self.test_dir, file), 'w') as f:
                f.write('test')

        media_files = self.transcriber.scan_directory(self.test_dir)
        self.assertEqual(len(media_files), 2)  # Should find 2 media files

if __name__ == '__main__':
    unittest.main()