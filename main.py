# main.py
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_and_export(input_csv, output_csv, n_clusters):
    df = pd.read_csv(input_csv)
    X = df.drop(columns=["id"])

    # Z-score normalization
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
    labels = kmeans.fit_predict(X_scaled)

    # Output result
    result = pd.DataFrame({
        "id": df["id"],
        "label": labels
    })
    result.to_csv(output_csv, index=False)
    print(f"Saved: {output_csv}")

if __name__ == "__main__":

    cluster_and_export(
        input_csv="public_data.csv",
        output_csv=f"public_submission.csv",
        n_clusters=15
    )

    cluster_and_export(
        input_csv="private_data.csv",
        output_csv=f"private_submission.csv",
        n_clusters=23
    )
