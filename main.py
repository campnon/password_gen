import string
import random

class pass_gen:
  def __init__(self, length, char_sets):
    self.len = length
    self.char = char_sets

  def make_random_pass(self):
    stri = self.pass_options()
    if stri is False:
      return Exception("There was a problem with your settings please try again.")
    return ''.join(random.choices(stri, k=self.len))

  def pass_options(self):
    chars = self.char
    if chars == 1:
      stri = string.ascii_letters
    elif chars == 2:
      stri = string.ascii_letters + string.digits
    elif chars == 3:
      stri = string.ascii_letters + string.digits + "@#$%?!"
    else: 
      return False
      
    return stri  
  
if __name__ == '__main__':
  length = input("Please enter the Length of your Password: ")
  char_sets = input("Enter 1 for Letter, 2 for Letters and Numbers, Enter 3 for Letters, Numbers, And special characters") 
  main = pass_gen(int(length), int(char_sets))
  print(main.make_random_pass())
    