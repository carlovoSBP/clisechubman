import logging
from pathlib import Path

import boto3
import yaml
from sechubman import Manager

logger = logging.getLogger(__name__)


SECURITYHUB_CLIENT = boto3.client("securityhub")


def _get_rules(rules_path: str = "rules.yaml") -> dict:
    with Path(rules_path).open() as file:
        rules = yaml.safe_load(file)
    return rules


def _get_manager(rules: dict) -> Manager:
    manager = (
        Manager(**rules["ManagerConfig"], client=SECURITYHUB_CLIENT)
        if "ManagerConfig" in rules
        else Manager(client=SECURITYHUB_CLIENT)
    )
    return manager


def _validate_rules(rules_path: str = "rules.yaml") -> bool:
    rules = _get_rules(rules_path)
    manager = _get_manager(rules)

    all_valid = True

    for it, rule_dict in enumerate(rules["Rules"], start=1):
        logger.info(f"Validating rule '{it}'")
        try:
            rule = manager.set_rules([rule_dict])[0]
            logger.info(
                f"Rule '{it}' with note '{rule.UpdatesToFilteredFindings['Note']['Text']}' is valid."
            )
        except Exception as e:
            logger.error(f"Error validating rule '{it}': {e}")
            all_valid = False

    return all_valid


def _apply_rules(rules_path: str = "rules.yaml") -> None:
    rules = _get_rules(rules_path)
    manager = _get_manager(rules)

    manager.set_rules(rules["Rules"])
    manager.get_and_update_all()
