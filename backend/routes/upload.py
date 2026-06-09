from fastapi import APIRouter, UploadFile, File
import pandas as pd
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Save latest uploaded file
    with open(
        "uploads/current_file.txt",
        "w"
    ) as f:
        f.write(file.filename)

    df = pd.read_csv(file_path)

    if "Unnamed: 0" in df.columns:
        df.drop(
            columns=["Unnamed: 0"],
            inplace=True
        )

    if "city" in df.columns:
        df["city"] = (
            df["city"]
            .astype(str)
            .str.strip()
            .str.title()
        )

    missing_values = (
        df.isnull()
        .sum()
        .to_dict()
    )

    numerical_columns = (
        df.select_dtypes(
            include=["int64", "float64"]
        )
        .columns
        .tolist()
    )

    categorical_columns = (
        df.select_dtypes(
            include=["object"]
        )
        .columns
        .tolist()
    )

    insights = []

    total_missing = int(
        df.isnull().sum().sum()
    )

    if total_missing > 0:
        insights.append(
            f"Dataset contains {total_missing} missing values."
        )

    insights.append(
        f"{len(numerical_columns)} numerical columns detected."
    )

    insights.append(
        f"{len(categorical_columns)} categorical columns detected."
    )

    return {
        "filename": file.filename,
        "rows": len(df),
        "columns": len(df.columns),
        "status": "profiled"
    }