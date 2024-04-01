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


    def main(self):
        initial_text = self.get_from_clipboard()
        lang = self.check_lang(text=initial_text)
        self.correct(lang=lang)

    def check_lang(self,text):
        my_tool = check_lang()
        return my_tool.is_persian_or_english(text)

        

    def correct(self,lang):
        if lang == "persian":
            pass
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
        persian_chars = "\u0600-\u06FF\u0750-\u077F\uFB8A-\uFB8E\uFB8F-\uFBAD\uFBD3-\uFD3D\uFD50-\uFDFC\uFBE8-\uFBEF"
        
        for char in text:
            if char in persian_chars:
                return True
        return False
        
        
    

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

    