from translate import Translator

lang = input("Enter the to-language : ")
text = input("Enter the text : ")

translator = Translator(to_lang=lang)
output = translator.translate(text)

print(output)