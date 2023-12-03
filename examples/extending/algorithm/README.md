
# Creating a new algorithm

Here are the steps to create a new algorithm. You can find the custom IQL algorithm
created for this example in [`custom_agorithm.py`](custom_algorithm.py).

1. Create your `CustomAlgorithm` and `CustomAlgorithmConfig` following the example
in [`custom_agorithm.py`](custom_algorithm.py). These will be the algorithm code
and an associated dataclass to validate loaded configs.
2. Create a `customalgorithm.yaml` with the configuration parameters you defined 
in your script. Make sure it has `customalgorithm_config` within its defaults at 
the top of the file to let hydra know which python dataclass it is 
associated to. You can see [`customiqlalgorithm.yaml`](customiqlalgorithm.yaml)
for an example.
3. Place your algorithm script in [`benchpy/algorithms`](../../../benchpy/algorithms) and 
your config in [`benchpy/conf/algorithm`](../../../benchpy/conf/algorithm) (or any other place you want to 
override from)
4. Add `{"custom_agorithm": CustomAlgorithmConfig}` to the [`benchpy.algorithm.algorithm_config_registry`](../../../benchpy/algorithms/__init__.py)
5. Load it with
```bash
python benchpy/run.py algorithm=customalgorithm task=...
```
