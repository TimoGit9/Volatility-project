# Volatility-project

## Installation
* requirements.txt specifies needed installs and Python version
* Please make sure you fulfill all requirements before continuing
* Download whole repository to your device 

## Description
Our project processes and analyses various macroeconomic data in the context of market volatility (approximated by VIX). Use Merged_Notebook.ipynb.

We let the user decide which data to plug in, but recommend using our tools to better capture relevant datasets. Our tools include PCA, correlation matrix, and correlation function. PCA preserves the most important variance in the data while assisting in the reduction of dimensionality. Our PCA study indicates that PC4 is the most associated with market volatility, as it exhibits the greatest association with VIX (0.4404). The U.S. 10-Year Treasury Yield, or DGS10, has the biggest impact on this component. PC1, PC2, and PC3 show lesser correlations (0.1646, 0.1595, and -0.1539, respectively), implying they reflect other macroeconomic trends but contribute less to predicting VIX. Based on PCA results alone, users may consider dropping the PPI indicator, as it adds minimal explanatory power to the model. Users can concentrate on the most instructive elements by using PCA, which lowers. Correlation matrix, where you can see correlations of various variables at the same time, and correlation function where you can quickly find correlation between 2 variables.

GARCH model can be used for volatility clustering, you can use it on any variable.

For better visualisation, we built interactive graph, where you can plug variables as per your liking. We also added a slider for you to be able to closely inspect different timeframes, and buttons for some of the most used timeframes. You are also able to create a snapshot of the graph when you reach to the upper right above the graph (alongside some other functions).

## Data
We provide datasets for some of the most popular macroeconomic indicators and market volatility. Time horizon is 10 years. Feel free to use your datasets if you wish, but make sure they are cleaned.
