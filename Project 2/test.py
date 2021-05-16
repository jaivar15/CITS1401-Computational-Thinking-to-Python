def compute(cases, average):
    division=[]
    for index in range(12):
        try:
            division.append(cases[index]/average[index])
        except ZeroDivisionError:
            division.append(0)
    return division
        
        
   
def compare_date(month):
    for index in range(12):
        if month == index:
            return True




def countries(country_name):
    iso_code, continent, location, date, new_cases, new_deaths = [], [], [], [], [], []
    filename="coviddata.csv"
    #open_file=open(filename, "r", encoding='utf-8-sig')
    open_file=open(filename, "r")
    headers=['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'new_cases_smoothed', 'c', 'new_deaths', 'new_deaths_smoothed', 'total_cases_per_million', 'new_cases_per_million', 'new_cases_smoothed_per_million', 'total_deaths_per_million', 'new_deaths_per_million', 'new_deaths_smoothed_per_million', 'reproduction_rate', 'icu_patients', 'icu_patients_per_million', 'hosp_patients', 'hosp_patients_per_million', 'weekly_icu_admissions', 'weekly_icu_admissions_per_million', 'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million', 'new_tests', 'total_tests', 'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'positive_rate', 'tests_per_case', 'tests_units', 'total_vaccinations', 'new_vaccinations', 'total_vaccinations_per_hundred', 'new_vaccinations_per_million', 'stringency_index', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy', 'human_development_index']


    for each_line in open_file:
        print(len(each_line))
        line = each_line.split(",")
        line[len(line) - 1] = line[len(line) - 1].replace('\n','')
        break
    continent_index = line.index("continent") if "continent" in line else exit("None")
    location_index = line.index("location") if "location" in line else exit("None")
    date_index = line.index("date") if "date" in line else exit("None")
    new_cases_index = line.index("new_cases") if "new_cases" in line else exit("None")
    new_deaths_index = line.index("new_cases") if "new_cases" in line else exit("None")


    # for each in range(len(headers)):
    #     if headers[each] in line:
    #         # find the index of that header in the file
    #     else:
    #         #exit the program saying the neccesary column is not provided

    for each_line in open_file:
        line = each_line.split(",")
        line[len(line) - 1] = line[len(line) - 1].replace('\n','')
        #appends each column into a seperate list 
        iso_code.append(line[0].lower().strip())
        continent.append(line[continent_index].lower().strip())
        location.append(line[location_index].lower().strip())
        date.append(line[date_index])
        new_cases.append(line[new_cases_index])
        new_deaths.append(line[8])

    
    del iso_code[0]
    del continent[0]
    del location[0]
    del date[0]
    del new_cases[0]
    del new_deaths[0]
            
    new_cases_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    new_death_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    average_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    average__new_cases_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]
    average__death_cases_per_month=[0,0,0,0,0,0,0,0,0,0,0,0]

    for each_row in range(len(new_cases)):
        if len(new_cases[each_row]) == 0 or new_cases[each_row] == "zero":
            new_cases[each_row] = 0
        if len(new_deaths[each_row]) == 0:
            new_deaths[each_row] = 0
    count=0


    for each_row in range(len(continent)):
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
    
    
    new_cases_average_for_each_month=compute(new_cases_per_month, average_per_month)
    new_deaths_average_for_each_month=compute(new_death_per_month, average_per_month)
    
    
    for each_row in range(len(continent)):
        split_date = date[each_row].split('/')
        if location[each_row] == country_name:
            if len(split_date[1]) == 1 or len(split_date[1]) == 2:
                day = int(split_date[1])
                if int(new_cases[each_row]) > new_cases_average_for_each_month[day-1]:
                    average__new_cases_per_month[day-1]=average__new_cases_per_month[day-1]+1
                if int(new_deaths[each_row]) > new_deaths_average_for_each_month[day-1]:
                    average__death_cases_per_month[day-1]=average__death_cases_per_month[day-1]+1
    
    
   # print(new_cases_per_month)
   # print(new_death_per_month)
   # print(average__new_cases_per_month)
   # print(average__death_cases_per_month)
    
    set_of_countries = set(location)
    unique_country_names= list(set_of_countries)
   # print(unique_country_names)
    
    return unique_country_names, new_cases_per_month, new_death_per_month, average__new_cases_per_month, average__death_cases_per_month
    
    
def main():
    results={}
    
    unique_country_names, new_cases_per_month, new_death_per_month, average__new_cases_per_month, average__death_cases_per_month = countries("italy")

    # for each in unique_country_names:
    #     country, new_cases_month, new_death_month, avg_new_month, avf_death_month = countries(each)
    #     results[each] = [new_cases_month, new_death_month, avg_new_month, avf_death_month]
    # print(results['afghanistan'])
main()
    
    
    
    
    
    
    
            

