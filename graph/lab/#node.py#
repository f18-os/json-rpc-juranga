import json
from collections import defaultdict

class node:
    def __init__(self, name, children = [], val= 0):
        self.name = name
        self.children = children
        self.val = val

    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)
            
def show_g(graph, level=0):
    print("%s%s val=%d:" % (level*"  ", graph.name, graph.val))
    for c in graph.children: 
        show_g(c, level= level + 1)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

def deserialized_increment(obj, obj_dict):
    if not obj_dict[obj.name] == 0:
        obj_dict[obj.name].val += 1;
        obj.val = obj_dict[obj.name].val;
    else:
        obj.val += 1
        obj_dict[obj.name] = obj
    for c in obj.children:
        deserialized_increment(c, obj_dict)
        
class nodeEncoder(json.JSONEncoder):
    def to_json(self, node):
        return json.dumps(node, default=lambda x: x.__dict__)

    def as_node(self, obj):
        return node(obj['name'], obj['children'], obj['val'])
            
    def from_json(self, obj):
        return json.loads(obj, object_hook = self.as_node)
