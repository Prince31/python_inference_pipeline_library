import pytest
import python_inference_pipeline_library.utility as utility

class TestUtility:

    def test_load_csv(self):
        result = utility.Utility().load_csv("assets/sample.csv")
        assert result == "891"

    def test_load_json(self):
        result = utility.Utility().load_json("assets/sample.json")
        assert result == "Inserted Column"