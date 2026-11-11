import os, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ.setdefault("PULSE_HOME", tempfile.mkdtemp(prefix="pulse-test-"))

import pulse_connect


def test_opens_once_when_the_app_knows_the_link():
    assert pulse_connect.should_open_dashboard({"view_key": "abc"}) is True
    assert pulse_connect.should_open_dashboard({"view_key": "abc", "dashboard_opened": True}) is False
    assert pulse_connect.should_open_dashboard({}) is False
    assert pulse_connect.should_open_dashboard({"view_key": "abc"}, allow_browser=False) is False


if __name__ == "__main__":
    test_opens_once_when_the_app_knows_the_link()
    print("ok")
