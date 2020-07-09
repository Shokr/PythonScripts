#!/usr/bin/env python3
import toml

data = toml.load("data.toml")
print(toml.dumps(data))
