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
    gh.SetSliderValue("adf54977-006a-4877-9e67-81d736ff07de",i)
    for j in range(0,11,1):
        #Rotation Slider
        gh.SetSliderValue("061dd51d-3d85-4a32-8aaa-0e6ba809ed75",j)
        for k in range(3,7,1):
            #NumberOfSides Slider
            gh.SetSliderValue("b46e0b0e-643d-4b3a-8a96-c6d4e120e4dd",k)
            gh.RunSolver("TowerOptionsAutomation.gh")
            baked = gh.BakeDataInObject("72628cf1-020e-425d-9746-6f323f8882f8")
            transVect = (12*i, 12*j, 12*(k-2))
            rs.MoveObject(baked,transVect)
