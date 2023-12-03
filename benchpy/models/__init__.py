

from .common import Model, ModelConfig, SequenceModel, SequenceModelConfig
from .gnn import Gnn, GnnConfig
from .mlp import Mlp, MlpConfig

classes = ["Mlp", "MlpConfig", "Gnn", "GnnConfig"]

model_config_registry = {"mlp": MlpConfig, "gnn": GnnConfig}
