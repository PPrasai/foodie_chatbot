from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core.events import Restarted
import zomatopy
import json
import regex as re

from mail_srv import MailServer
from response_builder import ResponseBuilder
from zomato_service import ZomatoService

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		
		zomatoService = ZomatoService()
		city_id = zomatoService.get_city_id(location)
		responseBuilder = ResponseBuilder()
		response = responseBuilder.build_response(city_id, budget, cuisine)
		
		return_slots = []

		if response == 'No results found':
			response = "Sorry, we could not find any matching restaurants."
			return_slots.append(SlotSet('restaurant_found', False))
			return_slots.append(SlotSet('search_result', response))
		else:
			return_slots.append(SlotSet('restaurant_found', True))
			return_slots.append(SlotSet('search_result', response))

		dispatcher.utter_message(response)
		return return_slots


'''
	Check if a given location is in our active 
	area of operation and set slot accordingly
'''
class ActionCheckAreaOfOperation(Action):

	def name(self):
		return 'action_check_ao'

	def run(self, dispatcher, tracker, domain):

		# TODO move to separate file
		list_of_supported_cities = [
			'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'agra', 'ajmer', 
			'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'ahmedabad', 'bareilly', 
			'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 
			'chandigarh', 'coimbatore', 'nagpur', 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 
			'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 
			'gurgaon', 'guwahati', 'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 
			'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi', 
			'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 
			'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 
			'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'prayagraj', 
			'puneraipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 
			'solapur', 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 
			'tirunelveli', 'tiruppur', 'tiruvannamalai', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 
			'vasai-virar city', 'vijayawada', 'visakhapatnam', 'vellore', 'warangal',
			"Bangalore", "Bengaluru", "bengaluru", "bangalore", "banglore", "Banglore",
			"Hyderabad", "Secunderabad", "Kacheguda", "Delhi", "New Delhi", "new delhi", "Dilli", "dilli",
			"Chennai", "madras", "Madras", "Kolkata", "Calcutta", "calcutta", "Mumbai", "Bombay", "bombay",
			"Ajmer", "Ajayameru", "ajayameru", "Amaravati", "Amritsar","ramdaspur","ambarsar",
			"belagavi","belgaon","venugrama", "Bokaro", "jharkhand", "Coimbatore", "Kovai", "Coyamuthur",
			"dehra dun", "amaravati", "Dharwad", "city of temples", "cannanore", "kolathunadu", "cawnpore",
			"cocanada", "cochin", "quilon", "kotah", "calicut", "kurnal", "mangaluru", "mysuru", "nasik",
			"palghat", "puducherry", "pondi", "allahabad", "poona", "rajamahendravaram", "ranch", "sholapore",
			"trivandrum", "trichur", "trichy", "nellai", "tinnevelly", "trinomali", "trinomalee", "arunachalam", 
			"vijaypura", "baroda", "banaras","kashi","kasi", "bejawada", "bezawada", "vishakhapatnam", "vizag", "waltair",
			"orugal"
		]

		user_location = tracker.get_slot('location')
		if user_location not in list_of_supported_cities:
			return [SlotSet('supported_location', False)]

		return [SlotSet('supported_location', True)]


'''
	Send email to an email address.
	Perform validation first
'''
class ActionSendMail(Action):

	def name(self):
		return 'action_send_mail'

	def validateEmail(self, email):
		pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
		if not re.match(pattern, email):
			return False
		
		return True

	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email_address')
		validEmail = self.validateEmail(email)
		SlotSet('valid_email_address', validEmail)

		message = tracker.get_slot('search_result')

		if validEmail:
			mailServer = MailServer()
			mailServer.send_mail(message, email)
			return [SlotSet('search_result', message + '\n*****SENT*****')]
		
		return [SlotSet('email_address', '')]
