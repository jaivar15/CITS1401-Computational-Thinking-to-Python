'''
    CITS1401 Computational Thinking with Python: Project 2
    Student Name: Varun Jain 
    Student Number: 21963986
    Due Date: Friday 21st May
'''


def main(filename):
    
    #returns the relevant columns from the csv file
    continent, location, date, new_cases, new_deaths = extact_columns(filename)

    #replaces incorrect or missing values with 0
    new_cases_fixed, new_deaths_fixed = replace_column_with_zero(new_cases, new_deaths)
    
    #returns the unique values from the countries list
    unique_country_names = unique_set(location)
    
    #returns a dictionary of all the countries as keys, and a list of values. 
    dict_country = store_each_country_into_dictionary(location, unique_country_names, date, new_cases_fixed, new_deaths_fixed)
    
    #returns a list of unique values from the continent list 
    unique_names_for_continent = unique_set(continent)
    
    #returns a dictionary of all the continents as keys, and a list of values. 
    dict_continent = store_each_continent_into_dictonary(continent, unique_names_for_continent, date, new_cases_fixed, new_deaths_fixed)


    return dict_country, dict_continent

'''
    Read the CSV file
'''

def read_csv_file(filename):
    try:
        file = open(filename, "r")
    except IOError:
        print("csv file not found")
    return file

'''
    Extracts the first row (header row) from the csv file, and returns the index for each of the relevant attribute
'''

def extract_headers(filename):
    open_file = read_csv_file(filename)
    #reads in the first line of the csv file
    for each_line in open_file:
        line = each_line.split(",")
        line[len(line) - 1] = line[len(line) - 1].replace('\n','')
        break
    #extracts the index value  for the following attributes: continent, location, date, new_cases, new_deaths
    continent_index = line.index("continent") if "continent" in line else exit("None")
    location_index = line.index("location") if "location" in line else exit("None")
    date_index = line.index("date") if "date" in line else exit("None")
    new_cases_index = line.index("new_cases") if "new_cases" in line else exit("None")
    new_deaths_index = line.index("new_deaths") if "new_deaths" in line else exit("None")

    return continent_index, location_index, date_index, new_cases_index, new_deaths_index


'''
    Extracts data from the covid file and seperates each column, and appends it to a individual list
    The relevent columns are found through extract_headers() which is passed through with theif index values. 
    Stores each attribute values into a seperate list. The columns that have been extracted from the csv file is: continent, location, date,new cases, and new deaths
'''   

def extact_columns(filename):
    open_file = read_csv_file(filename)
    continent, location, date, new_cases, new_deaths = [], [], [], [], []
    continent_index, location_index, date_index, new_cases_index, new_deaths_index = extract_headers(filename)
    for each_line in open_file:
        line = each_line.split(",")
        line[len(line) - 1] = line[len(line) - 1].replace('\n','')
        #extracts the relevant columns from a specifc index
        continent.append(line[continent_index].lower().strip())
        location.append(line[location_index].lower().strip())
        date.append(line[date_index])
        new_cases.append(line[new_cases_index])
        new_deaths.append(line[new_deaths_index])

    #exit the program if the csv only contains the headers 
    if len(continent) == 0 or len(continent) == 1:
        exit()
        
    #removes the header row for each attribute 
    del continent[0]
    del location[0]
    del date[0]
    del new_cases[0]
    del new_deaths[0]
    
    return continent, location, date, new_cases, new_deaths


'''
    Returns a list of unique values. 
'''

def unique_set(location):
    set_of_countries = set(location)
    unique_name = list(set_of_countries)
    return unique_name

'''
    Replaces any missing values or any incorrect values with 0
'''

def replace_column_with_zero(new_cases, new_deaths):
    for each_row in range(len(new_cases)):
        if len(new_cases[each_row]) == 0 or new_cases[each_row] == "zero":
            new_cases[each_row] = 0
        if len(new_deaths[each_row]) == 0 or new_deaths[each_row] == "zero":
            new_deaths[each_row] = 0
    return new_cases, new_deaths

'''
    List-wise division between the total cases recorded per month and the number of days recored in a month
'''

def compute(cases, average):
    division=[]
    for index in range(12):
        try:
            division.append(cases[index]/average[index])
        except ZeroDivisionError:
            division.append(0)
    return division


'''
    Returns True if the month value is between 1 and 12
'''

def check_day(day):
    for i in range(1,13):
        if day == i:
            return True
    return False
    
'''
    Returns a dictionary with key:value pairs. The key pair stores the country name, followed by four lists:
        1. total cases per month,
        2. total deaths per month,
        3. average cases per month,
        4. average deaths per monht
'''

def store_each_country_into_dictionary(location, unique_country_names, date, new_cases, new_deaths):
    results = {}
    for each_country in unique_country_names:
        #computing the four lists for each country and store the output into a dictionary called result
        new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly = computation_for_each_country(each_country, location, date, new_cases, new_deaths)
        results[each_country] = [new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly]
    return results

