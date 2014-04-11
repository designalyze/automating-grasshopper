#Python Workshop Lesson:Automation04
#http://www.designalyze.com/automateGHwithRhinoScript_04

#Automating A Tower Massing and Exporting it to separate files
 
import rhinoscriptsyntax as rs
import Rhino
 
#Load Grasshopper Plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
 
#SetSliderValue("GUID",Number)
#BakeDateInObject("GUID")
 
rs.EnableRedraw(True)
 
#set working directory
workingDir = rs.BrowseForFolder(None, "Pick a foler to save your files in")
rs.WorkingFolder(workingDir)
 
#create variable for file naming
num = 0
 
for i in range(1,3,1):
    #BaseSize Slider
    gh.SetSliderValue("adf54977-006a-4877-9e67-81d736ff07de",i)
    for j in range(0,4,1):
        #Rotation Slider
        gh.SetSliderValue("061dd51d-3d85-4a32-8aaa-0e6ba809ed75",j)
        for k in range(3,5,1):
            #NumberOfSides Slider
            gh.SetSliderValue("b46e0b0e-643d-4b3a-8a96-c6d4e120e4dd",k)
            gh.RunSolver("TowerOptionsAutomation.gh")
            baked = gh.BakeDataInObject("72628cf1-020e-425d-9746-6f323f8882f8")
            transVect = (12*i, 12*j, 12*(k-2))
            rs.MoveObject(baked,transVect)
 
 
            #convert to string and add filename
            strNum = str(num)
            filename = "myFileTest" + strNum + ".igs"
 
            #call a bunch of rhino commands to do selection and export
            rs.Command("_SelNone", True)
            rs.Command("_SelLast", True)
            rs.Command("_-Export " + filename + " _Enter", True)
            rs.Command("_SelNone", True)
 
            #increment the filename
            num = num + 1
