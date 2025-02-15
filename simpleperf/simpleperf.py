from socket import *
import argparse
import time
import sys
import re
import threading as thread

import ipaddress


# Define a function called "Check_ipaddress" that contains a parameter called "host"
def check_ipadress(host):

    '''

    This function validates the typed ip-address
    Argument:
    host: inputs their ip-address
    return: The function returns the ip-address if it valid

    '''

    # Making a try-except to handle the host ip-adress, it would check that the host ip-address is correct or incorrect
    try:
        # Creating a variable that contains an object from the host parameter
        ip = ipaddress.ip_address(host)
    # If the exception is entered (in the situation where the ip-adress is incorrect) then the code will execute the
    # following commands below
    except:
        # Printing an error message because the ip-adress is invalid
        print('Error: Incorrect ip-adress')
        # In this case the function returns false, which indicates that the ip-adress is incorrect
        return False

    # In this case the try-exceptions is successfully executed, and then the function returns true (meaning the
    # ip-adress is correct
    return True


# Define a function called "Check_port" that contains a parameter called "port"
def check_port(port):

    '''

    The function validates the port number
    Arguments:
    port: is the typed port number
    Return: returns the port number if its valid

    '''
    # Making a try-except that handles a port, it would check that the port is correct or incorrect
    try:
        # Making a variable that converts the port parameter to an interger
        portnr = int(port)

    # If the exception is entered, (which means that the port-number is incorrect) it would execute the following
    # lines bellow
    except:
        # Printing an error-message because the port number must be an integer
        print('Error: incorrect data-type- it should be an integer')
        # The function returns False, because the port-number is incorrect
        return False

    # Making an if-statment which checks that the port-number is between 1024 and 65535
    if 1023 < portnr <= 65535:
        # The if-sentence returns true, because the port-number is between 1024 and 65535
        return True

    # If the port-number is not between 1024 and 65535, it jumps inside the else-sentence
    else:
        # Prints an error-message that the port-number is incorrect (is not between 1024 and 65535)
        print('Error: Incorrect port-number')
        # The else-sentence returns false, because the port-number is incorrect
        return False


# Define a function called "check_time", and it contains a parameter called "time.c"
def check_time(time_c):

    '''
    Function that checks if the time is grater than 0
    Argument:
    time_c: the time specified by the client
    Return: Returns the time if it is greater than 0
    '''

    # Using an if-sentence to check if the time_c parameter is less or equals to 0
    if time_c <= 0:
        # if it's true, we print a message that the time must be more than 0 seconds
        print('The time which you are using, must be more than 0-seconds')

        # Using sys.exit() as implemented above to exit the system
        sys.exit()

    # In this case, the time_c parameter is greater than 0, and the function returns the value of time_c
    return time_c


# Define a function called check_parallel_connection, which contains a parameter number
def check_parallel_connection(number):

    '''
    Function that checks that the pararell number is between 1 or 5
    Arguments:
    number: the typed number
    Return: Returns the time if the typed number is between 1 or 5
    '''

    # If-sentence that checks that number are less than 1 or greater than 5
    if number < 1 or number > 5:
        # if this is true, is would print that the need number have to be an inger between 1 and 5
        print('The number parameter of parallel connection must be an integer between 1 and 5')
        # And after exit the system with sys.exit()
        sys.exit()
    # In this case the number is valid, and the function return a value between 1 and 5
    return number


# Need Fahmi's help :)

def print_stats_interval(client_ip, client_port, last_interval, start_time, total_interval_bytes, format):
    '''

    The function is printing the statistics is selected by the client, to different intervals

    argument:
    client_ip: the client_ip is the client ip-address
    client_port: is the client port
    last_interval: the time of the last printed interval
    start_time: the time in the beginning of the data transfer
    total_interval_bytes: the total amount of bytes sent in current interval
    format: output-format specified by the client
    return: None
    '''

    # Calculates the elapsed interval time, interval duration and the interval bandwidth
    print_intelval_dur = last_interval - start_time
    intervall_dur = time.monotonic() - last_interval
    intervall_bw = ((total_interval_bytes / 1000 ** 2) / intervall_dur) * 8

    # Making to variables that converts to a specified format
    cor_value, cor_unit = convert_unit(total_interval_bytes, format)

    # Defining printing variables
    client_info = f"{client_ip}:{client_port}"
    time_span = f'{print_intelval_dur:.1f} - {intervall_dur + print_intelval_dur:.1f}'
    count_byte = f'{cor_value:.0f} {cor_unit}'
    bandwidth_output = f'{intervall_bw:.2f} Mbps'

    # Printing the variables into a table
    string = f"{client_info:<20} {time_span:<20} {count_byte:<20} {bandwidth_output}"
    print(string)


