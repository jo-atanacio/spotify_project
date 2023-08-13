from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for demonstration
top_songs_data = {
    'short_term': {'Song A': 'Artist A', 'Song B': 'Artist B'},
    'medium_term': {'Song C': 'Artist C', 'Song D': 'Artist D'},
    'long_term': {'Song E': 'Artist E', 'Song F': 'Artist F'}
}
image = 

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/get_top_songs/<time_range>')
def get_top_songs(time_range):
    if time_range in top_songs_data:
        return jsonify(top_songs_data[time_range])
    else:
        return jsonify({})

if __name__ == "__main__":
    app.run(port=5001)  # Use any available port