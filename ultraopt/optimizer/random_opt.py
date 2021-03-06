#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com

import numpy as np

from ultraopt.optimizer.base_opt import BaseOptimizer


class RandomOptimizer(BaseOptimizer):

    def new_result_(self, budget, vectors: np.ndarray, losses: np.ndarray):
        pass

    def get_config_(self, budget, max_budget):
        return self.pick_random_initial_config(budget, origin="Random Search")

    def get_available_max_budget(self):
        for budget in reversed(sorted(self.budgets)):
            if self.budget2obvs[budget]["losses"]:
                return budget
        return self.budgets[0]
