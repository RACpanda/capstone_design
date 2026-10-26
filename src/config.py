from pathlib import Path


# 프로젝트 최상위 폴더
BASE_DIR = Path(__file__).resolve().parent.parent

# 원본 EEG 데이터 위치
DATA_DIR = BASE_DIR / "SeizeIT2" / "sub-001" / "ses-01" / "eeg"

# 분석 결과 저장 위치
OUTPUT_DIR = BASE_DIR / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"
TABLES_DIR = OUTPUT_DIR / "tables"
