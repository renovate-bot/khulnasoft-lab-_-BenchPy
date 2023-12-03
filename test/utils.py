

import importlib

_has_vmas = importlib.util.find_spec("vmas") is not None
_has_smacv2 = importlib.util.find_spec("smacv2") is not None
_has_pettingzoo = importlib.util.find_spec("pettingzoo") is not None
