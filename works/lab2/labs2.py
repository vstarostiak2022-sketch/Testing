from random import randint
a = "text variable"   
b = 1             
b1 = 1.1            
c = ["a", 1, 1.25, "Word", a]
d = {"a": "Word", "b": 1, a: b}
e = ("a", a)
f = {"ss", a + str(b)}
print("a =", a)
print("b =", b)
print("b1 =", b1)
print("c =", c)
print("d =", d)
print("e =", e)
print("f =", f)
#завдання 2 
print("First constant:", True)
print("Second constant:", False)
print(f"Third constant using f-string: {None}")
#3
num = 3.14159
print("round(3.14159, 2) =", round(num, 2))
#4
count = 0
while count < 3:
    print(f"While loop count: {count}")
    count += 1
#5
num = randint(0, 1)
if num:
    print(f"So num = {num}")
else:
    print(f"But num could also be {num}")

print("\n---\n")
#6 
try:
    num = int("abc")
except ValueError as e:
    print("Caught a value error >", e)
finally:
    print("Conversion attempt finished.")
#7
class DummyResource:
    def __enter__(self):
        print("Resource acquired")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released")

with DummyResource() as resource:
    print("Using the resource")
#8
greet = lambda name: f"Hello, {name}!"
print(greet("Vadim"))
