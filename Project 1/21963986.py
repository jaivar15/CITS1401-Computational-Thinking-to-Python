'''
    CITS1401 Computational Thinking with Python: Project 1
    Student Name: Varun Jain 
    Student Number: 21963986
    Due Date: Friday 16th April
'''


def main(csvfile, country, stats_type):
    location, month, new_cases = extract_data(csvfile)  
    if stats_type.lower().strip() == "statistics":
        mn, mx, avg, sd = process_data_per_month(country, location, month, new_cases)
    elif stats_type.lower().strip() == "correlation":
        mn, mx, avg, sd = process_data_for_correlation(country, location, month, new_cases)
    return mn, mx, avg, sd
     

'''
    Extracts data from the covid file and seperates each column, and appends it to a individual list 
    Extracts the Date column, splits the date format dd/mm/yyyy into an array of substrings by the '/' deliminator. 
    Each substring is stored into a new list, and converted into a int data type. 
'''   

def extract_data(datafile):
    try:
        infile = open(datafile,'r')           
    except Exception:
        exit()
    iso_code, continent, location, date, new_cases, new_deaths = [], [], [], [], [], []
    for line in infile:
        #Splits the data using the ',' deliminator
        each_day_stats = line.split(',')
        #removes the \n from the end of each row
        each_day_stats[len(each_day_stats) - 1] = each_day_stats[len(each_day_stats) - 1].replace('\n','')
        #appends each column into a seperate list 
        iso_code.append(each_day_stats[0].lower().strip())
        continent.append(each_day_stats[1].lower().strip())
        location.append(each_day_stats[2].lower().strip())
        date.append(each_day_stats[3])
        new_cases.append(each_day_stats[4])
        new_deaths.append(each_day_stats[5])
    #exit the program if the csv only contains the headers 
    if len(iso_code) == 0 or len(iso_code) == 1:
        exit()
    #delete all the header rows 
    del iso_code[0]
    del continent[0]
    del location[0]
    del date[0]
    del new_cases[0]
    del new_deaths[0]

    #splits the date into day, month and year
    day, month, year = [], [], []
    for index in range(len(location)):
        new_cases[index] = int(new_cases[index])
        each_date = date[index].split('/')
        day.append(int(each_date[0]))
        month.append(int(each_date[1]))
        year.append(int(each_date[2]))
    return location, month, new_cases


'''
    The minimum() function calculates the minimum recorded positive cases for each month in the list
    the function loops through the 2D list and finds the smallest value in each list. 
    Stores the min value found for each month in a list, minimum_value_month from arranged in order from Jan to Dec. 
'''

def minimum(months_list, minimum_value_month):
    for rows in range(len(months_list)):
        #set minimun value to positive infinity 
        min_val = float('inf')
        #loop through the month_list
        for columns in range(0,len(months_list[rows])):
            if months_list[rows][columns] > 0:
                if months_list[rows][columns] < min_val:
                    min_val = months_list[rows][columns]
        minimum_value_month[rows] = min_val
        #infinity value present in the list, replace it with zero 
        if minimum_value_month[rows] == float('inf'):
            minimum_value_month[rows] = 0
    return minimum_value_month



''' 
    The maximum() function calculates the maximum recored postive cases for each month. 
    Input Parameters: 
        - months_lists: stores: a 2d list of the covid cases recorded month wise. 
        - maximum_value_month: passes through a list filled with zeros 
    Output: 
        - a list ordered from Jan to Dec of the highest number of covid cases recorded in each month
'''


def maximum(months_list, maximum_value_month):
    #loop through the months_list for each month 
    for rows in range(len(months_list)):
        #set the maximum value to negative infinity 
        max_val = float('-inf')
        #loop through the values in each row
        for columns in range(0,len(months_list[rows])):
            if months_list[rows][columns] > 0:
                #find the max value for each month 
                if months_list[rows][columns] > max_val:
                    max_val = months_list[rows][columns]
        #stores the max values for each month
        maximum_value_month[rows] = max_val
        #replace negative infinity with zero 
        if maximum_value_month[rows] == float('-inf'):
            maximum_value_month[rows] = 0
    return maximum_value_month 

'''
    The average() function calculates the average of cases recorded in each month 
'''

def average(months_list, average_per_month):
    for rows in range(len(months_list)):
        sum_of_each_month = 0
        for columns in range(0, len(months_list[rows])):
            sum_of_each_month = sum_of_each_month + months_list[rows][columns]
        try:
            average_per_month[rows] = round(sum_of_each_month/len(months_list[rows]),4)
        except ZeroDivisionError:
            average_per_month[rows] = 0
    return average_per_month


'''
    The standardDeviation() calculates the std for each month. 
'''

def standardDeviation(months_list, average_per_month, std_dev):
    for rows in range(len(months_list)):
        sum_of_variance = 0
        for columns in range(0, len(months_list[rows])):
            variance_of_months = months_list[rows][columns] - average_per_month[rows]
            sum_of_variance  = sum_of_variance + variance_of_months**2
        try:
            std_dev[rows] = round((sum_of_variance/len(months_list[rows]))**0.5,4)
        except ZeroDivisionError:
            std_dev[rows] = 0
    return std_dev 
    