'''
    Similar to store_each_country_into_dictionary() but instead computes the value for continents. 
'''

def store_each_continent_into_dictonary(location, unique_country_names, date, new_cases, new_deaths):
    results = {}
    for each_country in unique_country_names:
        new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly = computation_for_each_continent(each_country, location, date, new_cases, new_deaths)
        results[each_country] = [new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly]
    return results 


'''
    Returns a list for the four measures: the total sum for each month, the total deaths for each month, the number of days where the case is greater than the average case and the
    number of days where the death case is greater than average case value. 
    
'''


def computation_for_each_country(each_country, location, date, new_cases, new_deaths):
    #returns a three lists: list of sum for confirmed and death cases per month, and list of the total number of days recored for eah month
    new_cases_per_month, new_death_per_month, total_number_of_days = confirmed_deaths_cases_per_month(each_country, location, date, new_cases, new_deaths)
    #list wise division between the total cases and the number of days
    new_cases_average_for_each_month=compute(new_cases_per_month, total_number_of_days)
    new_deaths_average_for_each_month=compute(new_death_per_month, total_number_of_days)
    #returns the number of days where the average is lower then the case value for both confirmed and deaths
    average__new_cases_per_month, average__death_cases_per_month = confirmed_deaths_average(each_country, date, location, new_cases, new_deaths, new_cases_average_for_each_month, new_deaths_average_for_each_month)
    return new_cases_per_month, new_death_per_month, average__new_cases_per_month, average__death_cases_per_month

'''
    Similar to computation_for_each_country() but instead returns values for each continent passed through the computation_for_each_continent() function
'''


def computation_for_each_continent(each_country, location, date, new_cases, new_deaths):
    #for continent, the number of days are set to default values
    number_of_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    new_cases_per_month, new_death_per_month, total_number_of_days_per_month = confirmed_deaths_cases_per_month(each_country, location, date, new_cases, new_deaths)
    new_cases_average_for_each_month=compute(new_cases_per_month, number_of_days)
    new_deaths_average_for_each_month=compute(new_death_per_month, number_of_days)
    average__new_cases_per_month, average__death_cases_per_month = confirmed_deaths_average(each_country, date, location, new_cases, new_deaths, new_cases_average_for_each_month, new_deaths_average_for_each_month)
    return new_cases_per_month, new_death_per_month, average__new_cases_per_month, average__death_cases_per_month


'''
    Returns a list of sum of the covid cases for each month, Jan to Dec
    Returns a list of sum of the death cases for each month, Jan to Dec
    Returns the total number of days recorded for each month, Jan to Dec
'''


def confirmed_deaths_cases_per_month(country_name, location, date, new_cases, new_deaths):
    
    new_cases_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    new_death_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    total_number_of_days_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    
    for each_row in range(len(location)):
        #splits the date into an array of substrings
        split_date = date[each_row].split('/')
        if location[each_row] == country_name:
            #checks if the month is between 1 and 12 and the length of the date list is three
            if len(split_date) == 3 and check_day(int(split_date[1])) == True:
                day = int(split_date[1])
                #records the total new and death cases for each month, only records positive cases
                if int(new_cases[each_row])>=0:
                    new_cases_per_month[day-1] = new_cases_per_month[day-1] + int(new_cases[each_row])
                if int(new_deaths[each_row])>=0:
                    new_death_per_month[day-1] = new_death_per_month[day-1] + int(new_deaths[each_row])
                #returns the total number of day for each month
                total_number_of_days_per_month[day-1] = total_number_of_days_per_month[day-1] + 1
            else:
                pass
    
    return new_cases_per_month, new_death_per_month, total_number_of_days_per_month

'''
    Returns a list of the total number of days for each month where the case recorded for a specific day is greater than the avergae for that particular month
    Returns a list of the total number of days for each month where the deaths recorded for a specific day is greater than avergae for that particular month
'''

def confirmed_deaths_average(country_name, date, location, new_cases, new_deaths, new_cases_average_for_each_month, new_deaths_average_for_each_month):
    
    average__new_cases_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    average__death_cases_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    
    for each_row in range(len(location)):
        split_date = date[each_row].split('/')
        #checks the country name
        if location[each_row] == country_name:
            if len(split_date) == 3 and check_day(int(split_date[1])) == True:
                day = int(split_date[1])
                #checks if covid case for a particular day is larger than the average case
                if int(new_cases[each_row]) > new_cases_average_for_each_month[day-1]:
                    average__new_cases_per_month[day-1]=average__new_cases_per_month[day-1]+1
                #checks if covid death case for a particular day is larger than the average case 
                if int(new_deaths[each_row]) > new_deaths_average_for_each_month[day-1]:
                    average__death_cases_per_month[day-1]=average__death_cases_per_month[day-1]+1
    return average__new_cases_per_month, average__death_cases_per_month




