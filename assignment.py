# a program to check whether an year is aleap year or not

year =2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010
for year in range(2000,2010):
  if year % 4==0:
     print(year,"is a leap year")
  else:
    print(year," is not a leap year")



# a program to check whether a letter is a consonant or a vowel


letters = "a"
letters_list= letters.split(",")

vowels = "aeiou"

for letter in letters_list :
  if letter in vowels :
    print(letter,"is a vowel")
  else:
    print(letter,"is a consonant")
