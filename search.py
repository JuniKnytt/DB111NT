import sqlite3




con = sqlite3.connect("data.db")
cur = con.cursor()

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