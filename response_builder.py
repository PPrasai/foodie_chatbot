from zomato_service import ZomatoService

class ResponseBuilder():
    
    response_dict_list = []
    formatted_dict = []
    zomatoService = None

    def __init__(self, *args, **kwargs):
        self.zomatoService = ZomatoService()

    def get_response_dict_list(self, limit, offset, city_id, cuisine):
        return self.zomatoService.get_restaurants_in_city_with_cuisine(city_id, cuisine, limit, offset)

    def build_formatted_dict(self, city_id, budget, cuisine, limit = 20, offset = 0):
        self.response_dict_list = self.get_response_dict_list(limit, offset, city_id, cuisine)

        multiplier = 1
        for response in self.response_dict_list:
            if response['currency'] == 'Rs.':
                multiplier = 1
            if response['currency'] == '$':
                multiplier = 69

            avg_cost = response['avg_cost_for_two'] * multiplier

            if budget == 'under 300':
                if avg_cost <= 300:
                    self.formatted_dict.append(response)
                
            if budget == 'over 700':
                if avg_cost >= 700:
                    self.formatted_dict.append(response)
            
            if budget == '300 to 700':
                if avg_cost > 300 and avg_cost < 700:
                    self.formatted_dict.append(response)

            if len(self.formatted_dict) >= 10:
                return self.formatted_dict
        
        # if the program breaks out of the loop without returning
        # it means we don't have 10 search results yet. we will 
        # have to request next page of the search result
        
        if len(self.response_dict_list) != 0 and int(self.response_dict_list[-1]['cursor']) + 20 < int(self.response_dict_list[-1]['total_results']):
            offset = self.response_dict_list[-1]['cursor']
            print('offset ', offset)
            self.build_formatted_dict(city_id, budget, cuisine, limit, offset)

    def build_response(self, city_id, budget, cuisine):
        cuisines_in_city = self.zomatoService.get_cuisines_in_city(city_id)

        try:
            cuisine = cuisine.capitalize()
            
            if len(cuisine.split()) > 1:
                cuisine = ' '.join([cuisine.split()[0].capitalize(), cuisine.split()[1].capitalize()])
                
            cuisine_id = [v[0] for i, v in enumerate(cuisines_in_city) if v[1] == cuisine][0]
            self.build_formatted_dict(city_id, budget, cuisine_id)

            response = 'Here are the results of you search: \n\n'
            counter = 0

            for one_dict in self.formatted_dict:
                counter += 1
                one_response = str(counter) + '. ' + one_dict['name'] + '\n' + one_dict['location']
                one_response = one_response + '\nHas ' + one_dict['rating_text'] + ' rating of ' + str(one_dict['rating_score'])
                one_response = one_response + '\nWith an average bill amount of ' + one_dict['currency'] + ' ' + str(one_dict['avg_cost_for_two']) + '\n\n'

                response = response + one_response
        except IndexError:
            response = 'No results found'

        return response