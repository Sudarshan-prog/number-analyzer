
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        number = int(request.form["number"])

        digit_sum = sum(int(digit) for digit in str(abs(number)))

        if number > 1:
            is_prime = all(
                number % i != 0
                for i in range(2, int(number ** 0.5) + 1)
            )
        else:
            is_prime = False

        result = {
            "number": number,
            "even_odd": "Even" if number % 2 == 0 else "Odd",
            "prime": "Prime" if is_prime else "Not Prime",
            "digit_sum": digit_sum
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)