# from urllib import request
#
# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# @app.route('/api/health', methods=["get"])
# def health():
#
#     return jsonify({
#         "status" : "working"
#     })
#
# @app.route('/api/anlyze', methods=["post"])
# def analyze():
#
#     data = request.get_json()
#




from flask import Flask, request, jsonify

app = Flask(__name__)


# GET /api/health
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "working"
    })


# POST /api/analyze
@app.route("/api/analyze", methods=["POST"])
def analyze():


    # Receive JSON
    data = request.get_json()

    # Get students
    students = data["students"]

    averages = []

    # Calculate average for each student
    for student in students:

        total = (
            student["math"] +
            student["science"] +
            student["english"]
        )

        average = total / 3

        averages.append(average)

    # Class average
    class_average = sum(averages) / len(averages)

    # Top student's average
    top_average = max(averages)

    # Count students who passed
    passed = 0

    for average in averages:
        if average >= 40:
            passed += 1

    # Pass percentage
    pass_percentage = (passed / len(students)) * 100

    # Return results
    return jsonify({
        "class_average": round(class_average, 1),
        "top_average": round(top_average, 1),
        "pass_percentage": round(pass_percentage, 1)
    })


if __name__ == "__main__":
    app.run(debug=True)