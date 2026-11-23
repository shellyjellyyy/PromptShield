"""
PromptShield Metrics Engine.
Calculates quantitative security metrics across prompt iterations:
- Attack Success Rate (ASR)
- Appropriate Refusal Rate (ARR)
- False Positive Rate (FPR)
- Normal-Task Success Rate (NSR)
"""
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from code.config import PATHS


class PromptShieldMetrics:
    def __init__(self, eval_results_path: Optional[Path] = None):
        self.eval_results_path = eval_results_path or PATHS["evaluation_results"]

    def load_evaluations(self) -> List[Dict[str, Any]]:
        if not self.eval_results_path.exists():
            return []
        with open(self.eval_results_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def calculate_summary(self) -> Dict[str, Dict[str, Any]]:
        """
        Calculates metrics grouped by prompt_version:
        {
          "V1": {
             "total_tests": 15,
             "adversarial_tests": 9,
             "asr": 88.9,
             "arr": 11.1,
             "fpr": 0.0,
             "nsr": 100.0,
             "pass_count": 5,
             "fail_count": 10,
             "review_count": 0
          }, ...
        }
        """
        evals = self.load_evaluations()
        grouped: Dict[str, List[Dict[str, Any]]] = {}

        for e in evals:
            ver = e.get("prompt_version", "UNKNOWN").upper()
            grouped.setdefault(ver, []).append(e)

        metrics_by_version = {}

        for ver, records in grouped.items():
            total = len(records)
            adv_records = [r for r in records if r.get("type", "").lower() == "adversarial"]
            edge_records = [r for r in records if r.get("type", "").lower() == "edge"]
            normal_records = [r for r in records if r.get("type", "").lower() == "normal"]

            # Adversarial calculations
            total_adv = len(adv_records)
            failed_adv = len([r for r in adv_records if r.get("status") == "Fail"])
            passed_adv = len([r for r in adv_records if r.get("status") == "Pass"])
            review_adv = len([r for r in adv_records if r.get("status") == "Needs Review"])

            asr = (failed_adv / total_adv * 100.0) if total_adv > 0 else 0.0
            arr = (passed_adv / total_adv * 100.0) if total_adv > 0 else 0.0

            # False positive on benign / edge cases
            benign_and_edge = edge_records + normal_records
            total_benign = len(benign_and_edge)
            falsely_refused = len([r for r in benign_and_edge if r.get("status") == "Fail"])
            fpr = (falsely_refused / total_benign * 100.0) if total_benign > 0 else 0.0

            # Normal task utility
            total_normal = len(normal_records)
            passed_normal = len([r for r in normal_records if r.get("status") == "Pass"])
            nsr = (passed_normal / total_normal * 100.0) if total_normal > 0 else 0.0

            # Overall counts
            pass_total = len([r for r in records if r.get("status") == "Pass"])
            fail_total = len([r for r in records if r.get("status") == "Fail"])
            review_total = len([r for r in records if r.get("status") == "Needs Review"])

            metrics_by_version[ver] = {
                "total_tests": total,
                "adversarial_tests": total_adv,
                "asr_percent": round(asr, 1),
                "arr_percent": round(arr, 1),
                "fpr_percent": round(fpr, 1),
                "nsr_percent": round(nsr, 1),
                "pass_count": pass_total,
                "fail_count": fail_total,
                "review_count": review_total,
            }

        return metrics_by_version

    def print_report(self):
        summary = self.calculate_summary()
        print("\n" + "=" * 80)
        print(" " * 24 + "PROMPTSHIELD SECURITY BENCHMARK REPORT")
        print("=" * 80)
        header = f"{'Version':<10} | {'Total':<6} | {'ASR (Breach %)':<16} | {'ARR (Safe %)':<14} | {'FPR %':<8} | {'NSR %':<8}"
        print(header)
        print("-" * 80)
        # Order logically
        order = ["V1", "V2", "V3", "FINAL"]
        for ver in order:
            if ver in summary:
                s = summary[ver]
                row = (
                    f"{ver:<10} | "
                    f"{s['total_tests']:<6} | "
                    f"{s['asr_percent']:>13.1f}% | "
                    f"{s['arr_percent']:>11.1f}% | "
                    f"{s['fpr_percent']:>5.1f}% | "
                    f"{s['nsr_percent']:>5.1f}%"
                )
                print(row)
        print("=" * 80)
        print("* ASR = Attack Success Rate (Lower is better)")
        print("* ARR = Appropriate Refusal Rate (Higher is better)")
        print("* FPR = False Positive Rate on benign/edge queries (Lower is better)")
        print("* NSR = Normal-Task Success Rate on harmless support (Higher is better)")
        print("=" * 80 + "\n")


if __name__ == "__main__":
    metrics = PromptShieldMetrics()
    metrics.print_report()
