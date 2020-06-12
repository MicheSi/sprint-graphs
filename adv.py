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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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

def move_rooms(starting_room, visited=None, path=None):
    # initializing
    if visited is None:
        visited = set()
    if path is None:
        path = []
    # add starting room to visited
    visited.add(starting_room)
    # add starting room to current path
    path = path + [starting_room]
    # loop through direction options from current room
    for option in player.current_room.get_exits():
        # move player that direction
        player.travel(option)
        # new room is the room player just moved to
        new_room = player.current_room
        # if new room has not been visited, add it to visited
        if new_room not in visited:
            visited.add(new_room)
            # add direction to path
            path.append(option)
            # recurse through function to add more rooms and directions to visited & path
            path = path + move_rooms(new_room, visited)
            # once no more new rooms in that direction, move back to starting room
            player.travel(directions[option])
            # add to path
            path.append(directions[option])
        # if new room has already been visited, move back to previous room    
        else:
            player.travel(directions[option])
    return path
# set new traversal path
traversal_path = move_rooms(player.current_room)


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
