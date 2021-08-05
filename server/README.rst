Example Greeter Server
======================



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
