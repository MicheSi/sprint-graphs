from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

s = Stack()

visited = set()

# add starting room to stack
s.push(player.current_room)

while s.size() > 0:
    # remove last room
    room = s.pop()
    
    player.travel(room)

    # if current room has not been visited
    if player.current_room not in visited:
        # add current room to visited
        visited.add(player.current_room)
        # add to path
        traversal_path.append(directions[room])
        # add to stack
        s.append(directions[room])
        
    # iterate through available moves
    for option in player.current_room.get_exits():
        # if can move in direction and that room has not been visited
        if option and player.current_room.get_room_in_direction(option) not in visited:
            # add to path
            traversal_path.append(option)
            # add to stack
            s.append(option)

    



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
