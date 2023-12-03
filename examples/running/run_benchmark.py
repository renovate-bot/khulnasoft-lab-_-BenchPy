

from benchpy.algorithms import MappoConfig, MasacConfig, QmixConfig
from benchpy.benchmark import Benchmark
from benchpy.environments import VmasTask
from benchpy.experiment import ExperimentConfig
from benchpy.models.mlp import MlpConfig

if __name__ == "__main__":

    # Loads from "benchpy/conf/experiment/base_experiment.yaml"
    experiment_config = ExperimentConfig.get_from_yaml()

    # Loads from "benchpy/conf/task/vmas"
    tasks = [VmasTask.BALANCE.get_from_yaml(), VmasTask.SAMPLING.get_from_yaml()]

    # Loads from "benchpy/conf/algorithm"
    algorithm_configs = [
        MappoConfig.get_from_yaml(),
        QmixConfig.get_from_yaml(),
        MasacConfig.get_from_yaml(),
    ]

    # Loads from "benchpy/conf/model/layers"
    model_config = MlpConfig.get_from_yaml()
    critic_model_config = MlpConfig.get_from_yaml()

    benchmark = Benchmark(
        algorithm_configs=algorithm_configs,
        tasks=tasks,
        seeds={0, 1},
        experiment_config=experiment_config,
        model_config=model_config,
        critic_model_config=critic_model_config,
    )
    benchmark.run_sequential()
