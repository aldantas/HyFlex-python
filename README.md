# HyFlex-python
Allows the implementation of Hyper-Heuristics in Python using the problems and
heuristics from the
[HyFlex](http://www.asap.cs.nott.ac.uk/external/chesc2011/hyflex_description.html)
Java Framework. It relies on [Py4J](https://www.py4j.org/) to create a
connection between the Python interpreter and the JVM.

## How to use
Install Py4J following any of the
[instructions](https://www.py4j.org/install.html#id1), and then locates where it
placed the `py4j0.x.jar` file in your machine.

In the file `start_server.sh`, replace `<path to py4j jar file>` with the correct
file path. Give it permission to run and start the JVM server application:

```
$ chmod +x start_server.sh
$ ./start_server.sh
```

That's it. Now you can use the Py4J libary in Python to connect to the JVM. See
`example_hyper_heuristic.py` for an example.
