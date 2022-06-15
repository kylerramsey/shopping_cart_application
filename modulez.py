def square_footage():
    feet_length = float(input("How long is the room? (Number): "))
    feet_width = float(input("How wide is the room? (Number): "))

    print(feet_width * feet_length)

square_footage()


def circum():
    circle_radius = float(input("What is the radius of the circle (Number): "))
    print(circle_radius * 2 * 3.14)

circum()