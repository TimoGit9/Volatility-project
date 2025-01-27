import matplotlib.pyplot as plt
class DataPreprocessor:
    def __init__(self, datasets={}):
        self.datasets = datasets
        return

    def PrintTest(self):
        print("Data Preprocessor")
        #print(self.datasets["VIX"].head())
    def TestPD(self):
        print(f"Data Preprocessor", flush=True)
    def PlotData(self):
        fig, ax1 = plt.subplots(figsize=(12, 6))

        ax1.set_title("Stock Market Volatility vs. Macroeconomic Indicators")
        ax1.plot(self.datasets["VIX"].index, self.datasets["VIX"]['CLOSE'], color='blue', label='Volatility')
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Volatility", color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')

        fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
        plt.show()

    def Show(self, name):
        print(self.datasets[name].head())
        return

