from src.pipeline import *
import json
import pytest

class TestSaveJson:

    # Test for sucesfful JSON saving
    def test_save_json_sucess(self, tmp_path, monkeypatch):
        data = {
            "type": "fuel",
            "content": "Sample receipt content"
        }
        filename = "test_items_receipt.json"

        # Use tmp_path as the base directory for saving files
        monkeypatch.chdir(tmp_path)

        # Call the save_json function
        save_json(data, filename)

        # Verify that the file was created in the correct directory
        expected_path = tmp_path / "xraw-data" / "processed" / "fuel" / filename
        assert expected_path.exists()

        # Verify the content of the saved JSON file
        with open(expected_path, "r") as file:
            saved_data = json.load(file)
            assert saved_data == data


    # Test for missing type in data
    def test_save_json_missing_type(self):
        data = {
            "content": "sample receipt content"
        }
        
        with pytest.raises(ValueError, match="Missing Type in data"):
            save_json(data, "fail.json")