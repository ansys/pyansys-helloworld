Example Greeter Server
======================

This is an example greeter server modeled after the gRPC example from
[gRPC examples](https://github.com/grpc/grpc/tree/master/examples)


Installation
------------

Prequisites
~~~~~~~~~~~

All gRPC servers rely on protoc and gRPC-specific code generated from
proto interface files.  Visit the `protos
<https://github.com/pyansys/pyansys-example/tree/master/python/helloworld/protos>`_
directory and follow the directions there to build and install the
``ansys-api-greeter-example-v1`` package required by this client.


Build and Install
~~~~~~~~~~~~~~~~~

This example is a python package and can be installed by cloning this
repository and running the following from this directory.

.. code::

   pip install .

Alternatively, you can create a source distribution and install it.
This has the advantage of being a portable package

.. code::

   python setup.py sdist
   pip install dist/ansys-examples-greeter-server-0.1.0.tar.gz

Once you have installed the server, you can run the server from
anywhere simply with:

.. code::

   python -m ansys.examples.greeter_server

This will automatically start the server.  If you wish to run the server from within Python, you can run:

.. code:: python

   >>> from ansys.examples.greeter_server.server import serve
   >>> serve(50051)
   Greeter service started on port 50051