# A function "called convert_unit", with two parameters "value, and cor_unit- stands for core-unit"
def convert_unit(value, cor_unit):

    '''

    The function convert the bytes to a specified format
    Arguments:
    value: The amount of bytes
    cor_unit: Which format to convert to
    return: Returns the total bytes in specified and the chosen unit

    '''

    # Making a dictionary that contains unit I want to use such as B-Bytes, KB- Kilobytes and MB- Megabytes
    # And what does equals
    units = {
        'B': 1,
        'KB': 1000,
        'MB': 1000 ** 2
    }

    # Defines a variable cor_unit which is the parameter cor_unit in an upper case
    # This will avoid low-and-upper case errors
    cor_unit = cor_unit.upper()

    # Trying to convert the input to a float
    try:
        value = float(value)
    # Raising a ValueError that the input must be a number
    except ValueError:
        raise ValueError('You need to input a number bby')

    # If cor_unit parameter are not in the unit's dictionary, we would raise a valueError that the input must the
    # three units in the dictionary
    if cor_unit not in units:
        raise ValueError('Choose right units B, KB or MB')

    # Dividing the input value to the cor_unit input inside the units-dictionary
    cor_value = value / units[cor_unit]

    # Creating a tuple which contains the converted value and the correct unit
    return_state = (cor_value, cor_unit)

    # The function return the tuple we made above
    return return_state


# A function has a parameter size_string, and it converts into an integer
def convert_bytes(string_size):

    '''

    The function handles a string which represents a specific amount and converts it to bytes
    Arguments:
    string_size: A sting with a specified amount in this format 2000MB
    Return: returns the size in bytes

    '''

    # Defines a variable that matches a size string that has optional unit suffix
    size_re = re.compile(r'^\s*(\d+)\s*([BKM])?B?\s*$')

    # Defines a variable match, and attempt to match the size_re with the parameter string_size as input
    match = size_re.match(string_size)

    # If the string size does not match the optional (unit suffix???), we raise a ValueError
    if not match:
        raise ValueError(f'Invalid size string: {string_size}')

    # Define a size variable to se if it matches the group, and then convert it to an integer
    size = int(match.group(1))

    # Extracts the unit suffix from the group??????
    unit = match.group(2)

    # If the unit equals "K", then the size will be multiplied like this (size = size * 1000)
    if unit == 'K':
        size *= 1000

    # Else-if the unit equals "M", then the size will ble multiplied like this (size = size * 1000 * 1000)
    elif unit == 'M':
        size *= 1000 * 1000

    # Returns the size in unit "bytes"
    return size

    # Fahmi


def handle_client(con_sock, client_ip, client_port, format):
    '''
    The function handles client connections and receives data from the client
    con_sock: connection socket from the client
    client_ip: the clients ip-address
    client_port: the client port
    format: output-format specified by the client
    return: None
    '''

    # Declaring variables
    total_bytes = 0
    start_time = None

    # Creating a while-loop that receives data until a "bye" command
    while True:
        # Try-exception to check if the connection is reset
        try:
            # Reciveing data
            data = con_sock.recv(1000)
            # if-sentence to start time if the data start's with "START TIME"
            if data.startswith('START TIME'.encode()):
                start_time = time.monotonic()
                total_bytes -= len('START TIME'.encode())
            # If-sentence to check if the data end's with "BYE" and the breaking out of the loop
            if not data or data.endswith(b'BYE'):
                total_bytes += len(data) - len(b'BYE')
                con_sock.sendall(b'ACK: BYE')
                break
            total_bytes += len(data)
        except ConnectionResetError:
            print('Connection is going to reset')
            sys.exit()

    # Try-exception to check if the start time is set
    try:
        # Calculates the end time and the time duration
        end_time = time.monotonic()
        duration = end_time - start_time
        # If-sentence to set duration to 1 second if transfer time is less than 1
        if duration < 1:
            duration = 1
        # Calculating the bandwidth and round the number to 2 decimal
        bandwidth = ((total_bytes / 1000 ** 2) / duration) * 8
        bandwidth = round(bandwidth, 2)
        # Convert to chosen format
        core_value, core_unit = convert_unit(total_bytes, format)

        # Defining printing variables
        client_info = f"{client_ip}:{client_port}"
        time_span = f"0.0 - {duration:.1f}"
        count_byte = f"{core_value:.0f} {core_unit}"
        bandwidth_output = f"{bandwidth:.2f} Mbps"

        # Printing the value in the variables into a table, then closing the connection socket
        print(f"\n{'ID':<20} {'Interval':<20} {'Transfer':<20} {'Bandwidth'}\n")
        output_str = f"{client_info:<20} {time_span:<20} {count_byte:<20} {bandwidth_output}"
        print(output_str)
        con_sock.close()

    except TypeError:
        print('Start message not recived by the client')
        sys.exit()


