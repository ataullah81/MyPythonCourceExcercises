#  capitalize() - Converts the first character to upper case

txt = "ataullah"
print(txt.capitalize())  # Ataullah

#  casefold() - Converts string into lower case
txt = "ATAULLAH"
print(txt.casefold())  # ataullah

#  center() - Returns a centered string
txt = "I am Ataullah"
print(txt.center(20, "-"))   #---I am Ataullah----

#  count() -  Returns the number of times a specified value occurs in a string
txt = "Pythin is fun"
print(txt.count("i")) # 2

#  encode() - Returns an encoded version of the string
txt = "Hyvä päivä"
print(txt.encode()) # b'Hyv\xc3\xa4 p\xc3\xa4iv\xc3\xa4'

txt = "Hyvä Päivä"
print(txt.encode(encoding="ascii", errors="backslashreplace")) # b'Hyv\\xe4 P\\xe4iv\\xe4'

#  endswith() - Returns true if the string ends with the specified value
txt = "Ataullah"
print(txt.endswith("h")) # True
print(txt.endswith("A")) # False

#  expandtabs() - Sets the tab size of the string
txt = "Python\tis\tfun"
print(txt.expandtabs(10)) # Python    is        fun

#  find() - Searches the string for a specified value and returns the position of where it was found
txt = "I love my country Bangladesh"
print(txt.find("y")) # 7
print(txt.find("B")) # 18

#  format() - Formats specified values in a string
txt = "I want to buy a house with {price:.2f} euros." #I want to buy a house with 90000.00 euros.
print(txt.format(price=90000))

#  format_map() - Formats specified values in a string
value = {'a': 'to', 'b': 'house', 'c': 80000}
txt = "I want {a} buy a {b} with {c} euros." #I want to buy a house with 80000.00 euros.
print(txt.format_map(value))

#  index() -  Searches the string for a specified value and returns the position of where it was found
txt = "Living abroad is not fun"
print(txt.index('i')) # 1
print(txt.index('r', 5, 20)) # 9

#  isalnum() -  Returns True if all characters in the string are alphanumeric
txt = "I love Bangladesh"
print(txt.isalnum()) # False
txt = "SkyIsBlue"
print(txt.isalnum()) # True

#  isalpha() -  Returns True if all characters in the string are in the alphabet
txt = 'I love Bangladesh'
print(txt.isalpha()) # False because of 2 whitespace
txt = 'Country2'
print(txt.isalpha()) # False because of number 2
txt = 'Country'
print(txt.isalpha()) # True

#  isdecimal() -  Returns True if all characters in the string are decimals
txt = 'Bangladesh'
print(txt.isdecimal()) # False
txt = "3"
print(txt.isdecimal()) # True

#  isdigit() -  Returns True if all characters in the string are digits
txt = 'Bangladesh'
print(txt.isdigit()) # False
txt = '310'
print(txt.isdigit()) # True

#  isidentifier() - Returns True if the string is an identifier
txt = 'Bangladesh'
print(txt.isidentifier()) #True
txt = '10Bangladesh'
print(txt.isidentifier()) #False because identifier cannot start with a number

#  islower() -  Returns True if all characters in the string are lower case
txt = "Ataullah"
print(txt.islower()) # False
txt = "ataullah"
print(txt.islower()) # True

#  isnumeric() -  Returns True if all characters in the string are numeric
txt = '310121'
print(txt.isnumeric()) # True

#  isprintable() -  Returns True if all characters in the string are printable
txt = "Hello here!"
print(txt.isprintable()) # True
txt = "Hello \t here!"
print(txt.isprintable()) # False //because tap is not printable

#  isspace() -  Returns True if all characters in the string are whitespaces
txt = 'I love Bangladesh'
print(txt.isspace()) #False
txt = '   '
print(txt.isspace()) #True

#  istitle() -  Returns True if the string follows the rules of a title
txt = 'I Love Bangladesh'
print(txt.istitle()) # True
txt = 'I love Bangladesh'
print(txt.istitle()) # False //because love did not start with capital letter, did not meet title rule

