import pandas as pd
from pathlib import Path

class DataReader:
    def __init__(self, basepath=None):
        self.base_path = Path(basepath) if basepath else Path(__file__).parent
        print(f"Base path: {self.base_path}")

    def ReadData(self):
        """
        Method that reads data from csv and Excel files.
        If there are additional variables that need to be analyzed, then there is need to add them here manually
        :return: Datasets of variables listed below:
            variables:
                -VIX
                -TenYear
                -SOFR
                -GDP
                -GNI
                -GNP
                -Unemployment
                -CPI
                -PPI
        """
        try:
            files = {
                "VIX": ("VIX_History.csv", "DATE"),
                #"TenYear": ("10y.xlsx", "Date"),
                "SOFR": ("SOFR.xlsx", "Effective Date"),
                "GDP": ("GDP.xlsx", "Period"),
                "GNI": ("GNI.xlsx", "Period"),
                "GNP": ("GNP.xlsx", "Period"),
                "Unemployment": ("Unemployment.xlsx", "Original Release Date"),
                "CPI": ("CPI.xlsx", "Original Release Date"),
                "PPI": ("PPI.xlsx", "Original Release Date"),
            }
            datasets = {}
            for name, (filename, date_col) in files.items():
                path = self.base_path / filename
                if filename.endswith(".csv"):
                    data = pd.read_csv(path, parse_dates=[date_col])
                else:
                    if name == "GDP":
                        data = pd.read_excel(path)
                        data["Date"] = pd.to_datetime(
                            data["Period"].str.extract(r"(\d{4})")[0] + "-" +
                            data["Period"].str.extract(r"Q(\d)")[0].map(
                                {"1": "03", "2": "06", "3": "09", "4": "12"}
                            ) + "-01",
                            format="%Y-%m-%d", errors="coerce"
                        )
                        data.drop(columns=["Period"], inplace=True)

                    else:
                        data = pd.read_excel(path)
                        if date_col in data.columns:
                            data["Date"] = pd.to_datetime(data[date_col], errors="coerce")
                            data.drop(columns=[date_col], inplace=True)  # Remove original date column
                datasets[name] = data
                print(f"Loaded {name} from {filename}")

            return datasets
        #exctioption that are thrown if there is an issue with loading the data. Check base path
        #if is correctly initialized, or add your own correct path to constructor of DataReader class
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
