#!/usr/bin/env python3
import re

def rearrange(name):
	pattern=r'^(\w+) (\w+)$'
	return re.sub(pattern,r'\1 \2',name.strip())
	
