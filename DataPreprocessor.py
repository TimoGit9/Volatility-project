import matplotlib.pyplot as plt
import pandas as pd
class DataPreprocessor:
    def __init__(self, datasets={}):
        self.datasets = datasets
        return

    def clean_gdp(self):
        """Cleans and processes the GDP dataset."""

        df = self.datasets.get("GDP")
        df = df[["Date", "GDP Final*.1"]].copy()
        df.columns = ["Date", "GDP_Final"]
        df["GDP_Final"] = pd.to_numeric(df["GDP_Final"], errors="coerce")
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.sort_values("Date", ascending=True, inplace=True)
        df.set_index("Date", inplace=True)
        df["GDP_Final"] = df["GDP_Final"].ffill()
        self.datasets["GDP"] = df
    def clean_Unemployment(self):
        """Cleans and processes the SOFR dataset."""
        df = self.datasets.get("Unemployment")

        df = df[["Period", "First Release"]].copy()
        df.columns = ["Period", "Unemployment_Rate"]
        df["Date"] = pd.to_datetime(
            df["Period"].str.extract(r'([A-Za-z]+) (\d{4})').apply(
                lambda x: x[1] + "-" +
                          {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
                           "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}[x[0]]
                          + "-01", axis=1
            ),
            format="%Y-%m-%d",
            errors="coerce"
        )
        df.drop(columns=["Period"], inplace=True)
        df["Unemployment_Rate"] = pd.to_numeric(df["Unemployment_Rate"], errors="coerce")
        df.sort_values("Date", ascending=True, inplace=True)
        df.set_index("Date", inplace=True)
        self.datasets["Unemployment"] = df


    def SetSameInterval(self):
        self.clean_gdp()
        self.clean_Unemployment()



