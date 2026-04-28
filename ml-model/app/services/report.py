import pandas as pd
import time


def generate_excel_report(results, filename=None):
    """
    Generate Excel report from results and return file path
    """

    # ✅ Create unique filename if not provided
    if filename is None:
        filename = f"report_{int(time.time())}.xlsx"

    # ✅ Convert to DataFrame
    df = pd.DataFrame(results)

    # ✅ Select and order columns
    columns_order = [
        "rank",
        "final_score",
        "ml_score",
        "keyword_score",
        "status",
        "suggested_role",
        "experience_years",
        "category",
        "matching_skills",
        "missing_skills"
    ]

    # Keep only existing columns
    columns_order = [col for col in columns_order if col in df.columns]
    df = df[columns_order]

    # ✅ Convert list fields to string (important for Excel readability)
    if "matching_skills" in df.columns:
        df["matching_skills"] = df["matching_skills"].apply(
            lambda x: ", ".join(x) if isinstance(x, list) else ""
        )

    if "missing_skills" in df.columns:
        df["missing_skills"] = df["missing_skills"].apply(
            lambda x: ", ".join(x) if isinstance(x, list) else ""
        )

    # ✅ Save Excel file
    df.to_excel(filename, index=False)

    return filename