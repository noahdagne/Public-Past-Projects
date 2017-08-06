#Noah Dagne
#INST326
def process_file(fin):
    is_data = False
    for line in fin:
        if is_data:
            arr = line.split(',')
            print('% - 30s : % - 30s: % - 30s : % - 30s: % - 30s : % - 30s\n ' % ((arr[0], arr[1], arr[5], arr[7], arr[11], arr[13])))
        if line.startswith('State, '):
            is_data = True
            arr2 = line.split(',')
            print('% - 25s : % - 25s: % - 25s : % - 25s: % - 25s : % - 25s\n ' % ((arr[0], arr[1], arr[5], arr[7], arr[11], arr[13])))

try:
    input_file = open('riskfactors.csv', 'r')
except:
    print("Unable to open file.")
    exit()

process_file(input_file)
input_file.close()