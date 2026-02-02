from src.pipeline import * 
from pathlib import Path
from unittest.mock import patch, MagicMock, call
import pytest


class TestProcess:
    
    # Test for succesful folder processing
    def test_folder_success(self, tmp_path):
        
        # Create fake image files in tmp_path
        img1 = tmp_path / "receipt1.png"
        img2 = tmp_path / "receipt2.png"
        img1.touch()
        img2.touch()
        
        fake_text = "EXTRACTED\nFROM_OCR\n"
        fake_parsed = {"type": "fuel"}

        # Mock parser
        parser = MagicMock()
        parser.parse.return_value = fake_parsed.copy()
        
        # Mock OCR and save_json
        with patch("src.pipeline.main.ocr_image", return_value=fake_text) as mock_ocr, \
             patch("src.pipeline.main.save_json") as mock_save_json:
            
            process_folder(parser, tmp_path)
        

        # OCR called once per file
        assert mock_ocr.call_count == 2

        # parser.parse(text)
        parser.parse.assert_has_calls([
            call(fake_text),
            call(fake_text) 
        ])
        
        # raw_ocr & save_json(data, filename)
        mock_save_json.assert_has_calls([
            
            call(
                {
                    "type": "fuel",
                    "raw_ocr": ["EXTRACTED\n", "FROM_OCR\n"]
                },
                "receipt1"
            ),
            call(
                {
                    "type": "fuel",
                    "raw_ocr": ["EXTRACTED\n", "FROM_OCR\n"]
                },
                "receipt2"
            ),
        ], any_order=True)

    # Test folder does not exist
    def test_folder_missing(self):
        fake_folder = Path("noFolder")

        with pytest.raises(FileNotFoundError):
            process_folder(parser=object(), folder=fake_folder)



    # Test for successful file processing
    def test_file_sucess(self, tmp_path):

        file = tmp_path / "receipt.png"
        file.touch()

        fake_text = "EXTRACTED\nFROM_OCR\n"
        fake_parsed = {"type": "items"}

        # Mock parser
        parser = MagicMock()
        parser.parse.return_value = fake_parsed.copy()

        # Mock OCR and save_json
        with patch("src.pipeline.main.ocr_image", return_value=fake_text) as mock_ocr, \
             patch("src.pipeline.main.save_json") as mock_save_json:
            
            process_file(parser, file)
        

        # OCR called correctly
        mock_ocr.assert_called_once_with(file)

        # Parser called correctly
        parser.parse.assert_called_once_with(fake_text)\
        
        # Save json called with data
        mock_save_json.assert_called_once_with(
            {
                "type": "items",
                "raw_ocr": ["EXTRACTED\n", "FROM_OCR\n"]
            },
            "receipt"
        )

    # Test file does not exist
    def test_file_missing(self):
        fake_file = Path("missing.png")

        with pytest.raises(FileNotFoundError):
            process_file(parser=object(), file=fake_file)