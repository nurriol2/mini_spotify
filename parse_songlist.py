#!/usr/bin/env python3

import re

class Songlist:

    def __init__(self, path):
        self.path = path
        self.query = []
        return

    def get_contents(self):
        file = open(self.path)
        contents = file.readlines()
        file.close
        return contents

    def format_contents(self):
        for q in self.get_contents():
            pattern = re.compile("^(\(*-*[\d:removed]*\)*)(\s\d+\.)*")
            mo = re.match(pattern, q).group()
            if mo:
                q = q.replace(mo, '')
                print(q)
        return
