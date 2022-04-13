# %%
from pathlib import Path

import numpy as np
import pandas as pd

# %% [markdown]
# Not necessary anymore, because data will be extended in javascript

# fmt: off
# %%
def interp(x, y, count):
    step = (y - x) / count
    return [x + i * step for i in range(count)]


# %%
step = 10

# %%
path = Path(__file__).parent.absolute()
df = (
    pd
    .read_csv(path / "data" / "nasa.csv")
    .rename(columns=({"diff_temp": "diff_temp_before"}))
)

df["diff_temp_after"] = df["diff_temp_before"].shift(-1)
df["diff_temp"] = df.apply(
    lambda row: interp(row["diff_temp_before"], row["diff_temp_after"], step), axis=1
)
df = (
    df
    .explode("diff_temp", ignore_index=True)
    .dropna()
    .filter(["year", "month", "diff_temp"])
)

# %%
df["theta"] = np.arange(df.shape[0]) % (step * 12) / (step * 12) * 2 * np.pi

# %%
max_abs_diff_temp = df["diff_temp"].abs().max()
df["radius"] = np.interp(
    df["diff_temp"],
    (-max_abs_diff_temp, max_abs_diff_temp),
    (0, 1)
)

# %%
(
    df.
    reset_index()
    .to_csv(path / "app" / "static" / "data" / "nasa.csv", index=False)
)
