import time
from communicator.com_config import Config as com_cfg


class Config:
    # Choose the Sensor on the device
    SENSOR = "GY521"
    GUID_FILENAME = "guid"

    DEBUG_MODE = False
    RAISE_ERROR = False
    DATA_VALUE_SIZE = com_cfg.DATA_VALUE_SIZE

    ################################################
    # Logging functions                            #
    ################################################
    def log(text):
        if Config.DEBUG_MODE:
            print("[---] [" + str(time.time()) + ")]", text)

    def warn(text):
        if Config.RAISE_ERROR:
            raise Exception(text)
        else:
            print("[!!!] [" + str(time.time()) + ")]", text)