'''
    months_list_values() returns a 2d list with all the recorded covid cases for a particular country, in order from Jan to Dec. 
'''
def months_list_values(country, location, month, new_cases):
    months_list = [[],[],[],[],[],[],[],[],[],[],[],[]]
    length = len(location)
    for index in range(length):
        if country == location[index]:
            months_list[month[index]-1].append(new_cases[index])
    return months_list

'''
    The store_values_by_month() function returns a list of 0's with each element representing a month. 
'''
def store_values_by_month():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#-------- STASTICS ---------#

'''
    The process_data_per_month() function finds the stastistical analysis of a single country
'''
def process_data_per_month(country, location, month, new_cases):
    country = country.lower().strip()
    months_lists = months_list_values(country, location, month, new_cases)
    min_value = minimum(months_lists, store_values_by_month())
    max_value = maximum(months_lists, store_values_by_month())
    avg = average(months_lists, store_values_by_month())
    std_dev = standardDeviation(months_lists, avg, store_values_by_month())
    return min_value, max_value, avg, std_dev

#-------- CORRELATION ---------#

#The correlation forumla is broken down into seperate functions. Each section of the forumla has its own help function in order to 
#break down the formula into simplier computation. 

'''
    The variance function calculates the distance between the individual sample points and the sample mean. 
'''
def variance(stats):
    sum = 0
    #sum up all the values in the list 
    for rows in range(len(stats)):
        sum = sum + stats[rows]
    #divide by the length of the list, which in this case is 12. 
    average_of_months = sum/len(stats)
    return [x - average_of_months for x in stats]

'''
    The multiply_variance_for_both_countries() function performs element wise list multiplication for country A with country B.
'''
def multiply_variance_for_both_countries(stats_A, stats_B):
    return [stats_A[i]*stats_B[i] for i in range(len(stats_A))]

'''
    The denimonator_square_root() function returns total the sqrt value in the correlation formula in the denonimator sectiom. 
'''

def denimonator_square_root(stats):
    total = 0
    for element in range(0, len(stats)):
        total = total + (stats[element])**2
    return total**0.5


'''
    multiply_denimonator(stats_A, stats_B) multiplies the denimonator values from the correlation formula 
'''
def multiply_denimonator(stats_A, stats_B):
    return stats_A*stats_B


'''
    The compute_correlation() function computes the correlation value of the two countries 
'''

def compute_correlation(stats_to_find, denominator_value):
    numerator_value = 0
    #sum up all the elements in the list 
    for element in range(0, len(stats_to_find)):
        numerator_value = numerator_value + stats_to_find[element]
    #finds the correlation value
    correlation_value = round((numerator_value/denominator_value),4)
    return correlation_value


'''
    The correlation_value_for_stats function returns the correlation value from the compute_correlation() function. 
    The following section of code computes the different components of the correlation formaula
'''

def correlation_value_for_stats(stats_value_one, stats_value_two):
    #finds the variance value for the two countries 
    variance_A = variance(stats_value_one)
    variance_B = variance(stats_value_two)
    #multiples the variance values by performing a element wise list multiplication
    variance_AB = multiply_variance_for_both_countries(variance_A, variance_B)
    #computes the denimontator value from the correlation formula 
    sqrt_den_for_A = denimonator_square_root(variance_A)
    sqrt_den_for_b = denimonator_square_root(variance_B)
    denominator_value = multiply_denimonator(sqrt_den_for_A, sqrt_den_for_b)
    #returns the correlation value of two countries 
    return compute_correlation(variance_AB, denominator_value)


'''
    The process_data_for_correlation() returns the  minimum, maximum, average and the standard deviation 
    correlation of the recorded postive cases between two countries.
'''

def process_data_for_correlation(country, location, month, new_cases):
    #country_A refers to the first country listed in the list
    country_A = country[0].lower().strip()
    #country_B refers to the second country listed in the list 
    country_B = country[-1].lower().strip()
    #Returns the min, max, avg, and std for both countries in the list. 
    min_value_A, max_value_A, avg_A, std_dev_A = process_data_per_month(country_A, location, month, new_cases)
    min_value_B, max_value_B, avg_B, std_dev_B = process_data_per_month(country_B, location, month, new_cases)
    #find stats: the correlation between the two countries for min, max, avg and std. 
    min_correlation = correlation_value_for_stats(min_value_A, min_value_B)
    max_correlation = correlation_value_for_stats(max_value_A, max_value_B)
    avg_correlation = correlation_value_for_stats(avg_A, avg_B)
    std_dev_correlation = correlation_value_for_stats(std_dev_A, std_dev_B)

    return min_correlation, max_correlation, avg_correlation, std_dev_correlation

rc5,rc6,rc7,rc8 = main('Covid-data-for-project_1_testing_2.csv',['china',"italy"], "correlation")
print(rc5,rc6,rc7,rc8)