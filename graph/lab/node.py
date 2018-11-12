import json

class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0

class nodeEncoder(json.JSONEncoder):
    def to_json(self, node):
        return json.dumps(node, default=lambda x: x.__dict__)

    def json_loader(self, obj):
        if 'node' in obj:
            return node(obj['node'])

    def from_json(self, obj):
        return json.loads(obj, object_hook=self.json_loader)

