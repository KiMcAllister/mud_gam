

spacer = ", a "

buildingrooms = {"house":["bedroom", "bathroom", "living_room", "kitchen", "dining_room",]}

class building:
    def __init__(self, type):
        self.type = type
    def rooms(self):
        print("The house contains {0}".format(buildingrooms[self.type]) )

house = building("house")

house.rooms()

#demo building will be a house



"""




class building:
    def __init__(self, type, rooms):
        self.type = type
        self.rooms = rooms
class room:
    def __init__(self, type, furniture, windows):
        self.type = type
        self.furniture = furniture
        self.windows = windows
class furniture:
    def __init__(self, type, loot):
        self.type = type
        self.loot = loot







building1 = building(room(("bedroom","garage"),furniture("table","loot"),[True,False]),[])
#house1 = building("house", [room(["bedroom","bathroom","livingroom"],["desk","chair"],[True, False])],)


spacer = ", a "
print(f"You are in a {building1.type}.")

#print(f"Inside the {house1.rooms[0].type[0]}, there is a {house1.rooms[0].furniture[0]} in the corner. {house1.rooms[0].windows[0]}")
#print(f"There are {len(house.rooms)} rooms inside of the {house.type}. It has a {spacer.join(house.rooms[:-1])}, and a {house.rooms[2]}")

"""