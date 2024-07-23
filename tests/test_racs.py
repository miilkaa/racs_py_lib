import pytest
from src.racs import Racs

class ReadTests:
    def __init__(self):
        self.racs = Racs(
            resource="library_tests",
            dataset="python"
        )
    def test_read_by_id(self):
        pass