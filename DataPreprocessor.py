import matplotlib.pyplot as plt
import pandas as pd
class DataPreprocessor:
    def __init__(self, datasets={}):
        self.datasets = datasets
        return

    def clean_gdp(self):
        """Cleans and processes the GDP dataset, ensuring monthly frequency with interpolation."""

        df = self.datasets.get("GDP")
        df = df[["Date", "GDP Final*.1"]].copy()
        df.columns = ["Date", "GDP_Final"]
        df["GDP_Final"] = pd.to_numeric(df["GDP_Final"], errors="coerce")
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.sort_values("Date", ascending=True, inplace=True)
        df.set_index("Date", inplace=True)
        start_date = df.index.min()
        end_date = df.index.max()
        df = df.reindex(pd.date_range(start=start_date, end=end_date, freq="MS"))
        df["GDP_Final"] = df["GDP_Final"].ffill(limit=2)
        df["GDP_Final"] = df["GDP_Final"].interpolate(method="linear")
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

    import pandas as pd

    def clean_VIX(self):
        """Cleans and processes the VIX dataset, ensuring that the value for each month
        is based on the last available trading day of that month."""

        df = self.datasets.get("VIX")
        df.loc[:, "DATE"] = pd.to_datetime(df["DATE"], format="%m/%d/%Y", errors="coerce")
        df = df[df["DATE"].dt.year >= 2015].copy()
        df.sort_values("DATE", ascending=True, inplace=True)
        df["Month"] = df["DATE"].dt.to_period("M")
        df_monthly = df.groupby("Month").last()[["DATE", "CLOSE"]].copy()
        df_monthly.index = df_monthly.index.to_timestamp()
        df_monthly = df_monthly[["CLOSE"]]
        df_monthly.columns = ["VIX"]
        self.datasets["VIX"] = df_monthly

    def clean_CPI(self):
        df = self.datasets.get("CPI")
        df = df[["Period", "First Release"]].copy()
        df.columns = ["Period", "CPI"]
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
        df["CPI"] = pd.to_numeric(df["CPI"], errors="coerce")
        df.sort_values("Date", ascending=True, inplace=True)
        df.set_index("Date", inplace=True)
        self.datasets["CPI"] = df

    def clean_PPI(self):
        def change_calculation(df):
            df['Value'] = (df['PPI'] - df['PPI'].shift(-1))
            df['Value'] = df['Value'].fillna(0)
            return df
        df = self.datasets.get("PPI")
        df = df[["Period", "First Release"]].copy()
        df.columns = ["Period", "PPI"]
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
        df["PPI"] = pd.to_numeric(df["PPI"], errors="coerce")
        df.sort_values("Date", ascending=True, inplace=True)
        df.set_index("Date", inplace=True)
        df = change_calculation(df)
        self.datasets["PPI"] = df


    def SetSameInterval(self):
        """Cleans all datasets, checks for misalignments, and merges them into a single DataFrame by Date."""
        self.clean_gdp()
        self.clean_Unemployment()
        self.clean_VIX()
        self.clean_CPI()
        self.clean_PPI()

        datasets_to_merge = ["GDP", "Unemployment", "VIX", "CPI", "PPI"]
        dataframes = {}

        for dataset_name in datasets_to_merge:
            df = self.datasets.get(dataset_name)
            dataframes[dataset_name] = df

        df_merged = pd.concat(dataframes.values(), axis=1, join="inner")
        df_merged.sort_index(inplace=True)

        self.datasets["Merged"] = df_merged

        return df_merged