def server(ip_bind, port, format):

    '''

    Function which is running in server mode, which is containing 3 parameters.
    ip_bind: the ip-address which is used to bind the server_socket
    port: the port number, which is also bind with the ip-address to the server_socket
    format: Which format that the data should be shown as the output
    Return: None

    '''

    # Creating a new server socket
    server_socket = socket(AF_INET, SOCK_STREAM)

    # Making a try-and-exception that binds the port and the ip-address, if the binding is not successful
    # Than it would print a message with an error, and then exit the system
    try:
        server_socket.bind((ip_bind, port))
    except:
        print('failng in binding ERROR!')
        sys.exit()

    # sjekk keyboardinterupt if tid!
    # The server is listening for a connection on the server socket
    server_socket.listen(1)
    server_output = f'A simpleperf server is listening on port {port}'
    # Formatting the message as the task stated
    print("-" * len(server_output))
    print(server_output)
    print("-" * len(server_output))

    # Making a while-loop that handles any incoming connections
    while True:
        # Accepting any incoming connection, and then requesting for the client_ip and the client_port
        # Then using it to print a connection message, with the server ip and port, than the client ip and port
        connection_socket, addr = server_socket.accept()
        client_ip = addr[0]
        client_port = addr[1]
        print(f'\nA simpleperf client with {client_ip}:{client_port} is connected with {ip_bind}:{port}')
        # Creating a new thread to handle multiple client's
        new_thread = thread.Thread(target=handle_client, args=(connection_socket, client_ip, client_port, format))
        new_thread.start()


def client_send_data(sock, client_ip, client_port, duration, format, num, interval):
    '''
    The function sends data to the server until either number of bytes is reached or duration
    argument:
    sock: client socket
    client_ip: client ip-address
    client_port: client port
    duration: the time specified by the client
    format: output-format specified by the client
    num: the amount of data to transfer
    interval: the interval time to print the transfer statistics
    return: None
    '''

    # Sending a message indicating that the server must start the time
    sock.sendall('START TIME'.encode())

    # Preparing data of 1000 bytes
    data = 'x'.encode() * 1000

    # Creating variables to prepare the tracking of data transfer
    total_bytes = 0
    start_time = time.monotonic()
    last_interval = start_time
    total_interval_bytes = 0

    # Creating a while-loop which transfer data until specified number of bytes is sent or time is reached
    while True:
        if num and total_bytes >= num:
            break
        elif not num and time.monotonic() - start_time >= duration:
            break
        # Else then it would send data and updates variables
        else:
            sock.sendall(data)
            total_interval_bytes += len(data)
            total_bytes += len(data)
        # If-sentence if interval is specified then print the interval statistics
        if interval and time.monotonic() - last_interval >= interval:
            print_stats_interval(client_ip, client_port, last_interval, start_time, total_interval_bytes, format)
            total_interval_bytes = 0
            last_interval = time.monotonic()

    # Prints the last interval
    if interval and total_interval_bytes > 0:
        print_stats_interval(client_ip, client_port, last_interval, start_time, total_interval_bytes,
                             format)
        print('-' * 75)
        total_interval_bytes = 0
        last_interval = time.monotonic()

    # Try-exception to see if the bye message is sent, and that the acknowlengment is recvied
    try:
        sock.sendall(b'BYE')
        ack = sock.recv(1024)
        if ack != b'ACK: BYE':
            raise RuntimeError('Acknowledgement not recived')
    except ConnectionResetError:
        raise ConnectionResetError('The connection has been restarted by the server')

    # Calculating the statistics of the transfer
    end_time = time.monotonic()
    elapsed_time = end_time - start_time
    bandwidth = ((total_bytes / 1000 ** 2) / elapsed_time) * 8

    # Converting total bytes into correct format
    if num:
        cor_value, cor_unit = convert_unit(num, format)
    else:
        cor_value, cor_unit = convert_unit(total_bytes, format)

    # endre på navnene
    address = f"{client_ip}:{client_port}"
    time_range = f"0.0 - {elapsed_time:.1f}"
    byte_count = f"{cor_value:.0f} {cor_unit}"
    bandwidth_str = f"{bandwidth:.2f} Mbps"

    output_str = f"{address:<20} {time_range:<20} {byte_count:<20} {bandwidth_str}"
    print(output_str)

    sock.close()


