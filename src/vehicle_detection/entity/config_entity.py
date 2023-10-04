## Create data classes to consider from data ingestion Configs
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    zip_file_dir: Path
    dataset_source: Path