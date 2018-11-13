# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from collections import defaultdict
import json
import os
from node import *
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


# Class providing functions for the client to use:
@service_class
class Node(object):

  @request
  def increment(self, graph):
    graph = nodeEncoder().from_json(graph)
    obj_dict = defaultdict(int)
    deserialized_increment(graph, obj_dict)
    return nodeEncoder().to_json(graph)

  @request
  def show(self, graph):
    graph = nodeEncoder().from_json(graph)
    show_g(graph)
    graph = nodeEncoder().to_json(graph)
    json_file = os.open("request.json", "w+")
    json_file.write(graph)
    
# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, Node(),framing_cls=JSONFramingNone)
