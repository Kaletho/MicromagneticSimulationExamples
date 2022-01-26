# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Structured Grid Reader'
m000000vts = XMLStructuredGridReader(registrationName='m000000.vts', FileName=['C:\\path\\to\\file.out\\m000000.vts'])
m000000vts.PointArrayStatus = ['m']

# Properties modified on m000000vts
m000000vts.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
m000000vtsDisplay = Show(m000000vts, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
m000000vtsDisplay.Representation = 'Outline'
m000000vtsDisplay.ColorArrayName = [None, '']
m000000vtsDisplay.SelectTCoordArray = 'None'
m000000vtsDisplay.SelectNormalArray = 'None'
m000000vtsDisplay.SelectTangentArray = 'None'
m000000vtsDisplay.OSPRayScaleArray = 'm'
m000000vtsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
m000000vtsDisplay.SelectOrientationVectors = 'm'
m000000vtsDisplay.ScaleFactor = 1.979999950663114e-08
m000000vtsDisplay.SelectScaleArray = 'None'
m000000vtsDisplay.GlyphType = 'Arrow'
m000000vtsDisplay.GlyphTableIndexArray = 'None'
m000000vtsDisplay.GaussianRadius = 9.89999975331557e-10
m000000vtsDisplay.SetScaleArray = ['POINTS', 'm']
m000000vtsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
m000000vtsDisplay.OpacityArray = ['POINTS', 'm']
m000000vtsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
m000000vtsDisplay.DataAxesGrid = 'GridAxesRepresentation'
m000000vtsDisplay.PolarAxes = 'PolarAxesRepresentation'
m000000vtsDisplay.ScalarOpacityUnitDistance = 3.901592465424459e-09

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
m000000vtsDisplay.ScaleTransferFunction.Points = [-0.9999912977218628, 0.0, 0.5, 0.0, 0.9999911785125732, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
m000000vtsDisplay.OpacityTransferFunction.Points = [-0.9999912977218628, 0.0, 0.5, 0.0, 0.9999911785125732, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=m000000vts)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'm2'
calculator1.Function = 'm.m'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Outline'
calculator1Display.ColorArrayName = ['POINTS', '']
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'm2'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'm'
calculator1Display.ScaleFactor = 1.979999950663114e-08
calculator1Display.SelectScaleArray = 'm2'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'm2'
calculator1Display.GaussianRadius = 9.89999975331557e-10
calculator1Display.SetScaleArray = ['POINTS', 'm2']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'm2']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 3.901592465424459e-09

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0000003043481183, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0000003043481183, 1.0, 0.5, 0.0]

# hide data in view
Hide(m000000vts, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=calculator1)
threshold1.Scalars = ['POINTS', 'm2']
threshold1.ThresholdRange = [0.0, 1.0000003043481183]

