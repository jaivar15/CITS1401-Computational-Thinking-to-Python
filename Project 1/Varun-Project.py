"""
Project 1: Computational Thinking with Python

By Varun Jain - 22xxxxxx
   11/04/21
"""

def main(csvfile, country, stats_type):
    file = open_file(csvfile)
    if file is None:
        return
    
    data = extract_data(file)
    if data is None:
        return
    location, day, month, year, new_cases = data
    
    if stats_type.lower().strip() == 'statistics':
        process_data(country, location, day, month, year, new_cases)
    elif stats_type.lower().strip() == 'correlation':
        correlation_process_data(country, location, day, month, year, new_cases)
    
    

def open_file(filename):
    data = None
    
    try:
        infile = open(filename, 'r')            
    except Exception:
        print("File not found: {0:s}".format(filename))
        return None
    return infile

def extract_data(datafile):
    data = datafile.read()
    datafile.close()
    if not data.strip():
        print('The file provided does not contain any data')
        return
    
    iso_code, continent, location, date, new_cases, new_deaths = [], [], [], [], [], []
    for each in data.split('\n'):
        each_day_stats = each.split(',')
        iso_code.append(each_day_stats[0].lower().strip())
        continent.append(each_day_stats[1].lower().strip())
        location.append(each_day_stats[2].lower().strip())
        date.append(each_day_stats[3])
        new_cases.append(each_day_stats[4])
        new_deaths.append(each_day_stats[5])
    if len(iso_code) == 1:
        print('The file provided only contains header row and not any real data')
        return
    del iso_code[0]
    del continent[0]
    del location[0]
    del date[0]
    del new_cases[0]
    del new_deaths[0]
    
    day, month, year = [], [], []
    for i in range(len(location)):
        new_cases[i] = int(new_cases[i])
        each_date = date[i].split('/')
        day.append(int(each_date[0]))
        month.append(int(each_date[1]))
        year.append(int(each_date[2]))
    
    return location, day, month, year, new_cases



def process_data(country, location, day, month, year, new_cases):
    country = country.lower().strip()
    length = len(location)
    
    months_list = [[],[],[],[],[],[],[],[],[],[],[],[]]
    
    for i in range(length):
        if country == location[i]:
            months_list[month[i]-1].append(new_cases[i])

   
    
    minimum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maximum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    average = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    std_dev = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for rows in range(len(months_list)):
        min_val = float('inf')
        for columns in range(0,len(months_list[rows])):
            if months_list[rows][columns] > 0:
                if months_list[rows][columns] < min_val:
                    min_val = months_list[rows][columns]
        minimum[rows] = min_val
        if minimum[rows] == float('inf'):
            minimum[rows] = 0
    print(minimum)
            
    
    for rows in range(len(months_list)):
        max_val = float('-inf')
        for columns in range(0,len(months_list[rows])):
            if months_list[rows][columns] > 0:
                if months_list[rows][columns] > max_val:
                    max_val = months_list[rows][columns]
        maximum[rows] = max_val
        if maximum[rows] == float('-inf'):
            maximum[rows] = 0
    print(maximum)
    

    for rows in range(len(months_list)):
        sum_of_each_month = 0
        for columns in range(0, len(months_list[rows])):
            sum_of_each_month = sum_of_each_month + float(months_list[rows][columns])
        try:
            average[rows] = round(sum_of_each_month/len(months_list[rows]),4)
        except ZeroDivisionError:
            average[rows] = 0
    print(average)


    for rows in range(len(months_list)):
        sum_of_variance = 0
        for columns in range(0, len(months_list[rows])):
            variance = float(months_list[rows][columns]) - average[rows]
            sum_of_variance  = sum_of_variance + variance**2
        try:
            std_dev[rows] = round((sum_of_variance/len(months_list[rows]))**0.5,4)
        except ZeroDivisionError:
            std_dev[rows] = 0
    print(std_dev)
    
    
    





    for i in range(12):
        if len(months_list[i]) != 0:
            minimum[i] = min(i for i in months_list[i] if i > 0)
            maximum[i] = max(months_list[i])
            mean = sum(months_list[i]) / len(months_list[i])
            variance = sum([((x - mean) ** 2) for x in months_list[i]]) / len(months_list[i])
            std_dev[i] = round(variance ** 0.5, 4)
            average[i] = round(mean, 4)
    
# average and std dev not matching for May, June for sample data of France which doesn't make sense
    return minimum, maximum, average, std_dev






def correlation_process_data(country, location, day, month, year, new_cases):
    country_A = country[0].lower().strip()
    country_B = country[-1].lower().strip()

    length = len(location)

    months_list_A = [[],[],[],[],[],[],[],[],[],[],[],[]]
    months_list_B = [[],[],[],[],[],[],[],[],[],[],[],[]]


    for i in range(length):
        if country_A == location[i]:
            months_list_A[month[i]-1].append(new_cases[i])

    for i in range(length):
        if country_B == location[i]:
            months_list_B[month[i]-1].append(new_cases[i])


    minimum_A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maximum_A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    average_A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    std_dev_A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    minimum_B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maximum_B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    average_B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    std_dev_B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    for rows in range(len(months_list_A)):
        min_val = float('inf')
        for columns in range(0,len(months_list_A[rows])):
            if months_list_A[rows][columns] > 0:
                if months_list_A[rows][columns] < min_val:
                    min_val = months_list_A[rows][columns]
        minimum_A[rows] = min_val
        if minimum_A[rows] == float('inf'):
            minimum_A[rows] = 0
    print(minimum_A)

    for rows in range(len(months_list_B)):
        min_val = float('inf')
        for columns in range(0,len(months_list_B[rows])):
            if months_list_B[rows][columns] > 0:
                if months_list_B[rows][columns] < min_val:
                    min_val = months_list_B[rows][columns]
        minimum_B[rows] = min_val
        if minimum_B[rows] == float('inf'):
            minimum_B[rows] = 0
    print(minimum_B)

    sum_A = 0
    for rows in range(len(minimum_A)):
        sum_A = sum_A + minimum_A[rows]
    average_A = sum_A/len(minimum_A)
    print(average_A)
    sum_B = 0
    for rows in range(len(minimum_B)):
        sum_B = sum_B + minimum_B[rows]
    average_B = sum_B/len(minimum_B)
    print(average_B)

    minimum_A = [x - average_A for x in minimum_A]
    minimum_B = [x - average_B for x in minimum_B]

    minimum_AB = [minimum_A[i]*minimum_B[i] for i in range(len(minimum_A))]

    total_A = 0
    for element in range(0, len(minimum_A)):
        total_A = total_A + (minimum_A[element])**2
    total_A = total_A**0.5

    total_B = 0
    for element in range(0, len(minimum_B)):
        total_B = total_B + (minimum_B[element])**2
    total_B = total_B**0.5


    multiply = total_A * total_B
    print(multiply)
    total = 0
    for element in range(0, len(minimum_AB)):
        total = total + minimum_AB[element]

    a = round((total/multiply),4)
    print(a)


main('coviddata.csv', ['france', 'italy'], 'correlation')
