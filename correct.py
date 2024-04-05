import pyperclip

class Correct:
    def __init__(self):
        self.persian_to_english = {
  "ض": "q",
  "ص": "w",
  "ث": "e",
  "ق": "r",
  #"ژ": "Zh",
  "گ": r"'",
  "چ": "]",
  #"پ": "P",
  "ی": "d",
  "ک": r";",
  "ت": "j",
  "ب": "f",
  "ن": "k",
  "م": "l",
  "و": r",",
  "ه": "i",
  "خ": "o",
  "د": "n",
  "ز": "c",
  "ر": "v",
  "ا": "h",
  "ع": "u",
  "غ": "y",
  "ف": "t",
  "ل": "g",
  "ج":"[",
  "ح":"p",
  "ذ":"b",
  "س":"s",
  "ش":"a",
  "ط":"x",
  "ظ":"z",
    
}
        self.english_to_persian = {
  "q": "ض",
  "w": "ص",
  "e": "ث",
  "r": "ق",
  # "Zh": "ژ",  # Uncomment if you have "Zh" in the original dict
  "g'": "گ",  # Assuming ' is the apostrophe character
  # "P": "پ",  # Uncomment if you have "P" in the original dict
  "d": "ی",
  ";": "ک",
  "j": "ت",
  "f": "ب",
  "k": "ن",
  "l": "م",
  ",": "و",
  "i": "ه",
  "o": "خ",
  "n": "د",
  "c": "ز",
  "v": "ر",
  "h": "ا",
  "u": "ع",
  "y": "غ",
  "t": "ف",
  "g": "ل",
  "[": "ج",
  "p": "ح",
  "b": "ذ",
  "s": "س",
  "a": "ش",
  "x": "ط",
  "z": "ظ",
}
        #self.text = None


    def main(self):
        initial_text = self.get_from_clipboard()
        self.text = initial_text
        #lang = self.check_lang(text=initial_text)
        self.send_to_clipboard(self.correct(lang="persian"))

    def check_lang(self,text):
        my_tool = check_lang()
        return my_tool.is_persian_or_english(text)

        

    def correct(self,lang):
        
        text = list(self.text)
        
        if lang == "persian":
            for i in range(len(text)):
                if text[i] == " ":
                    continue
                text[i] = self.persian_to_english[text[i]]
        
            answer = ""
            for i in text:
                answer += i

            return answer
        
        
        elif lang == "english":
            pass

    def get_from_clipboard(self):
        clipboard = pyperclip.paste()
        return clipboard

    def send_to_clipboard(self,corrected_text):
        pyperclip.copy(corrected_text)



class check_lang:
    def is_persian(self,text):
        """
        Checks if a string is written in Persian.

        Args:
            text: The text to check.

        Returns:
            True if the text is in Persian, False otherwise.
        """
        persian_chars = "\u0600-\u06FF\u0750-\u077F"  # Basic Persian alphabet
        english_chars = "\0-9a-zA-Z"  # Letters and numbers

        persian_count = 0
        english_count = 0
        for char in text:
            if char in persian_chars:
                persian_count += 1
            elif char in english_chars:
                english_count += 1

        if persian_count > english_count:
            return "persian"
        elif english_count > persian_count:
            return "english"
        else:
            return "other"
    
        
        
    

    def is_english(self,text):
        """
        Checks if a string is written in English.

        Args:
            text: The text to check.

        Returns:
            True if the text is in English, False otherwise.
        """
        english_chars = "\u0041-\u005A\u0061-\u007A"
        
        for char in text:
            if char in english_chars:
                return True
        return False
        

    def is_persian_or_english(self,text):
        """
        Checks if a string is written in Persian or English.

        Args:
            text: The text to check.

        Returns:
            "persian" if the text is in Persian, "english" if the text is in English,
            or None otherwise.
        """
        if self.is_persian(text):
            return "persian"
        elif self.is_english(text):
            return "english"
        else:
            return None

    


