import pytest
import python_inference_pipeline_library.utility as utility

class TestUtility:

    def test_load_csv(self):
        result = utility.Utility().load_csv("sample.csv")
        assert result == "PassengerId"