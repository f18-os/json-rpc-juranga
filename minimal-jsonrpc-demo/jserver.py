# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
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
    graph.val +=1;
    for c in graph.children:
      self.increment(c)
    return graph

  @request
  def show(self, graph, level=0):
      print("%s%s val=%d:" % (level*"  ", graph.name, graph.val))
      for c in graph.children: 
          c.show(level + 1)

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, Node(),framing_cls=JSONFramingNone)
