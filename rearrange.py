#!/usr/bin/env python3
import re

def rearrange(name):
	pattern=r'^(\w+) (\w+)$'
	print(re.sub(pattern,r'\2 \1',name.strip()))
rearrange('joseph makori ')	
