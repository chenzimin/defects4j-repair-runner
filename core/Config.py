import os
from os.path import expanduser

class Config(object):
	"""Runner configurations"""
	def __init__(self):
		defects4jRepairRoot = os.path.join(os.path.dirname(__file__),'../' )

		self.defects4jRepairRoot = defects4jRepairRoot
		self.projectsRoot = expanduser("/mnt/vdb1/home/ubuntu/projects")
		self.defects4jRoot = expanduser("/mnt/vdb1/home/ubuntu/defects4j")
		self.resultsRoot = os.path.join(defects4jRepairRoot, "results/2016-may")
		self.z3Root = os.path.join(defects4jRepairRoot, "libs", "z3")
		self.javaHome = expanduser("/usr/lib/jvm/java-8-oracle/jre/bin/")
		#self.javaHome7 = expanduser("/Library/Java/JavaVirtualMachines/jdk1.7.0_80.jdk/Contents/Home/bin/")
		self.javaArgs = "-Xmx4096m"

conf = Config()
