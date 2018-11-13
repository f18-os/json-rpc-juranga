# JSON RPC Lab

***

### Description

This directory contains the following files: 


* jclienttpy - a python3 executable file that serves as a basic client connecting to jserver.py that does the following:

  1. Connect to the server created by running jserver.py 

  2. Creates 4 node classes connected to each other in a b-tree like structure and sends them to the server as a JSON object.

* jserver.py - a python3 executable file that creates a naive server that listens to port 50001 

  1. Creates a server that clients can connect to in order to send Node objects as JSON interpretable

* node.py - a python3 file that contains the Node Class and a JSON Serializer/Deserializer class for the node.

* request.json - 

***

### Running Program

1) You must be using a UNIX OS to assure that this code runs
correctly. Running on Windows may cause issues with the piping code.

2) Make sure to have any version of python3 installed. Python2 is not
supported.

3) Once the above conditions are met, you will need to run the following 2 commands on separate shells:


	1) `python3 jserver.py`

    2) `python3 jclient.py`

