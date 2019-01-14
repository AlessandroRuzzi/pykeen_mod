# -*- coding: utf-8 -*-

"""Test pipeline module."""

import unittest

import json

from pykeen.constants import SEED, PREFERRED_DEVICE, HPO_MODE, EXECUTION_MODE, TRAINING_MODE, TEST_SET_PATH, \
    TEST_SET_RATIO, TRAINING_SET_PATH, KG_EMBEDDING_MODEL_NAME, TRANS_E_NAME, EMBEDDING_DIM
from pykeen.utilities.pipeline import Pipeline, CPU



CONFIG = {
    SEED:2,
    PREFERRED_DEVICE: CPU
}

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.config = CONFIG
        self.p = Pipeline(config=self.config)

    def test_instantiate_pipeline(self):
        """Test that Pipeline can be instantiated."""
        p = Pipeline(config=CONFIG)
        self.assertIsNotNone(p)

    def test_use_hpo(self):
        """Test whether execution mode is identified correctly."""
        self.p.config[EXECUTION_MODE] = HPO_MODE
        value = self.p._use_hpo(config=self.p.config)
        self.assertTrue(value)

        self.p.config[EXECUTION_MODE] = TRAINING_MODE
        value = self.p._use_hpo(config=self.p.config)
        self.assertFalse(value)

    def test_is_evaluation_required(self):
        """Test whether evaluation option is identified correctly."""
        self.p.config[TEST_SET_PATH] = '/test/path'
        value = self.p.is_evaluation_required
        self.assertTrue(value)

        del self.p.config[TEST_SET_PATH]

        self.p.config[TEST_SET_RATIO] = 0.1
        value = self.p.is_evaluation_required
        self.assertTrue(value)

        del self.p.config[TEST_SET_RATIO]

        value = self.p.is_evaluation_required
        self.assertFalse(value)

    def test_run(self):
        config_path = '../test_resources/configuration.json'

        with open(config_path) as json_data:
            config = json.load(json_data)

        self.p.config = config
        results = self.p.run()
        self.assertIsNotNone(results)


