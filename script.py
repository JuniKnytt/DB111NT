import sqlite3




con = sqlite3.connect("data.db")
cur = con.cursor()
#1 SEEING USER COUNT
print("\n#1 SEEING USER COUNT")
res = cur.execute("SELECT count(*) AS cnt FROM Users u")
print("User Count")
print(res.fetchone())


#2 NEW USER
print("\n#2 NEW USER")
data = [
    (21, "user21", "user21@hotmail.com")
]
cur.executemany("INSERT INTO Users VALUES(?, ?, ?)", data)
#con.commit() USE THESE TO EDIT DB

#3 SEEING NEW USER
print("\n#3 SEEING NEW USER")
res = cur.execute("SELECT count(*) AS cnt FROM Users u")
print("User Count")
print(res.fetchone())

#4 ADDING A NEW USER FAVORITE
print("\n#4 ADDING A NEW USER FAVORITE")
data = [
    (13, 21, 1)
]
cur.executemany("INSERT INTO userFavResort VALUES(?, ?, ?)", data)
#con.commit()

#5 SHOWING USER FAVORITE
print("\n#5 SHOWING USER FAVORITE")
print("UserFavID", "UserID", "ResortID")
for row in cur.execute("SELECT * FROM userFavResort ORDER BY userID"):
    print(row)

#6 READING USER1's REVIEW
print("\n#6 READING USER1's REVIEW")
print("Comment", "Score", "ResortID")
for row in cur.execute("SELECT comment, rating, resortID FROM Review WHERE userID == 1 ORDER BY rating"):
    print(row)

#7 USER1 EDITING REVIEW OF 1
print("\n#USER1 EDITING REVIEW OF Poor to Good Service")
cur.execute("UPDATE Review SET rating = '7', comment= 'It got better' WHERE reviewID = 4")


#8 READING AFTER EDIT REVIEW
print("\n#8 READING AFTER EDIT REVIEW")
print("Comment", "Score", "ResortID")
for row in cur.execute("SELECT comment, rating, resortID FROM Review WHERE userID == 1 ORDER BY rating"):
    print(row)

#9 USER SEARCHES FOR RESORT WITH 10 RATING
print("\n#9 USER SEARCHES FOR RESORTS WITH 10 RATING")
print("ResortName", "Rating")
for row in cur.execute("SELECT resortName, rating FROM Review r, SkiResort s WHERE s.resortID == r.resortID AND r.rating == 10"):
    print(row)

#10 USER SEARCHES FOR RESORT WITH RINKS
print("\n#10 USER SEARCHES FOR RESORT WITH RINKS")
print("ResortName")
for row in cur.execute("SELECT resortName FROM SkiResort s, SkiResortActivities ra WHERE ra.activityID == 1 AND ra.resortID == s.resortID"):
    print(row)

#11 List Activity Names of Radical Snowway
print("\n#11 List Activity Names of Radical Snowway")
print("Activities")
for row in cur.execute("select activityName FROM Activity a, SkiResortActivities sa, SkiResort r WHERE a.activityID == sa.activityID AND sa.resortID == r.resortID AND r.resortName == 'Radical Snoway'"):
    print(row)

#12 List Resort Favorite Count
print("\n#12 List Resort Favorite Count")
print("ResortName","NumberOfFaves")
for row in cur.execute("SELECT resortName as Name, count(f.resortID) as cnt FROM SkiResort r, userFavResort f WHERE r.resortID == f.resortID Group by Name"):
    print(row)

#13 Resort that offers snow rink with the highest user favorite count
print("\n#13 Resort that offers Snow rink with the highest user favorite count ")
print("ResortName", "favCount")
for row in cur.execute("Select Name, max(cnt) as cnt From (SELECT resortName as Name, count(f.resortID) as cnt FROM SkiResort r, userFavResort f WHERE r.resortID == f.resortID Group by Name) as l, SkiResortActivities sa, Activity a, SkiResort r WHERE l.Name == r.resortName AND r.resortID == sa.resortID AND sa.activityID == a.activityID AND a.activityName == 'snow rink'"):
    print(row)

#14 User4 Updates Email
print("\n#14 User4 Updates Email")
cur.execute("UPDATE Users SET userEmail = 'user4@califor@gmail.com' WHERE userID = 4")

#15 Print userEmail and usernames that use Gmail
print("\n#Print userEmail and usernames that use Gmail")
print("username","userEmail")
for row in cur.execute("Select username, userEmail From Users u WHERE u.userEmail LIKE '%gmail%'"):
    print(row)

#16 name of Resort with lowest adult booking price
print("\n#16 name of Resort with lowest adult booking price")
print("ResortName")
for row in cur.execute("select resortName From (select resortName, min(costAdult) FROM Bookable b, SkiResort s where b.resortID == s.resortID)"):
    print(row)

