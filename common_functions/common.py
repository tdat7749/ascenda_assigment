IGNORE_STRING = {"WiFi"}

def convert_to_lowercase_with_spaces(string: str) -> str:
  string = string.strip()
  if string not in IGNORE_STRING:
      spaced_string = ""
      for i in range(len(string.strip())):
          if i > 0 and string[i].isupper():
              spaced_string += ' '
          spaced_string += string[i]

      return spaced_string.lower()
  else:
      return string.lower()
