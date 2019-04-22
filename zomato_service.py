import zomatopy
import json

class ZomatoService():
    zomato = None
    config = {
        'user_key':'6ce88a5ec1419e335afa1c7f92f4b739'
    }
    result_start = 0
    result_shown = 0
    result_found = 0

    def __init__(self, *args, **kwargs):
        self.zomato = zomatopy.initialize_app(self.config)

    def get_city_id(self, city_name):
        city_name = '%20'.join(city_name.split(' '))
        city_detail = self.zomato.search_city_by_name(city_name)
        city_detail = json.loads(city_detail)

        for city in city_detail['location_suggestions']:
            if city['country_id'] == 1:
                return city['id']

    def get_cuisines_in_city(self, city_id):
        list_of_cuisines = self.zomato.search_cuisines_in_city(city_id)
        list_of_cuisines = json.loads(list_of_cuisines)
        formatted_list = []
        for cuisine in list_of_cuisines['cuisines']:
            formatted_list.append((cuisine['cuisine']['cuisine_id'], cuisine['cuisine']['cuisine_name']))
        
        return formatted_list

    def get_restaurants_in_city_with_cuisine(self, city_id, cuisine, limit = None, offset = None):
        list_of_restaurants = self.zomato.search_restaurant_in_city_with_cuisine(city_id, cuisine, limit, offset)
        list_of_restaurants = json.loads(list_of_restaurants)

        formatted_list = []

        self.result_start = list_of_restaurants['results_start']
        self.result_shown = list_of_restaurants['results_shown']
        self.result_found = list_of_restaurants['results_found']

        for restaurant in list_of_restaurants['restaurants']:
            formatted_list.append(
                {
                    'id': restaurant['restaurant']['id'],
                    'name': restaurant['restaurant']['name'],
                    'location': restaurant['restaurant']['location']['address'],
                    'cuisines': restaurant['restaurant']['cuisines'].split(', '),
                    'avg_cost_for_two': restaurant['restaurant']['average_cost_for_two'],
                    'currency': restaurant['restaurant']['currency'],
                    'rating_score': restaurant['restaurant']['user_rating'] ['aggregate_rating'],
                    'rating_text': restaurant['restaurant']['user_rating']['rating_text'],
                    'result_start': self.result_start,
                    'cursor': (int(self.result_start) + int(self.result_shown)),
                    'total_results': self.result_found
                }
            )
        
        return formatted_list

        

