#Unrolling Surfaces with Python
 
import rhinoscriptsyntax as rs
import Rhino

#Load Grasshopper Plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")

#Turn off Redraw
rs.EnableRedraw(False)

#Values for GH Sliders
uv = 5
sides = 6
row = uv*uv
#spacing for nesting
offset = 0.25

#Set Sliders Based on Values above
gh.SetSliderValue("SLIDER_GUID", uv)
gh.SetSliderValue("SLIDER_GUID", sides)

#Run it and Bake it
gh.RunSolver("GRASSHOPPERFILENAME.gh")
baked = gh.BakeDataInObject("BAKEDOBJECT_GUID")


#Create an empty list for nesting purposes
#and define the origin for translations
moved = []
origin = [0,0,0]

#Create a couple of Variable for our loop to increment
#We use these to keep track of the rows/columns we are on
columncount = 0
biggestY = 0
totalX = 0

#Iterate through the baked objects
for item in baked:
    #unroll the surfaces and join them.
    #delet the ones we don't need
    unrolltemp = rs.UnrollSurface(item, False)
    joined = rs.JoinSurfaces(unrolltemp)
    rs.DeleteObjects(unrolltemp)
    
    #Get the bounding box
    #Bounding Box returns pts we create an empty points list
    boxpts = []
    boxpts = rs.BoundingBox(joined)
    #Get the distance for the x and y values of the box
    xdist = rs.Distance(boxpts[0],boxpts[1])
    ydist = rs.Distance(boxpts[1],boxpts[2])
    #Check to see if the ydist is the biggest in the row
    #we use this to space our rows
    if ydist > biggestY:
        biggestY = ydist
    #create a bounding polyine
    #not necessary but help see the border
    polyline = rs.AddPolyline(boxpts[0:4])
    
    #define endpoint of xmove vector
    xpt = [xdist+offset,0,0]
    #set totalX
    totalX = totalX + xdist + offset
    #define xmove vector
    xmove = rs.VectorCreate(origin,xpt)
    #add objects to the moved list
    moved.append(joined)
    moved.append(polyline)
    #move all the objects
    rs.MoveObjects(moved,xmove)
    #increment the column count
    columncount += 1
    
    #check to see if the columncount is evenly divisible by the row
    #if it is we need to move the column
    if columncount % row == 0:
        #get the biggestY value and add the offset
        #I call this the formfeed (like a typewriter)
        formfeed = biggestY + offset
        #That makes this the carrigeReturn
        #Ding!
        carrigeReturn = [-totalX,formfeed,0]
        move = rs.VectorCreate(origin,carrigeReturn)
        #We then move all the objects back and reset the
        #biggestY and totalX values
        rs.MoveObjects(moved,move)
        biggestY = 0
        totalX = 0


#finally we delete the baked objects
rs.DeleteObjects(baked)

