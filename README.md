We are implementing the assignment in python :

DIRECTORY STRUCTURE : 

=> 2018111040
	-> Ds_Assignment2.pdf
	-> README.md
	-> requirements.txt
	-> src
		--> client.py
		--> server.py
		--> mst.py
	-> test
		--> input.txt
		--> input2.txt




==> INSTALLING DEPENDENCIES:
	1. Creating a virtual environment
		virtualenv -p python3 env
	2. Installing all packages 
		pip3 install -r requirements.txt

==> All Code is present in the folder src
==> Test cases are present in the folder tests

==> SERVER
1. The server code is present in the file called server.py.

2. For running the code
	python3 server.py <{optional IP address in case we are running it across systems}>

3. Details of the architecture are as follows :
	->  The IP address and the port number are taken and a socket is created. The server goes live and waits for connections
	-> 	A new thread is created for every new client , so that the commands can be collected from each client.
	-> 	All the commands are stored in a "commands_queue" .  Every thread uses a data lock to gain exclusive access to this queue. 
	->	Every command sent by every client is pushed to this queue, and they are executed linearly
	->	A thread is launched to run the commands. It also uses the data lock to gain access to the queue
	-> 	If the queue is empty, the thread goes to sleep for 1 second. Else, it sends the command string to the
		run_command function
	-> 	The run_command function parses the commmand into it's various parts.

	{ We have implementd the code for MST in a separate file called mst.py . We import class Graph() from this file }

	->	If the command is "add_graph" , a new graph is created with n nodes and added to a dictionary with it's identifier
	->	If the command is "add_edge", a new edge is added to the graph as per the parameters mentioned
	->	If the command is "get_mst" , the mst of the graph with the mentioned identifier is calculated. 
		ASSUMPTION :: The mst will give -1, as long as the number of connected components for the whole graph is not equal to 1. This ensures the MST actually spans the entire graph.
	->	If any other string is given as the command. The server will return a message indicating that a new proper 			command needs to be sent.
	
	PROVISION FOR CLIENT's COOMUNICATION ACROSS COMPUTERS:
	->	In order to function with clients across different computers, we are going to need the IP Address of the PC from which the server code is running. That can be provided as an optional parameter with the initial server command. The code will adjust it's own functioning accordingly. 
	However, there might be issues because of firewalls etc. So, that will have to be taken care of by the user.



==> CLIENT
1. The Client code is present in the file called client.py

2. For running the code
	python3 client.py <'{path to input file, in single quotes }'>  <{ optional IP address of server, in case we are running it across systems}>

3. Details of the architecture are as follows:
	->	The client takes the address of the input files. 
	->	It reads them line by line, makes a list of them. 
	->	It then appends the "quit" command to the end of the list. 
	->	This is to ensure that the client exits after all it's commands have been executed and does not hog resources ( 	as separate threads are being made for every client )
	->	After sending the command, the client waits for the response from the server. Upon receiving the response, it 		prints it out on the standard output.

	PROVISION FOR CLIENT's COOMUNICATION ACROSS COMPUTERS:
	->	In order to function with clients across different computers, we are going to need the IP Address of the PC from which the server code is running. That will then be provided as an optional parameter with the initial client command. The code will adjust it's own functioning accordingly. 
	However, there might be issues because of firewalls etc. So, that will have to be taken care of by the user.


==> MST IMPLEMENTATION
1. For the implementation of the MST, a scipy function for that effect has been used. 
	There is a slight catch though. The MST function from scipy returns an answer even when the MST does not span the entire graph. This is a concern because, according to our interpretation of the question, the MST is supposed to be -1, if the MST does not exist.

	->	In that spirit, another scipy function has been used that returns the number of Connected Components. This tells us whether there is some form of disconnection or not. If there is, then we know that the MST cannot exist. Hence, we return a -1.