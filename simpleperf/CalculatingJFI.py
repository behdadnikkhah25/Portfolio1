
# Function that takes in a list of throughputs and returns Jains Fairness Index

# Converted values in the list to float in order to be as accurate as possible
def jainsall(listFlows):

    # Declare
    total_sum = numerator = denominator = square_sum = totNum = valJFI = 0      # Declaring variables

    totNum = len(listFlows)                                                     # Getting the number of throughputs in the list

    try:                                                                        # Using try for exception handling
        for flow in listFlows:                                                  # For-loop that goes through all the throughputs in the list
            total_sum = total_sum + float(flow)                                 # Converting the throughputs and then calculating the total sum
            square_sum = square_sum + (float(flow)**2)                          # Converting the throughputs and then calculating the sum of the square of each value

        numerator = total_sum ** 2                                              # Calculating the upper part of the JFI formula
        denominator = totNum * (square_sum)                                     # Calculating the lower part of the JFI formula
        valJFI = numerator/denominator                                          # Calculating and returning the JFI value
        return f"JFI = {valJFI:.2}"

    except:
        return "Error! Unable to calculate JFI!"                                # If an error occurs, printing a message
    

list = [6.04,7.88,7.48,7.82]

print(jainsall(list))