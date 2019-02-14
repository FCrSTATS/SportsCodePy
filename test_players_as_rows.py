
import pytest

import SportsCodePy

import pandas as pd

lst1 = ["Spurs", "WBA", "Spurs", "Spurs", "WBA"]
lst2 = [200, 300, 400, 500, 600]
lst3 = [210, 320, 405, 507, 616]
lst4 = [1, 1, 1, 1, 1]
lst5 = [0.29, 0.45, 0.64, 0.34, 0.11]
lst6 = ["Ali", "Moore", "Kane", "Erikssen", "Moore"]
lst7 = [13, 45, 536, 600, 723]

test_df = pd.DataFrame(
    {'team_name': lst1,
     'start': lst2,
     'end': lst3,
     'period_id': lst4,
     'xGChain': lst5,
     'player_name': lst6,
     'time': lst7
    })


def.test_players_as_rows():
    result_statement = SportsCodePy.players_as_rows(test_df, 40, 2500, "player_name",
             "team_name", "time", 3, 3, "xGChain",
             "period_id", "ID", "xGChain", "new_test_players_.xml")
    assert result_statement == "XML created successfully"
