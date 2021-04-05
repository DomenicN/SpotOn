from fastspt.fastspt import *
from .version import _version_

import fastspt.fastSPT_tools, fastspt.readers, fastspt.writers
try:
	import fastspt.fastSPT_plot
except Exception as e:
	print("Could not import the plot submodule, error:")
	print(e)
