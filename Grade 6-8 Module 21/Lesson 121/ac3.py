class Parrot:
  species = "bird"

  def __init__(self, name, age):
    self.name = name
    self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("woo", 10)

print("Blu name is ",blu.name)
print("woo name is ",woo.name)

print("Blu age is ",blu.age)
print("Woo age is ",woo.age)