# Remote-Procedure-Call
- Built a Simple Middleware System thhat allows dynamically adding a service into the system and allows accessing the service from a client program.
- Designed a RPC protocol consisting of Server Stub and Client Stub, responsible to run any given function present in server machine as shared library on client side.
- Protocol can adapt any generic function and these functions are usable from client machine using import functions.
## Running Instructions
- ```python code_generator_client.py contract.json```
This will generate the rpc_client.py which will have client side stubs for every procedures defined in contract.json
- ```python code_generator_server.py contract.json```
This will generate the rpc_server.py which will have server side stubs for every procedures defined in contract.json
