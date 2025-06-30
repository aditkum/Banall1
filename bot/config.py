import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("7815597466:AAEZQnI1vtQTMS2x8bpOqsUp1eCD16JrGN0", None)
    PYRO_SESSION = getenv("BQCj3P8AwYdlcWOrhQSBwz4KIkrEiCUOgvv40JsfL3tnZj13bDFDEi-upXIyOwi2-aMcz6Z0-BZSMJ99DNJbJRgXbvzkPAEK1VDYZK41RIqgPRS4oomO6wAraaFAu1WbsPVbC_7HiGvvslUoyrwkq8MBhyO30bLqGSpjC4fr-0Kscf4CI71fmlC2eEC3j9lfXWJXoe5xiQSptcVCPVObG57UamdB5Qir6XeY2VXPjHek9EGCQ4AQ3mj7P9jfwmZd_DANFNihaU02FeTxM5iEpkHqQBvf9NRWBplrFy4v7AxnPzHf7ackBkdt-lF8YKHfIoVaN3YtIgb-NNAOqQCrZSyihvA6GQAAAAGfUoZ-AA", None)
    TELEGRAM_APP_HASH= getenv('da61e3a08b5ac78ce28b4a4cd854aeec')
    TELEGRAM_APP_ID=int(getenv('10738943'))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
