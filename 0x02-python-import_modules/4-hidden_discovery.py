#!/usr/bin/python3
import os


os.system("strings hidden_4.pyc | grep -Ev '__|<' | sort")
