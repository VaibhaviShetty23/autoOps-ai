class MemoryBank:
    def __init__(self):
        self.store = []

    def save(self, incident, cause, fix):
        self.store.append({
            "incident": incident,
            "cause": cause,
            "fix": fix
        })

    def recall(self, incident):
        for record in self.store[::-1]:
            if record["incident"] in incident:
                return record
        return None
