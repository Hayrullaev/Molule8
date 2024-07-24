
def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print(str(a) + str(b))

add_everything_up(256.9, 'Hello')
add_everything_up("HI", 89)
add_everything_up(56, 90)
