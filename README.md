A README file: info on how to run simpleperf and tests to generate data


# Simpleperf

Simpleperf is a program build in python- programming language. 
The code is using socket module and TCP as protocol, to measure and calculate different statistics. 
It calculates the different interval specified for a chosen amount of time,
the total amount of the data transmitted, the total amount of the time for the data transferred, 
and measures the bandwidth between two hosts. The host are -
*****firstly*** running in client mode** - and *****secondly*** in server mode**  

## Running the simpleperf:
 **Prerequisites**:

1. Fully install the python3 on your operating system  (*Windows, Mac OS, Linux etc.*)
2. After having python3 succsessfuly installed, you need to open a terminal window and execute following commands: 
python3 *simpleperf.py*. Note: You have to change the directory to where simpleperf is stored.

Next, you can run simpleperf in -**server mode** with options, by invoking it 
with the following commands: 

    python3 simpleperf -s -b <ip_address> -p <portnumber> -f MB


1. -s(--server)
   - Description: Running the code in server mode
     - Selected Mode: Server mode

2. -b(--bind)
   - Description: The ip- address of the server to bind the server
        - Default: *127.0.0.1*
        - Selected Mode: Server mode
   
3. -p(--port)
   - Description: the server port
     - Possible mode: Server mode & Client mode
     - Default: on port *(8088)*

4. -f(--format)
   - Description: Selected output for the format
     - selection alternatives:  (MB, KB and B) 
     - Possible mode: Server mode & Client mode

It is possible to run simpleperf in server mode on default, 
by invoking it with the following commands:

    python3 simpleperf -s



Operating the simpleperf program in client mode with options, 
can be invoked by the following commands:

    python3 simpleperf -c -I <server_ip> -p <server_port> -t <time> -P <parallel> -f <format> -n <num> -i <interval>

1. -c(--client)
   - Description: Running the code in client mode
     - Selected mode: Client mode

2. -I(--serverip)
   - Description: The server ip-address for connection  
        - Selected mode: Client mode
        - Default: 127.0.0.1

3. -p(--port)
   - Description: the server port
     - Possible mode: Server mode & Client mode
     - Default: on port *(8088)*

4. -t(--time)
   - Description: the total amount of the duration of the data transmitted
     - Selected mode: Client mode
     - Default: 25 seconds

5. -P(--parallel)
   - Description: the amount of parallel connection
     - Selection alternatives: between 1 or 5
     - Selected mode: Client mode
     - Default: 1

6. -f(--format)
   - Description: Selected output for the format
     - selection alternatives:  (MB, KB and B) 
     - Possible mode: Server mode & Client mode

7. -n(--num)
    - Description: Specify the total number of bytes wanted transferred 
     - Possible mode: Client mode
     - Default: None

8. -i(--interval)
   - Description: Displaying the statistitcs on the specified total amount of time 
     - Selection alternatives: specify the time in seconds 
     - Selected mode: Client mode
     - Default: None

Operating the client mode simply, can be invoked by the following commands:

    python3 simpleperf -c -I <server_ip> -p <server_port> -t <time>

## Example data for testing

Here is an example of how you can generate data

Firstly, you invoke the server by writing following commands:

    python3 simpleperf.py -s   

Then you should get a listing messaged displayed on your terminal, similar to this:

    ---------------------------------------------
    A simpleperf server is listening on port 8088
    ---------------------------------------------

The next step is to connect the client to the server, by the following commands:

    python3 simpleperf.py -c 

Then, you should receive a connection message displayed on your terminal for the client:

    Client connected with 127.0.0.1 port 8088

Additionally, you should also get a connection from the server containing the following:

    A simpleperf client with 127.0.0.1:52416 is connected with 127.0.0.1:8088



When the client has transmitted the data, the statistics is displayed to the client as such:

    ID                   Interval             Transfer             Bandwidth

    127.0.0.1:52416      0.0 - 25.0           15798 MB             5055.23 Mbps

The server also receives statistics, displayed as following:

    ID                   Interval             Transfer             Bandwidth

    127.0.0.1:52416      0.0 - 25.0           15798 MB             5056.74 Mbps









