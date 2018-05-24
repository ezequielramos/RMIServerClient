import Pyro4
import sys

try:
	ns = Pyro4.locateNS()
	server_names = ns.list('greeting-') #this should be returning me all servers registered on pyro's nameserver
except Pyro4.errors.NamingError:
	print("\nFailed to locate the nameserver. Make sure it's running, execute: \n\npyro4-ns\n")
	exit()

keys = list(server_names.keys())

if len(keys) == 0:
	print("\nCan't find any server available.\n")
	exit()

if sys.version_info.major == 3:
    name = input("What is your name? ").strip()
else:
	name = raw_input("What is your name? ").strip()

greeting_maker = Pyro4.Proxy(server_names[keys[0]]) #try to connect to the first server 

try:
	print(greeting_maker.get_fortune(name))
except Pyro4.errors.CommunicationError: #if failed to connect to the first server try with the second one
	greeting_maker = Pyro4.Proxy(server_names[keys[1]])
	print(greeting_maker.get_fortune(name))