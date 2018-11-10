import json

class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0

class nodeEncoder(json.JSONEncoder):
    def to_json(self, o):
        return o.__dict__

    def from_json(self, obj):
        if 'node' in obj:
            return node(obj['node'])

