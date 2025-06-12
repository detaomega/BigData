import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_and_export(input_csv: str, output_csv: str, n_clusters: int):
    df = pd.read_csv(input_csv)
    
    if 'id' in df.columns:
        ids = df['id']
        features = df.drop(columns=['id'])
    else:
        ids = None
        features = df

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    # KMeans 分群
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    labels = model.fit_predict(X_scaled)

    # 輸出格式為 id + cluster label
    if ids is not None:
        result = pd.DataFrame({'id': ids, 'label': labels})
    else:
        result = pd.DataFrame({'label': labels})
        result.insert(0, 'id', range(1, len(labels)+1))

    result.to_csv(output_csv, index=False)

if __name__ == "__main__":
    cluster_and_export(
        input_csv="public_data.csv",
        output_csv="public_submission.csv",
        n_clusters=15
    )

    cluster_and_export(
        input_csv="private_data.csv",
        output_csv="private_submission.csv",
        n_clusters=23
    )
