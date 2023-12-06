class RoleFunction:
    def __init__(self):
        self.OHQ = 0
        self.KHQ = 0
        self.HQ = 0

class Fuzzy_Role_Base:
    """
    self.index_profit : {
        0: 'TST',
        1: 'TSTB',
        2: 'TSC'
    }
    self.index_cost : {
        0: 'CPT',
        1: 'CPTB',
        2: 'CPC'
    }
    self.index_time : {
        0: 'TGN',
        1: 'TGTB',
        2: 'TGD'
    }
    self.label : {
        0: 'OHQ',
        1: 'KHQ',
        2: 'HQ'
    }
    """
    def __init__(self, index_profit, index_cost, index_time, label):
        self.index_profit = index_profit
        self.index_cost = index_cost
        self.index_time = index_time
        self.label = label

    def update_role_function(self, fuzzy):
        if fuzzy.μ_profit[self.index_profit] and fuzzy.μ_cost[self.index_cost] and fuzzy.μ_time[self.index_time]:
            value = min(fuzzy.μ_profit[self.index_profit], fuzzy.μ_cost[self.index_cost], fuzzy.μ_time[self.index_time])
            if self.label == 0:
                fuzzy.role_function.OHQ = max(fuzzy.role_function.OHQ, value)
            elif self.label == 1:
                fuzzy.role_function.KHQ = max(fuzzy.role_function.KHQ, value)
            else:
                fuzzy.role_function.HQ = max(fuzzy.role_function.HQ, value)

class Fuzzy:
    def __init__(self, profit, cost, time):
        self.μ_profit = self._fuzzifier_profit(profit)
        self.μ_cost = self._fuzzifier_cost(cost)
        self.μ_time = self._fuzzifier_time(time)
        self.fuzzy_role_base = [
            Fuzzy_Role_Base(0, 0, 0, 1),
            Fuzzy_Role_Base(0, 0, 1, 1),
            Fuzzy_Role_Base(0, 0, 2, 0),
            Fuzzy_Role_Base(0, 1, 0, 1),
            Fuzzy_Role_Base(0, 1, 1, 0),
            Fuzzy_Role_Base(0, 1, 2, 0),
            Fuzzy_Role_Base(0, 2, 0, 0),
            Fuzzy_Role_Base(0, 2, 1, 0),
            Fuzzy_Role_Base(0, 2, 2, 0),
            Fuzzy_Role_Base(1, 0, 0, 2),
            Fuzzy_Role_Base(1, 0, 1, 2),
            Fuzzy_Role_Base(1, 0, 2, 1),
            Fuzzy_Role_Base(1, 1, 0, 2),
            Fuzzy_Role_Base(1, 1, 1, 1),
            Fuzzy_Role_Base(1, 1, 2, 0),
            Fuzzy_Role_Base(1, 2, 0, 1),
            Fuzzy_Role_Base(1, 2, 1, 0),
            Fuzzy_Role_Base(1, 2, 2, 0),
            Fuzzy_Role_Base(2, 0, 0, 2),
            Fuzzy_Role_Base(2, 0, 1, 2),
            Fuzzy_Role_Base(2, 0, 2, 2),
            Fuzzy_Role_Base(2, 1, 0, 2),
            Fuzzy_Role_Base(2, 1, 1, 2),
            Fuzzy_Role_Base(2, 1, 2, 1),
            Fuzzy_Role_Base(2, 2, 0, 2),
            Fuzzy_Role_Base(2, 2, 1, 1),
            Fuzzy_Role_Base(2, 2, 2, 1),
        ]
        
        self.role_function = None
        self.investment_index = None

    @staticmethod
    def _fuzzifier_profit(profit):
        μ_low = lambda x: 1 if x < 20 else ((60 - x) / (60 - 20)) if 20 <= x <= 60 else 0
        μ_medium = lambda x: 0 if x < 0 else (x / 30) if 0 <= x < 30 else 1 if 30 <= x < 50 else ((100 - x) / (100 - 50)) if 50 <= x <= 100 else 0
        μ_high = lambda x: 0 if x < 20 else (x - 20) / (60 - 20) if 20 <= x <= 60 else 1
        return (μ_low(profit), μ_medium(profit), μ_high(profit))

    @staticmethod
    def _fuzzifier_cost(cost):
        μ_low = lambda x: 1 if x < 30 else (500 - x) / (500 - 30) if 30 <= x <= 500 else 0
        μ_medium = lambda x: 0 if x < 30 else (x - 30) / (100 - 30) if 30 <= x < 100 else 1 if 100 <= x < 150 else (500 - x) / (500 - 150) if 150 <= x <= 500 else 0
        μ_high = lambda x: 0 if x < 65 else (x - 65) / (500 - 65) if 65 <= x <= 500 else 1
        return (μ_low(cost), μ_medium(cost), μ_high(cost))

    @staticmethod
    def _fuzzifier_time(time):
        μ_short = lambda x: 1 if x < 3 else (18 - x) / (18 - 3) if 3 <= x <= 18 else 0
        μ_medium = lambda x: 0 if x < 3 else (x - 3) / (6 - 3) if 3 <= x < 6 else 1 if 6 <= x < 9 else (18 - x) / (18 - 9) if 9 <= x <= 18 else 0
        μ_long = lambda x: 0 if x < 3 else (x - 3) / (18 - 3) if 3 <= x <= 18 else 1
        return (μ_short(time), μ_medium(time), μ_long(time))
    
    def inference(self):
        self.role_function = RoleFunction()
        for fuzzy_role_base in self.fuzzy_role_base:
            fuzzy_role_base.update_role_function(self)
    
    def defuzzifier(self):
        if not self.role_function or self.role_function == RoleFunction():
            self.investment_index = 0
        else:
            self.investment_index = (self.role_function.OHQ * 2 + self.role_function.KHQ * 4 + self.role_function.HQ * 7.5) / (self.role_function.OHQ + self.role_function.KHQ + self.role_function.HQ)

    def __str__(self):
        return "{:.2f}/10".format(self.investment_index) if self.investment_index else "unknown"
