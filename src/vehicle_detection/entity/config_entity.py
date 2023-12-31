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
    coordinates_path: Path
    yolo_conversion_image_size: list
    yolo_voc_bbx: list
    coordinates_target_path: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_link: str
    base_model_path: Path
    params_image_size: int
    params_batch: int
    params_epochs: int
    params_classes: list