from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    completed_at = db.Column(db.DateTime, nullable = True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable = True)
    goal = db.relationship("Goal", back_populates="tasks")

    @classmethod
    def from_dict(cls, data_dict):
        return cls(title=data_dict["title"],
        description=data_dict["description"],
        completed_at=data_dict["completed_at"])

    def to_dict(self):
        task_dict = dict(
            id=self.task_id,
            title=self.title,
            description=self.description,
            is_complete=False
        )

        if self.goal_id:
            task_dict["goal_id"] = self.goal_id
        
        return task_dict