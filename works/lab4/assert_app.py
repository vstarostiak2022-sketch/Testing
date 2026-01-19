a = input("Enter a number: ")

assert a.isdigit(), "You must enter a number!"

a = int(a)
assert a > 0, "The number must be greater than 0!"

print(f"Entered number: {a}")


class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Length must be greater than 0!"
        assert type in ["square", "rectangle", "triangle"], \
            "Allowed figures: square, rectangle, triangle"
        self.type = type
        self.length = length


print("\nTesting Figure class:")
c = Figure("square", 1)
print(c.type, c.length)


class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Vadim", "Anonymous"]:
            raise ValueError("Allowed names: Vadim, Anonymous")
        if not hobby:
            raise ValueError("Hobby must not be empty!")
        self.name = name
        self.hobby = hobby


print("\nTesting Name class:")
b = Name("Vadim", "programming")
print(b.name, "-", b.hobby)
