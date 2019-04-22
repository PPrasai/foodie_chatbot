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

## previous one with unsupported address
* restaurant_search{"location": "birtamod", "cuisine": "north indian", "budget": "300 to 700"}
    - slot{"location": "birtamod"}
    - action_check_ao
    - utter_unsupported_city
    - utter_goodbye
    
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
    - export

