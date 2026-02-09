"""
Build Defects Dashboard from all zResults.csv files under the workspace.
Scans for *_zResults.csv, aggregates failures (Result=Fail), classifies defect types,
and writes z/zDefectsDashboard.html.

Place zDefects.py in the main folder or in the z folder.
Run: python zDefects.py  (from the main folder) or  python z/zDefects.py

The dashboard will be written to z/zDefectsDashboard.html.
Sections: Total Defects, Runs with failures, Plans affected, By defect type.
"""
import csv
import os
import re
from collections import defaultdict
from pathlib import Path

_script_dir = Path(__file__).resolve().parent
# Project root: directory that contains the "z" folder (works if script is in project root or in z/)
WORKSPACE = _script_dir if (_script_dir / "z").is_dir() else _script_dir.parent
Z_OUT = WORKSPACE / "z"
OUT_HTML = Z_OUT / "zDefectsDashboard.html"


def classify_defect(output: str, action_type: str, expected: str) -> str:
    """Infer defect category from Output, ActionType, Expected."""
    if not output or str(output).strip() == "":
        return "Unknown"
    out = str(output).strip()
    # API status codes
    if re.search(r"\b404\b", out) or (expected and "404" in str(expected)):
        return "API 404 Not Found"
    if re.search(r"\b415\b", out):
        return "API 415 Unsupported Media"
    if re.search(r"\b500\b", out):
        return "API 500 Server Error"
    # UI / locator
    if "xWaitFor" in out or "wait for" in out.lower():
        return "UI Wait / Locator"
    if "xClick" in out or "locator" in out.lower():
        return "UI Element / Locator"
    # Validation
    if "xCompareJson" in out or "Key path" in out:
        return "Validation (JSON compare)"
    if "xValidateJson" in out:
        return "Validation (JSON)"
    if "Expected" in out or "expected" in out.lower():
        return "Validation (expected vs actual)"
    # Generic
    if "Error in" in out:
        return "Action Error"
    return "Other"


def find_all_zresults(root: Path) -> list[tuple[Path, str]]:
    """Return list of (absolute_path, run_id). run_id = parent folder name."""
    found = []
    for path in root.rglob("*_zResults.csv"):
        try:
            rel = path.relative_to(root)
            # run_id e.g. "Feb/z/20260201_172348_API_Petstore" or "Jan2026/z/..."
            run_id = str(rel.parent).replace("\\", "/")
            found.append((path, run_id))
        except ValueError:
            continue
    return sorted(found, key=lambda x: (x[1], x[0].name))


def parse_zresults(path: Path, run_id: str, suite_name: str) -> list[dict]:
    """Parse one CSV and return list of defect rows (Result=Fail) with extra fields."""
    defects = []
    try:
        with open(path, newline="", encoding="utf-8", errors="replace") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                return []
            for row in reader:
                if row.get("Result", "").strip().lower() != "fail":
                    continue
                defect_type = classify_defect(
                    row.get("Output", ""),
                    row.get("ActionType", ""),
                    row.get("Expected", ""),
                )
                defects.append({
                    "run_id": run_id,
                    "suite": suite_name,
                    "DesignId": row.get("DesignId", ""),
                    "PlanId": row.get("PlanId", ""),
                    "StepId": row.get("StepId", ""),
                    "StepInfo": row.get("StepInfo", ""),
                    "ActionType": row.get("ActionType", ""),
                    "ActionName": row.get("ActionName", ""),
                    "Input": (row.get("Input") or "")[:200],
                    "Output": (row.get("Output") or "")[:500],
                    "Expected": (row.get("Expected") or "")[:100],
                    "Critical": row.get("Critical", ""),
                    "Time": row.get("Time", ""),
                    "TimeTaken": row.get("TimeTaken", ""),
                    "defect_type": defect_type,
                })
    except Exception as e:
        defects.append({
            "run_id": run_id,
            "suite": suite_name,
            "PlanId": "",
            "StepInfo": f"Error reading file: {e}",
            "Output": str(e),
            "defect_type": "Parse Error",
        })
    return defects


