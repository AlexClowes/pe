from importlib import import_module
import os

import pandas as pd
import pytest


csv_path = os.path.join(os.path.dirname(__file__), "answers.csv")
df = pd.read_csv(csv_path)
ids = [f"{n:02}" for n in df.values[:, 0]]



@pytest.mark.parametrize("problem_no, answer", df.values, ids=ids)
def test_problem_solution(problem_no, answer, capsys):
    import_module(f"{problem_no:02}").main()
    out, err = capsys.readouterr()
    assert out.strip() == str(answer)
    assert err == ""
