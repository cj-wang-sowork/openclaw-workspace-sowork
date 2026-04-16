"""
Market Intelligence System - Cross-Market Learning & Optimization
==================================================================
Aggregates learning across all markets, detects patterns, and optimizes
the five-layer learning system for enterprise-wide improvements.

Features:
- Cross-market pattern aggregation
- Global security threat detection
- Market benchmarking and performance optimization
- Learning level performance analysis
- Anomaly detection across markets
- Recommendations for system-wide improvements

@access: @internal
@version: 1.0
@depends: hermes_adapter.py, market_router.py, security_checker.py
"""

import logging
import json
from typing import Dict, List, Optional, Any, Tuple, Set
from dataclasses import dataclass, field, asdict
from enum import Enum
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from pathlib import Path
import statistics


class InsightType(Enum):
      """Types of market insights"""
      THREAT = "threat"
      OPPORTUNITY = "opportunity"
      OPTIMIZATION = "optimization"
      ANOMALY = "anomaly"
      TREND = "trend"


@dataclass
class MarketInsight:
      """A cross-market insight or recommendation"""
      insight_type: InsightType
      title: str
      description: str
      affected_markets: List[str]
      affected_levels: List[str]
      severity: float = 0.5  # 0-1 severity/importance
    recommendation: str = ""
    evidence: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> Dict:
              """Convert to dictionary"""
              return {
                  **asdict(self),
                  "insight_type": self.insight_type.value,
                  "created_at": self.created_at.isoformat()
              }


@dataclass
class MarketBenchmark:
      """Performance benchmark for a market"""
      market_code: str
      learning_level: str
      metric_name: str
      value: float
      percentile: float = 0.5  # 0-1 percentile rank
    trend: str = "stable"  # up, down, stable
    updated_at: datetime = field(default_factory=datetime.utcnow)


