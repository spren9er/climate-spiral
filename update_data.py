# %%
import duckdb
import pandas as pd

# %%
con = duckdb.connect(database=":memory:", read_only=False)
df = con.read_csv(
    "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv",
    skiprows=1,
    header=True,
)

# %%
monthly_df = pd.melt(
    df.select(
        "Year",
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ).to_df(),
    id_vars="Year",
    var_name="Month",
    value_name="Temperature",
)
monthly_df.rename(
    columns={"Year": "year", "Month": "month", "Temperature": "diff_temp"}, inplace=True
)
month_mapping = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}
monthly_df["month"] = monthly_df["month"].map(month_mapping)
monthly_df.sort_values(["year", "month"], inplace=True)

# %%
monthly_df.query("diff_temp != '***'").to_csv(
    "app/static/data/data.csv", index=False, header=True
)
