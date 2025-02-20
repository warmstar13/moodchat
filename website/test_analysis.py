import unittest
from datetime import datetime
from .analysis import split_text_to_messages, Message

class TestAnalysis(unittest.TestCase):
    maxDiff = None  # Это отключит сокращение вывода различий
    
    def test_split_text_to_messages(self):
        text = "Александр Геннадьевич, [20.02.2025 17:16]\nHello, how are you?\n\nИван Иванович, [21.02.2025 18:17]\nI'm fine, thank you!"
        expected = [
            Message(datetime(2025, 2, 20, 17, 16), "Александр Геннадьевич", "Hello, how are you?\n"),
            Message(datetime(2025, 2, 21, 18, 17), "Иван Иванович", "I'm fine, thank you!\n")
        ]
        self.assertEqual(split_text_to_messages(text), expected)

    def test_split_text_to_messages_empty(self):
        text = ""
        expected = []
        self.assertEqual(split_text_to_messages(text), expected)

    def test_split_text_to_messages_single_message(self):
        text = "Александр Геннадьевич, [20.02.2025 17:16]\nHello, how are you?"
        expected = [
            Message(datetime(2025, 2, 20, 17, 16), "Александр Геннадьевич", "Hello, how are you?\n")
        ]
        self.assertEqual(split_text_to_messages(text), expected)

    def test_split_text_to_messages_no_content(self):
        text = "Александр Геннадьевич, [20.02.2025 17:16]\n\nИван Иванович, [21.02.2025 18:17]"
        expected = [
            Message(datetime(2025, 2, 20, 17, 16), "Александр Геннадьевич", "\n"),
            Message(datetime(2025, 2, 21, 18, 17), "Иван Иванович", "")
        ]
        self.assertEqual(split_text_to_messages(text), expected)

if __name__ == '__main__':
    unittest.main()
