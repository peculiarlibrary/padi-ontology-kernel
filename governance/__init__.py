"""
PADI Governance Package
Facilitates the enforcement of 'Governance-as-Code' rules and 
manages the validation pipeline for the PADI Kernel.
"""

from .governance_engine import GovernanceEngine

__all__ = ["GovernanceEngine"]