def client(ip, port, duration, parallel, format, num_b, interval):

    '''

    The function which is running in client mode, containing 7 parameters - the following arguments:
    ip: ip-address of the server mode
    port: the port number of the server mode
    duration: the total duration of the data transmitted
    parallel: the amount of the parallel connection
    format: the transferred data in chosen format
    num_b: the chosen amount of bytes to be transmitted
    interval: The time between each statistics printed in seconds
    Return: None

    '''

    # Making an empty array to store upcoming threads
    array_list = []

    # num_b are converted to bytes as long as it's provided
    num_bytes = None
    if num_b:
        num_bytes = convert_bytes(num_b)

    # Making a for-loop to search every connection in the parallel-connections
    for conn in range(parallel):

        # Creating client socket for every parallel connection
        client_socket = socket(AF_INET, SOCK_STREAM)

        # Using try-exception to connecting to the server with the client ip and client port
        try:
            client_socket.connect((ip, port))
            client_ip, client_port = client_socket.getsockname()
        # If not, printing an error message than exiting the system
        except:
            print('failed to connect ERROR!')
            sys.exit()

        # If the connection is successful it would print a connection message
        if conn == 0:
            client_string = f'A simpleperf client connecting to {ip}, port {port}'
            print('-' * len(client_string))
            print(client_string)
            print('-' * len(client_string), '\n')

        if parallel != 1:
            print(f'Client {client_ip}:{client_port} connected with {ip} port {port}')
        else:
            print(f'Client connected with {ip} port {port}')


        # Creating a new thread for the client connection
        new_connection_thread = thread.Thread(target=client_send_data, args=(
            client_socket, client_ip, client_port, duration, format, num_bytes, interval))

        # Starting a new thread and then adding it to the array_list we made above
        new_connection_thread.start()
        array_list.append(new_connection_thread)

    # Print the output as asked format (table header)
    print(f"\n{'ID':<20} {'Interval':<20} {'Transfer':<20} {'Bandwidth'}\n")

    # Wait for all threads to end/finish
    for conn in array_list:
        conn.join()


if __name__ == '__main__':

    # Initializing a argument parser
    parser = argparse.ArgumentParser()

    # Defines the following options and commands that my program should do like the task states
    parser.add_argument("-s", "--server", action="store_true", help="Running in server mode")
    parser.add_argument('-c', '--client', action='store_true', help='Running in client mode')
    parser.add_argument('-b', '--bind', type=str, default='127.0.0.1', help='IP-adress for connecting')
    parser.add_argument('-I', '--serverip', type=str, default='127.0.0.1', help='Ip-adress from the client')
    parser.add_argument('-p', '--port', type=int, default=8088, help='Port-number for connecting')
    parser.add_argument('-t', '--time', type=int, default=25, help='Chose the time you want to send the packets')
    parser.add_argument('-n', '--num', type=str, default=None, help='Choose your units')
    parser.add_argument('-f', '--format', type=str, default='MB', help='Choose your format')
    parser.add_argument('-P', '--parallel', type=int, default=1, help='Use this to create parallel connections')
    parser.add_argument('-i', '--interval', type=int, default=None, help='To specify the time')

    # Parsing the following argument from the command line
    args = parser.parse_args()

    # If-sentence checks if both server and client are selected, then exiting the system if it's true
    if args.server and args.client:
        print('you cant use both')
        sys.exit()

    # If-sentence to check if server-mode is selected
    if args.server:
        # If-sentence to validate ip-address and the port are correct
        # Then running the server function
        if check_ipadress(args.bind) and check_port(args.port):
            server(args.bind, args.port, args.format)

    # If-sentence to check if the client_mode is selected
    elif args.client:

        # Checks the time-duration of the connection
        time_dur = check_time(args.time)

        # Checks the number of the parallel connection
        pararel_check = check_parallel_connection(args.parallel)

        # The interval is set to 0 default
        interval = None

        # If-sentence to check if the number of bytes is specified, then convert the number to the correct unit
        if args.num:
            number_con_bytes = convert_bytes(args.num)

        # If-sentence to check if an interval is specified, then it would calculate the value
        if args.interval:
            interval = check_time(args.interval)

        # If-sentence to check that the interval is not equal to duration
        if interval and interval >= time_dur:
            raise ValueError('Interval can not be as same as time')

        # Validates the server ip-address and the port-number
        if check_ipadress(args.serverip) and check_port(args.port):
            # Running the client function with the optional arguments
            client(args.serverip, args.port, time_dur, pararel_check, args.format, args.num, interval)

    # If both server and the client is not chosen, then print a message
    # change 1
    else:
        print('Error: you must run either in server or client mode')

