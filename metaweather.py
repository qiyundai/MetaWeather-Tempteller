import requests

def select(result):
    for i in range(len(result)):
        r_title = result[i]['title']
        temp_id = result[i]['woeid']
        assume = requests.get(f'https://www.metaweather.com/api/location/{temp_id}')
        state = assume.json()['parent']['title']
        is_it = input(f'did you mean {r_title} in {state}?')
        if 'y' in is_it:
            return result[i]['woeid']

def confirmed_location(result2):
    cons_dict = result2.json()
    city = cons_dict['title']
    state = cons_dict['parent']['title']
    return f'{city} in {state}'

def find_temp(result2):
    cons_dict = result2.json()
    temptotal = 0
    for i in range(len(cons_dict['consolidated_weather'])):
        temptotal += cons_dict['consolidated_weather'][i]['the_temp']
    return temptotal/(len(cons_dict['consolidated_weather']))
            
location = input("Please type in the location of which temperature you'd like to know about: ")

loca = {'query': location}

r1 = requests.get("https://www.metaweather.com/api/location/search/", params=loca)

r_list = r1.json()

ID = select(r_list)
print(ID)
r2 = requests.get(f'https://www.metaweather.com/api/location/{ID}')

current_temp = find_temp(r2)

print(f'Found it for you, my dear. The current temperature at {confirmed_location(r2)} is C°{current_temp}.')