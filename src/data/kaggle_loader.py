import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


class KaggleStockLoader:

    def __init__(self,
                 dataset="jacksoncrow/stock-market-dataset",
                 output_dir="data/external"):
        self.dataset = dataset
        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)

    def authenticate(self):
        api = KaggleApi()
        api.authenticate()
        return api

    def download(self):
        api = self.authenticate()

        print("Downloading Kaggle dataset...")

        api.dataset_download_files(
            self.dataset,
            path=self.output_dir,
            unzip=False
        )

        print("Download complete.")

    def extract(self):
        zip_path = os.path.join(self.output_dir, "stock-market-dataset.zip")

        print("Extracting dataset...")

        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(self.output_dir)

        print("Extraction complete.")
