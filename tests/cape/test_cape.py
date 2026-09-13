import unittest

from cape.cape import evaluate_access


class TestCAPE(unittest.TestCase):

    def test_p01_missing_input(self):
        result = evaluate_access("SENSITIVE", "", "TRUSTED")
        self.assertEqual(result[0], "BLOCK")
        self.assertEqual(result[1], "CAPE-P01")

    def test_p01_invalid_input(self):
        result = evaluate_access("SENSITIVE", "ADNAN", "TRUSTED")
        self.assertEqual(result[0], "BLOCK")
        self.assertEqual(result[1], "CAPE-P01")

    def test_p02_untrusted_device(self):
        result = evaluate_access("SENSITIVE", "UNTRUSTED", "TRUSTED")
        self.assertEqual(result[0], "BLOCK")
        self.assertEqual(result[1], "CAPE-P02")

    def test_p03_external_network(self):
        result = evaluate_access("SENSITIVE", "TRUSTED", "EXTERNAL")
        self.assertEqual(result[0], "REQUIRE_REAUTHENTICATION")
        self.assertEqual(result[1], "CAPE-P03")

    def test_p04_allow(self):
        result = evaluate_access("STANDARD", "TRUSTED", "TRUSTED")
        self.assertEqual(result[0], "ALLOW")
        self.assertEqual(result[1], "CAPE-P04")

    def test_policy_priority(self):
        result = evaluate_access("SENSITIVE", "UNTRUSTED", "EXTERNAL")
        self.assertEqual(result[0], "BLOCK")
        self.assertEqual(result[1], "CAPE-P02")
        
    if __name__ == "__main__":
        unittest.main()
        
        


