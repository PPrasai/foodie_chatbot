import logging
import tensorflow
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.run import serve_application
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)

def train_core_model():
	fallbackPolicy = FallbackPolicy(\
		fallback_action_name = 'action_default_fallback', 
		core_threshold = 0.2, 
		nlu_threshold = 0.6
	)
	
	agent = Agent(
		'./restaurant_domain.yml',
		policies = [
			MemoizationPolicy(max_history = 4),
			KerasPolicy(),
			fallbackPolicy
		]
	)

	data = agent.load('./data/stories.md')
	
	agent.train(
		data,
		epochs = 500,
		batch_size = 50,
		validation_split = 0.2
	)

	agent.persist('./models/dialogue')
	return agent


if __name__ == '__main__':
	interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
	action_endpoint = EndpointConfig(url = 'http://localhost:5055/webhook')
	
	agent = Agent.load(
		'./models/dialogue', 
		interpreter = interpreter,
		action_endpoint = action_endpoint
	)

	rasa_core.run.serve_application(agent, channel = 'cmdline')