
class Course:
    def __init__(self, code, name, contains):
        self.code = code
        self.name = name
        self.contains = contains
        self.signed_up = []
        self.waiting_list = []

    def enroll(self, name):
        if name in self.signed_up or name in self.waiting_list:
            raise ValueError(f"{name}: is already registered")
        if len(self.signed_up) < self.contains:
            self.signed_up.append(name)
            return "enrolled"
        else:
            self.waiting_list.append(name)
            return "waitlisted"

    def __str__(self):
        return f"{self.code} {self.name} | {len(self.signed_up)}/{self.contains} | waitlist: {len(self.waiting_list)}"