# Properties modified on threshold1
threshold1.ThresholdRange = [0.010000003043481183, 1.0000003043481183]

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'm2'
m2LUT = GetColorTransferFunction('m2')
m2LUT.RGBPoints = [0.9999997491958628, 0.231373, 0.298039, 0.752941, 1.0000000267719904, 0.865003, 0.865003, 0.865003, 1.0000003043481183, 0.705882, 0.0156863, 0.14902]
m2LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'm2'
m2PWF = GetOpacityTransferFunction('m2')
m2PWF.Points = [0.9999997491958628, 0.0, 0.5, 0.0, 1.0000003043481183, 1.0, 0.5, 0.0]
m2PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['POINTS', 'm2']
threshold1Display.LookupTable = m2LUT
threshold1Display.SelectTCoordArray = 'None'
threshold1Display.SelectNormalArray = 'None'
threshold1Display.SelectTangentArray = 'None'
threshold1Display.OSPRayScaleArray = 'm2'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'm'
threshold1Display.ScaleFactor = 1.979999950663114e-08
threshold1Display.SelectScaleArray = 'm2'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'm2'
threshold1Display.GaussianRadius = 9.89999975331557e-10
threshold1Display.SetScaleArray = ['POINTS', 'm2']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'm2']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = m2PWF
threshold1Display.ScalarOpacityUnitDistance = 4.56416774602697e-09
threshold1Display.OpacityArrayName = ['POINTS', 'm2']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [0.9999997491958628, 0.0, 0.5, 0.0, 1.0000003043481183, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [0.9999997491958628, 0.0, 0.5, 0.0, 1.0000003043481183, 1.0, 0.5, 0.0]

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=threshold1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'm']
glyph1.ScaleArray = ['POINTS', 'm2']
glyph1.ScaleFactor = 1.979999950663114e-08
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1
glyph1.ScaleArray = ['POINTS', 'No scale array']

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'm2']
glyph1Display.LookupTable = m2LUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'm2'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'm'
glyph1Display.ScaleFactor = 2.2991986714515636e-08
glyph1Display.SelectScaleArray = 'm2'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'm2'
glyph1Display.GaussianRadius = 1.1495993357257816e-09
glyph1Display.SetScaleArray = ['POINTS', 'm2']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'm2']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.9999998243634824, 0.0, 0.5, 0.0, 1.0000002789732303, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.9999998243634824, 0.0, 0.5, 0.0, 1.0000002789732303, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'm', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(m2LUT, renderView1)

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'm'
mLUT = GetColorTransferFunction('m')
mLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5000000760870238, 0.865003, 0.865003, 0.865003, 1.0000001521740476, 0.705882, 0.0156863, 0.14902]
mLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'm'
mPWF = GetOpacityTransferFunction('m')
mPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0000001521740476, 1.0, 0.5, 0.0]
mPWF.ScalarRangeInitialized = 1

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'm', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
glyph1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(mLUT, glyph1Display)

# hide data in view
Hide(calculator1, renderView1)

# hide data in view
Hide(threshold1, renderView1)

# get color legend/bar for mLUT in view renderView1
mLUTColorBar = GetScalarBar(mLUT, renderView1)
mLUTColorBar.WindowLocation = 'UpperRightCorner'
mLUTColorBar.Title = 'm'
mLUTColorBar.ComponentTitle = 'Z'

# change scalar bar placement
mLUTColorBar.Orientation = 'Horizontal'
mLUTColorBar.WindowLocation = 'AnyLocation'
mLUTColorBar.Position = [0.32571049136786195, 0.0829145728643216]
mLUTColorBar.ScalarBarLength = 0.3299999999999998

# Properties modified on renderView1
renderView1.EnableRayTracing = 1

# Properties modified on renderView1
renderView1.EnableRayTracing = 0

# change scalar bar placement
mLUTColorBar.Position = [0.31575033200531216, 0.07537688442211055]
mLUTColorBar.ScalarBarLength = 0.3299999999999998

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1506, 796)

# current camera placement for renderView1
renderView1.CameraPosition = [5.941660937421882e-07, 6.54087686162723e-08, 5.114301572408239e-07]
renderView1.CameraFocalPoint = [5.694907982978493e-08, 3.7693742800437774e-08, 8.96189535763861e-08]
renderView1.CameraViewUp = [-0.02548127810882554, 0.9991240342866591, -0.03319440580416537]
renderView1.CameraParallelScale = 1.2084286869128692e-07

# save screenshot
SaveScreenshot('C:/path/to/file/traceScreenShot.png', renderView1, ImageResolution=[1506, 796])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1506, 796)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [5.941660937421882e-07, 6.54087686162723e-08, 5.114301572408239e-07]
renderView1.CameraFocalPoint = [5.694907982978493e-08, 3.7693742800437774e-08, 8.96189535763861e-08]
renderView1.CameraViewUp = [-0.02548127810882554, 0.9991240342866591, -0.03319440580416537]
renderView1.CameraParallelScale = 1.2084286869128692e-07

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).