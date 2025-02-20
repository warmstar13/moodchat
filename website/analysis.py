from pathlib import Path
import os
import nltk
import re
from datetime import datetime

class Message:
    def __init__(self, date, sender, content=None):
        self.date = date
        self.sender = sender
        self.content = content

    def add_content(self, content):
        self.content = content

    def __repr__(self):
        return f"Message(date={self.date!r}, sender={self.sender!r}, content={self.content!r})"

    def __eq__(self, other):
        if not isinstance(other, Message):
            return NotImplemented
        return (self.date == other.date and 
                self.sender == other.sender and 
                self.content == other.content)

def analyze_chat(chat_file):
    filename, file_extension = os.path.splitext(chat_file.name)
    if file_extension == '.txt':
        text = chat_file.read().decode('utf-8')
        messages_list = split_text_to_messages(text)
        return messages_list

    return "Invalid file type. Please upload a .txt file."

def split_text_to_messages(text):
    strings = text.split("\n")
    regex = r'(.+?), \[(\d{2}\.\d{2}\.\d{4}, \d{2}:\d{2})\]'
    content = ""
    messages = []
    cur_message = None
    for string in strings:
        match = re.search(regex, string)
        if match:
            if cur_message is not None:
                if content != "":
                    content = content.rstrip('\n') + '\n'
                cur_message.add_content(content)
                messages.append(cur_message)
            content = ""
            sender = match.group(1)
            date_str = match.group(2)
            date = datetime.strptime(date_str, '%d.%m.%Y, %H:%M')
            cur_message = Message(date, sender)
        else:
            if cur_message is not None:
                content += string + '\n'
    if cur_message is not None:
        if content != "":
            content = content.rstrip('\n') + '\n'
        cur_message.add_content(content)
        messages.append(cur_message)
            
    return messages