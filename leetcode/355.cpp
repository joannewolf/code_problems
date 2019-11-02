#include <utility>
#include <algorithm>
class Twitter {
private:
    vector<pair<int, int>> news; // [userId, tweetId]
    map<int, vector<int>> followed;
public:
    /** Initialize your data structure here. */
    Twitter() {
        
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        news.insert(news.begin(), make_pair(userId, tweetId));
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int> newsFeed, followedId = followed[userId];
        for (int i = 0; i < news.size() && newsFeed.size() < 10; i++) {
            if (news[i].first == userId || find(followedId.begin(), followedId.end(), news[i].first) != followedId.end())
                newsFeed.push_back(news[i].second);
        }
        return newsFeed;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        if (followed.find(followerId) == followed.end())
            followed[followerId] = vector<int>(1, followeeId);
        else if (find(followed[followerId].begin(), followed[followerId].end(), followeeId) == followed[followerId].end())
            followed[followerId].push_back(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        if (followed.find(followerId) != followed.end()) {
            vector<int>::iterator it = find(followed[followerId].begin(), followed[followerId].end(), followeeId);
            if (it != followed[followerId].end())
                followed[followerId].erase(it);
        }
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */