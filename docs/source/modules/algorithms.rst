
benchpy.algorithms
====================

.. currentmodule:: benchpy.algorithms

.. contents:: Contents
    :local:

Here you can find the :ref:`algorithm table <algorithm-table>`.

Common
------

.. autosummary::
   :nosignatures:
   :toctree: ../generated
   :template: autosummary/class_private.rst

   Algorithm
   AlgorithmConfig

Algorithms
----------

.. autosummary::
   :nosignatures:
   :toctree: ../generated
   :template: autosummary/class_private.rst

   {% for name in benchpy.algorithms.classes %}
     {{ name }}
   {% endfor %}
