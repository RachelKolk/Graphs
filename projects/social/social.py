import math
import random
import time

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
            # pass
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            # pass
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

    # def populateGraphLinear(self, numUsers, avgFriendships):
    #     self.lastID = 0
    #     self.users = {}
    #     self.friendships = {}

    #     for i in range(numUsers):
    #         self.addUser(f"User {i + 1}")

    #     targetFriendships = (numUsers * avgFriendships) // 2
    #     totalFriendships = 0
    #     collisions = 0
    #     while totalFriendships < targetFriendships:
    #         userID = random.randint(1, self.lastID)
    #         friendID = random.randint(1, self.lastID)
    #         if self.addFriendship(userID, friendID):
    #             totalFriendships += 2
    #         else:
    #             collisions += 1
    #     print(f"Collisions: {collisions}")


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
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)


    # using this to see how many average users would be in a user's extended network
    # print(len(connections))
    # connections = sg.getAllSocialPaths(3)
    # print(len(connections))
    # connections = sg.getAllSocialPaths(321)
    # print(len(connections))
    # connections = sg.getAllSocialPaths(305)
    # print(len(connections))
    # connections = sg.getAllSocialPaths(758)
    # print(len(connections))
    # connections = sg.getAllSocialPaths(627)
    # print(len(connections))

# test for linear graph implementation 
# if __name__ == '__main__':
# 	sg = SocialGraph()
# 	numUsers = 100
# 	avgFriendships = 15
# 	linear_start_time = time.time()
# 	sg.populateGraphLinear(numUsers, avgFriendships)
# 	linear_end_time = time.time()
# 	print(f"Linear runtime: {linear_end_time - linear_start_time} seconds")
# 	q_start_time = time.time()
# 	sg.populateGraph(numUsers, avgFriendships)
# 	q_end_time = time.time()
# 	print(f"Quadratic runtime: {q_end_time - q_start_time} seconds")


'''
Part 3 -- Questions:

    1.) addFriendship() would have to be called 500 times because if the average
        number of friends is 10 for all 100 users it would have to be called 1 time,
        per every friendship, which you would assume would be 1000 times (100 * 10), but 
        because the function creates a bidirectional friendship between the users it
        would be called 1000 / 2 times, or 500.

    2.) If I run the code using the specifications and choose 5 different user IDs as
        the arguments for the connections data in an attempt to get an average the percentage
        changes slightly. But it was never less than a 90% connection rate between a user
        and all the other people in their extended network they're connected to--
        the highest I saw was 98%. This seems weird...? 
        And oddly enough it seems like the whole 7 degrees of seperation is actually a legitimate
        thing. While I did see some connections that were less, I think the average would
        be 7, at least for this data set. 
'''