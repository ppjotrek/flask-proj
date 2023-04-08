from flask import Flask, render_template

app = Flask(__name__)

items = ["Pierwszy element", "Drugi element", "Trzeci element"]

@app.route('/items')
def show_items():
    return render_template("items.html", items=items)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')