# Program to swap cases in a given string (e.g., "Hello World" -> "hELLO wORLD")
text = input("Enter a string: ")
toggled_text = ""

for char in text:
    if char.isupper():
        toggled_text += char.lower()
    elif char.islower():
        toggled_text += char.upper()
    else:
        toggled_text += char  # Keep spaces or special characters as they are

print(f"Original: {text}")
print(f"Toggled:  {toggled_text}")
