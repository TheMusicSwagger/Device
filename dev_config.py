class Config:
    # Choose the Sensor on the device
    SENSOR=""
    GUID_FILENAME="guid"

    DEBUG_MODE=False
    RAISE_ERROR=False
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