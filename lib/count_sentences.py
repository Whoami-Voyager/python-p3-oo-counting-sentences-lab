#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  def get_value(self):
    return self._value
  def set_value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
  value = property(get_value, set_value)

  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
    wordlist = self.value.split()
    count = 0
    for word in wordlist:
      if word.endswith(".") or word.endswith("?") or word.endswith("!"):
        count += 1
    return count

testing = MyString(
  value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
  )
