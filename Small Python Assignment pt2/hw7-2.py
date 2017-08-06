#Noah Dagne
#INST326
def process_file(fin):
    is_data = False
    for line in fin:
        if is_data:
            arr = line.split(',')
            print(('%-25s : %-25s\n' % (arr[0], arr[5])))
        if line.startswith('State,'):
            is_data = True
            arr2 = line.split(',')
            print(arr2[0], arr2[5])
            print(('%-25s : %-25s\n' % (arr2[0], arr2[5])))



try:
    input_file = open('riskfactors.csv', 'r')
except:
    print("Unable to open file.")
    exit()

process_file(input_file)
input_file.close()