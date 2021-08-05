### Ansys Python gRPC Examples

The following examples demonstrate how to create a basic pyansys
server/client package following both Google and Ansys's recommendations
regarding gRPC.

The main aim of these examples is to demonstrate any Ansys specific
tools, packaging, or paradigms designed to make it easier to build,
maintain, and deliver services.

For all other documentation, reference the official documentation at
[gRPC](https://grpc.io/).


#### Directory Description

Every gRPC service contains a Server and Client with a proto file or
files describing the services exposed by the service.  This example
contains the minimum components necessary to install a greeter service
and client package to demonstrate how to package and run a basic
service.


#### Installing and Running this Service

1. First, visit the
[protos](https://github.com/pyansys/pyansys-helloworld/tree/main/protos)
directory and follow the instructions there to build the proto package
from the example proto files.

2.  Install the server within the
[server](https://github.com/pyansys/pyansys-helloworld/tree/main/server)
directory by following the README there.  This relies on the package
you built from the previous step; please be sure you installed that.

3. Install the client within the
[client](https://github.com/pyansys/pyansys-helloworld/tree/main/client)
directory by following the README there.  This also relies on the
proto package you built from the previous step; please be sure you
installed that.


Once you have the server and client installed on your local environment, startup the server with:

```
python -m ansys.examples.greeter_server
```

Then, within a different terminal, start the client with:

```
python -m ansys.examples.greeter_client
```

If everything worked out, the client should start, connect to the
server and print:

```
Greeter client received: Hello, you!
```

For further details, see the READMEs within the `proto`, `server`, or
`client` directories.


#### Packages

If you want to just want to run the greeter example without building
any of the packages, you can download the source distributions from
[Releases](https://github.com/pyansys/pyansys-helloworld/releases).
Please follow the directions in the release.
