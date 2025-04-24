class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def to_dict(self):
        return {"title": self.title, "done": self.done}

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["done"])
