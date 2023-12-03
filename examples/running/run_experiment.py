from benchpy.algorithms import MappoConfig
from benchpy.environments import VmasTask
from benchpy.experiment import Experiment, ExperimentConfig
from benchpy.models.mlp import MlpConfig

if __name__ == "__main__":

    # Loads from "benchpy/conf/experiment/base_experiment.yaml"
    experiment_config = ExperimentConfig.get_from_yaml()

    # Loads from "benchpy/conf/task/vmas/balance.yaml"
    task = VmasTask.BALANCE.get_from_yaml()

    # Loads from "benchpy/conf/algorithm/mappo.yaml"
    algorithm_config = MappoConfig.get_from_yaml()

    # Loads from "benchpy/conf/model/layers/mlp.yaml"
    model_config = MlpConfig.get_from_yaml()
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
