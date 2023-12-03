import torch.nn

from benchpy.algorithms import MappoConfig
from benchpy.environments import VmasTask
from benchpy.experiment import Experiment, ExperimentConfig
from benchpy.models.common import SequenceModelConfig
from benchpy.models.mlp import MlpConfig


if __name__ == "__main__":

    model_config = SequenceModelConfig(
        model_configs=[
            MlpConfig.get_from_yaml(),  # Loads from "benchpy/conf/model/layers/mlp.yaml"
            MlpConfig(  # This one we specify ourselves
                num_cells=[4],  # One layer with 4 neurons
                activation_class=torch.nn.Tanh,  # Tanh activation
                layer_class=torch.nn.Linear,  # Linear layer class
            ),
        ],
        intermediate_sizes=[
            5
        ],  # Nuber of intermediate outputs. List of size n_layers - 1
    )

    # Some basic other configs
    task = VmasTask.BALANCE.get_from_yaml()
    algorithm_config = MappoConfig.get_from_yaml()
    experiment_config = ExperimentConfig.get_from_yaml()
    critic_model_config = MlpConfig.get_from_yaml()

    experiment = Experiment(
        task=task,
        algorithm_config=algorithm_config,
        model_config=model_config,
        critic_model_config=critic_model_config,
        seed=0,
        config=experiment_config,
    )
    experiment.run()
