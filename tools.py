import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = None


def load_dataset(path):
    global df
    df = pd.read_csv(path)
    return f"Dataset loaded: {df.shape}"


def dataset_summary():
    return df.describe().to_string()


def missing_values():
    return df.isnull().sum().to_string()


def correlation_heatmap():

    corr = df.corr(numeric_only=True)

    sns.heatmap(corr, annot=True)
    plt.savefig("heatmap.png")
    plt.close()

    return "Heatmap saved as heatmap.png"


def train_model():

    numeric_df = df.select_dtypes(include="number")

    target = numeric_df.columns[-1]

    X = numeric_df.drop(columns=[target])
    y = numeric_df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    return f"Model trained. R2 score: {score}"