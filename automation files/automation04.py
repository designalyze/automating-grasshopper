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
    gh.SetSliderValue("GUID_FOR_SLIDER_1",i)
    for j in range(0,4,1):
        #Rotation Slider
        gh.SetSliderValue("GUID_FOR_SLIDER_2",j)
        for k in range(3,5,1):
            #NumberOfSides Slider
            gh.SetSliderValue("GUID_FOR_SLIDER_3",k)
            gh.RunSolver("FILENAME.gh")
            baked = gh.BakeDataInObject("GUID_FOR_BAKE_OBJECT")
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
