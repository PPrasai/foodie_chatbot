import logging

from rasa_core import utils, train
from rasa_core.training import interactive
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    
    interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
    action_endpoint = EndpointConfig(url = 'http://localhost:5055/webhook')
    agent = Agent.load(
        './models/dialogue', 
        interpreter = interpreter, 
        action_endpoint = action_endpoint
    )
    
    interactive.run_interactive_learning(agent)