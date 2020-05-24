#!/usr/bin/env python3

import re

class Songlist:

    def __init__(self, path):
        self.path = path
        return

    def get_contents(self):
        file = open(self.path)
        contents = file.readlines()
        file.close
        return contents

    def format_contents(self):
        pattern = re.compile()


        return
