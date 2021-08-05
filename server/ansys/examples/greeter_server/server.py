# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server.

Source obtained from:
https://github.com/grpc/grpc/tree/master/examples/python/helloworld

"""

from concurrent import futures

import grpc

from ansys.api.greeter_example.v1 import greeter_pb2
from ansys.api.greeter_example.v1 import greeter_pb2_grpc


class Greeter(greeter_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print('Say Hello request received')
        return greeter_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve(port=50051):
    """Serve the greeter service.

    Parameters
    ----------
    port : int, optional
        Port number of the server.

    """
    print(f'Greeter service started on port {port}')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()