#  isupper() -  Returns True if all characters in the string are upper case
txt = 'Bangladesh'
print(txt.isupper()) # False
txt = 'BANGLADESH'
print(txt.isupper()) # True

#  join() - Joins the elements of an iterable to the end of the string
txt = 'I Love Bangladesh'
print("-".join(txt))  #I- -L-o-v-e- -B-a-n-g-l-a-d-e-s-h

#  ljust() -  Returns a left justified version of the string
txt = "Bangladesh"
print(txt.ljust(20, 'o')) # Bangladeshoooooooooo

#  lower() -  Converts a string into lower case
txt = "Bangladesh"
print(txt.lower()) #bangladesh

#  lstrip() - Returns a left trim version of the string
txt = '    I Love Bangladesh   and'
print(txt.lstrip())  #I Love Bangladesh   and

#  maketrans() -  Returns a translation table to be used in translations
txt = "Hello Auti"
x= txt.maketrans("A","i")
print(txt.translate(x))  #Hello iuti

#  partition() -  Returns a tuple where the string is parted into three parts
txt = 'I love Bangladesh'
print(txt.partition('love')) #('I ', 'love', ' Bangladesh')

##  replace() -  Returns a string where a specified value is replaced with a specified value
txt = 'I love Bangladesh'
print(txt.replace('Bangladesh', 'Finland')) #I love Finland

#  rfind() -  Searches the string for a specified value and returns the last position of where it was found
txt = "I love my country Bangladesh"
print(txt.rfind('my')) #7

#  rindex() - Searches the string for a specified value and returns the last position of where it was found
txt = "I love my country Bangladesh"
print(txt.rfind('love')) #2

#  rjust() -  Returns a right justified version of the string
txt = "Bangladesh"
print(txt.rjust(20, 'o')) # ooooooooooBangladesh

#  rpartition() - Returns a tuple where the string is parted into three parts
txt="I live in Finland but I love Bangladesh"
print(txt.rpartition('but')) #('I live in Finland ', 'but', ' I love Bangladesh')

#  rsplit() - Splits the string at the specified separator, and returns a list
txt="I live in Finland, but, I love Bangladesh"
print(txt.rsplit(","))  #['I live in Finland', ' but', ' I love Bangladesh']

#  rstrip() - Returns a right trim version of the string
txt = 'Lovesssss'
print(txt.rstrip("s"))  #Love

#  split() -  Splits the string at the specified separator, and returns a list
txt="I live in Finland but I love Bangladesh"
print(txt.split()) #['I', 'live', 'in', 'Finland', 'but', 'I', 'love', 'Bangladesh']

txt="I-live-in-Finland-but-I-love-Bangladesh"
print(txt.split("-")) #['I', 'live', 'in', 'Finland', 'but', 'I', 'love', 'Bangladesh']

#  splitlines() - Splits the string at line breaks and returns a list
txt="I live in Finland but I love \nBangladesh"
print(txt.splitlines()) # ['I live in Finland but I love ', 'Bangladesh']

#  startswith() - Returns true if the string starts with the specified value
txt = "I love my country Bangladesh"
print(txt.startswith("I")) #True

txt = "I love my country Bangladesh"
print(txt.startswith("B")) #False

#  strip() -  Returns a trimmed version of the string
txt = ",,,,,,,,,Hello,,,,///"
print(txt.strip(",/"))  #Hello

#  swapcase() - Swaps cases, lower case becomes upper case and vice versa
txt = "I love my country Bangladesh"
print(txt.swapcase()) #i LOVE MY COUNTRY bANGLADESH

#  title() -  Converts the first character of each word to upper case
txt = "I love my country Bangladesh"
print(txt.title()) # I Love My Country Bangladesh

#  translate() -  Returns a translated string
txt = "I love my country"
print(txt.translate("country")) # Need to practice more

#  upper() -  Converts a string into upper case
txt = "I love my country"
print(txt.upper()) #I LOVE MY COUNTRY

#  zfill() -  Fills the string with a specified number of 0 values at the beginning
txt = "82"
print(txt.zfill(10)) #0000000082

