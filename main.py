import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.preprocessing import StandardScaler


def read_and_preprocess(input_csv: str):
    df = pd.read_csv(input_csv)
    
    if 'id' in df.columns:
        ids = df['id']
        features = df.drop(columns=['id'])
    else:
        ids = pd.Series(range(1, len(df) + 1))
        features = df

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    return ids, features_scaled, features.shape[1]


def cluster_and_export(input_csv: str, output_csv: str):
    ids, features_scaled, n_dims = read_and_preprocess(input_csv)
    n_clusters = 4 * n_dims - 1


    model = KMeans(n_clusters=n_clusters, random_state=40)

    labels = model.fit_predict(features_scaled)

    result = pd.DataFrame({'id': ids, 'label': labels})
    result.to_csv(output_csv, index=False)

if __name__ == "__main__":
    cluster_and_export("public_data.csv", "public_submission.csv")
    cluster_and_export("private_data.csv", "private_submission.csv")
