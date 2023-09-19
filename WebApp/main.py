from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def multiply_by_two():
    result = None

    if request.method == "POST":
        input_value = request.form["number"]
        try:
            input_number = float(input_value)
            if input_number < 11:
                result = round(input_number * 2, 2)

            if 10 < input_number < 21:
                result = round(input_number * 1.75, 2)

            if 20 < input_number < 151:
                result = round(input_number * 1.5, 2)

            if 150 < input_number < 201:
                result = round(input_number * 1.35, 2)

            if 200 < input_number < 1001:
                result = round(input_number * 1.3, 2)

            if 1000 < input_number < 2001:
                result = round(input_number * 1.25, 2)

            if input_number > 2000:
                result = round(input_number * 1.2, 2)
            
        except ValueError:
            result = "Invalid input. Please enter a valid number."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
