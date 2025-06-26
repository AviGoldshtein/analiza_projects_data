class Agent:
    def __init__(self, code_name, real_name, location, status, missionsCompleted = 0,  id = 0):
        self.id = id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missionsCompleted = missionsCompleted

    def __str__(self) -> str:
        return (f"id: {self.id}\n"
                f"code_name: {self.code_name}\n"
                f"real_name: {self.real_name}\n"
                f"location: {self.location}\n"
                f"status: {self.status}\n"
                f"missionsCompleted: {self.missionsCompleted}\n")