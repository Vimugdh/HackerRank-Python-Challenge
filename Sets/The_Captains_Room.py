'''
THE CAPTAIN'S ROOM
'''

def takeInput():
    K = int(input())
    roomNums = list(map(int, input().split()))
    return roomNums


def findCaptain(roomNums):
    uniqueRooms = set()
    commonRooms = set()
    for item in roomNums:
        if item not in uniqueRooms:
            uniqueRooms.add(item)
        else:
            commonRooms.add(item)
    print(uniqueRooms.difference(commonRooms).pop())

    
roomNums = takeInput()
findCaptain(roomNums)