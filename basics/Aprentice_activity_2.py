import operator

saved_string = ''

def remove_letter(): #Remove a selected letter from a string
    typed_string = str(raw_input("Type a String: "))
    letter_to_remove = str(raw_input("type the letter you want to remove: ")) #this will accept a string not only a letter
    letter_to_remove = letter_to_remove[0] #this will take only the first letter
    string_length = len(typed_string)
    location = 0

    while (location < string_length): #this will do it by reference
     if typed_string[location] == letter_to_remove:
      typed_string = typed_string[:location] + typed_string[location+1::]
      string_length -= 1
     location += 1
    print ("Result: %s" % typed_string)
    return


def num_compare(): #Compare 2 numbers to determine the larger
    num1 = int(raw_input("First number: "))
    num2 = int(raw_input("Second number: "))
    if num1 < num2 :
     print num2
    elif num1 > num2:
     print num2
    else:
     print("EQUALS")
    return


def print_string(): #Print the previously stored string
    print (saved_string)
    return


def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
    dict_op = { "+" : operator.add, "-" : operator.sub, "*" : operator.mul, "%" : operator.div }
    num1 = int(raw_input("First number: "))
    op = str(raw_input("OPERATOR : "))
    num2 = int(raw_input("Second number :"))
    
    print dict_op[op](num1,num2)
    return


def accept_and_store(): #Accept and store a string
    global saved_string 
    saved_string = str(raw_input("Input string: "))
    return



def main(): #menu goes here
    opt_select = [accept_and_store,
                  calculator,
                  print_string,
                  num_compare,
                  remove_letter]
    while (True):
     print ("SELECT OPTIONS")
     print("1\taccept and store")
     print("2\tcalculator")
     print("3\tprint string")
     print("4\tnum compare")
     print("5\tremove letter")
     opt_choice = int(raw_input("SELECTION: "))
     opt_choice -= 1
     opt_select[opt_choice]() 
    return

main()
