import csv

from flask import Flask, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import sqlite3

import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Define the data to be inserted
ski_resorts_data = [
    ('Mountain Peak Resort', 'Snowy Valley', 'A premier resort with ski slopes and luxurious accommodations.', '2000'),
    ('Alpine Retreat', 'Frosty Hills', 'Experience the thrill of skiing with breathtaking views.', '1800'),
    ('Snowy Pines Resort', 'Frozen Lake District', 'Family-friendly resort offering skiing and snowboarding lessons.', '1600'),
    ('Peak Paradise', 'Icy Ridge', 'Unmatched skiing experience with top-notch amenities.', '2200'),
    ('Crystal Slopes Resort', 'White Summit', 'Ski and relax in the lap of nature with world-class facilities.', '2100'),
    ('Powder Haven', 'Chill Mountain Range', 'Skiing and snow sports paradise for enthusiasts.', '1900'),
    ('Glacier Peaks Resort', 'Icy Peak Valley', 'Explore the beauty of winter with our skiing trails.', '2300'),
    ('Frosty Meadows Lodge', 'Snowy Plains', 'Enjoy the warmth of our cozy lodge after an exciting day on the slopes.', '1700'),
    ('Summit Serenity', 'Frozen Peaks Village', 'Escape to serenity with our ski resort at high altitudes.', '2400'),
    ('Polar Ridge Resort', 'Arctic Slopes', 'Experience the Arctic charm with our ski resort and icy adventures.', '2500'),
    ('White Cap Chalet', 'Snowy Ridge Town', 'Skiing fun and relaxation in the heart of the snowy town.', '2000'),
    ('Avalanche Haven', 'Frozen Valley', 'Thrilling slopes and snow-covered landscapes await at our resort.', '2100'),
    ('Frozen Crest Resort', 'Icicle Ridge', 'Discover the beauty of winter with skiing and snowboarding at our resort.', '1800'),
    ('Snowfall Sanctuary', 'Chilled Plateau', 'Find sanctuary in the midst of snowy slopes and peaceful surroundings.', '2200'),
    ('Frostbite Ridge Retreat', 'Icy Plateau', 'Skiing adventure combined with luxurious retreat facilities.', '2300'),
    ('Winter Wonderland Resort', 'Snowy Escarpment', 'Experience a winter wonderland with our ski resort at high elevations.', '2400'),
    ('Peak View Lodge', 'Snowy Highlands', 'Panoramic views and top-class skiing facilities for an unforgettable experience.', '2100'),
    ('Glacial Gateway Resort', 'Frozen Gateway', 'Gateway to glacial adventures with skiing and snow sports.', '2000'),
    ('Chill Haven Chalet', 'Snowy Oasis', 'A cozy chalet offering the perfect blend of relaxation and skiing excitement.', '1900'),
    ('Arctic Escape', 'Frozen Oasis', 'Escape to the Arctic with our ski resort offering icy adventures.', '2500')
]

# Insert data into SkiResort table
cursor.executemany('INSERT INTO SkiResort (resortName, resortLocation, resortDescription, resortElevation) VALUES (?, ?, ?, ?)', ski_resorts_data)

# Commit the changes and close the connection
conn.commit()
conn.close()




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

##I
def search_resort_by_name(resort_name):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM SkiResort WHERE resortName LIKE ?", ('%' + resort_name + '%',))
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
main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/search")
def search():
    q = request.args.get("q")
    print(q)

    if q:
        results = search_resort_by_name(q)
        pass
    else:
        results = search_resort_by_id(q)
    print("Resort Result:", search_resort_by_name(q))
    print(results)
    return render_template("search_results.html", results=results)

@main.route("/all")
def all_resorts():
    # Retrieve all ski resorts from the database
    results = search_all_ski_resorts()
    return render_template("all.html", results=results)

def search_all_ski_resorts():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    
    # Use a LEFT JOIN to include resorts without reviews
    cur.execute("""
        SELECT r.*, AVG(re.rating) AS average_rating
        FROM SkiResort r
        LEFT JOIN Review re ON r.resortID = re.resortID
        GROUP BY r.resortID
    """)
    
    result = cur.fetchall()
    con.close()
    return result

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    db.init_app(app)

    app.register_blueprint(main)

    return app





app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
