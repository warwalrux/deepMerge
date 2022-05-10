#!/usr/bin/python3
import argparse
import yaml
import pprint
import sys
import logging

pp = pprint.PrettyPrinter()
logging.basicConfig(level=logging.DEBUG)

class deepMerger():

    def __init__(self)
        """ Merge Utility"""
        # deepMerge dict preference
        # Set to: "A" to prefer a
        # Set to: "B" to prefer b
        # Set to: None / Unset to error out.
        self.preference = "B"

    def raiseException(self, messagedata):
        raise Exception(messagedata["msg"])

    def Merge(self, a, b, path=None):
        "merges b into a"
        if path is None: path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    deepMerge(a[key], b[key], path + [str(key)])
                elif isinstance(a[key], list) and isinstance(b[key], list):
                    if self.preference == "B":
                        logging.debug("Deep Merge Preference is set to \"B\"")
                        a[key] = [*b[key], *a[key]]
                    elif self.preference == "A":
                        logging.debug("Deep Merge Preference is set to \"A\"")
                        a[key] = [*a[key], *b[key]]
                    else:
                        logging.debug("Deep Merge Preference is not set!")
                        self.raiseException({ "msg": 'Conflict at %s' % '.'.join(path + [str(key)])})
                elif a[key] == b[key]:
                    pass # same leaf value
                else:
                    self.raiseException({ "msg": 'Conflict at %s' % '.'.join(path + [str(key)])})
            else:
                a[key] = b[key]
        return a
