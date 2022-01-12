import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns




ticker = ["AMZN", "BA", "DIS", "IBM", "KO", "MSFT"]

stocks = yf.download(ticker, start = "2010-01-01", end = "2019-02-06")
stocks.to_csv("corr_stocks.csv")

stocks = pd.read_csv("corr_stocks.csv", header = [0, 1], index_col = [0], parse_dates = [0])
stocks.columns = stocks.columns.to_flat_index()
stocks.columns = pd.MultiIndex.from_tuples(stocks.columns)
stocks.swaplevel(axis = 1).sort_index(axis = 1)

close = stocks.loc[:, "Close"].copy()
ret = close.pct_change().dropna()

ret.corr()

plt.figure(figsize=(12,8))
sns.set(font_scale=1.4)
sns.heatmap(ret.corr(), cmap = "Greens_r", annot = True, annot_kws={"size":15}, vmax = 0.6)
plt.show()

