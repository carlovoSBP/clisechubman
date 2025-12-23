from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging import utils

from .clisechubman import _apply_rules

LOGGER = Logger()
utils.copy_config_to_registered_loggers(source_logger=LOGGER)


@LOGGER.inject_lambda_context(log_event=True)
def lambda_handler(event: dict, context: object) -> None:
    """Lambda handler to apply suppression rules to Security Hub findings."""
    _apply_rules()
