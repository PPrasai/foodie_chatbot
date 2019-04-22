from rasa_core import train, utils

import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
	
	train.train_dialogue_model(
		domain_file = 'restaurant_domain.yml',
		stories_file = 'data/stories.md',
		output_path = 'models/dialogue',
		policy_config = 'core_policies.yml',
		kwargs = {
			'augmentation_factor': 50,
			'validation_split': 0.2
		}
	)

	utils.configure_colored_logging(loglevel = 'INFO')