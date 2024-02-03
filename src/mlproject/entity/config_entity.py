from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen= True)
class DataIngestionConfig:        # written type : told my method to  return these four variables
    root_dir: Path
    source_URL: str
    local_data_file: Path
   
    unzip_dir: Path









@dataclass(frozen = True)
class DatavalidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict