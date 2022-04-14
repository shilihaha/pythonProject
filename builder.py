# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:10:40 2019

@author: chenyaoxing
"""
import os
import shutil
import time

builderFile = "build.config"
configFile_ISE = "C:/Xilinx/14.7/ISE_DS/EDK/gnu/microblaze/nt/bin/" + builderFile
configFile_Vivado = "C:/Xilinx/SDK/2017.2/gnu/microblaze/nt/bin/" + builderFile
elfCheck_ISE = "C:/Xilinx/14.7/ISE_DS/EDK/bin/nt/"

gitPath = "./"

v6ProjectRootDir = gitPath + "Firmware/"
kucProjectRootDir = gitPath + "Firmware_KUC/"

configurationFolder_debug = "Debug/"
configurationFolder_release = "Release/"

#include path
libraryPath = gitPath + "library/"
rtosPath = libraryPath + "FreeRTOS/"
rtosPath0 = rtosPath + "include/"
rtosPath1 = rtosPath + "portable/GCC/MicroBlazeV8/"
rtosPath2 = rtosPath + "portable/MemMang/"
sourcePath = gitPath + "source/"
shellPath = sourcePath + "shell/"
fdkPath = sourcePath + "fdk_driver/"
fdkAccessLayerPath = fdkPath + "access_layer/"
fdkLogicLayerPath = fdkPath + "logic_layer/"
srcPath = "src/"

v6_system_xml = v6ProjectRootDir + "mb_system_hw_platform/system.xml"
v6_standalonebsp_microblaze = "standalone_bsp_0/microblaze_0"
mb_gcc_compiler_v6_debug = "mb-gcc -DMICROBLAZE -DVIRTEX6 -Wall -O1 -g3"
mb_gcc_compiler_v6_release = "mb-gcc -DMICROBLAZE -DVIRTEX6 -Wall -O2"
mb_gcc_compiler_miscellaneous_processor_options_v6 = " -c -fmessage-length=0 -mlittle-endian -mxl-barrel-shift -mxl-pattern-compare -mno-xl-soft-div -mcpu=v8.50.c -mno-xl-soft-mul -mxl-multiply-high -mhard-float -mxl-float-convert -mxl-float-sqrt -Wl,--no-relax -ffunction-sections -fdata-sections -MMD -MP -MF"

mb_gcc_linker_v6 = "mb-gcc -Wl,-T -Wl,"
mb_gcc_linker_miscellaneous_processor_options_v6 = " -mlittle-endian -mxl-barrel-shift -mxl-pattern-compare -mno-xl-soft-div -mcpu=v8.50.c -mno-xl-soft-mul -mxl-multiply-high -mhard-float -mxl-float-convert -mxl-float-sqrt -Wl,--no-relax -Wl,--gc-sections -o "
mb_gcc_linker_software_platform_flags_options_v6 = "   -Wl,--start-group,-lxil,-lgcc,-lc,--end-group"

kuc_standalonebsp_microblaze = "standalone_bsp_0/mb_base_system_i_mb_min_sys_microblaze_0"
mb_gcc_compiler_kuc_debug = "mb-gcc -DMICROBLAZE -DXILINX -D_DEBUG -DULTRASCALE -Wall -O1 -g3"
mb_gcc_compiler_kuc_release = "mb-gcc -DMICROBLAZE -DULTRASCALE -Wall -O2"
mb_gcc_compiler_miscellaneous_processor_options_kuc = " -c -fmessage-length=0 -mxl-frequency -mlittle-endian -mcpu=v10.0 -mxl-soft-mul -Wl,--no-relax -ffunction-sections -fdata-sections -MMD -MP -MF"

mb_gcc_linker_kuc = "mb-gcc -Wl,-T -Wl,"
mb_gcc_linker_miscellaneous_processor_options_kuc = " -mlittle-endian -mcpu=v10.0 -mxl-soft-mul -Wl,--no-relax -Wl,--gc-sections -o "
mb_gcc_linker_software_platform_flags_options_kuc = "   -Wl,--start-group,-lxil,-lgcc,-lc,--end-group"

class Builder():
    def getprojectlist_s1(self, projectRootDir = v6ProjectRootDir):
        self.projectList = []
        self.ProjectRootList = os.listdir(projectRootDir)
        for j in self.ProjectRootList:
            if (j == "firmware") or (j == "standalone_bsp_0") or (j == ".metedata"):
                continue
            if os.path.exists(projectRootDir + j + "/.cproject"):
                if os.path.exists(projectRootDir + j + "/src" + "/main.c"):
                    self.projectList.append(j)
        print("Project List:",self.projectList)

    def createprocessfolder_s2(self, projectRootDir = v6ProjectRootDir, configurationFolder = configurationFolder_debug):
        if os.path.exists(projectRootDir + configurationFolder):
            shutil.rmtree(projectRootDir + configurationFolder)
            os.makedirs(projectRootDir + configurationFolder)
            os.makedirs(projectRootDir + configurationFolder + shellPath.replace(sourcePath, ''))
            os.makedirs(projectRootDir + configurationFolder + srcPath)
            os.makedirs(projectRootDir + configurationFolder + rtosPath.replace(libraryPath, '') + rtosPath1.replace(rtosPath, ''))
            os.makedirs(projectRootDir + configurationFolder + rtosPath.replace(libraryPath, '') + rtosPath2.replace(rtosPath, ''))
            os.makedirs(projectRootDir + configurationFolder + fdkAccessLayerPath.replace(sourcePath, ''))
            fdkLogicLayerList = os.listdir(fdkLogicLayerPath)
            for k in fdkLogicLayerList:
                if os.path.isdir(fdkLogicLayerPath + k):
                    os.makedirs(projectRootDir + configurationFolder + fdkLogicLayerPath.replace(sourcePath, '') + k)
                    for m in os.listdir(fdkLogicLayerPath + k):
                        if os.path.isdir(fdkLogicLayerPath + k + "/" + m):
                            os.makedirs(projectRootDir + configurationFolder + fdkLogicLayerPath.replace(sourcePath, '') + k + "/" + m)
                            # print(projectRootDir + configurationFolder + fdkLogicLayerPath.replace(sourcePath, '') + k + "/" + m)
                        else:
                            pass
        else:
            os.makedirs(projectRootDir + configurationFolder)
            os.makedirs(projectRootDir + configurationFolder + shellPath.replace(sourcePath, ''))
            os.makedirs(projectRootDir + configurationFolder + srcPath)
            os.makedirs(projectRootDir + configurationFolder + rtosPath.replace(libraryPath, '') + rtosPath1.replace(rtosPath, ''))
            os.makedirs(projectRootDir + configurationFolder + rtosPath.replace(libraryPath, '') + rtosPath2.replace(rtosPath, ''))
            os.makedirs(projectRootDir + configurationFolder + fdkAccessLayerPath.replace(sourcePath, ''))
            fdkLogicLayerList = os.listdir(fdkLogicLayerPath)
            for k in fdkLogicLayerList:
                if os.path.isdir(fdkLogicLayerPath + k):
                    os.makedirs(projectRootDir + configurationFolder + fdkLogicLayerPath.replace(sourcePath, '') + k)
                    for m in os.listdir(fdkLogicLayerPath + k):
                        if os.path.isdir(fdkLogicLayerPath + k + "/" + m):
                            os.makedirs(projectRootDir + configurationFolder + fdkLogicLayerPath.replace(sourcePath, '') + k + "/" + m)
                        else:
                            pass

    def createincludecommand_s3(self, mb_gcc_compiler = mb_gcc_compiler_v6_debug, projectRootDir = v6ProjectRootDir, standalonebsp = v6_standalonebsp_microblaze):
        standaloneBspPath = projectRootDir + standalonebsp + "/include"
        pathInclude0 = " -I" + "\"" + shellPath + "\""
        pathInclude1 = " -I" + "\"" + rtosPath + "\""
        pathInclude2 = " -I" + "\"" + rtosPath0 + "\""
        pathInclude3 = " -I" + "\"" + rtosPath1 + "\""
        pathInclude4 = " -I" + "\"" + rtosPath2 + "\""
        pathInclude5 = " -I" + "\"" + fdkPath + "\""
        pathInclude6 = " -I" + "\"" + fdkAccessLayerPath + "\""
        pathInclude7 = " -I" + "\"" + fdkLogicLayerPath + "\""
        pathInclude8 = " -I" + "\"" + standaloneBspPath + "\""
        self.mbGccInclude = mb_gcc_compiler + pathInclude0 + pathInclude1 + pathInclude2 + pathInclude3 + pathInclude4 + pathInclude5 + pathInclude6 + pathInclude7 + pathInclude8
        self.fdkLogicLayerList = []
        for i in os.listdir(fdkLogicLayerPath):
            if os.path.isdir(fdkLogicLayerPath + i):
                self.fdkLogicLayerList.append(fdkLogicLayerPath + i)
                self.mbGccInclude = self.mbGccInclude + " -I" + "\"" + fdkLogicLayerPath + i + "\""
                for j in os.listdir(fdkLogicLayerPath + i):
                    if os.path.isdir(fdkLogicLayerPath + i + "/" + j):
                        self.fdkLogicLayerList.append(fdkLogicLayerPath + i + "/" + j)
                        self.mbGccInclude = self.mbGccInclude + " -I" + "\"" + fdkLogicLayerPath + i + "/" + j + "\""

    def createcompliecommad_s4(self, projectRootDir = v6ProjectRootDir, configurationFolder = configurationFolder_debug, buildFilePath = gitPath + builderFile):
        self.srcDirList = [[] for i in range(len(self.projectList))]
        self.shellDirList = []
        self.fdkDirList = []
        self.fdkAccessDirList = []
        self.fdkLogicDirList = []
        self.fdkLogicSubDirList = []
        self.rtosDirList = []
        self.rtosSubDirList1 = []
        self.rtosSubDirList2 = []

        with open(buildFilePath, "w+") as builder:
            for j in self.projectList:
                print("project index:", self.projectList.index(j))
                print("project:", self.projectList[self.projectList.index(j)])
                index = self.projectList.index(j)
                for i in os.listdir(projectRootDir + j + "/" + srcPath):
                    if os.path.splitext(i)[1] == '.c':
                        fileName = projectRootDir + j + "/" + srcPath + i.replace(".c", "")
                        intermediateFilePath = projectRootDir + j + "/" + configurationFolder + srcPath + i.replace(".c", "")
                        if os.path.exists(intermediateFilePath.replace(i.replace(".c", ""), "")):
                            pass
                        else:
                            os.makedirs(intermediateFilePath.replace(i.replace(".c", ""), ""))
                        self.srcDirList[index].append(intermediateFilePath + '.o')
                        dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".c" + "\""
                        builder.write(self.mbGccInclude + mb_gcc_compiler_miscellaneous_processor_options_v6 + dFile2O)
                        builder.write("\r\n")

            for i in os.listdir(shellPath):
                if os.path.splitext(i)[1] == '.c':
                    fileName = shellPath + i.replace(".c", "")
                    intermediateFilePath = projectRootDir + configurationFolder + shellPath.replace(sourcePath, '') + i.replace(".c", "")
                    self.shellDirList.append(intermediateFilePath + '.o')
                    dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".c" + "\""
                    builder.write(self.mbGccInclude + mb_gcc_compiler_miscellaneous_processor_options_v6 + dFile2O)
                    builder.write("\r\n")
            for i in os.listdir(fdkPath):
                if os.path.splitext(i)[1] == '.c':
                    fileName = fdkPath + i.replace(".c", "")
                    intermediateFilePath = projectRootDir + configurationFolder + fdkPath.replace(sourcePath, '') + i.replace(".c", "")
                    self.fdkDirList.append(intermediateFilePath + '.o')
                    dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".c" + "\""
                    builder.write(self.mbGccInclude + mb_gcc_compiler_miscellaneous_processor_options_v6 + dFile2O)
                    builder.write("\r\n")
            for i in os.listdir(fdkAccessLayerPath):
                if os.path.splitext(i)[1] == '.c':
                    fileName = fdkAccessLayerPath + i.replace(".c", "")
                    intermediateFilePath = projectRootDir + configurationFolder + fdkAccessLayerPath.replace(sourcePath, '') + i.replace(".c", "")
                    self.fdkAccessDirList.append(intermediateFilePath + '.o')
                    dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".c" + "\""
                    builder.write(self.mbGccInclude + mb_gcc_compiler_miscellaneous_processor_options_v6 + dFile2O)
                    builder.write("\r\n")
            for i in os.listdir(fdkLogicLayerPath):
                if os.path.splitext(i)[1] == '.c':
                    fileName = fdkLogicLayerPath + i.replace(".c", "")
                    intermediateFilePath = projectRootDir + configurationFolder + fdkLogicLayerPath.replace(sourcePath, '') + i.replace(".c", "")
                    self.fdkLogicDirList.append(intermediateFilePath + '.o')
                    dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".c" + "\""
                    builder.write(self.mbGccInclude + mb_gcc_compiler_miscellaneous_processor_options_v6 + dFile2O)
                    builder.write("\r\n")
            for m in self.fdkLogicLayerList:
                for i in os.listdir(m):
                    # print(i)
                    if os.path.splitext(i)[1] == '.c':
                        fileName = m + "/" + i.replace(".c", "")
                        intermediateFilePath = projectRootDir + configurationFolder + m.replace(sourcePath, '') + "/" + i.replace(".c", "")
                        self.fdkLogicSubDirList.append(intermediateFilePath + '.o')
                        dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".c" + "\""
                        builder.write(self.mbGccInclude + mb_gcc_compiler_miscellaneous_processor_options_v6 + dFile2O)
                        builder.write("\r\n")
            for i in os.listdir(rtosPath):
                # print(i)
                if os.path.splitext(i)[1] == '.c':
                    fileName = rtosPath + i.replace(".c", "")
                    intermediateFilePath = projectRootDir + configurationFolder + rtosPath.replace(libraryPath, '') + i.replace(".c", "")
                    self.rtosDirList.append(intermediateFilePath + '.o')
                    dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".c" + "\""
                    builder.write(self.mbGccInclude + mb_gcc_compiler_miscellaneous_processor_options_v6 + dFile2O)
                    builder.write("\r\n")
            for i in os.listdir(rtosPath1):
                if os.path.splitext(i)[1] == '.c':
                    fileName = rtosPath1 + i.replace(".c", "")
                    intermediateFilePath = projectRootDir + configurationFolder + rtosPath1.replace(libraryPath, '') + i.replace(".c", "")
                    dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".c" + "\""
                elif os.path.splitext(i)[1] == '.S':
                    fileName = rtosPath1 + i.replace(".S", "")
                    intermediateFilePath = projectRootDir + configurationFolder + rtosPath1.replace(libraryPath, '') + i.replace(".S", "")
                    dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".S" + "\""
                else:
                    continue
                self.rtosSubDirList1.append(intermediateFilePath + '.o')
                builder.write(self.mbGccInclude + mb_gcc_compiler_miscellaneous_processor_options_v6 + dFile2O)
                builder.write("\r\n")
            for i in os.listdir(rtosPath2):
                if os.path.splitext(i)[1] == '.c':
                    fileName = rtosPath2 + i.replace(".c", "")
                    intermediateFilePath = projectRootDir + configurationFolder + rtosPath2.replace(libraryPath, '') + i.replace(".c", "")
                    self.rtosSubDirList2.append(intermediateFilePath + '.o')
                    dFile2O = "\"" + intermediateFilePath + ".d" + "\"" + " -MT" + "\"" + intermediateFilePath + ".d" + "\"" + " -o " + "\"" + intermediateFilePath + ".o" + "\"" + " " + "\"" + fileName + ".c" + "\""
                    builder.write(self.mbGccInclude + mb_gcc_compiler_miscellaneous_processor_options_v6 + dFile2O)
                    builder.write("\r\n")

        builder.close()

    def createlinkercommand_s5(self, projectRootDir = v6ProjectRootDir, configurationFolder = configurationFolder_debug, buildFilePath = gitPath + builderFile, mb_gcc_linker = mb_gcc_linker_v6, mb_gcc_linker_miscellaneous = mb_gcc_linker_miscellaneous_processor_options_v6, mb_gcc_linker_software = mb_gcc_linker_software_platform_flags_options_v6, standalonebsp = v6_standalonebsp_microblaze):
        with open(buildFilePath, "a+") as builder:
            self.standalone_bsp_lib = " -L" + "\"" + projectRootDir + standalonebsp + "/lib" + "\""
            for j in range(0, len(self.projectList)):
                self.link_script_file_path = projectRootDir + self.projectList[j] + "/" + srcPath + "lscript.ld"
                self.elf_file_path = "\"" + projectRootDir + self.projectList[j] + "/" + configurationFolder + self.projectList[j] + ".elf" + "\""
                self.linker_include_file = ""
                if os.path.exists(self.link_script_file_path):
                    self.link_script_file_path = "\"" + self.link_script_file_path + "\""
                    for m in range(0, len(self.srcDirList[j])):
                        #print(self.srcDirList[j][m])
                        self.linker_include_file = self.linker_include_file + " " + "\"" + self.srcDirList[j][m] + "\""
                    for m in range(0, len(self.shellDirList)):
                        #print(self.shellDirList[m])
                        self.linker_include_file = self.linker_include_file + " " + "\"" + self.shellDirList[m] + "\""
                    for m in range(0, len(self.fdkDirList)):
                        #print(self.fdkDirList[m])
                        self.linker_include_file = self.linker_include_file + " " + "\"" + self.fdkDirList[m] + "\""
                    for m in range(0, len(self.fdkAccessDirList)):
                        #print(self.fdkAccessDirList[m])
                        self.linker_include_file = self.linker_include_file + " " + "\"" + self.fdkAccessDirList[m] + "\""
                    for m in range(0, len(self.fdkLogicDirList)):
                        #print(self.fdkLogicDirList[m])
                        self.linker_include_file = self.linker_include_file + " " + "\"" + self.fdkLogicDirList[m] + "\""
                    for m in range(0, len(self.fdkLogicSubDirList)):
                        #print(self.fdkLogicSubDirList[m])
                        self.linker_include_file = self.linker_include_file + " " + "\"" + self.fdkLogicSubDirList[m] + "\""
                    for m in range(0, len(self.rtosDirList)):
                        #print(self.rtosDirList[m])
                        self.linker_include_file = self.linker_include_file + " " + "\"" + self.rtosDirList[m] + "\""
                    for m in range(0, len(self.rtosSubDirList1)):
                        #print(self.rtosSubDirList1[m])
                        self.linker_include_file = self.linker_include_file + " " + "\"" + self.rtosSubDirList1[m] + "\""
                    for m in range(0, len(self.rtosSubDirList2)):
                        #print(self.rtosSubDirList2[m])
                        self.linker_include_file = self.linker_include_file + " " + "\"" + self.rtosSubDirList2[m] + "\""
                    self.finalCommand = mb_gcc_linker + self.link_script_file_path + self.standalone_bsp_lib + mb_gcc_linker_miscellaneous + self.elf_file_path + self.linker_include_file + mb_gcc_linker_software
                    # print("final command:",self.finalCommand)
                    builder.write(self.finalCommand)
                    builder.write("\r\n")
                else:
                    link_script_file_path = ""
                    continue
        builder.close()

    def setCommand_s6(self, buildFilePath = gitPath + builderFile):
        # os.chdir(buildFilePath.replace("build.config", ""))
        with open(buildFilePath, "r") as builder:
            osCommand = builder.readlines()
            for i in osCommand:
                os.system(i)
        builder.close()

    def buildv6project(self):
        self.getprojectlist_s1(projectRootDir=v6ProjectRootDir)
        self.createprocessfolder_s2(projectRootDir=v6ProjectRootDir, configurationFolder=configurationFolder_debug)
        self.createincludecommand_s3(mb_gcc_compiler=mb_gcc_compiler_v6_debug, projectRootDir=v6ProjectRootDir, standalonebsp=v6_standalonebsp_microblaze)
        self.createcompliecommad_s4(projectRootDir=v6ProjectRootDir, configurationFolder=configurationFolder_debug, buildFilePath = gitPath + builderFile)
        self.createlinkercommand_s5(projectRootDir=v6ProjectRootDir, configurationFolder=configurationFolder_debug, buildFilePath = gitPath + builderFile, mb_gcc_linker=mb_gcc_linker_v6, mb_gcc_linker_miscellaneous=mb_gcc_linker_miscellaneous_processor_options_v6, mb_gcc_linker_software=mb_gcc_linker_software_platform_flags_options_v6, standalonebsp=v6_standalonebsp_microblaze)
        self.setCommand_s6(buildFilePath = gitPath + builderFile)
        binFIlePath = gitPath + "bin/" + configurationFolder_debug + "v6"
        if os.path.exists(binFIlePath):
            pass
        else:
            os.makedirs(binFIlePath)
        with open(binFIlePath + "/" + "size.log", "w") as sizeLog:
            generateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            sizeLog.write("[IMPORTANT]: Auto Generated Codes, Please don't edit it mannually." + "\r")
            sizeLog.write("             Generated Time: " + generateTime + "\n" + "\n")
            for j in self.projectList:
                elfPath = v6ProjectRootDir + j + "/" + configurationFolder_debug
                os.chdir(gitPath)
                for i in os.listdir(elfPath):
                    if os.path.splitext(i)[1] == '.elf':
                        output = os.popen("mb-size " + "\"" + elfPath + i + "\n")
                        sizeLog.write("*********************************************************************************" + "\r")
                        sizeLogOutput = output.read()
                        sizeLog.write(sizeLogOutput)
                        # os.chdir(elfCheck_ISE)
                        output = os.popen("elfcheck " + elfPath + i + " -hw " + v6_system_xml + " -pe " + "microblaze_0" + "\n")
                        checkSizeOutput = output.read()
                        sizeLog.write(checkSizeOutput)
                        if checkSizeOutput.find("elfcheck passed") >= 0:
                            print("[Check Info] %s Size Check Passed!!!"%(elfPath + i))
                            print("   --File Will Be Moved Into Bin Folder...")
                            shutil.copy2(elfPath + i, binFIlePath)
                        else:
                            print("[Error Info] %s Size Overflow!!!"%(elfPath + i))
                            print("   --File Will Not Be Moved Into Bin Folder")
                        sizeLog.write("\n")
                        # os.chdir(configFile_ISE.replace("build.config", ""))
        sizeLog.close()

        self.getprojectlist_s1(projectRootDir=v6ProjectRootDir)
        self.createprocessfolder_s2(projectRootDir=v6ProjectRootDir, configurationFolder=configurationFolder_release)
        self.createincludecommand_s3(mb_gcc_compiler=mb_gcc_compiler_v6_release, projectRootDir=v6ProjectRootDir, standalonebsp=v6_standalonebsp_microblaze)
        self.createcompliecommad_s4(projectRootDir=v6ProjectRootDir, configurationFolder=configurationFolder_release, buildFilePath = gitPath + builderFile)
        self.createlinkercommand_s5(projectRootDir=v6ProjectRootDir, configurationFolder=configurationFolder_release, buildFilePath = gitPath + builderFile, mb_gcc_linker=mb_gcc_linker_v6, mb_gcc_linker_miscellaneous=mb_gcc_linker_miscellaneous_processor_options_v6, mb_gcc_linker_software=mb_gcc_linker_software_platform_flags_options_v6, standalonebsp=v6_standalonebsp_microblaze)
        self.setCommand_s6(buildFilePath = gitPath + builderFile)
        binFIlePath = gitPath + "bin/" + configurationFolder_release + "v6"
        if os.path.exists(binFIlePath):
            pass
        else:
            os.makedirs(binFIlePath)
        with open(binFIlePath + "/" + "size.log", "w") as sizeLog:
            generateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            sizeLog.write("[IMPORTANT]: Auto Generated Codes, Please don't edit it mannually." + "\r")
            sizeLog.write("             Generated Time: " + generateTime + "\n" + "\n")
            for j in self.projectList:
                elfPath = v6ProjectRootDir + j + "/" + configurationFolder_release
                os.chdir(gitPath)
                for i in os.listdir(elfPath):
                    if os.path.splitext(i)[1] == '.elf':
                        output = os.popen("mb-size " + "\"" + elfPath + i + "\n")
                        sizeLog.write("*********************************************************************************" + "\r")
                        sizeLogOutput = output.read()
                        sizeLog.write(sizeLogOutput)
                        # os.chdir(elfCheck_ISE)
                        output = os.popen("elfcheck " + elfPath + i + " -hw " + v6_system_xml + " -pe " + "microblaze_0" + "\n")
                        checkSizeOutput = output.read()
                        sizeLog.write(checkSizeOutput)
                        if checkSizeOutput.find("elfcheck passed") >= 0:
                            print("[Check Info] %s Size Check Passed!!!"%(elfPath + i))
                            print("   --File Will Be Moved Into Bin Folder...")
                            shutil.copy2(elfPath + i, binFIlePath)
                        else:
                            print("[Error Info] %s Size Overflow!!!"%(elfPath + i))
                            print("   --File Will Not Be Moved Into Bin Folder...")
                        sizeLog.write("\n")
                        # os.chdir(configFile_ISE.replace("build.config", ""))
        sizeLog.close()

    def buildkucproject(self):
        self.getprojectlist_s1(projectRootDir=kucProjectRootDir)
        self.createprocessfolder_s2(projectRootDir=kucProjectRootDir, configurationFolder=configurationFolder_debug)
        self.createincludecommand_s3(mb_gcc_compiler=mb_gcc_compiler_kuc_debug, projectRootDir=kucProjectRootDir, standalonebsp=kuc_standalonebsp_microblaze)
        self.createcompliecommad_s4(projectRootDir=kucProjectRootDir, configurationFolder=configurationFolder_debug, buildFilePath = gitPath + builderFile)
        self.createlinkercommand_s5(projectRootDir=kucProjectRootDir, configurationFolder=configurationFolder_debug, buildFilePath = gitPath + builderFile, mb_gcc_linker=mb_gcc_linker_kuc, mb_gcc_linker_miscellaneous=mb_gcc_linker_miscellaneous_processor_options_kuc, mb_gcc_linker_software=mb_gcc_linker_software_platform_flags_options_kuc, standalonebsp=kuc_standalonebsp_microblaze)
        self.setCommand_s6(buildFilePath = gitPath + builderFile)
        binFIlePath = gitPath + "bin/" + configurationFolder_debug + "kuc"
        if os.path.exists(binFIlePath):
            pass
        else:
            os.makedirs(binFIlePath)
        with open(binFIlePath + "/" + "size.log", "w") as sizeLog:
            generateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            sizeLog.write("[IMPORTANT]: Auto Generated Codes, Please don't edit it mannually." + "\r")
            sizeLog.write("             Generated Time: " + generateTime + "\n" + "\n")
            for j in self.projectList:
                elfPath = kucProjectRootDir + j + "/" + configurationFolder_debug
                for i in os.listdir(elfPath):
                    if os.path.splitext(i)[1] == '.elf':
                        shutil.copy2(elfPath + i, binFIlePath)
                        output = os.popen("mb-size " + elfPath + i + "\n")
                        sizeLog.write(output.read())
        sizeLog.close()

        self.getprojectlist_s1(projectRootDir=kucProjectRootDir)
        self.createprocessfolder_s2(projectRootDir=kucProjectRootDir, configurationFolder=configurationFolder_release)
        self.createincludecommand_s3(mb_gcc_compiler=mb_gcc_compiler_kuc_release, projectRootDir=kucProjectRootDir, standalonebsp=kuc_standalonebsp_microblaze)
        self.createcompliecommad_s4(projectRootDir=kucProjectRootDir, configurationFolder=configurationFolder_release, buildFilePath = gitPath + builderFile)
        self.createlinkercommand_s5(projectRootDir=kucProjectRootDir, configurationFolder=configurationFolder_release, buildFilePath = gitPath + builderFile, mb_gcc_linker=mb_gcc_linker_kuc, mb_gcc_linker_miscellaneous=mb_gcc_linker_miscellaneous_processor_options_kuc, mb_gcc_linker_software=mb_gcc_linker_software_platform_flags_options_kuc, standalonebsp=kuc_standalonebsp_microblaze)
        self.setCommand_s6(buildFilePath = gitPath + builderFile)
        binFIlePath = gitPath + "bin/" + configurationFolder_release + "kuc"
        if os.path.exists(binFIlePath):
            pass
        else:
            os.makedirs(binFIlePath)
        with open(binFIlePath + "/" + "size.log", "w") as sizeLog:
            generateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            sizeLog.write("[IMPORTANT]: Auto Generated Codes, Please don't edit it mannually." + "\r")
            sizeLog.write("             Generated Time: " + generateTime + "\n" + "\n")
            for j in self.projectList:
                elfPath = kucProjectRootDir + j + "/" + configurationFolder_release
                for i in os.listdir(elfPath):
                    if os.path.splitext(i)[1] == '.elf':
                        shutil.copy2(elfPath + i, binFIlePath)
                        output = os.popen("mb-size " + "\"" + elfPath + i + "\n")
                        sizeLog.write(output.read())
        sizeLog.close()

if __name__ == "__main__":
    for key in os.environ.keys():
        print(key)
    # print(os.getenv('SDK14.7_MGCC'))
    # print(os.getenv('SDK2017.2_MGCC'))
    #print(os.getenv('SDK14.7_MGCC').replace("\\", "/"))
    #print(os.getenv('SDK2017.2_MGCC').replace("\\", "/"))
    print("time:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    builder = Builder()
    builder.buildv6project()
    builder.buildkucproject()
