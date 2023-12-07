import csv

from flask import Flask, request, render_template, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

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
main = Blueprint("main", __name__)

# @main.route("/")
# def index():
#     return render_template("index.html")


@main.route("/")
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
