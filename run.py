import search
import token

fplay = token.playz()
# gives the choose function the start and goal and capacity and the flag
fplay.choose({'x': 5, 'y': 3, 'z': 0}, {'x': 4, 'y': 0, 'z': 4}, [5,3,8], 1)
print("Start position =>", fplay.start(),"\n", "Goal position =>", fplay.goaldiff)
# gives the token to the search
list = search.depth_first_search(fplay, fplay.start(), "")

# to print the steps
for node in list:
    x = node["x"]
    y = node["y"]
    z = node["z"]
    print(x, y, z)
print("\n \n")

fplay = token.playz()
fplay.choose({'x': 7, 'y': 0, 'z': 0,}, {'x': 2, 'y': 2, 'z': 3}, [7,4,3], 1)
print("Start position =>", fplay.start(),"\n", "Goal position =>", fplay.goaldiff)
list = search.depth_first_search(fplay, fplay.start(), "")


for node in list:
    x = node["x"]
    y = node["y"]
    z = node["z"]
    print(x, y, z)
print("\n \n")

fplay = token.playz()
fplay.choose({'x': 0, 'y': 0}, {'x': 0, 'y': 6}, [4,9], 0)
print("Start position =>", fplay.start(),"\n", "Goal position =>", fplay.goaldiff)
list = search.depth_first_search(fplay, fplay.start(), "")


for node in list:
    x = node["x"]
    y = node["y"]
    print(x, y)