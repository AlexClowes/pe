from importlib import import_module
import os

import pandas as pd
import pytest


csv_path = os.path.join(os.path.dirname(__file__), "answers.csv")
df = pd.read_csv(csv_path, dtype={"answer":str})
ids = [f"{n:03}" for n in df.values[:, 0]]


@pytest.mark.parametrize("problem_no, answer", df.values, ids=ids)
def test_problem_solution(problem_no, answer, capsys):
    import_module(f"{problem_no:03}").main()
    out, err = capsys.readouterr()
    assert out.strip() == answer
    assert err == ""
