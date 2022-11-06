import string
import random

class Pass_Gen:
  def __init__(self):
    pass

  def Make_Random_Pass(self, reach, char_sets):
    try:
      self.reach = int(reach)
      self.char = int(char_sets)
    except: return Exception("One of the input was not a number, please try again")
    stri = self.Pass_Options()
    if stri is False:
      return Exception("There was a problem with your settings please try again.")
    return ''.join(random.choices(stri, k=self.reach))

  def Pass_Options(self):
    if self.char == 1:
      stri = string.ascii_letters
    elif self.char == 2:
      stri = string.ascii_letters + string.digits
    elif self.char == 3:
      stri = string.ascii_letters + string.digits + "@#$%?!"
    else: 
      return False
      
    return stri  
  
if __name__ == '__main__':
  length = input("Please enter the Length of your Password: ")
  char_sets = input("Enter 1 for Letter, 2 for Letters and Numbers, Enter 3 for Letters, Numbers, And special characters") 
  print(Pass_Gen().Make_Random_Pass(length, char_sets))
