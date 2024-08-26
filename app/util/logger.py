import sys
from logging import Logger, Formatter, StreamHandler, INFO, ERROR, DEBUG

class BotLogger(Logger):
	def __init__(self, name: str = __name__, level: int = INFO):
		# Initialize the base
		super().__init__(name, level)

		# Personalize
		formatter = Formatter("%(name)s - %(levelname)s - %(asctime)s: %(message)s")
		handler = StreamHandler(sys.stdout)
		handler.setFormatter(formatter)
		self.addHandler(handler)