#17 list resorts by elevation
print("\n#17 list resorts by elevation")
print("Name","Elevation")
for row in cur.execute("select resortName as Name, resortElevation as elevation from skiresort s order by elevation"):
    print(row)

#18 show resorts that have pictures of their snow slopes and the picture url
print("\n#18 show resorts that have pictures of their snow slopes and the picture url")
print("Name","photoURL")
for row in cur.execute("select resortName, photoURL From photo p, skiresort s where p.photoDescription LIKE '%Snow slopes%' AND p.resortID = s.resortID"):
    print(row)

#19 NEW USER REGISTERS
print("\n#19 NEW USER REGISTERS")
data = [
    (22, "user22", "user22@gmail.com")
]
print("UserName", "UserEmail")
for row in cur.execute("SELECT username, userEmail FROM Users ORDER BY userID"):
    print(row)

#20 NEW USER CREATES REVIEW AND Updated Board and sort best rated by top
print("\n#20 NEW USER CREATES REVIEW and Show reviewboard")
data = [
    (6, 22, 'Amazing Slides', 9, '2023-12-12', 3)
]
cur.executemany("INSERT INTO Review VALUES(?, ?, ?, ?, ?, ?)", data)
print("UserName", "Comment", "Rating", "ResortName")
for row in cur.execute("select username, comment, rating, resortName from users u, review r, skiresort s where u.userID == r.userID and s.resortID == r.resortID order by rating DESC"):
    print(row)
"""
cur.execute("CREATE INDEX IF NOT EXISTS idx_user_id ON Users(userID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_resort_id ON SkiResort(resortID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_review_user ON Review(userID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_review_resort ON Review(resortID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_review_rating ON Review(rating)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_sra_activity ON SkiResortActivities(activityID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_sra_resort ON SkiResortActivities(resortID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_activity_id ON Activity(activityID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_userfav_user ON userFavResort(userID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_userfav_resort ON userFavResort(resortID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_bookable_resort ON Bookable(resortID)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_photo_resort ON Photo(resortID)")

def search_users_by_id(user_id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Users WHERE userID=?", (user_id,))
    result = cur.fetchall()
    con.close()
    return result

def search_resort_by_id(resort_id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM SkiResort WHERE resortID=?", (resort_id,))
    result = cur.fetchall()
    con.close()
    return result

def search_reviews_by_user_id(user_id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Review WHERE userID=?", (user_id,))
    result = cur.fetchall()
    con.close()
    return result

def search_reviews_by_resort_id(resort_id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Review WHERE resortID=?", (resort_id,))
    result = cur.fetchall()
    con.close()
    return result

def search_reviews_by_rating(rating):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Review WHERE rating=?", (rating,))
    result = cur.fetchall()
    con.close()
    return result

def search_resorts_by_activity(activity_id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT r.* FROM SkiResort r, SkiResortActivities sa WHERE sa.activityID=? AND sa.resortID=r.resortID", (activity_id,))
    result = cur.fetchall()
    con.close()
    return result

def search_user_favorites_by_user_id(user_id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM userFavResort WHERE userID=?", (user_id,))
    result = cur.fetchall()
    con.close()
    return result

def search_user_favorites_by_resort_id(resort_id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM userFavResort WHERE resortID=?", (resort_id,))
    result = cur.fetchall()
    con.close()
    return result

def search_bookable_by_resort_id(resort_id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Bookable WHERE resortID=?", (resort_id,))
    result = cur.fetchall()
    con.close()
    return result

def search_photos_by_resort_id(resort_id):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Photo WHERE resortID=?", (resort_id,))
    result = cur.fetchall()
    con.close()
    return result

#example
user_result = search_users_by_id(1)
print("User Result:", user_result)

resort_result = search_resort_by_id(1)
print("Resort Result:", resort_result)

reviews_by_user_result = search_reviews_by_user_id(1)
print("Reviews by User Result:", reviews_by_user_result)

reviews_by_resort_result = search_reviews_by_resort_id(1)
print("Reviews by Resort Result:", reviews_by_resort_result)

reviews_by_rating_result = search_reviews_by_rating(10)
print("Reviews by Rating Result:", reviews_by_rating_result)

resorts_by_activity_result = search_resorts_by_activity(1)
print("Resorts by Activity Result:", resorts_by_activity_result)

user_favorites_by_user_result = search_user_favorites_by_user_id(1)
print("User Favorites by User Result:", user_favorites_by_user_result)

user_favorites_by_resort_result = search_user_favorites_by_resort_id(1)
print("User Favorites by Resort Result:", user_favorites_by_resort_result)

bookable_by_resort_result = search_bookable_by_resort_id(1)
print("Bookable by Resort Result:", bookable_by_resort_result)

photos_by_resort_result = search_photos_by_resort_id(1)
print("Photos by Resort Result:", photos_by_resort_result)

"""