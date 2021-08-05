Example Greeter Client
======================

This is an example greeter client modeled after the gRPC example from
[gRPC examples](https://github.com/grpc/grpc/tree/master/examples)


Installation
------------

Prequisites
~~~~~~~~~~~

All gRPC clients rely on protoc and gRPC-specific code generated from
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
   pip install dist/ansys-examples-greeter-0.1.0.tar.gz


Usage
~~~~~
First, be sure you have the `ansys-example-greeter-server` up and
running by following the directions in
[server](https://github.com/pyansys/pyansys-helloworld/tree/main/server).

Next, simply run the client package main with:

.. code::

   python -m ansys.examples.greeter_client

This runs the `__main__.py` contained in the package's directory.
Provided the server is up and running, this should return:

.. code::

   Greeter client received: Hello, you!

If you wish to run the example within Python, you can run:

.. code:: python

   >>> from ansys.examples.greeter_client.client import run
   >>> run()
   Greeter client received: Hello, you!
