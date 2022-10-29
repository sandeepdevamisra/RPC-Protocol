import sys
from rpc_client import clientRPC
rpc = clientRPC()
resp = rpc.foo("4")
print(resp)


