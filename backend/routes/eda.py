from fastapi import APIRouter, HTTPException
import pandas as pd
import os
import matplotlib.pyplot as plt

from services.chart_service import (
generate_missing_chart
)

router = APIRouter()

@router.get("/eda-report")
async def eda_report():
    try:
        with open(
            "uploads/current_file.txt",
            "r"
        ) as f:
            latest_file = (
                f.read()
                .strip()
            )
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="No file uploaded yet."
        )

    file_path = (
        f"uploads/{latest_file}"
    )

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="Uploaded file not found."
        )

    df = pd.read_csv(file_path)

    if "Unnamed: 0" in df.columns:
        df.drop(
            columns=["Unnamed: 0"],
            inplace=True
        )

    report = {
        "filename": latest_file,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": (
            df.columns.tolist()
        ),
        "missing_values": (
            df.isnull()
            .sum()
            .to_dict()
        )
    }

    # Revenue (only if exists)
    if (
        "quantity" in df.columns and
        "price_per_unit" in df.columns
    ):
        revenue = (
            df["quantity"].fillna(0)
            * df["price_per_unit"]
        ).sum()
        report["total_revenue"] = float(
            revenue
        )
    else:
        report["total_revenue"] = 0

    # Charts
    report["charts"] = []

    generate_missing_chart(df)

    report["charts"].append(
        "reports/missing_values.png"
    )

    categorical_cols = (
        df.select_dtypes(
            include=["object"]
        )
        .columns
        .tolist()
    )

    if len(categorical_cols) > 0:
        col = categorical_cols[0]

        plt.figure(
            figsize=(8, 4)
        )

        (
            df[col]
            .astype(str)
            .value_counts()
            .head(10)
            .plot(kind="bar")
        )

        plt.title(
            f"Top {col}"
        )

        plt.tight_layout()

        chart_path = (
            f"reports/{col}_distribution.png"
        )

        plt.savefig(
            chart_path
        )

        plt.close()

        report["charts"].append(
            chart_path
        )

    report["charts_generated"] = True

    # Insights
    insights = []

    total_missing = int(
        df.isnull()
        .sum()
        .sum()
    )

    insights.append(
        f"Dataset contains {total_missing} missing values."
    )

    insights.append(
        f"Dataset has {len(df.columns)} columns."
    )

    insights.append(
        f"Dataset contains {len(df)} rows."
    )

    report["insights"] = insights

    return report