def escape_html(s: str) -> str:
    if s is None:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_html(all_defects: list[dict], by_run: dict, by_suite: dict, by_plan: dict, by_type: dict) -> str:
    total = len(all_defects)
    total_runs = len(by_run)
    total_plans_affected = len(by_plan)
    type_order = [
        "API 404 Not Found",
        "API 415 Unsupported Media",
        "API 500 Server Error",
        "UI Wait / Locator",
        "UI Element / Locator",
        "Validation (JSON compare)",
        "Validation (JSON)",
        "Validation (expected vs actual)",
        "Action Error",
        "Other",
        "Parse Error",
    ]
    type_counts = [(t, by_type.get(t, 0)) for t in type_order if by_type.get(t, 0)] + [
        (k, v) for k, v in sorted(by_type.items()) if k not in type_order
    ]

    rows_html = []
    for d in all_defects:
        rows_html.append(
            f"""
        <tr>
            <td>{escape_html(d['run_id'])}</td>
            <td>{escape_html(d['suite'])}</td>
            <td>{escape_html(d['PlanId'])}</td>
            <td>{escape_html(d['StepId'])}</td>
            <td>{escape_html(d['StepInfo'])}</td>
            <td><span class="type-badge type-{d['defect_type'].split()[0].lower()}">{escape_html(d['defect_type'])}</span></td>
            <td class="output-cell" title="{escape_html(d['Output'])}">{escape_html(d['Output'][:80])}{'…' if len((d.get('Output') or '')) > 80 else ''}</td>
        </tr>"""
        )

    run_rows = "".join(
        f'<tr><td>{escape_html(k)}</td><td>{v}</td></tr>'
        for k, v in sorted(by_run.items(), key=lambda x: -x[1])
    )
    suite_rows = "".join(
        f'<tr><td>{escape_html(k)}</td><td>{v}</td></tr>'
        for k, v in sorted(by_suite.items(), key=lambda x: -x[1])
    )
    plan_rows = "".join(
        f'<tr><td>{escape_html(k)}</td><td>{v}</td></tr>'
        for k, v in sorted(by_plan.items(), key=lambda x: -x[1])[:30]
    )
    type_rows = "".join(
        f'<tr><td>{escape_html(k)}</td><td>{v}</td></tr>' for k, v in type_counts
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FoXYiZ Defects Dashboard</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f1f5f9; color: #1e293b; line-height: 1.5; }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 1.5rem; }}
        .header {{ background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
        .header h1 {{ font-size: 2rem; font-weight: 700; margin-bottom: 0.25rem; }}
        .header p {{ opacity: 0.9; font-size: 1rem; }}
        .summary-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem; margin-bottom: 1.5rem; }}
        .card {{ background: white; padding: 1.25rem; border-radius: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-left: 4px solid #64748b; }}
        .card.danger {{ border-left-color: #dc2626; }}
        .card h3 {{ font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin-bottom: 0.5rem; }}
        .card .value {{ font-size: 1.75rem; font-weight: 700; color: #1e293b; }}
        section {{ background: white; border-radius: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 1.5rem; overflow: hidden; }}
        section h2 {{ padding: 1rem 1.25rem; background: #f8fafc; border-bottom: 1px solid #e2e8f0; font-size: 1.1rem; }}
        .table-wrap {{ overflow-x: auto; max-height: 400px; overflow-y: auto; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.875rem; }}
        th {{ background: #f1f5f9; padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #475569; position: sticky; top: 0; }}
        td {{ padding: 0.6rem 0.75rem; border-bottom: 1px solid #f1f5f9; }}
        tr:hover {{ background: #f8fafc; }}
        .output-cell {{ max-width: 280px; word-break: break-word; }}
        .type-badge {{ display: inline-block; padding: 0.2rem 0.5rem; border-radius: 6px; font-size: 0.7rem; font-weight: 600; }}
        .type-api {{ background: #fecaca; color: #991b1b; }}
        .type-ui {{ background: #fed7aa; color: #9a3412; }}
        .type-validation {{ background: #fef08a; color: #854d0e; }}
        .type-action {{ background: #e2e8f0; color: #475569; }}
        .type-other {{ background: #e2e8f0; color: #64748b; }}
        .type-parse {{ background: #fecaca; color: #7f1d1d; }}
        .two-col {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }}
        @media (max-width: 900px) {{ .two-col {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Defects Dashboard</h1>
            <p>Aggregated failures from all zResults.csv runs</p>
        </div>
        <div class="summary-grid">
            <div class="card danger">
                <h3>Total Defects</h3>
                <div class="value">{total}</div>
            </div>
            <div class="card">
                <h3>Runs with failures</h3>
                <div class="value">{total_runs}</div>
            </div>
            <div class="card">
                <h3>Plans affected</h3>
                <div class="value">{total_plans_affected}</div>
            </div>
        </div>
        <div class="two-col">
            <section>
                <h2>By defect type</h2>
                <div class="table-wrap">
                    <table>
                        <thead><tr><th>Type</th><th>Count</th></tr></thead>
                        <tbody>{type_rows}</tbody>
                    </table>
                </div>
            </section>
            <section>
                <h2>By suite (top)</h2>
                <div class="table-wrap">
                    <table>
                        <thead><tr><th>Suite</th><th>Defects</th></tr></thead>
                        <tbody>{suite_rows}</tbody>
                    </table>
                </div>
            </section>
        </div>
        <div class="two-col">
            <section>
                <h2>By run</h2>
                <div class="table-wrap">
                    <table>
                        <thead><tr><th>Run</th><th>Defects</th></tr></thead>
                        <tbody>{run_rows}</tbody>
                    </table>
                </div>
            </section>
            <section>
                <h2>By plan (top 30)</h2>
                <div class="table-wrap">
                    <table>
                        <thead><tr><th>Plan</th><th>Defects</th></tr></thead>
                        <tbody>{plan_rows}</tbody>
                    </table>
                </div>
            </section>
        </div>
        <section>
            <h2>All defects ({total} rows)</h2>
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Run</th>
                            <th>Suite</th>
                            <th>Plan</th>
                            <th>Step</th>
                            <th>Step info</th>
                            <th>Type</th>
                            <th>Output / error</th>
                        </tr>
                    </thead>
                    <tbody>
                        {''.join(rows_html)}
                    </tbody>
                </table>
            </div>
        </section>
    </div>
</body>
</html>"""


def main():
    Z_OUT.mkdir(parents=True, exist_ok=True)
    all_results = find_all_zresults(WORKSPACE)
    all_defects = []
    by_run = defaultdict(int)
    by_suite = defaultdict(int)
    by_plan = defaultdict(int)
    by_type = defaultdict(int)

    for path, run_id in all_results:
        # Suite name from filename, e.g. "API_Petstore_zResults.csv" -> "API_Petstore"
        suite_name = path.stem.replace("_zResults", "").replace(".csv", "")
        defects = parse_zresults(path, run_id, suite_name)
        for d in defects:
            all_defects.append(d)
            by_run[run_id] += 1
            by_suite[suite_name] += 1
            if d.get("PlanId"):
                by_plan[d["PlanId"]] += 1
            by_type[d["defect_type"]] += 1

    html = build_html(all_defects, dict(by_run), dict(by_suite), dict(by_plan), dict(by_type))
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"Written {len(all_defects)} defects to {OUT_HTML}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
