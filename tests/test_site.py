from pathlib import Path
import unittest

PAGE = Path(__file__).parents[1] / "site" / "index.html"


class DeploymentPageTests(unittest.TestCase):
    def test_page_identifies_trunk_based_development(self):
        html = PAGE.read_text(encoding="utf-8")
        self.assertIn("<title>Trunk-Based Workflow Demo</title>", html)
        self.assertIn("short-lived", html)
        self.assertIn("main", html)

    def test_page_links_to_pipeline_and_analyzer(self):
        html = PAGE.read_text(encoding="utf-8")
        self.assertIn("https://github.com/manas0x/trunk-based-workflow-demo/actions", html)
        self.assertIn("https://gitflow-analyzer.onrender.com/", html)


    def test_feature_flag_keeps_incomplete_behavior_disabled(self):
        html = PAGE.read_text(encoding="utf-8")
        self.assertIn("delivery-insights", html)
        self.assertIn("incomplete behavior disabled", html)


if __name__ == "__main__":
    unittest.main()
