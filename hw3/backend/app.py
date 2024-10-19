from datetime import datetime, timezone
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.order_by(Task.order.asc()).all()
    return jsonify([{"id": task.id, "description": task.description} for task in tasks])


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    max_order_task = Task.query.order_by(Task.order.desc()).first()
    new_order = max_order_task.order + 1 if max_order_task else 1

    new_task = Task(description=data["description"], order=new_order)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"id": new_task.id, "description": new_task.description})


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"})


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.json
    task.description = data.get("description", task.description)
    db.session.commit()
    return jsonify({"id": task.id, "description": task.description})


@app.route("/tasks/move/<int:id>", methods=["PATCH"])
def move_task(id):
    task = Task.query.get_or_404(id)
    data = request.json
    direction = data.get("direction")

    if direction == "up":
        prev_task = (
            Task.query.filter(Task.order < task.order)
            .order_by(Task.order.desc())
            .first()
        )
        if prev_task:
            task.order, prev_task.order = prev_task.order, task.order
    elif direction == "down":
        next_task = (
            Task.query.filter(Task.order > task.order)
            .order_by(Task.order.asc())
            .first()
        )
        if next_task:
            task.order, next_task.order = next_task.order, task.order

    db.session.commit()
    return jsonify({"message": "Task moved successfully"})


@app.before_request
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
