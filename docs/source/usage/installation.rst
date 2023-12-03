Installation
============


Install TorchRL
---------------

You can install :torchrl:`null` `TorchRL <https://github.com/pytorch/rl>`__ from PyPi.

.. code-block:: console

   pip install torchrl

For more details, or for installing nightly versions, see the
`TorchRL installation guide <https://github.com/pytorch/rl#installation>`__.

Install BenchPy
-----------------

You can just install it from github

.. code-block:: console

   pip install benchpy

Or also clone it locally to access the configs and scripts

.. code-block:: console

    git clone https://github.com/khulnasoft-lab/BenchPy.git
    pip install -e BenchPy

Install environments
--------------------

All enviornment dependencies are optional in BenchPy and can be installed separately.

VMAS
^^^^
:github:`null` `GitHub <https://github.com/proroklab/VectorizedMultiAgentSimulator>`__

.. code-block:: console

   pip install vmas

PettingZoo
^^^^^^^^^^
:github:`null` `GitHub <https://github.com/Farama-Foundation/PettingZoo>`__


.. code-block:: console

   pip install "pettingzoo[all]"


SMACv2
^^^^^^
:github:`null` `GitHub <https://github.com/oxwhirl/smacv2>`_


Follow the instructions on the environment `repository <https://github.com/oxwhirl/smacv2>`_.

`Here <https://github.com/khulnasoft-lab/BenchPy/blob/main/.github/unittest/install_smacv2.sh>`_
is how we install it on linux.

Install models
--------------

Some models in BenchPy require extra dependencies that can be installed separately


GNN
^^^

GNN models require :pyg:`null` `pytorch_geometric <https://pytorch-geometric.readthedocs.io/>`__.

To install it, you can run:

.. code-block:: console

   pip install torch_geometric

For more information, see the `installation <https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html>`__ instructions of the library.
