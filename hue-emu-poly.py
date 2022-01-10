#!/usr/bin/env python3
"""
This is a NodeServer to Emulate a Hue Hub for Polyglot v2 written in Python3
by JimBo (Jim Searle) jimboca3@gmail.com
"""
from polyinterface import Interface,LOGGER,LOG_HANDLER
from nodes import HueEmuController
import sys,os

if __name__ == "__main__":
    try:
        #
        # Move config into new persist_dir
        #
        fname = "config.json"
        config_dir = "config"
        fpath = config_dir + "/" + fname
        if not os.path.exists(config_dir):
            try:
                os.mkdir(config_dir)
            except (Exception) as err:
                LOGGER.error("Unable to mkdir {}: {}".format(config_dir,err))
                sys.exit(0)
        if os.path.exists(fname):
            LOGGER.debug("Moving {} -> {}".format(fname,fpath))
            try:
                os.rename(fname,fpath)
            except (Exception) as err:
                LOGGER.error("Unable to rename {} -> {}: {}".format(fname,fpath,err))

        polyglot = Interface('HueEmulator')
        """
        Instantiates the Interface to Polyglot.
        """
        polyglot.start()
        """
        Starts MQTT and connects to Polyglot.
        """
        control = HueEmuController(polyglot)
        """
        Creates the Controller Node and passes in the Interface
        """
        control.runForever()
        """
        Sits around and does nothing forever, keeping your program running.
        """
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
        """
        Catch SIGTERM or Control-C and exit cleanly.
        """
