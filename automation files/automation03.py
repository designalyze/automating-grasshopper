#Python Workshop Lesson:Automation03
#http://www.designalyze.com/automateGHwithRhinoScript_03

#Automating A Tower Massing
 
import rhinoscriptsyntax as rs
import Rhino
 
#Load Grasshopper Plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
 
#SetSliderValue("GUID",Number)
#BakeDateInObject("GUID")
 
rs.EnableRedraw(True)
 
for i in range(1,6,1):
    #BaseSize Slider
    gh.SetSliderValue("GUID_FOR_SLIDER_1",i)
    for j in range(0,11,1):
        #Rotation Slider
        gh.SetSliderValue("GUID_FOR_SLIDER_2",j)
        for k in range(3,7,1):
            #NumberOfSides Slider
            gh.SetSliderValue("GUID_FOR_SLIDER_3",k)
            gh.RunSolver("FILENAME.gh")
            baked = gh.BakeDataInObject("GUID_FOR_BAKE_OBJECT")
            transVect = (12*i, 12*j, 12*(k-2))
            rs.MoveObject(baked,transVect)
