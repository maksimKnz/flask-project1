from flask import Flask, render_template
import data

print(data.tours)
app = Flask(__name__)
tours = data.tours
departures = data.departures


@app.route('/')
def main():
    return render_template('index.html', tours=tours, departures=departures)


@app.route('/departures/<departure>')
def show_departure(departure):
    sorted_list = {}

    for key, tour in tours.items():
        if tour["departure"] == departure:
            sorted_list.update({key: tour})
    return render_template('departure.html', departure=departure, departures=departures, tours=sorted_list)


@app.route('/tours/<int:id>')
def show_tour(id):
    return render_template('tour.html', tour=tours[id], departures=departures)


app.run()
