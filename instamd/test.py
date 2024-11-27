import unittest

from instamd.script import extract_text


class Test_Extracting_Text(unittest.TestCase):

    def test_extracting_text(self):
        orig_md = """
#tag1 #tag2

Introduction

![[Image 1]]

Some paragraph

![[Image 2]]
"""
        extracted_text = extract_text(orig_md)
        print(extracted_text)


if __name__ == "__main__":
    unittest.main()
