class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.userTweets[userId].append([self.time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followed = self.follows[userId]
        tweets = []
        tweets.extend(self.userTweets[userId])
        for followee in followed:
            userTweets = self.userTweets[followee]
            tweets.extend(userTweets)
        heapq.heapify_max(tweets)
        limit = min(10,len(tweets))
        res = [heapq.heappop_max(tweets) for i in range(limit)]
        res = [tweet[1] for tweet in res]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
