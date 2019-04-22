## Generic story
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_ao
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "under 300"}
    - slot{"budget": "under 300"}
    - action_restaurant
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_entry{"email_address": "test@email.com"}
    - slot{"email_address": "test@email.com"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart

## Generic story
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_ao
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - action_restaurant
    - utter_ask_email_send
* affirm{"email_address": "some@email.com"}
    - slot{"email_address": "some@email.com"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart

## Invalid email story
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi", "cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "under 300"}
    - slot{"budget": "under 300"}
    - action_restaurant
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_entry{"email_address": "goodness@gracious.org"}
    - slot{"email_address": "goodness@gracious.org"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart

## Alteranate previous one
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi", "cuisine": "Chinese"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "under 300"}
    - slot{"budget": "under 300"}
    - action_restaurant
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_restart

## Alteranate previous one
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi", "cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "under 300"}
    - slot{"budget": "under 300"}
    - action_restaurant
    - utter_ask_email_send
* email_entry{"email_address": "goodness@gracious.tech"}
    - slot{"email_address": "goodness@gracious.tech"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart

## location and cuisine available in first message
* restaurant_search{"location": "siliguri", "cuisine": "American"}
    - slot{"location": "pune"}
    - action_check_ao
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - action_restaurant
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_entry{"email_address": "test12@testing.com"}
    - slot{"email_address": "test12@testing.com"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart

## everything available in first message
* restaurant_search{"location": "bangalore", "cuisine": "north indian", "budget": "300 to 700"}
    - slot{"location": "bangalore"}
    - action_check_ao
    - slot{"cuisine": "North Indian"}
    - slot{"budget": "300 to 700"}
    - action_restaurant
    - utter_ask_email_send
* email_entry{"email_address": "letters.prasai@iiitb.edu"}
    - slot{"email_address": "letters.prasai@iiitb.edu"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart

## previous one with unsupported address
* restaurant_search{"location": "birtamod", "cuisine": "north indian", "budget": "300 to 700"}
    - slot{"location": "birtamod"}
    - action_check_ao
    - utter_unsupported_city
    - utter_goodbye
    - action_restart
    
## Unsupported city story
* greet
    - utter_greet
* restaurant_search{"location": "kathmandu"}
    - slot{"location": "kathmandu"}
    - action_check_ao
    - utter_unsupported_city
    - utter_goodbye

## Another unsupported city story
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "new mexico"}
    - slot{"location": "new mexico"}
    - action_check_ao
    - utter_unsupported_city
    - utter_goodbye
    - action_restart
    
## Generated Story 7089028123113851322
* greet
    - utter_greet
* restaurant_search{"budget": "over 700", "location": "kathmandu"}
    - slot{"budget": "over 700"}
    - slot{"location": "kathmandu"}
    - action_check_ao
    - slot{"supported_location": false}
    - utter_unsupported_city
    - utter_goodbye
    - action_restart
* restaurant_search{"budget": "over 700", "cuisine": "Mexican", "location": "delhi"}
    - slot{"budget": "over 700"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_entry{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart
* email_entry
    - export

## Generated Story -6631315458868422774
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_entry{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart
    - export

## Generated Story -2266702393660045134
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_send
* restaurant_search{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart
    - export

## Generated Story 5034154689202717136
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "pune"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "pune"}
    - action_check_ao
    - slot{"supported_location": false}
    - utter_unsupported_city
    - utter_goodbye
    - action_restart
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "mumbai"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Found Tamasha in Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai\nFound Garage Inc. Public House in 15, Walton Road, Colaba, Behind Bata Showroom, Causeway, Colaba, Mumbai\nFound Hitchki in 002, First International Financial Centre, G Block, Bandra Kurla Complex, Mumbai\nFound Hitchki in 5, Transocean, Hiranandani Business Park, Lake Boulevard Road, Powai, Mumbai\nFound The Fusion Kitchen in Plot D9, Road 21, Andheri East, Near Passport Office, Adjoining Maruti Fortpoint, Shree Krishna Nagar, Marol MIDC Industry Estate, Marol, Mumbai\n"}
    - utter_ask_email_send
* restaurant_search{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Found Tamasha in Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai\nFound Garage Inc. Public House in 15, Walton Road, Colaba, Behind Bata Showroom, Causeway, Colaba, Mumbai\nFound Hitchki in 002, First International Financial Centre, G Block, Bandra Kurla Complex, Mumbai\nFound Hitchki in 5, Transocean, Hiranandani Business Park, Lake Boulevard Road, Powai, Mumbai\nFound The Fusion Kitchen in Plot D9, Road 21, Andheri East, Near Passport Office, Adjoining Maruti Fortpoint, Shree Krishna Nagar, Marol MIDC Industry Estate, Marol, Mumbai\n\n"}
    - utter_goodbye
    - action_restart
    - export

## Generated Story -2079272652438967907
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "bangalore"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "bangalore"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Found Biergarten in 4th B Cross, Koramangala 5th Block, Bangalore\nFound ShakesBierre in Level 5, Eva Mall, Brigade Road, Bangalore\nFound Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore\nFound Byg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore\nFound TBC Sky Lounge in Astra Hotel, 2795, 27th Main, Sector 1, HSR, Bangalore\n"}
    - utter_ask_email_send
* goodbye
    - utter_goodbye
    - action_restart
    - export

## Generated Story -2611243859319303677
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "siliguri"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "siliguri"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "under 300"}
    - slot{"budget": "under 300"}
    - action_restaurant
    - slot{"restaurant_found": false}
    - slot{"search_result": "Sorry, we could not find any matching restaurants."}
    - utter_goodbye
    - action_restart
    - export

## Generated Story -721545024421033135
* greet
    - utter_greet
* restaurant_search{"budget": "over 700", "cuisine": "mexican", "location": "delhi"}
    - slot{"budget": "over 700"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - action_restaurant
    - slot{"restaurant_found": false}
    - slot{"search_result": "Sorry, we could not find any matching restaurants."}
    - utter_goodbye
    - action_restart
    - export

## Generated Story -1316443391714682756
* greet
    - utter_greet
* restaurant_search{"budget": "over 700", "cuisine": "Mexican", "location": "delhi"}
    - slot{"budget": "over 700"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - action_restaurant
    - slot{"restaurant_found": false}
    - slot{"search_result": "Sorry, we could not find any matching restaurants."}
    - utter_goodbye
    - action_restart
    - export

## Generated Story 5056452580040666992
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - slot{"restaurant_found": false}
    - slot{"search_result": "Sorry, we could not find any matching restaurants."}
    - utter_goodbye
    - action_restart
    - export

## Generated Story -4536812181986451373
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "siliguri"}
    - slot{"location": "siliguri"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Sagar\nWard 8, MG Road, Near Gandhi Maidan, Khalpara, Siliguri\nHas Good rating of 3.9\nWith an average bill amount of Rs. 600\n\n2. Guru Sweets & Snacks\nOppostie Vishal Cinema, Sevoke Road, Dasrath Pally, Bhanu Nagar, Bankim Nagar, Siliguri\nHas Good rating of 3.7\nWith an average bill amount of Rs. 400\n\n3. Amardeep Restaurant\nSevoke Road, Janta Nagar, Siliguri\nHas Good rating of 3.5\nWith an average bill amount of Rs. 600\n\n4. Sri Mahabir Bhojanalya\nSevak Mor, Hill Cart Road, Khalpara, Siliguri\nHas Average rating of 3.4\nWith an average bill amount of Rs. 500\n\n5. Chennai.com\nM.R Road Khalpara\nHas Average rating of 3.3\nWith an average bill amount of Rs. 600\n\n6. Desi Galli Restaurant\nGhosh mansion, Seth Sri lal Market, Siliguri -734001\nHas Average rating of 3.2\nWith an average bill amount of Rs. 450\n\n7. Feast - The Food Court\ngj, Patiram Jote, Siliguri\nHas Average rating of 3.2\nWith an average bill amount of Rs. 600\n\n8. Kalpana Hotel\nNJP Main Road, opposite Railway Station, Nayapara, Siliguri\nHas Average rating of 2.9\nWith an average bill amount of Rs. 350\n\n"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* restaurant_search{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. Sagar\nWard 8, MG Road, Near Gandhi Maidan, Khalpara, Siliguri\nHas Good rating of 3.9\nWith an average bill amount of Rs. 600\n\n2. Guru Sweets & Snacks\nOppostie Vishal Cinema, Sevoke Road, Dasrath Pally, Bhanu Nagar, Bankim Nagar, Siliguri\nHas Good rating of 3.7\nWith an average bill amount of Rs. 400\n\n3. Amardeep Restaurant\nSevoke Road, Janta Nagar, Siliguri\nHas Good rating of 3.5\nWith an average bill amount of Rs. 600\n\n4. Sri Mahabir Bhojanalya\nSevak Mor, Hill Cart Road, Khalpara, Siliguri\nHas Average rating of 3.4\nWith an average bill amount of Rs. 500\n\n5. Chennai.com\nM.R Road Khalpara\nHas Average rating of 3.3\nWith an average bill amount of Rs. 600\n\n6. Desi Galli Restaurant\nGhosh mansion, Seth Sri lal Market, Siliguri -734001\nHas Average rating of 3.2\nWith an average bill amount of Rs. 450\n\n7. Feast - The Food Court\ngj, Patiram Jote, Siliguri\nHas Average rating of 3.2\nWith an average bill amount of Rs. 600\n\n8. Kalpana Hotel\nNJP Main Road, opposite Railway Station, Nayapara, Siliguri\nHas Average rating of 2.9\nWith an average bill amount of Rs. 350\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart
    - export

## Generated Story 4127872811390370226
* greet
    - utter_greet
* restaurant_search{"budget": "over 700", "cuisine": "mexican", "location": "delhi"}
    - slot{"budget": "over 700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n2. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n3. Chili's Grill & Bar\n3rd Floor, Ambience Mall, Nelson Madela Road, Vasant Kunj, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1500\n\n4. Fourty Four\nA 15/18, Sector 44, Noida\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 700\n\n5. Chili's Grill & Bar\n3rd Floor, DLF Mall Of India, Sector 18, Noida\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n6. Cafe Wink\nG-1, Sikka Galaxy, Plot 9, Shreshtha Vihar, Anand Vihar, New Delhi\nHas Vynikaj\u00face rating of 4.7\nWith an average bill amount of Rs. 700\n\n7. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1600\n\n8. Ministry Of Beer\nM 44, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n9. Chili's Grill & Bar\n3rd Floor, Ambience Mall, DLF Phase 3, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1800\n\n10. Dramebaaz\n2624, First & Second Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1450\n\n"}
    - utter_ask_email_send
* restaurant_search{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n2. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n3. Chili's Grill & Bar\n3rd Floor, Ambience Mall, Nelson Madela Road, Vasant Kunj, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1500\n\n4. Fourty Four\nA 15/18, Sector 44, Noida\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 700\n\n5. Chili's Grill & Bar\n3rd Floor, DLF Mall Of India, Sector 18, Noida\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n6. Cafe Wink\nG-1, Sikka Galaxy, Plot 9, Shreshtha Vihar, Anand Vihar, New Delhi\nHas Vynikaj\u00face rating of 4.7\nWith an average bill amount of Rs. 700\n\n7. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1600\n\n8. Ministry Of Beer\nM 44, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n9. Chili's Grill & Bar\n3rd Floor, Ambience Mall, DLF Phase 3, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1800\n\n10. Dramebaaz\n2624, First & Second Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1450\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart
    - export

## Generated Story 2772405094739811916
* greet
    - utter_greet
* restaurant_search{"location": "siliguri", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "siliguri"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Dhaba By Amber \nSaluja Residency, Hill Cart Road, Near Sevoke More, Siliguri\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 900\n\n2. Half Full\nThird Floor, The Planet Mall, Sevoke Road, Near Bankim Nagar\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1000\n\n3. Punjabi Kadhai\nSidhi Arcade, Near Anandloke Hospital, Sevoke Road, Janta Nagar, Siliguri\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 750\n\n4. Open House Cafe & Pub\nInfinity Square, 2nd Mile, Sevoke Road, Bankim Nagar, Siliguri\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 1000\n\n5. Hashtag\nThird Floor, The Planet Mall, Sevoke Road, Near Bankim Nagar\nHas Very Good rating of 4.3\nWith an average bill amount of Rs. 1200\n\n6. Worth The Hype\n1st Floor, Planet Mall, Sevoke Road, Bankim Nagar, Siliguri\nHas Very Good rating of 4.2\nWith an average bill amount of Rs. 700\n\n7. The Swedish\n2nd Floor, The Planet Mall, Opposite Cosmos Mall, Sevoke Road, Siliguri \nHas Very Good rating of 4.2\nWith an average bill amount of Rs. 800\n\n8. Skkky\nSkkky Club, Quantum Building, Paribahan Nagar, Matigara, Patiram Jote, Siliguri\nHas Very Good rating of 4.2\nWith an average bill amount of Rs. 1000\n\n9. The Barcode\nVega Circle Mall, Level 3, Sevoke Road, 3rd Mile, Bankim Nagar, Siliguri\nHas Very Good rating of 4.1\nWith an average bill amount of Rs. 1000\n\n10. The Yellow Chilli\nThird Floor, The Planet Mall, Sevoke Road, Near Bankim Nagar\nHas Very Good rating of 4.1\nWith an average bill amount of Rs. 700\n\n"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_entry{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. Dhaba By Amber \nSaluja Residency, Hill Cart Road, Near Sevoke More, Siliguri\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 900\n\n2. Half Full\nThird Floor, The Planet Mall, Sevoke Road, Near Bankim Nagar\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1000\n\n3. Punjabi Kadhai\nSidhi Arcade, Near Anandloke Hospital, Sevoke Road, Janta Nagar, Siliguri\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 750\n\n4. Open House Cafe & Pub\nInfinity Square, 2nd Mile, Sevoke Road, Bankim Nagar, Siliguri\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 1000\n\n5. Hashtag\nThird Floor, The Planet Mall, Sevoke Road, Near Bankim Nagar\nHas Very Good rating of 4.3\nWith an average bill amount of Rs. 1200\n\n6. Worth The Hype\n1st Floor, Planet Mall, Sevoke Road, Bankim Nagar, Siliguri\nHas Very Good rating of 4.2\nWith an average bill amount of Rs. 700\n\n7. The Swedish\n2nd Floor, The Planet Mall, Opposite Cosmos Mall, Sevoke Road, Siliguri \nHas Very Good rating of 4.2\nWith an average bill amount of Rs. 800\n\n8. Skkky\nSkkky Club, Quantum Building, Paribahan Nagar, Matigara, Patiram Jote, Siliguri\nHas Very Good rating of 4.2\nWith an average bill amount of Rs. 1000\n\n9. The Barcode\nVega Circle Mall, Level 3, Sevoke Road, 3rd Mile, Bankim Nagar, Siliguri\nHas Very Good rating of 4.1\nWith an average bill amount of Rs. 1000\n\n10. The Yellow Chilli\nThird Floor, The Planet Mall, Sevoke Road, Near Bankim Nagar\nHas Very Good rating of 4.1\nWith an average bill amount of Rs. 700\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart
    - export

## Generated Story -2467273052587836803
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "hyderabaad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabaad"}
    - action_check_ao
    - slot{"supported_location": false}
    - utter_unsupported_city
    - utter_goodbye
    - action_restart
    - export

## Generated Story -2603344071530147013
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "hyderabaad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabaad"}
    - action_check_ao
    - slot{"supported_location": false}
    - utter_unsupported_city
    - utter_goodbye
    - action_restart
    - export

## Generated Story -1750472937962840231
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kathmandu"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kathmandu"}
    - action_check_ao
    - slot{"supported_location": false}
    - utter_unsupported_city
    - utter_goodbye
    - action_restart
    - export

## Generated Story -4959467838133090329
* restaurant_search{"cuisine": "south indian", "location": "chennai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chennai"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "under 300"}
    - slot{"budget": "under 300"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Prems Graama Bhojanam\n19, Sardar Patel Road, Next To GRT, Adyar, Chennai\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 300\n\n2. Welcome Hotel\n112/241, Purasawalkam High Road, Purasavakkam, Chennai.\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 250\n\n3. Eating Circles\n6, CP Ramaswamy Road, Alwarpet, Chennai\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 250\n\n4. Andhikkadai\n20, Dhandeeswaram Main Road, Velachery, Chennai\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 300\n\n5. Murugan Idli Shop\n77-1/A, G.N. Chetty Road, T. Nagar, Chennai\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 150\n\n6. Rayar's Mess\n31, Arundale Street, Mylapore, Chennai\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 100\n\n7. Idlies\n17, 18th Avenue, Ashok Nagar, Chennai\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 300\n\n8. Sapthagiri Tiffin Centre\n27/2, Sivagnanam Street, Pondy Bazaar, T. Nagar, Chennai\nHas Very Good rating of 4.3\nWith an average bill amount of Rs. 200\n\n9. Nair Mess\n22, Mohammed Abdullah 2nd Street, Opposite Chepauk Stadium, Chepauk, Triplicane, Chennai\nHas Very Good rating of 4.3\nWith an average bill amount of Rs. 200\n\n10. Ratna Cafe\n255, Triplicane High Road, Triplicane, Chennai\nHas Very Good rating of 4.3\nWith an average bill amount of Rs. 300\n\n"}
    - utter_ask_email_send
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -5401073206999282069
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Dana Choga\n5 & Amp; 6, Atul Kataria Chowk, Sector 14, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 500\n\n2. Echoes Hudson Lane\n2522 2nd & 3rd Floor, Hudson Lane, Kingsway Camp, Model Town 1, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n3. Desi Dakaar\nSector 26, Noida\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 500\n\n4. Amar Jyoti\n186, Sarojini Nagar Market, Sarojini Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n5. Chinese Veg Crunch\nA-4, Shop No-32, DDA Market, Paschim Vihar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 450\n\n6. Food of Dreams\nPaschim Vihar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 500\n\n7. Me-Bo: Meal in a Bowl\n8 IDC, MG Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n8. Asian Soi\nPatparganj, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n9. Diners Den\n30/5, Nangiya Park, Ground Floor, Shakti Nagar, Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 400\n\n10. Armaan's Food\nArcade A, Amprali Princely Estate, Sector-76 Near Sector 72, Noida\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n"}
    - utter_ask_email_send
* affirm{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. Dana Choga\n5 & Amp; 6, Atul Kataria Chowk, Sector 14, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 500\n\n2. Echoes Hudson Lane\n2522 2nd & 3rd Floor, Hudson Lane, Kingsway Camp, Model Town 1, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n3. Desi Dakaar\nSector 26, Noida\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 500\n\n4. Amar Jyoti\n186, Sarojini Nagar Market, Sarojini Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n5. Chinese Veg Crunch\nA-4, Shop No-32, DDA Market, Paschim Vihar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 450\n\n6. Food of Dreams\nPaschim Vihar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 500\n\n7. Me-Bo: Meal in a Bowl\n8 IDC, MG Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n8. Asian Soi\nPatparganj, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n9. Diners Den\n30/5, Nangiya Park, Ground Floor, Shakti Nagar, Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 400\n\n10. Armaan's Food\nArcade A, Amprali Princely Estate, Sector-76 Near Sector 72, Noida\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story -1498861248302719207
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "under 300"}
    - slot{"budget": "under 300"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Dana Choga\n5 & Amp; 6, Atul Kataria Chowk, Sector 14, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 500\n\n2. Echoes Hudson Lane\n2522 2nd & 3rd Floor, Hudson Lane, Kingsway Camp, Model Town 1, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n3. Desi Dakaar\nSector 26, Noida\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 500\n\n4. Amar Jyoti\n186, Sarojini Nagar Market, Sarojini Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n5. Chinese Veg Crunch\nA-4, Shop No-32, DDA Market, Paschim Vihar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 450\n\n6. Food of Dreams\nPaschim Vihar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 500\n\n7. Me-Bo: Meal in a Bowl\n8 IDC, MG Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n8. Asian Soi\nPatparganj, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n9. Diners Den\n30/5, Nangiya Park, Ground Floor, Shakti Nagar, Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 400\n\n10. Armaan's Food\nArcade A, Amprali Princely Estate, Sector-76 Near Sector 72, Noida\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* restaurant_search{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. Dana Choga\n5 & Amp; 6, Atul Kataria Chowk, Sector 14, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 500\n\n2. Echoes Hudson Lane\n2522 2nd & 3rd Floor, Hudson Lane, Kingsway Camp, Model Town 1, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n3. Desi Dakaar\nSector 26, Noida\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 500\n\n4. Amar Jyoti\n186, Sarojini Nagar Market, Sarojini Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n5. Chinese Veg Crunch\nA-4, Shop No-32, DDA Market, Paschim Vihar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 450\n\n6. Food of Dreams\nPaschim Vihar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 500\n\n7. Me-Bo: Meal in a Bowl\n8 IDC, MG Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n8. Asian Soi\nPatparganj, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n9. Diners Den\n30/5, Nangiya Park, Ground Floor, Shakti Nagar, Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 400\n\n10. Armaan's Food\nArcade A, Amprali Princely Estate, Sector-76 Near Sector 72, Noida\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 600\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart

## Generated Story 2035648298481058708
* greet
    - utter_greet
* restaurant_search{"location": "tirunelveli"}
    - slot{"location": "tirunelveli"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n"}
    - utter_ask_email_send
* email_entry{"email_address": "pinninti.charan@gmail.com"}
    - slot{"email_address": "pinninti.charan@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart
    - export

## Generated Story -5421020653985509020
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "bhopal"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "bhopal"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Shahnama - Jehan Numa Palace\nHotel Jehan Numa Palace, 157, Shymala Hills, TT Nagar, Bhopal\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 2000\n\n2. Saffron\nThird Floor, DB City Mall, Maharana Pratap Nagar, Bhopal\nHas Very Good rating of 4.1\nWith an average bill amount of Rs. 750\n\n3. Hakeem's\nShop - 3, CPA Building, E-5, Bitthan Market, Arera Colony, Bhopal\nHas Good rating of 3.9\nWith an average bill amount of Rs. 800\n\n4. Andhra Mirchi\nTrilanga Main Road, Near Aura Mall, Shahpura, Bhopal, Madhya Pradesh\nHas Good rating of 3.7\nWith an average bill amount of Rs. 1200\n\n5. Hakeem's\nShop No 1,2 Danish Nagar Hoshangabad Road Near ashima mall bhopal\nHas Good rating of 3.7\nWith an average bill amount of Rs. 800\n\n6. Hakeem Hotel\nNew Market, TT Nagar, Bhopal\nHas Good rating of 3.6\nWith an average bill amount of Rs. 800\n\n7. Delight Korner Cafe Restaurant\nR-8, Zone 1, Maharana Pratap Nagar, Bhopal\nHas Good rating of 3.5\nWith an average bill amount of Rs. 800\n\n8. Hakeem Hotel\n7, Minal Gate 1 J.K Road, Ayodhya Road, BHEL, Bhopal\nHas Average rating of 3.4\nWith an average bill amount of Rs. 800\n\n9. Hakeem's\nShop 345, Lower Ground Floor, Ultimate Arcade, Near Vishal Mega Mart, Kolar Road, Kolar, Bhopal\nHas Average rating of 3.4\nWith an average bill amount of Rs. 800\n\n10. Moti Mahal Delux\nSecond Floor, Aashima Mall, Hoshangabad Road, Bhopal\nHas Average rating of 3.4\nWith an average bill amount of Rs. 800\n\n"}
    - utter_ask_email_send
* restaurant_search{"email_address": "charan.pinninti@gmail.com"}
    - slot{"email_address": "charan.pinninti@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"email_address": ""}
    - utter_goodbye
    - action_restart
* goodbye
    - utter_goodbye
    - action_restart
* goodbye
    - export

## Generated Story 777408331512581490
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Sahib\u2019s Barbeque by Ohri\u2019s\nOhris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1400\n\n2. Flechazo\n2nd Floor, Sun Towers, Sector 1, Huda Techno Enclave, Above Mangatrai Jewellers, Madhapur, Hyderabad\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1300\n\n3. AB's - Absolute Barbecues\nPlot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n4. Over The Moon Brew Company\nPlot B 2, Survey  6/1, Quiet Lands, Gachibowli, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1200\n\n5. Farzi Cafe\n1200, Road 59, Jubilee Hills, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1800\n\n6. Barbeque Pride\n790, Rangoli Building, Road 36, Jubilee Hills, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n7. Exotica\n5th Floor, 12th Square Building, Opposite Audi Showroom, Road 12, Banjara Hills, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n8. Jewel of Nizam - The Minar - The Golkonda Resort\nJewel of Nizam The Minar Golkonda resorts Gandipet\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 2500\n\n9. The Fisherman's Wharf\n304, Puppalaguda, Financial District,ISB - Outer Ring Road, Gachibowli, Hyderabad\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1500\n\n10. SodaBottleOpenerWala\nUnit 4, Ground Floor, Niharika Jubilee One, Road 1, Jubilee Hills, Hyderabad\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1400\n\n"}
    - utter_ask_email_send
* restaurant_search{"email_address": "charan.pinninti@gmail.com"}
    - slot{"email_address": "charan.pinninti@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. Sahib\u2019s Barbeque by Ohri\u2019s\nOhris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1400\n\n2. Flechazo\n2nd Floor, Sun Towers, Sector 1, Huda Techno Enclave, Above Mangatrai Jewellers, Madhapur, Hyderabad\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1300\n\n3. AB's - Absolute Barbecues\nPlot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n4. Over The Moon Brew Company\nPlot B 2, Survey  6/1, Quiet Lands, Gachibowli, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1200\n\n5. Farzi Cafe\n1200, Road 59, Jubilee Hills, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1800\n\n6. Barbeque Pride\n790, Rangoli Building, Road 36, Jubilee Hills, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n7. Exotica\n5th Floor, 12th Square Building, Opposite Audi Showroom, Road 12, Banjara Hills, Hyderabad\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n8. Jewel of Nizam - The Minar - The Golkonda Resort\nJewel of Nizam The Minar Golkonda resorts Gandipet\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 2500\n\n9. The Fisherman's Wharf\n304, Puppalaguda, Financial District,ISB - Outer Ring Road, Gachibowli, Hyderabad\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1500\n\n10. SodaBottleOpenerWala\nUnit 4, Ground Floor, Niharika Jubilee One, Road 1, Jubilee Hills, Hyderabad\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1400\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart
    - export

## Generated Story -7685186173269203282
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_cuisine
* affirm
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_restaurant
    - utter_ask_email_send
* restaurant_search{"email_address": "pinninti.charan@gmail.com"}
    - slot{"email_address": "pinninti.charan@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - utter_goodbye
    - action_restart
    - export
    
## Generated Story 8319200245433724680
* greet{"greet": "hey"}
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "siliguri"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "siliguri"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - action_restaurant

## Generated Story 614128655324774765
* greet
    - utter_greet
* restaurant_search{"budget": "300 to 700", "cuisine": "mexican", "location": "siliguri"}
    - slot{"budget": "300 to 700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "siliguri"}
    - action_check_ao
    - slot{"supported_location": true}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Virrest\nChampasari More, Near Priya Store, Champasari, Siliguri\nHas Average rating of 3.1\nWith an average bill amount of Rs. 500\n\n"}
    - utter_ask_email_send
* affirm{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. Virrest\nChampasari More, Near Priya Store, Champasari, Siliguri\nHas Average rating of 3.1\nWith an average bill amount of Rs. 500\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart

## Generated Story -7481959009053360923
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n2. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n3. Sanadige\n22/48, Commercial Centre, Chanakyapuri, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 2200\n\n4. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n5. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n6. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n7. Indian Grill Room\n315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n8. Barbeque Nation\nUnit 601, 6th Floor, Unity One, MLCP Plot, Rohini West Metro Station Complex, Rohini, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1400\n\n9. Burma Burma\nS 25, Second Floor, A 3, Select Citywalk Mall, Saket, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1500\n\n10. Biryani Badshah\nK-14, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 800\n\n"}
    - utter_ask_email_send
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story -1045375420016710345
* restaurant_search{"budget": "300 to 700", "cuisine": "Italian", "location": "delhi"}
    - slot{"budget": "300 to 700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n2. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n3. Sanadige\n22/48, Commercial Centre, Chanakyapuri, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 2200\n\n4. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n5. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n6. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n7. Indian Grill Room\n315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n8. Barbeque Nation\nUnit 601, 6th Floor, Unity One, MLCP Plot, Rohini West Metro Station Complex, Rohini, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1400\n\n9. Burma Burma\nS 25, Second Floor, A 3, Select Citywalk Mall, Saket, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1500\n\n10. Biryani Badshah\nK-14, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 800\n\n"}
    - utter_ask_email_send
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story 1612469605295038387
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "over 700"}
    - slot{"budget": "over 700"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n2. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n3. Sanadige\n22/48, Commercial Centre, Chanakyapuri, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 2200\n\n4. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n5. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n6. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n7. Indian Grill Room\n315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n8. Barbeque Nation\nUnit 601, 6th Floor, Unity One, MLCP Plot, Rohini West Metro Station Complex, Rohini, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1400\n\n9. Burma Burma\nS 25, Second Floor, A 3, Select Citywalk Mall, Saket, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1500\n\n10. Biryani Badshah\nK-14, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 800\n\n11. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n12. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n13. Hudson Oven\n84, Mall Road, Kingsway Camp, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 800\n\n14. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n15. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n16. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n17. Liv Bar\nWorldmark 1, Lower Ground Floor, R3, Aerocity, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n18. Fourty Four\nA 15/18, Sector 44, Noida\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 700\n\n19. Unplugged Courtyard\nOpposite Plot 269, Phase II, Udyog Vihar, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n20. Chili's Grill & Bar\n3rd Floor, DLF Mall Of India, Sector 18, Noida\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n21. Chili's Grill & Bar\nS 8 & 9, 2nd Floor, Pacific Mall, Tagore Garden, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n22. Cafe Wink\nG-1, Sikka Galaxy, Plot 9, Shreshtha Vihar, Anand Vihar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 700\n\n23. Ministry Of Beer\nM 44, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n24. Decode Air Bar\nSCO 39, 1st Floor, Sector 29, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n25. The Barbeque Company\n4, Hargovind Enclave, Opposite Shanti Mukund Hospital, Karkardooma, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1300\n\n26. Chili's Grill & Bar\n3rd Floor, Ambience Mall, Nelson Madela Road, Vasant Kunj, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n27. POMP - Pizza On My Plate\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n28. Chili's Grill & Bar\n3rd Floor, Ambience Mall, DLF Phase 3, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1800\n\n29. Dramebaaz\n2624, First & Second Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1450\n\n30. The Bing's\nNear Savitri Cinemas, Greater Kailash 2 (GK2), New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n31. Phonebooth Express\nDelhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n32. Housefull Cafe Lounge\n2509, 3rd floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1400\n\n33. Speak Greasy\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n34. Scene - High Bar\nShop No.1, 3rd Floor, Ninex City Mart, Sector 49, Sohna Road, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1200\n\n35. Cafe Pasticcino\nN 2, Qutub Plaza, DLF Phase 1, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1000\n\n36. Jimmy Boy\n7, First Floor, Satya Niketan, Satyaniketan, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n37. Hauz Khas Social\n9-A & 12, Hauz Khas Village, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1300\n\n38. Chili's Grill & Bar\nM-9, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1500\n\n39. Jazbaa\nF-89, Vishal Enclave, Rajouri Garden, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1700\n\n40. Phonebooth Reloaded\nG14b, Ground Floor, Vijay Nagar, Hudson lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1000\n\n41. AB's - Absolute Barbecues\nShop LG 1-3, MGF Metropolis Mall, MG Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1600\n\n42. Manhattan Bar Exchange & Brewery\n1st Floor, Global Foyer Mall, Sector 43, Golf Course Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1400\n\n43. Pizza Express\nT-317, 3rd Floor, Ambience Mall, DLF Phase 3, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1900\n\n44. Pirates of Grill\nC-12, Vishal Enclave, Main Nazafgarh Road, Rajouri Garden, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1500\n\n45. Owl is Well\nGreater Kailash 1 (GK 1), New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1000\n\n46. Epic Kitchen N Bar\nG-16A, 1st , 2nd & 3rd Floor, Vijay Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1300\n\n47. By the Bay\n2522, 1st Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 900\n\n48. Matchbox\n30, 1st Floor, Hauz Khas Village, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1700\n\n49. Burgerama\nSushant Shopping Arcade, Sushant Lok, Gurgaon, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 800\n\n50. Fat Cat Bistro\nC116, Ground Floor, Panchsheel Vihar, Khirki Main Road, Malviya Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 800\n\n51. Red Scooter Italia\nKailash Colony, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 800\n\n52. CG's - Lounge Cafe Bar\nA-4, 1st Floor, Vishal Enclave, Rajouri Garden, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1700\n\n53. Cafeteria & Co.\nG 14, Hudson Lane, Vijay Nagar, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 900\n\n54. Pa Pa Ya\nDome, Level 4, Select Citywalk, A-3, District Centre, Saket, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2000\n\n55. Detroit\nF40, 2nd Floor, Inner Circle, \nConnaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n56. The Luggage Room Kitchen And Bar\nM-39, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1300\n\n57. Boombox Brewstreet\nSCO 53, 1st Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1600\n\n58. Cyber Hub Social\nShop 04A, Ground Floor DLF Cyber Hub, Tower - 08C, DLF Cyber City, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1300\n\n59. Gravity Spacebar\nPlot 6 & 7, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1400\n\n60. The Reader's Cafe\n208-212, Indirapuram Habitat Centre, Ahinsa Khand 1, Indirapuram, Ghaziabad\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1000\n\n61. I Sacked Newton\n5th Floor, Logix City Centre Mall, Sector 32, Sector 31, Noida\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2000\n\n62. Tama Brewery & World Kitchen\nSCO 14-15, 2nd Floor, Huda Market, Sector 16, Faridabad\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n63. Chili's Grill & Bar\n161-A, Ground Floor, DLF Place Mall, Saket, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n64. Yum Yum Cha\nShop 69, First floor, Middle Lane, Khan Market, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1800\n\n65. Garage Inc.\n30, 2nd Floor, Powerhouse Buliding, Hauz Khas Village, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1900\n\n66. HotMess\nM-11, Middle Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1900\n\n67. Punter House Cafe Reloaded\n102-106, 1st Floor, City Centre Mall, Sector 12, Dwarka\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n68. Decode\nJ2/1 ,BK Dutta Market, Rajouri Garden, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n69. Master Of Malts\n2nd Floor, Scindia House, Atma Ram Mansion, K.G. Marg, Connaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1600\n\n70. Hippie Bus World's Street Food\nTerrace, Sikka Galaxy Complex, Sreshtha Vihar Market, Anand Vihar, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n71. Farzi Cafe\n7-8, Ground Floor, Cyber Hub, DLF Cyber City, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2200\n\n72. Yum Yum Cha\nCyber Hub, DLF Cyber City, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1800\n\n73. Downtown - Diners & Living Beer Cafe\nSCO 34, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2200\n\n74. Cervesia\nSCO 22, 1st Floor, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n75. Bell Pepperz\nA-4, Community Centre, Ashok Vihar Phase 2, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1300\n\n76. The Ivy\n89/90 Ground Floor, Baani Square, Sector 50, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n77. Sazerac\n21, 1st Floor, Sunder Nagar Market, Behind HDFC Bank, Sunder Nagar, New Delhi\nHas Terbaik rating of 4.5\nWith an average bill amount of Rs. 2300\n\n78. PomoDoro Bistro\nUGF, H-222, Sushant Shopping Arcade, Phase 1, Sushant Lok, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n79. Crudo Juicery\nSF-85, Galleria Market, DLF Phase 4, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n80. 2Tree Coffee\n4, 3rd Floor, PVR Anupam Complex, Community Centre, Saket, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n81. Vagator Beach Shack\nLGF 34, South Point Mall, Golf Course Road, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n82. Food Scouts\nPunjabi Bagh, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 750\n\n83. Cafe StayWoke\n1st Floor, Shop Number 104, South Point Mall, Golf Course Road, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1100\n\n84. Crazy Monkey\nShop 3, E151, Krishna Market, Lajpat Nagar 1, New Delhi, Delhi NCR\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n85. Drunken Detective\n1st Floor, C Block, Indirapuram Habitat Center, Ahinsa Khand 1, Indirapuram, Ghaziabad\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n86. Number 7 - The Asian Story\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n87. The Lo-cal Kitchen\nR-21, Greater Kailash 1 (GK 1), New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n88. Bae Gourmet Kitchen\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n89. Mad Batter\n2nd Floor, The Shopping Mall, Arjun Marg, DLF Phase 1, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n90. Odeon Social\n23, 1st Floor, Odeon Building, Radial 5, D Block, Connaught Place, New Delhi\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 1300\n\n"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_entry{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n2. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n3. Sanadige\n22/48, Commercial Centre, Chanakyapuri, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 2200\n\n4. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n5. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n6. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n7. Indian Grill Room\n315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n8. Barbeque Nation\nUnit 601, 6th Floor, Unity One, MLCP Plot, Rohini West Metro Station Complex, Rohini, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1400\n\n9. Burma Burma\nS 25, Second Floor, A 3, Select Citywalk Mall, Saket, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1500\n\n10. Biryani Badshah\nK-14, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 800\n\n11. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n12. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n13. Hudson Oven\n84, Mall Road, Kingsway Camp, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 800\n\n14. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n15. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n16. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n17. Liv Bar\nWorldmark 1, Lower Ground Floor, R3, Aerocity, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n18. Fourty Four\nA 15/18, Sector 44, Noida\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 700\n\n19. Unplugged Courtyard\nOpposite Plot 269, Phase II, Udyog Vihar, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n20. Chili's Grill & Bar\n3rd Floor, DLF Mall Of India, Sector 18, Noida\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n21. Chili's Grill & Bar\nS 8 & 9, 2nd Floor, Pacific Mall, Tagore Garden, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n22. Cafe Wink\nG-1, Sikka Galaxy, Plot 9, Shreshtha Vihar, Anand Vihar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 700\n\n23. Ministry Of Beer\nM 44, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n24. Decode Air Bar\nSCO 39, 1st Floor, Sector 29, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n25. The Barbeque Company\n4, Hargovind Enclave, Opposite Shanti Mukund Hospital, Karkardooma, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1300\n\n26. Chili's Grill & Bar\n3rd Floor, Ambience Mall, Nelson Madela Road, Vasant Kunj, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n27. POMP - Pizza On My Plate\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n28. Chili's Grill & Bar\n3rd Floor, Ambience Mall, DLF Phase 3, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1800\n\n29. Dramebaaz\n2624, First & Second Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1450\n\n30. The Bing's\nNear Savitri Cinemas, Greater Kailash 2 (GK2), New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n31. Phonebooth Express\nDelhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n32. Housefull Cafe Lounge\n2509, 3rd floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1400\n\n33. Speak Greasy\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n34. Scene - High Bar\nShop No.1, 3rd Floor, Ninex City Mart, Sector 49, Sohna Road, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1200\n\n35. Cafe Pasticcino\nN 2, Qutub Plaza, DLF Phase 1, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1000\n\n36. Jimmy Boy\n7, First Floor, Satya Niketan, Satyaniketan, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n37. Hauz Khas Social\n9-A & 12, Hauz Khas Village, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1300\n\n38. Chili's Grill & Bar\nM-9, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1500\n\n39. Jazbaa\nF-89, Vishal Enclave, Rajouri Garden, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1700\n\n40. Phonebooth Reloaded\nG14b, Ground Floor, Vijay Nagar, Hudson lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1000\n\n41. AB's - Absolute Barbecues\nShop LG 1-3, MGF Metropolis Mall, MG Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1600\n\n42. Manhattan Bar Exchange & Brewery\n1st Floor, Global Foyer Mall, Sector 43, Golf Course Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1400\n\n43. Pizza Express\nT-317, 3rd Floor, Ambience Mall, DLF Phase 3, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1900\n\n44. Pirates of Grill\nC-12, Vishal Enclave, Main Nazafgarh Road, Rajouri Garden, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1500\n\n45. Owl is Well\nGreater Kailash 1 (GK 1), New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1000\n\n46. Epic Kitchen N Bar\nG-16A, 1st , 2nd & 3rd Floor, Vijay Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1300\n\n47. By the Bay\n2522, 1st Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 900\n\n48. Matchbox\n30, 1st Floor, Hauz Khas Village, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1700\n\n49. Burgerama\nSushant Shopping Arcade, Sushant Lok, Gurgaon, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 800\n\n50. Fat Cat Bistro\nC116, Ground Floor, Panchsheel Vihar, Khirki Main Road, Malviya Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 800\n\n51. Red Scooter Italia\nKailash Colony, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 800\n\n52. CG's - Lounge Cafe Bar\nA-4, 1st Floor, Vishal Enclave, Rajouri Garden, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1700\n\n53. Cafeteria & Co.\nG 14, Hudson Lane, Vijay Nagar, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 900\n\n54. Pa Pa Ya\nDome, Level 4, Select Citywalk, A-3, District Centre, Saket, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2000\n\n55. Detroit\nF40, 2nd Floor, Inner Circle, \nConnaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n56. The Luggage Room Kitchen And Bar\nM-39, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1300\n\n57. Boombox Brewstreet\nSCO 53, 1st Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1600\n\n58. Cyber Hub Social\nShop 04A, Ground Floor DLF Cyber Hub, Tower - 08C, DLF Cyber City, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1300\n\n59. Gravity Spacebar\nPlot 6 & 7, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1400\n\n60. The Reader's Cafe\n208-212, Indirapuram Habitat Centre, Ahinsa Khand 1, Indirapuram, Ghaziabad\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1000\n\n61. I Sacked Newton\n5th Floor, Logix City Centre Mall, Sector 32, Sector 31, Noida\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2000\n\n62. Tama Brewery & World Kitchen\nSCO 14-15, 2nd Floor, Huda Market, Sector 16, Faridabad\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n63. Chili's Grill & Bar\n161-A, Ground Floor, DLF Place Mall, Saket, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n64. Yum Yum Cha\nShop 69, First floor, Middle Lane, Khan Market, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1800\n\n65. Garage Inc.\n30, 2nd Floor, Powerhouse Buliding, Hauz Khas Village, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1900\n\n66. HotMess\nM-11, Middle Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1900\n\n67. Punter House Cafe Reloaded\n102-106, 1st Floor, City Centre Mall, Sector 12, Dwarka\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n68. Decode\nJ2/1 ,BK Dutta Market, Rajouri Garden, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n69. Master Of Malts\n2nd Floor, Scindia House, Atma Ram Mansion, K.G. Marg, Connaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1600\n\n70. Hippie Bus World's Street Food\nTerrace, Sikka Galaxy Complex, Sreshtha Vihar Market, Anand Vihar, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n71. Farzi Cafe\n7-8, Ground Floor, Cyber Hub, DLF Cyber City, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2200\n\n72. Yum Yum Cha\nCyber Hub, DLF Cyber City, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1800\n\n73. Downtown - Diners & Living Beer Cafe\nSCO 34, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2200\n\n74. Cervesia\nSCO 22, 1st Floor, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n75. Bell Pepperz\nA-4, Community Centre, Ashok Vihar Phase 2, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1300\n\n76. The Ivy\n89/90 Ground Floor, Baani Square, Sector 50, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n77. Sazerac\n21, 1st Floor, Sunder Nagar Market, Behind HDFC Bank, Sunder Nagar, New Delhi\nHas Terbaik rating of 4.5\nWith an average bill amount of Rs. 2300\n\n78. PomoDoro Bistro\nUGF, H-222, Sushant Shopping Arcade, Phase 1, Sushant Lok, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n79. Crudo Juicery\nSF-85, Galleria Market, DLF Phase 4, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n80. 2Tree Coffee\n4, 3rd Floor, PVR Anupam Complex, Community Centre, Saket, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n81. Vagator Beach Shack\nLGF 34, South Point Mall, Golf Course Road, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n82. Food Scouts\nPunjabi Bagh, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 750\n\n83. Cafe StayWoke\n1st Floor, Shop Number 104, South Point Mall, Golf Course Road, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1100\n\n84. Crazy Monkey\nShop 3, E151, Krishna Market, Lajpat Nagar 1, New Delhi, Delhi NCR\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n85. Drunken Detective\n1st Floor, C Block, Indirapuram Habitat Center, Ahinsa Khand 1, Indirapuram, Ghaziabad\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n86. Number 7 - The Asian Story\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n87. The Lo-cal Kitchen\nR-21, Greater Kailash 1 (GK 1), New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n88. Bae Gourmet Kitchen\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n89. Mad Batter\n2nd Floor, The Shopping Mall, Arjun Marg, DLF Phase 1, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n90. Odeon Social\n23, 1st Floor, Odeon Building, Radial 5, D Block, Connaught Place, New Delhi\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 1300\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart

## Generated Story 8308804998530758363
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search

## Generated Story -7468340589888976481
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "banglore"}
    - slot{"location": "banglore"}
    - action_check_ao
    - slot{"supported_location": false}
    - utter_unsupported_city
    - utter_goodbye
    - action_restart

## Generated Story -114922082652714333
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bokaro steel city"}
    - slot{"location": "bokaro steel city"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n2. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n3. Sanadige\n22/48, Commercial Centre, Chanakyapuri, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 2200\n\n4. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n5. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n6. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n7. Indian Grill Room\n315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n8. Barbeque Nation\nUnit 601, 6th Floor, Unity One, MLCP Plot, Rohini West Metro Station Complex, Rohini, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1400\n\n9. Burma Burma\nS 25, Second Floor, A 3, Select Citywalk Mall, Saket, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1500\n\n10. Biryani Badshah\nK-14, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 800\n\n11. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n12. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n13. Hudson Oven\n84, Mall Road, Kingsway Camp, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 800\n\n14. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n15. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n16. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n17. Liv Bar\nWorldmark 1, Lower Ground Floor, R3, Aerocity, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n18. Fourty Four\nA 15/18, Sector 44, Noida\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 700\n\n19. Unplugged Courtyard\nOpposite Plot 269, Phase II, Udyog Vihar, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n20. Chili's Grill & Bar\n3rd Floor, DLF Mall Of India, Sector 18, Noida\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n21. Chili's Grill & Bar\nS 8 & 9, 2nd Floor, Pacific Mall, Tagore Garden, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n22. Cafe Wink\nG-1, Sikka Galaxy, Plot 9, Shreshtha Vihar, Anand Vihar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 700\n\n23. Ministry Of Beer\nM 44, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n24. Decode Air Bar\nSCO 39, 1st Floor, Sector 29, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n25. The Barbeque Company\n4, Hargovind Enclave, Opposite Shanti Mukund Hospital, Karkardooma, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1300\n\n26. Chili's Grill & Bar\n3rd Floor, Ambience Mall, Nelson Madela Road, Vasant Kunj, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n27. POMP - Pizza On My Plate\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n28. Chili's Grill & Bar\n3rd Floor, Ambience Mall, DLF Phase 3, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1800\n\n29. Dramebaaz\n2624, First & Second Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1450\n\n30. The Bing's\nNear Savitri Cinemas, Greater Kailash 2 (GK2), New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n31. Phonebooth Express\nDelhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n32. Housefull Cafe Lounge\n2509, 3rd floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1400\n\n33. Speak Greasy\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n34. Scene - High Bar\nShop No.1, 3rd Floor, Ninex City Mart, Sector 49, Sohna Road, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1200\n\n35. Cafe Pasticcino\nN 2, Qutub Plaza, DLF Phase 1, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1000\n\n36. Jimmy Boy\n7, First Floor, Satya Niketan, Satyaniketan, New Delhi\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 800\n\n37. Hauz Khas Social\n9-A & 12, Hauz Khas Village, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1300\n\n38. Chili's Grill & Bar\nM-9, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1500\n\n39. Jazbaa\nF-89, Vishal Enclave, Rajouri Garden, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1700\n\n40. Phonebooth Reloaded\nG14b, Ground Floor, Vijay Nagar, Hudson lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1000\n\n41. AB's - Absolute Barbecues\nShop LG 1-3, MGF Metropolis Mall, MG Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1600\n\n42. Manhattan Bar Exchange & Brewery\n1st Floor, Global Foyer Mall, Sector 43, Golf Course Road, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1400\n\n43. Pizza Express\nT-317, 3rd Floor, Ambience Mall, DLF Phase 3, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1900\n\n44. Pirates of Grill\nC-12, Vishal Enclave, Main Nazafgarh Road, Rajouri Garden, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1500\n\n45. Owl is Well\nGreater Kailash 1 (GK 1), New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1000\n\n46. Epic Kitchen N Bar\nG-16A, 1st , 2nd & 3rd Floor, Vijay Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1300\n\n47. By the Bay\n2522, 1st Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 900\n\n48. Matchbox\n30, 1st Floor, Hauz Khas Village, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1700\n\n49. Burgerama\nSushant Shopping Arcade, Sushant Lok, Gurgaon, Gurgaon\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 800\n\n50. Fat Cat Bistro\nC116, Ground Floor, Panchsheel Vihar, Khirki Main Road, Malviya Nagar, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 800\n\n51. Red Scooter Italia\nKailash Colony, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 800\n\n52. CG's - Lounge Cafe Bar\nA-4, 1st Floor, Vishal Enclave, Rajouri Garden, New Delhi\nHas Excellent rating of 4.6\nWith an average bill amount of Rs. 1700\n\n53. Cafeteria & Co.\nG 14, Hudson Lane, Vijay Nagar, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 900\n\n54. Pa Pa Ya\nDome, Level 4, Select Citywalk, A-3, District Centre, Saket, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2000\n\n55. Detroit\nF40, 2nd Floor, Inner Circle, \nConnaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n56. The Luggage Room Kitchen And Bar\nM-39, Outer Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1300\n\n57. Boombox Brewstreet\nSCO 53, 1st Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1600\n\n58. Cyber Hub Social\nShop 04A, Ground Floor DLF Cyber Hub, Tower - 08C, DLF Cyber City, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1300\n\n59. Gravity Spacebar\nPlot 6 & 7, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1400\n\n60. The Reader's Cafe\n208-212, Indirapuram Habitat Centre, Ahinsa Khand 1, Indirapuram, Ghaziabad\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1000\n\n61. I Sacked Newton\n5th Floor, Logix City Centre Mall, Sector 32, Sector 31, Noida\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2000\n\n62. Tama Brewery & World Kitchen\nSCO 14-15, 2nd Floor, Huda Market, Sector 16, Faridabad\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n63. Chili's Grill & Bar\n161-A, Ground Floor, DLF Place Mall, Saket, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n64. Yum Yum Cha\nShop 69, First floor, Middle Lane, Khan Market, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1800\n\n65. Garage Inc.\n30, 2nd Floor, Powerhouse Buliding, Hauz Khas Village, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1900\n\n66. HotMess\nM-11, Middle Circle, Connaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1900\n\n67. Punter House Cafe Reloaded\n102-106, 1st Floor, City Centre Mall, Sector 12, Dwarka\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n68. Decode\nJ2/1 ,BK Dutta Market, Rajouri Garden, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n69. Master Of Malts\n2nd Floor, Scindia House, Atma Ram Mansion, K.G. Marg, Connaught Place, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1600\n\n70. Hippie Bus World's Street Food\nTerrace, Sikka Galaxy Complex, Sreshtha Vihar Market, Anand Vihar, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n71. Farzi Cafe\n7-8, Ground Floor, Cyber Hub, DLF Cyber City, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2200\n\n72. Yum Yum Cha\nCyber Hub, DLF Cyber City, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1800\n\n73. Downtown - Diners & Living Beer Cafe\nSCO 34, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 2200\n\n74. Cervesia\nSCO 22, 1st Floor, Sector 29, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n75. Bell Pepperz\nA-4, Community Centre, Ashok Vihar Phase 2, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1300\n\n76. The Ivy\n89/90 Ground Floor, Baani Square, Sector 50, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n77. Sazerac\n21, 1st Floor, Sunder Nagar Market, Behind HDFC Bank, Sunder Nagar, New Delhi\nHas Terbaik rating of 4.5\nWith an average bill amount of Rs. 2300\n\n78. PomoDoro Bistro\nUGF, H-222, Sushant Shopping Arcade, Phase 1, Sushant Lok, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n79. Crudo Juicery\nSF-85, Galleria Market, DLF Phase 4, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n80. 2Tree Coffee\n4, 3rd Floor, PVR Anupam Complex, Community Centre, Saket, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n81. Vagator Beach Shack\nLGF 34, South Point Mall, Golf Course Road, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1500\n\n82. Food Scouts\nPunjabi Bagh, New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 750\n\n83. Cafe StayWoke\n1st Floor, Shop Number 104, South Point Mall, Golf Course Road, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1100\n\n84. Crazy Monkey\nShop 3, E151, Krishna Market, Lajpat Nagar 1, New Delhi, Delhi NCR\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 700\n\n85. Drunken Detective\n1st Floor, C Block, Indirapuram Habitat Center, Ahinsa Khand 1, Indirapuram, Ghaziabad\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 1200\n\n86. Number 7 - The Asian Story\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n87. The Lo-cal Kitchen\nR-21, Greater Kailash 1 (GK 1), New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n88. Bae Gourmet Kitchen\nGreater Kailash 1 (GK1), New Delhi\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n89. Mad Batter\n2nd Floor, The Shopping Mall, Arjun Marg, DLF Phase 1, Gurgaon\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 800\n\n90. Odeon Social\n23, 1st Floor, Odeon Building, Radial 5, D Block, Connaught Place, New Delhi\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 1300\n\n91. Domino's Pizza\nB 15, City Center, Sector 4, Bokaro Locality, Bokaro\nHas Not rated rating of 0\nWith an average bill amount of Rs. 400\n\n"}
    - utter_ask_email_send
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story -2647730994510594234
* greet
    - utter_greet
* restaurant_search{"budget": "over 700", "cuisine": "American", "location": "delhi"}
    - slot{"budget": "over 700"}
    - slot{"cuisine": "American"}
    - slot{"location": "delhi"}
    - action_check_ao
    - slot{"supported_location": true}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n2. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n3. Hudson Oven\n84, Mall Road, Kingsway Camp, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 800\n\n4. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n5. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n6. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n7. Liv Bar\nWorldmark 1, Lower Ground Floor, R3, Aerocity, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n8. Fourty Four\nA 15/18, Sector 44, Noida\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 700\n\n9. Unplugged Courtyard\nOpposite Plot 269, Phase II, Udyog Vihar, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n10. Chili's Grill & Bar\n3rd Floor, DLF Mall Of India, Sector 18, Noida\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n"}
    - utter_ask_email_send
* restaurant_search{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n2. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n3. Hudson Oven\n84, Mall Road, Kingsway Camp, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 800\n\n4. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n5. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n6. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n7. Liv Bar\nWorldmark 1, Lower Ground Floor, R3, Aerocity, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n8. Fourty Four\nA 15/18, Sector 44, Noida\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 700\n\n9. Unplugged Courtyard\nOpposite Plot 269, Phase II, Udyog Vihar, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n10. Chili's Grill & Bar\n3rd Floor, DLF Mall Of India, Sector 18, Noida\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart

## Generated Story -1052003806808181993
* greet
    - utter_greet
* restaurant_search{"location": "siliguri"}
    - slot{"location": "siliguri"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "under 300"}
    - slot{"budget": "under 300"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Plum By Bent Chair\nThe Walk, Worldmark 2, Aerocity, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1800\n\n2. The Hook\nSCO 30, Sector 29, Gurgaon\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 1600\n\n3. Hudson Oven\n84, Mall Road, Kingsway Camp, Delhi University-GTB Nagar, New Delhi\nHas Excellent rating of 4.9\nWith an average bill amount of Rs. 800\n\n4. Pirates of Grill\nGround Floor, MGF Mega City Mall, MG Road, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 2000\n\n5. 38 Barracks\nM-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1600\n\n6. Feel Alive\nSCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1200\n\n7. Liv Bar\nWorldmark 1, Lower Ground Floor, R3, Aerocity, New Delhi\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 1800\n\n8. Fourty Four\nA 15/18, Sector 44, Noida\nHas Excellent rating of 4.8\nWith an average bill amount of Rs. 700\n\n9. Unplugged Courtyard\nOpposite Plot 269, Phase II, Udyog Vihar, Gurgaon\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n10. Chili's Grill & Bar\n3rd Floor, DLF Mall Of India, Sector 18, Noida\nHas Excellent rating of 4.7\nWith an average bill amount of Rs. 1500\n\n"}
    - utter_ask_email_send
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story -6400577398291256038
* greet
    - utter_greet
* restaurant_search{"budget": "300 to 700", "cuisine": "chinese", "location": "bengaluru"}
    - slot{"budget": "300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - action_check_ao
    - slot{"supported_location": false}
    - utter_unsupported_city
    - utter_goodbye
    - action_restart

## Generated Story 3963926566752534467
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_ao
    - slot{"supported_location": true}
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"restaurant_found": true}
    - slot{"search_result": "Here are the results of you search: \n\n1. Overdose\n23, Lake Terrace, Sarath Bose Road, Southern Avenue, Kolkata\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 550\n\n2. The Bhoj Company\n60, Hemanta Basu Sarani, Dalhousie BBD Bagh, Kolkata(Stephen House) Opp.B.B.D Bagh mini bus stand\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 500\n\n3. Second House Restaurant\n14, Sardar Shankar Road, Behind Lake Mall, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 550\n\n4. Macazzo\n64, Southern Avenue, Near Menoka Cinema Hall, Beside Medinova Diagnostic Services, Southern Avenue, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 500\n\n5. Momo I Am\nCD 18, Next To Kalyan Jewelers, City Centre 1, Sector 1, Salt Lake\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n6. Momo I Am\nShop G-B, Ground Floor, Tarun Alo Apartment, Chinar Park\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n7. Momo I Am\n43 Ballygunge Gardens, Gariahat, Golpark, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n8. Momo I Am\n195 C, Near Bandhan Bank, Lake Gardens, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n9. Tung Nam\n24, Chattwala Gully, Near Terreti Bazar, Bara Bazar, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n10. Kolkata Restro\n132/1 B, Bidhan Sarani, Hatibagan, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n"}
    - utter_ask_email_send
* affirm
    - utter_ask_email_address
* email_entry{"email_address": "letters.prasai@gmail.com"}
    - slot{"email_address": "letters.prasai@gmail.com"}
    - utter_sending_email
    - action_send_mail
    - slot{"search_result": "Here are the results of you search: \n\n1. Overdose\n23, Lake Terrace, Sarath Bose Road, Southern Avenue, Kolkata\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 550\n\n2. The Bhoj Company\n60, Hemanta Basu Sarani, Dalhousie BBD Bagh, Kolkata(Stephen House) Opp.B.B.D Bagh mini bus stand\nHas Excellent rating of 4.5\nWith an average bill amount of Rs. 500\n\n3. Second House Restaurant\n14, Sardar Shankar Road, Behind Lake Mall, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 550\n\n4. Macazzo\n64, Southern Avenue, Near Menoka Cinema Hall, Beside Medinova Diagnostic Services, Southern Avenue, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 500\n\n5. Momo I Am\nCD 18, Next To Kalyan Jewelers, City Centre 1, Sector 1, Salt Lake\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n6. Momo I Am\nShop G-B, Ground Floor, Tarun Alo Apartment, Chinar Park\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n7. Momo I Am\n43 Ballygunge Gardens, Gariahat, Golpark, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n8. Momo I Am\n195 C, Near Bandhan Bank, Lake Gardens, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n9. Tung Nam\n24, Chattwala Gully, Near Terreti Bazar, Bara Bazar, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n10. Kolkata Restro\n132/1 B, Bidhan Sarani, Hatibagan, Kolkata\nHas Very Good rating of 4.4\nWith an average bill amount of Rs. 600\n\n\n*****SENT*****"}
    - utter_goodbye
    - action_restart

## Generated Story 6747742325400049123
* greet
    - utter_greet
* restaurant_search{"location": "birtamod"}
    - slot{"location": "birtamod"}
    - action_check_ao
    - slot{"supported_location": false}
    - utter_unsupported_city
    - utter_goodbye
    - action_restart

## goodbye 1
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart

## goodbye 2
* greet
    - utter_greet
* restaurant_search
    -utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart

## goodbye 3
* goodbye
    - utter_goodbye
    - action_restart

