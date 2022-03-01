def triangle():
    print("Triangles")
    return 0

running = True
while running:
    triangle()
    response = 0
    while response !="No":
        response = input("Again?")
        if response == "Yes":
            break
        elif response == "No":
            print("Alright")
            running = 0
            break