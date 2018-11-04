import praw
import collections, numpy as np
import pandas as pd

# Grabs Reddit instance
reddit = praw.Reddit('Trenddit')
subreddit = reddit.subreddit('politics')
wordVector = np.array([])
titleVector = np.array([])

uselessWords = np.array(["the", "for", "than", "says", "him", "her",
"with", "gets", "most", "all", "just", "now", "one", "more"])

# Gives array with full list of words
for post in subreddit.top(time_filter='week', limit=20):
    titleWordArray = post.title.split()
    titleVector = np.append(titleVector, post.title)
    wordVector = np.append(wordVector, titleWordArray)


# Converts all elements into lowercase
wordVector = np.char.lower(wordVector)
wordVector = np.char.replace(wordVector, ",", "")
wordVector = np.char.replace(wordVector, ":", "")
# # Removes small words
#

# wordVector = np.setdiff1d(wordVector, uselessWords)
for word in wordVector:
    if len(word) < 3 or word in uselessWords:
        smallWords = np.where(wordVector == word)
        wordVector = np.delete(wordVector, smallWords[0][0])

# print(wordVector)
countedVector = collections.Counter(wordVector)
print(countedVector)

# # turns keys into array
# keyArray = np.array([])
# for key in countedVector.keys():
#     newKey = [key, countedVector[key]]
#     keyArray = np.append(keyArray, newKey)
#
# # print(keyArray)
#
# ddArray = np.arange(keyArray.size).reshape(int(keyArray.size/2), 2)
# # print(ddArray)
#
# #converts to Matrix and makes Excel copy of Data
# wordMatrix = pd.DataFrame(keyArray)
# wordMatrix.to_csv("word_listings.csv", na_rep="")
