#Noah Dagne
#INST326
def process_file(fin):
    is_data = False
    for line in fin:
        if is_data:
            print(line)
        if line.startswith('State,'):
            is_data = True


try:
    input_file = open('riskfactors.csv', 'r')
except:
    print("Unable to open file.")
    exit()

process_file(input_file)
input_file.close()