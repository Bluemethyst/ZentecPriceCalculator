from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate_gst():
    input_value = None
    inclusive_result = None
    exclusive_result = None
    margin_int = None
    margin_percent = None

    if request.method == "POST":
        input_value = request.form.get("input_value")

        if input_value and input_value.strip():
            try:
                input_number = float(input_value)

                if input_number < 10:
                    result = (round(input_number * 2, 2))

                if 9.99 < input_number < 15:
                    result = (round(input_number * 1.9, 2))

                if 14.99 < input_number < 20:
                    result = (round(input_number * 1.8, 2))

                if 19.99 < input_number < 25:
                    result = (round(input_number * 1.75, 2))

                if 24.99 < input_number < 30:
                    result = (round(input_number * 1.7, 2))

                if 29.99 < input_number < 35:
                    result = (round(input_number * 1.65, 2))

                if 34.99 < input_number < 40:
                    result = (round(input_number * 1.6, 2))

                if 39.99 < input_number < 45:
                    result = (round(input_number * 1.55, 2))

                if 44.99 < input_number < 60:
                    result = (round(input_number * 1.5, 2))

                if 59.99 < input_number < 70:
                    result = (round(input_number * 1.48, 2))

                if 69.99 < input_number < 80:
                    result = (round(input_number * 1.47, 2))

                if 79.99 < input_number < 90:
                    result = (round(input_number * 1.46, 2))

                if 89.99 < input_number < 100:
                    result = (round(input_number * 1.45, 2))

                if 99.99 < input_number < 110:
                    result = (round(input_number * 1.44, 2))

                if 109.99 < input_number < 120:
                    result = (round(input_number * 1.43, 2))

                if 119.99 < input_number < 130:
                    result = (round(input_number * 1.42, 2))

                if 129.99 < input_number < 140:
                    result = (round(input_number * 1.41, 2))

                if 139.99 < input_number < 150:
                    result = (round(input_number * 1.4, 2))

                if 149.99 < input_number < 160:
                    result = (round(input_number * 1.39, 2))

                if 159.99 < input_number < 170:
                    result = (round(input_number * 1.38, 2))

                if 169.99 < input_number < 180:
                    result = (round(input_number * 1.37, 2))

                if 179.99 < input_number < 190:
                    result = (round(input_number * 1.36, 2))

                if 189.99 < input_number < 200:
                    result = (round(input_number * 1.35, 2))

                if 199.99 < input_number < 225:
                    result = (round(input_number * 1.345, 2))

                if 224.99 < input_number < 250:
                    result = (round(input_number * 1.34, 2))

                if 249.99 < input_number < 300:
                    result = (round(input_number * 1.335, 2))

                if 299.99 < input_number < 375:
                    result = (round(input_number * 1.33, 2))

                if 374.99 < input_number < 475:
                    result = (round(input_number * 1.325, 2))

                if 474.99 < input_number < 550:
                    result = (round(input_number * 1.32, 2))

                if 549.99 < input_number < 650:
                    result = (round(input_number * 1.315, 2))

                if 649.99 < input_number < 750:
                    result = (round(input_number * 1.31, 2))

                if 749.99 < input_number < 850:
                    result = (round(input_number * 1.305, 2))

                if 849.99 < input_number < 1000:
                    result = (round(input_number * 1.3, 2))

                if 999.99 < input_number < 1100:
                    result = (round(input_number * 1.295, 2))

                if 1099.99 < input_number < 1200:
                    result = (round(input_number * 1.29, 2))

                if 1199.99 < input_number < 1300:
                    result = (round(input_number * 1.285, 2))

                if 1299.99 < input_number < 1400:
                    result = (round(input_number * 1.28, 2))

                if 1399.99 < input_number < 1500:
                    result = (round(input_number * 1.275, 2))

                if 1499.99 < input_number < 1600:
                    result = (round(input_number * 1.27, 2))

                if 1599.99 < input_number < 1700:
                    result = (round(input_number * 1.265, 2))

                if 1699.99 < input_number < 1800:
                    result = (round(input_number * 1.26, 2))

                if 1799.99 < input_number < 1900:
                    result = (round(input_number * 1.225, 2))

                if 1899.99 < input_number < 2000:
                    result = (round(input_number * 1.25, 2))

                if input_number > 1999.99:
                    result = (round(input_number * 1.2, 2))

                inclusive_result = round(result * 1.15, 2)
                exclusive_result = round(result, 2)
                margin_int = round(inclusive_result - exclusive_result, 2)
                margin_percent = round(exclusive_result / input_number, 2)

            except ValueError:
                inclusive_result = "Invalid input. Please enter a valid number."
                exclusive_result = "Invalid input. Please enter a valid number."
                margin_int = "Invalid input. Please enter a valid number."
                margin_percent = "Invalid input. Please enter a valid number."

    return render_template("index.html", input_value=input_value, inclusive_result=inclusive_result, exclusive_result=exclusive_result, margin_int=margin_int, margin_percent=margin_percent)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5333, debug=True)
