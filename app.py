import csv
from flask import Flask, jsonify, request

# Create and activate a new virtual environment with Python 3.8
# Install required modules using `pip install flask requests`

# Create a new file main.py
app = Flask(__name__)

# Import articles.csv and read all the data
articles_file = "data/articles.csv"
with open(articles_file, "r") as file:
    reader = csv.DictReader(file)
    all_articles = list(reader)

liked_articles = []
not_liked_articles = []

# Add the header "id" before the first comma in the first line
with open(articles_file, "r") as file:
    lines = file.readlines()
    lines[0] = "id," + lines[0].split(",", 1)[1]
    with open(articles_file, "w") as updated_file:
        updated_file.writelines(lines)

# Create the first GET request to get the first article
@app.route("/get_article", methods=["GET"])
def get_article():
    if len(all_articles) > 0:
        return jsonify(all_articles[0])
    else:
        return jsonify({"message": "No articles remaining."})

# Create the second POST request to mark the article as liked
@app.route("/like_article", methods=["POST"])
def like_article():
    if len(all_articles) > 0:
        article = all_articles.pop(0)
        liked_articles.append(article)
        return jsonify({"message": "Article liked successfully."})
    else:
        return jsonify({"message": "No articles remaining."})

# Create the third POST request to mark the article as not liked
@app.route("/not_like_article", methods=["POST"])
def not_like_article():
    if len(all_articles) > 0:
        article = all_articles.pop(0)
        not_liked_articles.append(article)
        return jsonify({"message": "Article marked as not liked."})
    else:
        return jsonify({"message": "No articles remaining."})

# Run the Flask app
if __name__ == "__main__":
    app.run()