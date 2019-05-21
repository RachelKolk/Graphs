import math
import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue) 

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()


    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # creates users using the argument passed in
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        # avg = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)
        # create a place to hold the possible friendships
        possibleFriendships = []
        # loops through the users list
        for userID in self.users:
            # checks the firends options in the range of users - from the first to the last
            for friendID in range(userID + 1, self.lastID + 1):
                # and then appends them to the possible friendship array
                possibleFriendships.append((userID, friendID))
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # shuffles the possible friendship array to make it random
        random.shuffle(possibleFriendships)
       
        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)
        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # !!!! IMPLEMENT ME
        # bfs will return the shortest path

        # create an empty queue
        q = Queue()
        # create an empty dictionary for visited friends
        visited = {}  # Note that this is a dictionary, not a set
        # add a path to the starting vertext to the queue
        q.enqueue([userID])
        # while the queue is not empty ...
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # assign v to the last vertex from the path
            v = path[-1]
            # if it has not been visited yet ...
            if v not in visited:
                # mark it as visited by adding it to the visited dict
                visited[v] = path
                # then enqueue paths to each of its neighbors to the queue
                for next_vert in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(next_vert)
                    q.enqueue(path_copy)
        # return visited dictionary
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(500, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)


