# -*- coding: utf-8 -*-

# Copyright 2018 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Provide fixtures for test modules in ``tests.test_for_experimental``."""

from __future__ import absolute_import

from os.path import dirname, join

import pytest

from memote.experimental.experimental_base import ExperimentalBase
from memote.experimental.medium import Medium
from memote.experimental.experiment import Experiment
from memote.experimental.essentiality import EssentialityExperiment
from memote.experimental.growth import GrowthExperiment

DATA_PATH = join(dirname(__file__), "data")


@pytest.fixture(scope="module", params=[
    ExperimentalBase,
    Medium,
    Experiment,
    EssentialityExperiment,
    GrowthExperiment
])
def klass(request):
    return request.param
