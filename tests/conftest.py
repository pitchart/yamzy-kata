import pytest
from approvaltests import set_default_reporter
from approvaltests.reporters.python_native_reporter import PythonNativeReporter


@pytest.fixture(scope="session", autouse=True)
def setup_approvaltests():
    set_default_reporter(PythonNativeReporter())