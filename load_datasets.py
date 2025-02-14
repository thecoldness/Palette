import kagglehub

# Download latest version
path = kagglehub.dataset_download("datasets/celebahq")

print("Path to dataset files:", path)