"""Define constants for the OpenSprinkler component."""
import voluptuous as vol

from datetime import timedelta

from homeassistant.helpers import config_validation as cv

CONF_INDEX = "index"
CONF_RUN_SECONDS = "run_seconds"

DOMAIN = "opensprinkler"

DEFAULT_NAME = "OpenSprinkler"
DEFAULT_PORT = 8080

SCAN_INTERVAL = timedelta(seconds=5)

SCHEMA_SERVICE_RUN_SECONDS = {
    vol.Required(CONF_INDEX): cv.positive_int,
    vol.Required(CONF_RUN_SECONDS): cv.positive_int,
}
SCHEMA_SERVICE_RUN = {
    vol.Optional(CONF_RUN_SECONDS): vol.Or(
        cv.ensure_list(cv.positive_int),
        cv.ensure_list(SCHEMA_SERVICE_RUN_SECONDS),
        cv.positive_int,
    )
}
SCHEMA_SERVICE_STOP = {}

SERVICE_RUN = "run"
SERVICE_STOP = "stop"
