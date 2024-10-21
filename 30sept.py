"""
I have a meeting in ten minutes, and I'd love to sneak a little walk in. I can walk one city block per minute,
so I should be able to plan out a valid route. I'm representing my walk as an array of cardinal directions n, s, w, e.

Here is your challenge: Given an array of directions to walk, return true if the route will take me exactly 10 minutes
AND return me to my office.

Constraints:
A route will only contain the four cardinal directions. You don't need to worry about my ability to travel up and down,
my superpowers are a secret anyway

Test Cases:
With input ['n','s','n','s','n','s','n','s','n','s'], return true
With input ['w','e','w','e','w','e','w','e','w','e','w','e'], return false
With input ['n', 's', 'e', 'w', 's', 'e', 'n', 'w', 'w', 'e'], return true
With input ['w'], return false
With input ['n','n','n','s','n','s','n','s','n','s'], return false
"""
def execute_walk_successfully(start, directions):
    x, y = start
    for direction in directions:
        match direction.lower():  # Convert the direction to lowercase for case-insensitive comparison
            case "n":
                y += 1
            case "s":
                y -= 1
            case "e":
                x += 1
            case "w":
                x -= 1
            case _:
                raise ValueError(f"Invalid direction: {direction}")
    return (x, y) == start


# The route will take me exactly 10 minutes if the length of the array is 10
# The route will return me to the office if after updating my location coordinates
# following the directions in the input, the final position is (0, 0)
def valid_route(directions):
    return len(directions) == 10 and execute_walk_successfully(start=(0, 0), directions=directions)


if __name__ == "__main__":
    assert valid_route(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]) == True
    assert valid_route(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e", "w", "e"]) == False
    assert valid_route(["n", "s", "e", "w", "s", "e", "n", "w", "w", "e"]) == True
    assert valid_route(["w"]) == False
    assert valid_route(["n", "n", "n", "s", "n", "s", "n", "s", "n", "s"]) == False
