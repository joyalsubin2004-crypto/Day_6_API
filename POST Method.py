from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/analyze", methods=["POST"])
def analyze():

    # Get JSON data from request
    data = request.get_json()

    # Get students list
    students = data["students"]

    results = []

    for student in students:

        # Calculate total
        total = (
            student["math"] +
            student["science"] +
            student["english"]
        )

        # Calculate average
        average = total / 3

        # Store result
        results.append({
            "math": student["math"],
            "science": student["science"],
            "english": student["english"],
            "total": total,
            "average": round(average, 2)
        })

    return jsonify({
        "results": results
    })


if __name__ == "__main__":
    app.run(debug=True)