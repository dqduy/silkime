import sys, os, shutil, subprocess, time

#Build tool
javaHome		= os.environ.get("JAVA_HOME")
sdkPath			= os.environ.get("ANDROID_HOME")
gradleExecWin		= "gradlew.bat"
gradleExecLinux		= "gradlew"
hostType 	= ""
buildType	= ""

#Project config
rootDir 	= ""
javaDir		= ""
scriptDir	= ""
genDir		= ""

#App config
outputFile 	= "silkime"
versionCode	= "0.1.0"
versionName	= "v" + versionCode

def buildProjectPath(rootPath, host, build):
	global rootDir
	rootDir = rootPath
	global hostType
	hostType = host
	global buildType
	buildType = build

	global javaDir
	javaDir 	= rootDir + os.sep + "java"	
	global scriptDir
	scriptDir 	= rootDir + os.sep + "scripts"
	global genDir
	genDir 		= rootDir + os.sep + "_generated"

	print("\033[1;34;40mLoad build config\033[0;37;40m")
	print("Host: \033[1;32;40m%s\033[0;37;40m" % hostType)
	print("Build Type: \033[1;32;40m%s\033[0;37;40m\n" % buildType)
	
	print("\033[1;34;40mLoad project config\033[0;37;40m")
	print("Root dir: 		\033[1;34;40m%s\033[0;37;40m" % rootDir)
	print("Java dir: 		\033[1;34;40m%s\033[0;37;40m" % javaDir)
	print("Script dir:		\033[1;34;40m%s\033[0;37;40m" % scriptDir)
	print("Genrerated dir: 	\033[1;34;40m%s\033[0;37;40m" % genDir)
	print("\n")
	
def buildWorkingDir():
	#Copy project template to build dir
	src = javaDir + os.sep + "project"
	des = genDir + os.sep + "_asproject"
	if os.path.exists(des):
		shutil.rmtree(des)
	
	print("\033[1;34;40mFrom\n\033[0;37;40m" + src)
	print("\033[1;34;40mTo\n\033[0;37;40m" + des)

	shutil.copytree(src, des)
	
	print("\n")

def buildJava():
	print("===========================================================")
	print("                      \033[1;32;40mBUILD JAVA\033[0;37;40m")
	print("===========================================================")

	if hostType == "windows":
		gradleExec = gradleExecWin
	elif hostType == "linux":
		gradleExec = gradleExecLinux
		
	cmd = javaDir + os.sep + "project" + os.sep + gradleExec + " assembleRelease -p " + genDir + os.sep + "_asproject"
	print(cmd)
	subprocess.call(cmd, shell=True)
	
	print("\n")

def buildPackage():
	print("===========================================================")
	print("                      \033[1;32;40mBUILD PACKAGE\033[0;37;40m")
	print("===========================================================")
		
	src = genDir + os.sep + "_asproject" + os.sep + "app" + os.sep + "build" + os.sep + "outputs" + os.sep + "apk" + os.sep + "release" + os.sep + "app-release.apk"
	des = genDir + os.sep + "apks"
	
	print("\033[1;34;40mFrom:\n\033[0;37;40m" + src)
	print("\033[1;34;40mTo\n\033[0;37;40m" + des)
	
	if not os.path.exists(des):
		os.mkdir(des)
	des +=  os.sep + outputFile + "-" + versionName + "-release.apk"
	shutil.copyfile(src, des)
	
	print("\n")

def main(argv):
	start = time.time()
	print("===========================================================")
	print("                      \033[1;32;40mBUILD APPLICATION\033[0;37;40m")
	print("===========================================================")
	
	print(str(argv))
	buildProjectPath(argv[0], argv[1], argv[2])
	
	buildWorkingDir()
	
	buildJava()
	
	buildPackage()

	elapsedTime = time.time() - start
	print("Running time: %s s" % str(elapsedTime))

if __name__ == '__main__':
    main(sys.argv[1:])