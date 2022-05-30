# #WAP which infinitely print natural numbers. Raise
# the StopIteration exception after displaying first
# 20 numbers to exit from the program.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self 

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)