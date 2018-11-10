import json

class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0

    def encode(self, obj):
        obj = json.JSONEncoder.encode(self, obj)
        return obj

    def decode(self, obj):
        obj = json.JSONDecoder.decode(self, obj)
        return obj

