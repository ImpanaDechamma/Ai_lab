import random

ROWS = 4
COLS = 4

def display_room(room):
    for row in room:
        print(row)
    print()

def create_room():
    room = []

    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(random.choice(["Dirty", "Clean"]))
        room.append(row)

    return room

def clean_room(room):
    cleaned_locations = []
    total_dirty = 0

    for i in range(ROWS):
        for j in range(COLS):
            if room[i][j] == "Dirty":
                total_dirty += 1

    for i in range(ROWS):
        for j in range(COLS):
            if room[i][j] == "Dirty":
                room[i][j] = "Clean"
                cleaned_locations.append((i, j))

    if total_dirty == 0:
        performance = 100
    else:
        performance = (len(cleaned_locations) / total_dirty) * 100

    return cleaned_locations, performance

room = create_room()

print("Room state before cleaning:")
display_room(room)

cleaned_locations, performance = clean_room(room)

print("Room state after cleaning:")
display_room(room)

print("Locations cleaned by the robot:")
for location in cleaned_locations:
    print(location)

print(f"\nPerformance: {performance:.2f}%")