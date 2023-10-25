from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate_gst():
    inputValue = None
    gst = None
    costPriceInclGst = None
    costPriceExclGst = None
    result = 0
    
    if request.method == "POST":
        inputValueStr = request.form.get("input_value")
        gstCheckbox = request.form.get('gst')
        try:
            inputValue = float(inputValueStr)
            if gstCheckbox:
                gst = True
            else:
                gst = False
            
            if gst == True:
                inputValuePlusGst = inputValue * 1.15
            else:
                inputValuePlusGst = inputValue
                
                
            if inputValue < 10:
                result = (round(inputValuePlusGst * 2, 2))
                calcInt = 2

            if 9.99 < inputValuePlusGst < 15:
                result = (round(inputValuePlusGst * 1.9, 2))
                calcInt = 1.9

            if 14.99 < inputValuePlusGst < 20:
                result = (round(inputValuePlusGst * 1.8, 2))
                calcInt = 1.8

            if 19.99 < inputValuePlusGst < 25:
                result = (round(inputValuePlusGst * 1.75, 2))
                calcInt = 1.75

            if 24.99 < inputValuePlusGst < 30:
                result = (round(inputValuePlusGst * 1.7, 2))
                calcInt = 1.7

            if 29.99 < inputValuePlusGst < 35:
                result = (round(inputValuePlusGst * 1.65, 2))
                calcInt = 1.65

            if 34.99 < inputValuePlusGst < 40:
                result = (round(inputValuePlusGst * 1.6, 2))
                calcInt = 1.6

            if 39.99 < inputValuePlusGst < 45:
                result = (round(inputValuePlusGst * 1.55, 2))
                calcInt = 1.55

            if 44.99 < inputValuePlusGst < 60:
                result = (round(inputValuePlusGst * 1.5, 2))
                calcInt = 1.5

            if 59.99 < inputValuePlusGst < 70:
                result = (round(inputValuePlusGst * 1.48, 2))
                calcInt = 1.48

            if 69.99 < inputValuePlusGst < 80:
                result = (round(inputValuePlusGst * 1.47, 2))
                calcInt = 1.47

            if 79.99 < inputValuePlusGst < 90:
                result = (round(inputValuePlusGst * 1.46, 2))
                calcInt = 1.46

            if 89.99 < inputValuePlusGst < 100:
                result = (round(inputValuePlusGst * 1.45, 2))
                calcInt = 1.45

            if 99.99 < inputValuePlusGst < 110:
                result = (round(inputValuePlusGst * 1.44, 2))
                calcInt = 1.44

            if 109.99 < inputValuePlusGst < 120:
                result = (round(inputValuePlusGst * 1.43, 2))
                calcInt = 1.43

            if 119.99 < inputValuePlusGst < 130:
                result = (round(inputValuePlusGst * 1.42, 2))
                calcInt = 1.42

            if 129.99 < inputValuePlusGst < 140:
                result = (round(inputValuePlusGst * 1.41, 2))
                calcInt = 1.41

            if 139.99 < inputValuePlusGst < 150:
                result = (round(inputValuePlusGst * 1.4, 2))
                calcInt = 1.4

            if 149.99 < inputValuePlusGst < 160:
                result = (round(inputValuePlusGst * 1.39, 2))
                calcInt = 1.39

            if 159.99 < inputValuePlusGst < 170:
                result = (round(inputValuePlusGst * 1.38, 2))
                calcInt = 1.38

            if 169.99 < inputValuePlusGst < 180:
                result = (round(inputValuePlusGst * 1.37, 2))
                calcInt = 1.37

            if 179.99 < inputValuePlusGst < 190:
                result = (round(inputValuePlusGst * 1.36, 2))
                calcInt = 1.36

            if 189.99 < inputValuePlusGst < 200:
                result = (round(inputValuePlusGst * 1.35, 2))
                calcInt = 1.35

            if 199.99 < inputValuePlusGst < 225:
                result = (round(inputValuePlusGst * 1.345, 2))
                calcInt = 1.345

            if 224.99 < inputValuePlusGst < 250:
                result = (round(inputValuePlusGst * 1.34, 2))
                calcInt = 1.34

            if 249.99 < inputValuePlusGst < 300:
                result = (round(inputValuePlusGst * 1.335, 2))
                calcInt = 1.335

            if 299.99 < inputValuePlusGst < 375:
                result = (round(inputValuePlusGst * 1.33, 2))
                calcInt = 1.33

            if 374.99 < inputValuePlusGst < 475:
                result = (round(inputValuePlusGst * 1.325, 2))
                calcInt = 1.325

            if 474.99 < inputValuePlusGst < 550:
                result = (round(inputValuePlusGst * 1.32, 2))
                calcInt = 1.32

            if 549.99 < inputValuePlusGst < 650:
                result = (round(inputValuePlusGst * 1.315, 2))
                calcInt = 1.315

            if 649.99 < inputValuePlusGst < 750:
                result = (round(inputValuePlusGst * 1.31, 2))
                calcInt = 1.31

            if 749.99 < inputValuePlusGst < 850:
                result = (round(inputValuePlusGst * 1.305, 2))
                calcInt = 1.305

            if 849.99 < inputValuePlusGst < 1000:
                result = (round(inputValuePlusGst * 1.3, 2))
                calcInt = 1.3

            if 999.99 < inputValuePlusGst < 1100:
                result = (round(inputValuePlusGst * 1.295, 2))
                calcInt = 1.295

            if 1099.99 < inputValuePlusGst < 1200:
                result = (round(inputValuePlusGst * 1.29, 2))
                calcInt = 1.29

            if 1199.99 < inputValuePlusGst < 1300:
                result = (round(inputValuePlusGst * 1.285, 2))
                calcInt = 1.285

            if 1299.99 < inputValuePlusGst < 1400:
                result = (round(inputValuePlusGst * 1.28, 2))
                calcInt = 1.28

            if 1399.99 < inputValuePlusGst < 1500:
                result = (round(inputValuePlusGst * 1.275, 2))
                calcInt = 1.275

            if 1499.99 < inputValuePlusGst < 1600:
                result = (round(inputValuePlusGst * 1.27, 2))
                calcInt = 1.27

            if 1599.99 < inputValuePlusGst < 1700:
                result = (round(inputValuePlusGst * 1.265, 2))
                calcInt = 1.265

            if 1699.99 < inputValuePlusGst < 1800:
                result = (round(inputValuePlusGst * 1.26, 2))
                calcInt = 1.26

            if 1799.99 < inputValuePlusGst < 1900:
                result = (round(inputValuePlusGst * 1.225, 2))
                calcInt = 1.225

            if 1899.99 < inputValuePlusGst < 2000:
                result = (round(inputValuePlusGst * 1.25, 2))
                calcInt = 1.25

            if inputValuePlusGst > 1999.99:
                result = (round(inputValuePlusGst * 1.2, 2))
                calcInt = 1.2
        except ValueError:
            inputValuePlusGst = 0
            result = 0  
            
        if gst == True:
            costPriceExclGst = round(inputValue / 1.15, 2)
            costPriceInclGst = inputValue
            sellPriceExclGst = round(result / 1.15, 2)
            sellPriceInclGst = round(result, 2)
        else:
            costPriceExclGst = round(inputValue, 2)
            costPriceInclGst = round(inputValuePlusGst * 1.15, 2)
            sellPriceExclGst = round(result / 1.15, 2)
            sellPriceInclGst = round(result, 2)
        marginExclGst = round(sellPriceExclGst - costPriceExclGst, 2)
        marginInclGst = round(sellPriceInclGst - costPriceInclGst, 2)
        marginPercentage = round(calcInt * 100 - 100, 2)

    return render_template("index.html", 
                           costPriceExclGst=costPriceExclGst, 
                           costPriceInclGst=costPriceInclGst, 
                           sellPriceExclGst=sellPriceExclGst, 
                           sellPriceInclGst=sellPriceInclGst,
                           marginExclGst=marginExclGst,
                           marginInclGst=marginInclGst,
                           marginPercentage=marginPercentage
                           )
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5333, debug=True)
