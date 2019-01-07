#!/usr/bin/env python


import subprocess
def stemWord(str):
    # process= subprocess.Popen(("./stemwords", "-l", "ta"), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    # out = process.communicate(input='கண்கள்\n')[0]
    # return out.decode()
    p = subprocess.run(("./stemmer/stemwords", "-l", "ta"), stdout=subprocess.PIPE,
            input=str, encoding='utf-8')
    return (p.stdout)
