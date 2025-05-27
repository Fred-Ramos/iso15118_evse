import os
<<<<<<< HEAD
from typing import Optional

import environs

import logging
logger = logging.getLogger(__name__)

class SettingKey:
    PKI_PROTOCOL = "PKI_PROTOCOL"
    PKI_PATH = "PKI_PATH"
    MESSAGE_LOG_JSON = "MESSAGE_LOG_JSON"
    MESSAGE_LOG_EXI = "MESSAGE_LOG_EXI"
    ENABLE_TLS_1_3 = "ENABLE_TLS_1_3"


shared_settings = {}
=======
>>>>>>> everest/everest
SHARED_CWD = os.path.dirname(os.path.abspath(__file__))
JAR_FILE_PATH = SHARED_CWD + "/EXICodec.jar"

WORK_DIR = os.getcwd()

ENV_PATH = WORK_DIR + "/libexec/everest/3rd_party/josev/.env"

<<<<<<< HEAD
def load_shared_settings(env_path: Optional[str] = None):
    env = environs.Env(eager=False)
    env.read_env(path=env_path)  # read .env file, if it exists
    
    # choose default protocol as the first one on the .env, with iso_2 as default
    protocols = env.list("PROTOCOLS", default=["ISO_15118_2"])
    default_protocol = protocols[0]
    pki_protocol = _get_protocol_namespace(default_protocol)
    settings = {
        SettingKey.PKI_PROTOCOL: pki_protocol,
        SettingKey.PKI_PATH: env.str("PKI_PATH", default=SHARED_CWD + "/pki/"),
        SettingKey.MESSAGE_LOG_JSON: env.bool("MESSAGE_LOG_JSON", default=True),
        SettingKey.MESSAGE_LOG_EXI: env.bool("MESSAGE_LOG_EXI", default=False),
        SettingKey.ENABLE_TLS_1_3: env.bool("ENABLE_TLS_1_3", default=False),
    }
    shared_settings.update(settings)
    env.seal()  # raise all errors at once, if any

def _get_protocol_namespace(protocol: str) -> str:
    """Helper function to map protocol names to their respective namespace."""
    if protocol == "ISO_15118_2":
        return "iso15118_2"
    elif protocol in ["ISO_15118_20_AC", "ISO_15118_20_DC"]:
        return "iso15118_20"
    else:
        return "unknown"  # Return a fallback for unsupported protocols
    
def set_pki_protocol(protocol: str) -> None:
    """Set the selected protocol and update shared_settings."""
    global shared_settings

    pki_protocol = _get_protocol_namespace(protocol)
    logger.debug(f"Setting PKI Protocol {pki_protocol}")

    shared_settings[SettingKey.PKI_PROTOCOL] = pki_protocol
=======
PKI_Path = ""

def set_PKI_PATH(path: str) -> None:
    global PKI_Path
    PKI_Path = path

def get_PKI_PATH() -> str:
    return PKI_Path

MESSAGE_LOG_JSON = True
MESSAGE_LOG_EXI = False

V20_EVSE_SERVICES_CONFIG = SHARED_CWD + "/examples/secc/15118_20/service_config.json"

enabled_tls_1_3 = False

def enable_tls_1_3() -> None:
    global enabled_tls_1_3
    enabled_tls_1_3 = True

def is_tls_1_3_enabled() -> bool:
    return enabled_tls_1_3

shared_settings = None

ignoring_value_range = False

def set_ignoring_value_range(ignoring):
    global ignoring_value_range 
    ignoring_value_range = ignoring

def get_ignoring_value_range() -> bool:
    return ignoring_value_range
>>>>>>> everest/everest
