class Member:
    def _init_(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def _str_(self):
        return f"{self.member_id} - {self.name}"
