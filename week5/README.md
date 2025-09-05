## 🏡 Project Overview

This week's assignment focused on the critical initial phase of a machine learning project: data preprocessing and feature engineering. Using the popular Ames Housing dataset, the goal was to prepare the data for a future house price prediction model.

The process involved handling missing values, creating new, more informative features from existing ones, and converting categorical data into a numerical format suitable for machine learning algorithms.

## 📚 Key Concepts & Techniques

This project covers several fundamental data science techniques:

* **Missing Value Imputation:** Filling in missing data points using statistical measures (median for numerical features, mode for categorical features).
* **Feature Engineering:** Creating new features to improve model accuracy. This includes combining existing features and deriving features based on domain knowledge (e.g., calculating the age of the house).
* **Categorical Data Encoding:**
    * **Ordinal Encoding:** Manually mapping categorical features with an inherent order (like quality ratings) to numerical values.
    * **One-Hot Encoding:** Converting nominal (non-ordered) categorical features into a set of binary columns.
* **Correlation Analysis:** Using a heatmap to visualize the relationship between various features and the target variable (`SalePrice`).

## 🛠️ Tools & Libraries Used

* **Language:** `Python`
* **Libraries:** `Pandas`, `NumPy`, `Seaborn`, `Matplotlib`
* **Environment:** `Jupyter Notebook`

## ⚙️ Workflow

The data preparation process was executed in the following steps:

1.  **Data Loading & Inspection:** The `train.csv` and `test.csv` datasets were loaded, and their initial shapes and columns were inspected. A significant number of columns with missing values were identified.

2.  **Missing Value Imputation:**
    * Numerical columns with missing values were filled using the **median** value of each respective column.
    * Categorical columns were filled using the **mode** (the most frequent value).

3.  **Feature Engineering:** To capture more information, several new features were created:

    ```python
    # Create new features
    train['TotalBathrooms'] = (train['FullBath'] + (0.5 * train['HalfBath']) +
                               train['BsmtFullBath'] + (0.5 * train['BsmtHalfBath']))

    train['HouseAge'] = train['YrSold'] - train['YearBuilt']
    train['RemodAge'] = train['YrSold'] - train['YearRemodAdd']
    train['TotalSF'] = train['TotalBsmtSF'] + train['1stFlrSF'] + train['2ndFlrSF']
    ```

4.  **Categorical Encoding:**
    * **Ordinal Features:** Features with a clear order, like `ExterQual` (Exterior Quality), were manually mapped to numbers (e.g., 'Ex': 5, 'Gd': 4).
    * **Nominal Features:** The remaining categorical columns were one-hot encoded using `pd.get_dummies()`, creating binary columns for each category.

## 📊 Visualizations

After cleaning the data, visualizations were created to better understand the target variable and its relationship with other features.

#### Sale Price Distribution
A histogram was plotted to check the distribution of `SalePrice`. The distribution is right-skewed, which is common for price data.


#### Feature Correlation with Sale Price
A heatmap was used to visualize which features are most strongly correlated with `SalePrice`. Features like `OverallQual`, `TotalSF`, and `GrLivArea` show a high positive correlation.


## 📈 Outcome

After all preprocessing steps, the final training dataset was transformed from its original shape of `(1460, 81)` to `(1460, 248)`. The significant increase in columns is due to one-hot encoding. The dataset is now entirely numerical and clean, making it ready for training a machine learning model.
