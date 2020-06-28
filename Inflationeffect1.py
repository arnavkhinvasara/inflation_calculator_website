#imports
import datetime
import random
import numpy as np
from flask import Flask, render_template, request
app = Flask(__name__)

def Inflation_predictor (x):
    with open("C:/Users/arnav_000/Documents/Python/future_years.txt") as fy:
        future = fy.readlines()
        future_years = []
        for element in future:
            future_years.append(element.strip())

    with open("C:/Users/arnav_000/Documents/Python/rates.txt") as r:
        rates = r.readlines()
        future_rates = []
        for element in rates:
            future_rates.append(element.strip())

    if str(x) in future_years:
        wanted_index = future_years.index(str(x))
        return float(future_rates[wanted_index])

    with open("C:/Users/arnav_000/Documents/Python/future_years.txt", "a") as fy:
        fy.write(str(x)+"\n")

    x = x - 1950
    top = -0.03 * x
    rate_mate = round(8.97 * pow(2.71828, top) + 1, 2)
    rate_mate2 = rate_mate + random.uniform(-0.25, 0.25)
    with open("C:/Users/arnav_000/Documents/Python/rates.txt", "a") as r:
        r.write((str(rate_mate2)+"\n"))
    return rate_mate2

@app.route('/', methods = ['GET', 'POST'])
def external():
    if request.method!="POST":
        return render_template("inflation_calculator.html", rate_mate2 = " ")

    try:
        x = request.form["t1"]

        num_string = "0123456789"
        appending_list = []
        for char in x:
            if char in num_string:
                appending_list.append(char)

        if len(appending_list)!=4:
            return render_template("inflation_calculator.html", rate_mate2 = " Your year needs to be comprised of 4 digits.")
        x = int(x)
        year = x

        today = datetime.date.today()
        today = str(today)
        year_wanted = today[0]+today[1]+today[2]+today[3]

        if int(year_wanted)>=x:
            rate_mate2 = "Your year needs to be in the future."
            return render_template("inflation_calculator.html", rate_mate2 = rate_mate2, year = " in " + str(year))

        with open("C:/Users/arnav_000/Documents/Python/future_years.txt") as fy:
            future = fy.readlines()
            future_years = []
            for element in future:
                future_years.append(element.strip())

        with open("C:/Users/arnav_000/Documents/Python/rates.txt") as r:
            rates = r.readlines()
            future_rates = []
            for element in rates:
                future_rates.append(element.strip())

        if str(x) in future_years:
            wanted_index = future_years.index(str(x))
            rate_mate2 = float(future_rates[wanted_index])
            rate_mate2 = str(round(rate_mate2, 2)) + "%"
            return render_template("inflation_calculator.html", rate_mate2 = rate_mate2, year=" in " + str(year))

        with open("C:/Users/arnav_000/Documents/Python/future_years.txt", "a") as fy:
            fy.write(str(x)+"\n")

        x = x - 1950
        top = -0.03 * x
        rate_mate = round(8.97 * pow(2.71828, top) + 1, 2)
        rate_mate2 = round(rate_mate + random.uniform(-0.25, 0.25), 2)

        with open("C:/Users/arnav_000/Documents/Python/rates.txt", "a") as r:
            r.write((str(rate_mate2)+"\n"))

        rate_mate2 = str(round(rate_mate2, 2)) + "%"
        return render_template("inflation_calculator.html", rate_mate2 = rate_mate2, year=" in " + str(year))

    except:
        try:
            x = request.form["t2"]

            if request.method!="POST":
                return render_template("inflation_calculator.html", price_mate = " ")

            num_string2 = "0123456789"
            appending_list2 = []
            for char in x:
                if char in num_string2:
                    appending_list2.append(char)

            if len(appending_list2)!=4:
                return render_template("inflation_calculator.html", price_mate = " Your year needs to be comprised of 4 digits.")

            x2 = int(x)
            year2 = x2

            today2 = datetime.date.today()
            today2 = str(today2)
            year_wanted2 = today2[0]+today2[1]+today2[2]+today2[3]

            if int(year_wanted2)>=x2:
                price_mate = "Your year needs to be in the future."
                return render_template("inflation_calculator.html", price_mate = price_mate, year2 = " in " + str(year2))

            count = 0
            y = int(year_wanted2)
            criteria = x2 - y
            all_rates = []
            while count < criteria:
                all_rates.append(round(Inflation_predictor(y), 2))
                y+=1
                count+=1

            all_rates2 = []
            for element in all_rates:
                appender = 1 + element/100
                all_rates2.append(appender)
            price_mate = str(round(10 * np.prod(all_rates2), 2)) + "$"
            return render_template("inflation_calculator.html", price_mate = price_mate, year2 = " in " + str(year2))

        except:
            x = request.form["t3"]

            if request.method!="POST":
                return render_template("inflation_calculator.html", worth_mate = " ")

            num_string3 = "0123456789"
            appending_list3 = []
            for char in x:
                if char in num_string3:
                    appending_list3.append(char)

            if len(appending_list3)!=4:
                return render_template("inflation_calculator.html", worth_mate = " Your year needs to be comprised of 4 digits.")

            x3 = int(x)
            year3 = x3
            today3 = datetime.date.today()
            today3 = str(today3)
            year_wanted3 = today3[0]+today3[1]+today3[2]+today3[3]

            if int(year_wanted3)>=x3:
                worth_mate = "Your year needs to be in the future."
                return render_template("inflation_calculator.html", worth_mate = worth_mate, year3 = " in " + str(year3))
            count2 = 0
            y2 = int(year_wanted3)
            criteria2 = x3 - y2
            all_rates2 = []
            while count2 < criteria2:
                all_rates2.append(round(Inflation_predictor(y2), 2))
                y2+=1
                count2+=1

            all_rates3 = []
            for element in all_rates2:
                appender2 = 1 - element/100
                all_rates3.append(appender2)
            worth_mate = str(round(10 * np.prod(all_rates3), 2)) + "$"
            return render_template("inflation_calculator.html", worth_mate = worth_mate, year3 = " in " + str(year3) )

if __name__ == "__main__":
    app.run(debug=True)