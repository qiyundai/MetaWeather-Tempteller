import requests

def select(result):
    for i in range(len(result)):
        r_title = result[i]['title']
        is_it = input(f'did you mean {r_title}?')
        if 'y' in is_it:
            return result[i]['woeid']
def confirmed_location(result2):
    cons_dict = result2.json()
    return cons_dict['title']

def find_temp(result2):
    cons_dict = result2.json()
    return cons_dict['consolidated_weather'][0]['the_temp']
            
location = input("Please type in the location of which temperature you'd like to know about: ")

loca = {'query': location}

r1 = requests.get("https://www.metaweather.com/api/location/search/", params=loca)

r_list = r1.json()

ID = select(r_list)

r2 = requests.get(f'https://www.metaweather.com/api/location/{ID}')

current_temp = find_temp(r2)

print(f'Found it for you, my dear. The current temperature at {confirmed_location(r2)} is F°{current_temp}.')