class MarketIntelligence:
      """
          Enterprise-wide market intelligence system.

                  Provides cross-market insights, optimization recommendations,
                      and system-wide learning aggregation.

                              Features:
                                  - Pattern aggregation across all markets
                                      - Security threat analysis
                                          - Performance benchmarking
                                              - Anomaly detection
                                                  - Trend analysis
                                                      - Optimization recommendations
                                                          """

    def __init__(self, logger: Optional[logging.Logger] = None):
              """
                      Initialize market intelligence.

                                      Args:
                                                  logger: Logger instance
                                                          """
              self.logger = logger or logging.getLogger(__name__)
              self.insights: List[MarketInsight] = []
              self.benchmarks: Dict[str, MarketBenchmark] = {}
              self.market_metrics: Dict[str, Dict[str, Any]] = defaultdict(dict)
              self.threat_inventory: Dict[str, List[Dict]] = defaultdict(list)
              self.opportunity_inventory: Dict[str, List[Dict]] = defaultdict(list)
              self.learning_history: List[Dict] = []

    def aggregate_market_metrics(self, market_data: Dict[str, Any]) -> None:
              """
                      Aggregate metrics from all markets.

                                      Args:
                                                  market_data: Dictionary of market metrics {market_code: {metric: value}}
                                                          """
              for market_code, metrics in market_data.items():
                            self.market_metrics[market_code].update(metrics)
                            self.logger.debug(f"Aggregated metrics for {market_code}")

          def detect_cross_market_threats(self, violation_data: Dict[str, List[Dict]]) -> List[MarketInsight]:
                    """
                            Detect security threats affecting multiple markets.

                                            Args:
                                                        violation_data: Violation data {market_code: [violations]}

                                                                            Returns:
                                                                                        List of detected threats as insights
                                                                                                """
                    threats = []
                    violation_types: Dict[str, List[str]] = defaultdict(list)

        # Aggregate violations by type across markets
        for market_code, violations in violation_data.items():
                      for violation in violations:
                                        violation_type = violation.get("type", "unknown")
                                        violation_types[violation_type].append(market_code)

                  # Identify cross-market patterns
                  for vtype, markets in violation_types.items():
                                if len(markets) > 1:  # Affects multiple markets
                                    insight = MarketInsight(
                                                          insight_type=InsightType.THREAT,
                                                          title=f"Cross-Market Security Threat: {vtype}",
                                                          description=f"{vtype} detected in {len(markets)} markets",
                                                          affected_markets=markets,
                                                          affected_levels=["personal", "team"],
                                                          severity=min(1.0, len(markets) / 5),  # Scale by market count
                                                          recommendation=f"Implement unified defense for {vtype}",
                                                          evidence=markets
                                    )
                                                  threats.append(insight)
                                                  self.insights.append(insight)

                                          self.logger.info(f"Detected {len(threats)} cross-market threats")
                                          return threats

    def identify_opportunities(self, performance_data: Dict[str, Dict]) -> List[MarketInsight]:
              """
                      Identify optimization opportunities based on best performers.

                                      Args:
                                                  performance_data: Performance metrics by market

                                                                      Returns:
                                                                                  List of opportunities
                                                                                          """
              opportunities = []

        # Find best-performing markets
              if not performance_data:
                            return opportunities

        metrics_by_type = defaultdict(list)
        for market_code, metrics in performance_data.items():
                      for metric, value in metrics.items():
                                        metrics_by_type[metric].append((market_code, value))

                  # Identify laggards and suggest learning from leaders
                  for metric, market_values in metrics_by_type.items():
                                if len(market_values) > 1:
                                                  values = [v for _, v in market_values]
                                                  avg_value = statistics.mean(values)
                                                  top_market = max(market_values, key=lambda x: x[1])[0]
                                                  bottom_market = min(market_values, key=lambda x: x[1])[0]

                if avg_value > 0:  # Avoid division issues
                                      gap = (max(values) - min(values)) / avg_value
                                      if gap > 0.2:  # Significant gap detected
                                          opportunity = MarketInsight(
                                                                        insight_type=InsightType.OPPORTUNITY,
                                                                        title=f"Optimization Opportunity: {metric}",
                                                                        description=f"{bottom_market} can learn from {top_market}",
                                                                        affected_markets=[bottom_market],
                                                                        affected_levels=["enterprise", "brand"],
                                                                        severity=min(1.0, gap),
                                                                        recommendation=f"Implement {metric} best practices from {top_market}",
                                                                        evidence=[f"{top_market}: {max(values)}", f"{bottom_market}: {min(values)}"]
                                          )
                                                                opportunities.append(opportunity)
                                                                self.insights.append(opportunity)

                                                self.logger.info(f"Identified {len(opportunities)} optimization opportunities")
                                                return opportunities

    def detect_anomalies(self, market_patterns: Dict[str, Dict]) -> List[MarketInsight]:
              """
                      Detect anomalous behavior in markets.

                                      Args:
                                                  market_patterns: Patterns by market {market_code: {pattern: value}}

                                                                      Returns:
                                                                                  List of detected anomalies
                                                                                          """
              anomalies = []

        # Calculate statistical anomalies
              all_values = defaultdict(list)
        for market_code, patterns in market_patterns.items():
                      for pattern, value in patterns.items():
                                        all_values[pattern].append((market_code, value))

                  # Identify outliers
                  for pattern, market_values in all_values.items():
                                if len(market_values) > 2:
                                                  values = [v for _, v in market_values]
                                                  mean_val = statistics.mean(values)
                                                  stdev = statistics.stdev(values) if len(values) > 1 else 0

                if stdev > 0:
                                      for market_code, value in market_values:
                                                                z_score = abs((value - mean_val) / stdev)
                                                                if z_score > 2:  # More than 2 std devs from mean
                                                                    anomaly = MarketInsight(
                                                                                                      insight_type=InsightType.ANOMALY,
                                                                                                      title=f"Anomalous Pattern: {market_code}",
                                                                                                      description=f"Unusual {pattern} behavior detected",
                                                                                                      affected_markets=[market_code],
                                                                                                      affected_levels=["all"],
                                                                                                      severity=min(1.0, z_score / 5),
                                                                                                      recommendation="Investigate and validate behavior",
                                                                                                      evidence=[f"Value: {value}", f"Mean: {mean_val:.2f}", f"Z-Score: {z_score:.2f}"]
                                                                    )
                                                                                              anomalies.append(anomaly)
                                                                                              self.insights.append(anomaly)

                                                                          self.logger.info(f"Detected {len(anomalies)} anomalies")
                                                                          return anomalies

    def analyze_learning_level_performance(self, level_data: Dict[str, Dict]) -> Dict[str, Any]:
              """
                      Analyze performance across learning levels.

                                      Args:
                                                  level_data: Performance by level {level: {metric: value}}

                                                                      Returns:
                                                                                  Analysis dictionary
                                                                                          """
              analysis = {
                  "by_level": {},
                  "ranking": [],
                  "recommendations": []
              }

        for level, metrics in level_data.items():
                      analysis["by_level"][level] = {
                                        "metric_count": len(metrics),
                                        "avg_performance": statistics.mean(metrics.values()) if metrics else 0
                      }

        # Rank levels by performance
        ranked = sorted(
                      analysis["by_level"].items(),
                      key=lambda x: x[1]["avg_performance"],
                      reverse=True
        )
        analysis["ranking"] = [level for level, _ in ranked]

        # Generate recommendations
        if ranked:
                      top_level = ranked[0][0]
                      bottom_level = ranked[-1][0]
                      analysis["recommendations"].append(
                          f"Enterprise-wide: {bottom_level} should adopt {top_level} best practices"
                      )

        return analysis

    def generate_system_health_report(self) -> Dict[str, Any]:
              """
                      Generate comprehensive system health report.

                                      Returns:
                                                  Health report dictionary
                                                          """
              return {
                  "timestamp": datetime.utcnow().isoformat(),
                  "total_insights": len(self.insights),
                  "threats": len([i for i in self.insights if i.insight_type == InsightType.THREAT]),
                  "opportunities": len([i for i in self.insights if i.insight_type == InsightType.OPPORTUNITY]),
                  "anomalies": len([i for i in self.insights if i.insight_type == InsightType.ANOMALY]),
                  "markets_analyzed": len(self.market_metrics),
                  "critical_insights": len([i for i in self.insights if i.severity > 0.8]),
                  "recent_insights": [i.to_dict() for i in self.insights[-5:]]
              }

    def export_intelligence_report(self, output_path: str) -> bool:
              """
                      Export intelligence report to file.

                                      Args:
                                                  output_path: Output file path

                                                                      Returns:
                                                                                  True if successful
                                                                                          """
              try:
                            report = {
                                              "exported_at": datetime.utcnow().isoformat(),
                                              "health_report": self.generate_system_health_report(),
                                              "insights": [i.to_dict() for i in self.insights],
                                              "benchmarks": {k: asdict(v) for k, v in self.benchmarks.items()}
                            }

            with open(output_path, 'w', encoding='utf-8') as f:
                              json.dump(report, f, indent=2, default=str)

            self.logger.info(f"Exported intelligence report to {output_path}")
            return True
except Exception as e:
            self.logger.error(f"Failed to export report: {e}")
            return False


# CLI Entry Point
if __name__ == "__main__":
      logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
      )

    intelligence = MarketIntelligence()

    # Simulate market data
    market_data = {
              "us-en": {"access_success": 0.95, "violation_count": 2},
              "de-de": {"access_success": 0.92, "violation_count": 5},
              "jp-ja": {"access_success": 0.91, "violation_count": 8}
    }

    intelligence.aggregate_market_metrics(market_data)

    # Detect threats
    violation_data = {
              "us-en": [{"type": "credential_leak", "severity": "high"}],
              "de-de": [{"type": "credential_leak", "severity": "high"}],
              "jp-ja": [{"type": "credential_leak", "severity": "high"}]
    }
    threats = intelligence.detect_cross_market_threats(violation_data)

    # Generate report
    health_report = intelligence.generate_system_health_report()
    print("\nSystem Health Report:")
    print(json.dumps(health_report, indent=2))
