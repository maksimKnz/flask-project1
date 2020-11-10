from flask import Flask, render_template


import data


app = Flask(__name__)
tours = data.tours
departures = data.departures
title = data.title
subtitle = data.subtitle
description = data.description

@app.route('/')
def main():
    return render_template('index.html', tours=tours, departures=departures, title=title, subtitle=subtitle, description=description)


@app.route('/departures/<departure>')
def show_departure(departure):
    sorted_list = []

    for key, tour in tours.items():
        if tour["departure"] == departure:
            tour.update({'id': key})
            sorted_list.append(tour)
    return render_template('departure.html', departure=departure, departures=departures, tours=sorted_list, title=title)


@app.route('/tours/<int:id>')
def show_tour(id):
    return render_template('tour.html', tour=tours[id], departures=departures, title=title)


if __name__ == '__main__':
    app.run()
