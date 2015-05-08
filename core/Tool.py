import json
import os
import subprocess
from pprint import pprint
from core.Config import conf
from os.path import expanduser

class Tool(object):
	"""docstring for Tool"""
	def __init__(self, name, configName):
		self.name = name
		self.configName = configName
		self.parseData();

	def parseData(self):
		path = os.path.join(os.path.dirname(__file__),'../data/tools/' + self.configName + '.json' )
		with open(path) as data_file:
			self.data = json.load(data_file)
			self.main = self.data["main"]
			self.jar = expanduser(self.data["jar"])
		pass
	def initTask(self, project, id):
		workdir =  '/tmp/' + project.name.lower() + '_' + str(id)  + '_' + self.name
		cmd = 'export PATH="' + conf.defects4jRoot + '/framework/bin:$PATH";'
		cmd += 'cp -r ' + conf.projectsRoot + '/' + project.name.lower() + '/' + project.name.lower() + '_' + str(id) + ' ' + workdir +  ';'
		cmd += 'cd ' + workdir +';'
		cmd += 'defects4j compile;'
		cmd += 'mkdir lib/;'
		cmd += 'cp -r ' + conf.defects4jRoot + '/framework/projects/lib/* lib/;'
		cmd += 'cp -r ' + conf.defects4jRoot + '/framework/projects/' + project.name + '/lib/* lib/;'
		cmd += 'find . -type f -name "package-info.java" -delete;'
		print cmd
		subprocess.check_output(cmd, shell=True)
		return workdir
	def getHostname(self):
		cmd = 'hostname;'
		return subprocess.check_output(cmd, shell=True)
