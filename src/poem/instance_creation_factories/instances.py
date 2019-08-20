# -*- coding: utf-8 -*-

"""Implementation of basic instance factory which creates just instances based on standard KG triples."""

from dataclasses import dataclass
from typing import Mapping

import numpy as np

from .utils import Assumption
from ..typing import EntityMapping, MappedTriples, RelationMapping

__all__ = [
    'Instances',
    'OWAInstances',
    'CWAInstances',
    'MultimodalInstances',
    'MultimodalOWAInstances',
    'MultimodalCWAInstances',
]


@dataclass
class Instances:
    """Triples and mappings to their indices."""

    mapped_triples: MappedTriples
    entity_to_id: EntityMapping
    relation_to_id: RelationMapping

    @property
    def num_instances(self) -> int:  # noqa: D401
        """The number of instances."""
        return self.mapped_triples.shape[0]

    @property
    def num_entities(self) -> int:  # noqa: D401
        """The number of entities."""
        return len(self.entity_to_id)


@dataclass
class OWAInstances(Instances):
    """Triples and mappings to their indices for OWA."""

    assumption: Assumption = Assumption.open


@dataclass
class CWAInstances(Instances):
    """Triples and mappings to their indices for CWA."""

    labels: np.ndarray
    assumption: Assumption = Assumption.closed


@dataclass
class MultimodalInstances(Instances):
    """Triples and mappings to their indices as well as multimodal data."""

    numeric_literals: Mapping[str, np.ndarray]
    literals_to_id: Mapping[str, int]


@dataclass
class MultimodalOWAInstances(OWAInstances, MultimodalInstances):
    """Triples and mappings to their indices as well as multimodal data for OWA."""


@dataclass
class MultimodalCWAInstances(CWAInstances, MultimodalInstances):
    """Triples and mappings to their indices as well as multimodal data for CWA."""
