"""TP-Link adapter for Mozilla WebThings Gateway."""

from os import path
import functools
import gateway_addon
import signal
import sys
import time

sys.path.append(path.join(path.dirname(path.abspath(__file__)), 'lib'))

from pkg.mimiio_adapter import MimiioAdapter  


_ADAPTER = None

print = functools.partial(print, flush=True)


def cleanup(signum, frame):
    """Clean up any resources before exiting."""
    if _ADAPTER is not None:
        _ADAPTER.close_proxy()

    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)
    _ADAPTER = MimiioAdapter(verbose=True)

    # Wait until the proxy stops running, indicating that the gateway shut us
    # down.
    while _ADAPTER.proxy_running():
        time.sleep(2)