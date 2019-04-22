## Versions
Rasa NLU = 0.14.6
Rasa Core = 0.13.8
Python = 3.6.8


## Installation instructions
conda create --name chatbot python=3.6.8	            # creates new environment with name 'chatbot'
conda activate chatbot				                    # activates the environment 'chatbot'
conda install -n chatbot pip			                # enables usage of pip in virtual envs

pip install rasa_nlu
pip install rasa_nlu[spacy]
pip install rasa_nlu[tensorflow]

python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en

pip install rasa_core
pip install rasa_core_sdk                               # used to start server for custom actions


## Run
python nlu_model.py                                     # trains NLU to recognize entities
python train_init.py                                    # trains core to communicate
python -m rasa_core_sdk.endpoint --actions actions      # starts the server that has custom actions
python dialogue_management_model.py                     # runs the bot