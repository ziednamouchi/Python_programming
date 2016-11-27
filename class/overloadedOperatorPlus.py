#The Dog Class with Overloaded Addition
class Dog:
#constructor
 def __init__(self, name, month, day, year, speakText):
  self.name = name
  self.month = month
  self.day = day
  self.year = year
  self.speakText = speakText
#speakText accessor
 def speak(self):
  return self.speakText
#Name accessor
 def getName(self):
  return self.name
#birthdate accessor
 def birthDate(self):
  return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
#speakText mutator
 def changeBark(self,bark):
  self.speakText = bark
# When creating the new puppy we don’t know it’s birthday. Pick the first dog’s birthday plus one year.
#The speakText will be the concatenation of both dog’s text. The dog on the left side of the + operator is the object referenced by the "self" parameter.
#The "otherDog" parameter is the dog on the right side of the + operator.
 def __add__(self,otherDog):
  return Dog("Puppy of " + self.name + " and " + otherDog.name, \
   self.month, self.day,self.year + 1,\
   self.speakText + otherDog.speakText)
def main():
 boyDog = Dog("Mesa", 5, 15, 2004, "WOOOOF")
 girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
 print(boyDog.speak())
 print(girlDog.speak())
 print(boyDog.birthDate())
 print(girlDog.birthDate())
 boyDog.changeBark("woofywoofy")
 print(boyDog.speak())
 puppy = boyDog + girlDog
 print(puppy.speak())
 print(puppy.getName())
 print(puppy.birthDate())
if __name__ == "__main__":
 main()
