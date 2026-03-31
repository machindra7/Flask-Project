from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        tasks.append({"task": task, "done": False})
        return redirect("/")

    return render_template("index.html", tasks=tasks)

@app.route("/done/<int:index>")
def done(index):
    tasks[index]["done"] = True
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)