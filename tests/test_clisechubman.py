from unittest import TestCase

from typer.testing import CliRunner

from clisechubman.main import app

RUNNER = CliRunner()


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)


class TestCLI(TestCase):
    def test_cli_invocation(self):
        result = RUNNER.invoke(app)
        self.assertEqual(result.exit_code, 0)

    def test_validate_rules_command(self):
        result = RUNNER.invoke(
            app, ["validate-rules", "tests/fixtures/rules.yaml"], catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 0)

    def test_validate_broken_rules_command(self):
        result = RUNNER.invoke(
            app,
            ["validate-rules", "tests/fixtures/broken_rules.yaml"],
            catch_exceptions=False,
        )
        self.assertEqual(result.exit_code, 1)
