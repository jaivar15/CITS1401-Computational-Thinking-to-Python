def main(filename):
    continent, location, date, new_cases, new_deaths = extact_columns(filename)
    new_cases_2 = fix_columns_new_cases(new_cases)
    new_deaths_2 = fix_columns_new_deaths(new_deaths)
    
    unique_country_names = unique_set(location)
    country = store_into_dictonary(location, unique_country_names, date, new_cases_2, new_deaths_2)
    
    unique_coun_names = unique_set(continent)
    country_2 = store_into_dictonary_cont(continent, unique_coun_names, date, new_cases_2, new_deaths_2)
    return country, country_2




def read_csv_file(filename):
    try:
        file = open(filename, "r")
    except IOError:
        print("csv file not found")
    return file

def extract_headers(filename):
    open_file = read_csv_file(filename)
    for each_line in open_file:
        line = each_line.split(",")
        line[len(line) - 1] = line[len(line) - 1].replace('\n','')
        break
    continent_index = line.index("continent") if "continent" in line else exit("None")
    location_index = line.index("location") if "location" in line else exit("None")
    date_index = line.index("date") if "date" in line else exit("None")
    new_cases_index = line.index("new_cases") if "new_cases" in line else exit("None")
    new_deaths_index = line.index("new_deaths") if "new_deaths" in line else exit("None")

    return continent_index, location_index, date_index, new_cases_index, new_deaths_index

def extact_columns(filename):
    open_file = read_csv_file(filename)
    continent, location, date, new_cases, new_deaths = [], [], [], [], []
    continent_index, location_index, date_index, new_cases_index, new_deaths_index = extract_headers(filename)
    for each_line in open_file:
        line = each_line.split(",")
        line[len(line) - 1] = line[len(line) - 1].replace('\n','')
        continent.append(line[continent_index].lower().strip())
        location.append(line[location_index].lower().strip())
        date.append(line[date_index])
        new_cases.append(line[new_cases_index])
        new_deaths.append(line[new_deaths_index])
    
    del continent[0]
    del location[0]
    del date[0]
    del new_cases[0]
    del new_deaths[0]
    return continent, location, date, new_cases, new_deaths


def unique_set(location):
    set_of_countries = set(location)
    unique_name = list(set_of_countries)
    return unique_name

def fix_columns_new_cases(new_cases):
    for each_row in range(len(new_cases)):
        if len(new_cases[each_row]) == 0 or new_cases[each_row] == "zero":
            new_cases[each_row] = 0
    return new_cases

def fix_columns_new_deaths(new_deaths):
    for each_row in range(len(new_deaths)):
        if len(new_deaths[each_row]) == 0 or new_deaths[each_row] == "zero":
            new_deaths[each_row] = 0
    return new_deaths

def compute(cases, average):
    division=[]
    for index in range(12):
        try:
            division.append(cases[index]/average[index])
        except ZeroDivisionError:
            division.append(0)
    return division

def compute_for_continents(cases):
    division = []
    number_of_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    for index in range(12):
        try:
            division.append(cases[index]/number_of_days[index])
        except ZeroDivisionError:
            division.append(0)
    return division
    

def store_into_dictonary(location, unique_country_names, date, new_cases, new_deaths):
    results = {}
    for each_country in unique_country_names:
        new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly = compute_lists(each_country, location, date, new_cases, new_deaths)
        results[each_country] = [new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly]
    return results

def store_into_dictonary_cont(location, unique_country_names, date, new_cases, new_deaths):
    results = {}
    for each_country in unique_country_names:
        new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly = compute_lists_cont(each_country, location, date, new_cases, new_deaths)
        results[each_country] = [new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly]
    return results

#def store_into_continents_dictonary(location, unique_country_names, date, new_cases, new_deaths):
 #   results = {}
  #  for each_country in unique_country_names:
   #     new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly = compute_for_continents(each_country, location, date, new_cases, new_deaths)
    #    results[each_country] = [new_cases_per_month, new_deaths_per_month, avg_new_cases_montly, avg_new_deaths_monthly]
    #print(new_deaths_per_month)
    #return results


def compute_lists(each_country, location, date, new_cases, new_deaths):
    new_cases_per_month, new_death_per_month, average_per_month = confirmed_deaths_cases_per_month(each_country, location, date, new_cases, new_deaths)
    new_cases_average_for_each_month=compute(new_cases_per_month, average_per_month)
    new_deaths_average_for_each_month=compute(new_death_per_month, average_per_month)
    average__new_cases_per_month, average__death_cases_per_month = confirmed_deaths_average(each_country, date, location, new_cases, new_deaths, new_cases_average_for_each_month, new_deaths_average_for_each_month)
    return new_cases_per_month, new_death_per_month, average__new_cases_per_month, average__death_cases_per_month



def compute_lists_cont(each_country, location, date, new_cases, new_deaths):
    new_cases_per_month, new_death_per_month, average_per_month = confirmed_deaths_cases_per_month(each_country, location, date, new_cases, new_deaths)
    new_cases_average_for_each_month=compute_for_continents(new_cases_per_month)
    new_deaths_average_for_each_month=compute_for_continents(new_death_per_month)
    average__new_cases_per_month, average__death_cases_per_month = confirmed_deaths_average(each_country, date, location, new_cases, new_deaths, new_cases_average_for_each_month, new_deaths_average_for_each_month)
    return new_cases_per_month, new_death_per_month, average__new_cases_per_month, average__death_cases_per_month








#     unique_countries_names = unique_set(location)
#     store_into_dictonary(unique_country_names)
#     confirmed_deaths_cases_per_month()
#     return unique_countries

def confirmed_deaths_cases_per_month(country_name, location, date, new_cases, new_deaths):
    new_cases_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    new_death_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    average_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    for each_row in range(len(location)):
        split_date = date[each_row].split('/')
        if location[each_row] == country_name:
            if len(split_date[1]) == 1 or len(split_date[1]) ==2:
                day = int(split_date[1])
                if int(new_cases[each_row])>=0:
                    new_cases_per_month[day-1] = new_cases_per_month[day-1] + int(new_cases[each_row])
                if int(new_deaths[each_row])>=0:
                    new_death_per_month[day-1] = new_death_per_month[day-1] + int(new_deaths[each_row])
                average_per_month[day-1] = average_per_month[day-1] + 1
            else:
                pass
    
    return new_cases_per_month, new_death_per_month, average_per_month

def confirmed_deaths_average(country_name, date, location, new_cases, new_deaths, new_cases_average_for_each_month, new_deaths_average_for_each_month):
    average__new_cases_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    average__death_cases_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    for each_row in range(len(location)):
        split_date = date[each_row].split('/')
        if location[each_row] == country_name:
            if len(split_date[1]) == 1 or len(split_date[1]) == 2:
                day = int(split_date[1])
                if int(new_cases[each_row]) > new_cases_average_for_each_month[day-1]:
                    average__new_cases_per_month[day-1]=average__new_cases_per_month[day-1]+1
                if int(new_deaths[each_row]) > new_deaths_average_for_each_month[day-1]:
                    average__death_cases_per_month[day-1]=average__death_cases_per_month[day-1]+1
    return average__new_cases_per_month, average__death_cases_per_month




