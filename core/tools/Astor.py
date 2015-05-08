import json
import re
import os
import subprocess
import datetime
from core.Tool import Tool
from core.Config import conf
from pprint import pprint

class Astor(Tool):
	"""docstring for Astor"""
	def __init__(self, name="Genprog"):
		super(Astor, self).__init__(name, "astor")

	def runAstor(self, 
		project, 
		id,
		mode="statement",
		maxgen="1000000",
		population="1"):
		source = None
		for index, src in project.src.iteritems():
			if id <= int(index):
				source = src
				break
		cmdInfo = 'export PATH="' + conf.defects4jRoot + '/framework/bin:$PATH";'
		cmdInfo += 'defects4j info -p ' + project.name + ' -v ' + str(id)
		info = subprocess.check_output(cmdInfo, shell=True)

		failingTest = ""
		reg = re.compile('- (.*)::(.*)')
		m = reg.findall(info)
		for i in m:
			failingTest += i[0] + ":"    

		workdir = self.initTask(project, id)
		cmd = 'cd ' + workdir +  ';'
		cmd += 'time java -cp ' + self.jar + ' ' + self.main
		cmd += ' -mode ' + mode
		cmd += ' -location .' 
		cmd += ' -dependencies lib/'
		cmd += ' -failing ' + failingTest
		cmd += ' -package ' + project.package
		cmd += ' -jvm4testexecution ' + conf.javaHome
		cmd += ' -javacompliancelevel ' + str(project.complianceLevel[str(id)]['source'])
		cmd += ' -maxgen ' + maxgen
		cmd += ' -population ' + population 
		cmd += ' -srcjavafolder ' + source['srcjava']
		cmd += ' -srctestfolder ' + source['srctest']
		cmd += ' -binjavafolder ' + source['binjava']
		cmd += ' -bintestfolder ' + source['bintest'] + ';'

		path = os.path.join(project.logPath, str(id), self.name, 'result')
		print path
		if not os.path.exists(os.path.dirname(path)):
			os.makedirs(os.path.dirname(path))
		#cmd += 'cp -r outputMutation/ ' + os.path.dirname(path) + ';'
		cmd += 'rm -rf ' + workdir +  ';'

		print cmd
		log = subprocess.check_output(cmd, shell=True)
		slittedLog = log.split('Solution details')
		if(len(slittedLog) > 1):
			print slittedLog[1]
			self.parseLog(slittedLog[1], project, id)
		else:
			slittedLog = log.split('End Repair Loops:')
                	if(len(slittedLog) > 1):
                        	print slittedLog[1]
                        	self.parseLog(slittedLog[1], project, id)

	def run(self, 
		project, 
		id):
		self.runAstor(project, id)

	def parseLog(self, log, project, id):
		programVariant = None
		timeEvaluation = None
		timeTotal = None
		m = re.search('ProgramVariant ([0-9]+)', log)
		if m:
			programVariant = m.group(1)
		m = re.search('Time Evolution\(ms\): ([0-9]+)', log)
		if m:
			timeEvaluation = m.group(1)
		m = re.search('Time Total\(ms\): ([0-9]+)', log)
		if m:
			timeTotal = m.group(1)

		operations = []

		operationsSplit = log.split('operation:')
		if(len(operationsSplit) > 1):
			for op in operationsSplit:
				generation = None
				className = None
				line = None
				patch = None

				m = re.search('location= (.*)', op)
				if m:
					className = m.group(1)
				else:
					continue
				m = re.search('line= ([0-9]+)', op)
				if m:
					line = m.group(1)
				m = re.search('fixed statement= "(.*)"', op)
				if m:
					patch = m.group(1)
				m = re.search('remove original statement', op)
				if m:
					patch = 'remove'
				m = re.search('generation= ([0-9]+)', op)
				if m:
					generation = m.group(1)

				if(patch == None):
					continue
				operations.append({
					'generation': int(generation),
					'patchLocation': {
						'className': className,
						'line': int(line)
					},
					'patch': patch,
				})

		results = {
			'programVariant': programVariant,
			'operations': operations,
			'timeEvaluation': timeEvaluation,
			'timeEvaluation': timeEvaluation,
			'timeTotal': timeTotal,
			'node': self.getHostname(),
            'date': datetime.datetime.now().isoformat()
		}
		reg = re.compile('#([a-zA-Z]+) *: *([0-9]+)')
		m = reg.findall(log)
		for i in m:
			results[i[0]] = i[1]
		reg = re.compile("time val([0-9]+) \[[0-9]+\]: \[([0-9, ]+)\]")
		m = reg.findall(log)
		for i in m:
			results["timeVal" + i[0]] = []
			t = re.compile('([0-9]+)')
			v = t.findall(i[1])
			for j in v:
				results["timeVal" + i[0]].append(int(j))
			

		path = os.path.join(project.logPath, str(id), self.name, "results.json")
		if not os.path.exists(os.path.dirname(path)):
			os.makedirs(os.path.dirname(path))
		file = open(path, "w")
		file.write(json.dumps(results, indent=4, sort_keys=True))
		file.close()
