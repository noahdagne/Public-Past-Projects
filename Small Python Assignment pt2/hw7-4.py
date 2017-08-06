#Noah Dagne
#INST326
def updatemin( key, min_values, values):
    if(values < min_values[key]):
        min_values[key] = values

def process_file(fin):
    is_data = False
    for line in fin:
        if is_data:
            arr = line.split(',')
            heart = float(arr[1].replace('%', ''))
            motor = float(arr[5].replace('%', ''))
            teen = float(arr[7].replace('%', ''))
            smoking = float(arr[11].replace('%', ''))
            obesity = float(arr[13].replace('%', ''))

            updatemin('Heart Disease Death Rate (2007)', min_values, heart)
            updatemin('Motor Vehicle Death Rate (2009)', min_values, motor)
            updatemin('Teen Birth Rate (2009)', min_values, teen)
            updatemin('Adult Smoking (2010)', min_values, smoking)
            updatemin('Adult Obesity (2010)', min_values, obesity)

        if line.startswith('State,'):
            is_data = True
    print(min_values)

min_values = {'Heart Disease Death Rate (2007)': 99999999,
              'Motor Vehicle Death Rate (2009)': 99999999,
              'Teen Birth Rate (2009)': 99999999,
              'Adult Smoking (2010)': 99999999,
              'Adult Obesity (2010)':99999999}


try:
    input_file = open('riskfactors.csv', 'r')
except:
    print("Unable to open file.")
    exit()

process_file(input_file)
input_file.close()


