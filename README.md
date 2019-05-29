# RMIServerClient

<a href="https://travis-ci.org/ezequielramos/RMIServerClient">
  <image src="https://travis-ci.org/ezequielramos/RMIServerClient.png?branch=master">
  </image>
</a>
 
Tested with python 2.7

We recommend you to use it on a python virtual environment.

If you're running this on a debian distro you can just run dependencies.sh and it'll install all necessary dependencies:

```
$ ./dependencies.sh
```

Pyro's Name Server should be installed, you can run it with the default configuration (localhost:9090) or you can choose other host and port to bind.

```
$ pyro4-ns
$ pyro4-ns -n 127.0.0.1 -p 3000
```

The Server can be runned on default configuration or choosing a specific host and port:

```
$ python server.py
$ python server.py 127.0.0.1 3000
```

As well the Client can be running with on the same way:

```
$ python client.py
$ python client.py 127.0.0.1 3000
```
