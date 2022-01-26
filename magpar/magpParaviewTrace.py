# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'AVS UCD Reader'
a1seg0006inp = AVSUCDReader(registrationName='1seg.0006.inp', FileNames=['C:\\path_to\\file\\1seg.0006.inp'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
a1seg0006inpDisplay = Show(a1seg0006inp, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'M_x'
m_xLUT = GetColorTransferFunction('M_x')
m_xLUT.RGBPoints = [-0.99998539686203, 0.231373, 0.298039, 0.752941, -9.626150131225586e-06, 0.865003, 0.865003, 0.865003, 0.9999661445617676, 0.705882, 0.0156863, 0.14902]
m_xLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'M_x'
m_xPWF = GetOpacityTransferFunction('M_x')
m_xPWF.Points = [-0.99998539686203, 0.0, 0.5, 0.0, 0.9999661445617676, 1.0, 0.5, 0.0]
m_xPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
a1seg0006inpDisplay.Representation = 'Surface'
a1seg0006inpDisplay.ColorArrayName = ['POINTS', 'M_x']
a1seg0006inpDisplay.LookupTable = m_xLUT
a1seg0006inpDisplay.SelectTCoordArray = 'None'
a1seg0006inpDisplay.SelectNormalArray = 'None'
a1seg0006inpDisplay.SelectTangentArray = 'None'
a1seg0006inpDisplay.OSPRayScaleArray = 'M_x'
a1seg0006inpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a1seg0006inpDisplay.SelectOrientationVectors = 'None'
a1seg0006inpDisplay.ScaleFactor = 20.0
a1seg0006inpDisplay.SelectScaleArray = 'M_x'
a1seg0006inpDisplay.GlyphType = 'Arrow'
a1seg0006inpDisplay.GlyphTableIndexArray = 'M_x'
a1seg0006inpDisplay.GaussianRadius = 1.0
a1seg0006inpDisplay.SetScaleArray = ['POINTS', 'M_x']
a1seg0006inpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
a1seg0006inpDisplay.OpacityArray = ['POINTS', 'M_x']
a1seg0006inpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
a1seg0006inpDisplay.DataAxesGrid = 'GridAxesRepresentation'
a1seg0006inpDisplay.PolarAxes = 'PolarAxesRepresentation'
a1seg0006inpDisplay.ScalarOpacityFunction = m_xPWF
a1seg0006inpDisplay.ScalarOpacityUnitDistance = 2.4406900898401664
a1seg0006inpDisplay.OpacityArrayName = ['POINTS', 'M_x']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
a1seg0006inpDisplay.ScaleTransferFunction.Points = [-0.99998539686203, 0.0, 0.5, 0.0, 0.9999661445617676, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
a1seg0006inpDisplay.OpacityTransferFunction.Points = [-0.99998539686203, 0.0, 0.5, 0.0, 0.9999661445617676, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
a1seg0006inpDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=a1seg0006inp)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'm'
calculator1.Function = 'M_x*iHat + M_y*jHat + M_z*kHat'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'M_x']
calculator1Display.LookupTable = m_xLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'M_x'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'm'
calculator1Display.ScaleFactor = 20.0
calculator1Display.SelectScaleArray = 'M_x'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'M_x'
calculator1Display.GaussianRadius = 1.0
calculator1Display.SetScaleArray = ['POINTS', 'M_x']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'M_x']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = m_xPWF
calculator1Display.ScalarOpacityUnitDistance = 2.4406900898401664
calculator1Display.OpacityArrayName = ['POINTS', 'M_x']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-0.99998539686203, 0.0, 0.5, 0.0, 0.9999661445617676, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-0.99998539686203, 0.0, 0.5, 0.0, 0.9999661445617676, 1.0, 0.5, 0.0]

# hide data in view
Hide(a1seg0006inp, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=calculator1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'm']
glyph1.ScaleArray = ['POINTS', 'M_x']
glyph1.ScaleFactor = 20.0
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1
glyph1.ScaleArray = ['POINTS', 'No scale array']

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'M_x']
glyph1Display.LookupTable = m_xLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'M_x'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'm'
glyph1Display.ScaleFactor = 22.075371551513673
glyph1Display.SelectScaleArray = 'M_x'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'M_x'
glyph1Display.GaussianRadius = 1.1037685775756836
glyph1Display.SetScaleArray = ['POINTS', 'M_x']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'M_x']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-0.9999450445175171, 0.0, 0.5, 0.0, 0.9997065663337708, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-0.9999450445175171, 0.0, 0.5, 0.0, 0.9997065663337708, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'M_z'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(m_xLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'M_z'
m_zLUT = GetColorTransferFunction('M_z')
m_zLUT.RGBPoints = [-0.9996507167816162, 0.231373, 0.298039, 0.752941, 0.0001004636287689209, 0.865003, 0.865003, 0.865003, 0.999851644039154, 0.705882, 0.0156863, 0.14902]
m_zLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'M_z'
m_zPWF = GetOpacityTransferFunction('M_z')
m_zPWF.Points = [-0.9996507167816162, 0.0, 0.5, 0.0, 0.999851644039154, 1.0, 0.5, 0.0]
m_zPWF.ScalarRangeInitialized = 1

# hide data in view
Hide(calculator1, renderView1)

# get color legend/bar for m_zLUT in view renderView1
m_zLUTColorBar = GetScalarBar(m_zLUT, renderView1)
m_zLUTColorBar.WindowLocation = 'UpperRightCorner'
m_zLUTColorBar.Title = 'M_z'
m_zLUTColorBar.ComponentTitle = ''

# change scalar bar placement
m_zLUTColorBar.Orientation = 'Horizontal'
m_zLUTColorBar.WindowLocation = 'AnyLocation'
m_zLUTColorBar.Position = [0.3575830013280212, 0.07160804020100503]
m_zLUTColorBar.ScalarBarLength = 0.33000000000000035

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1506, 796)

# current camera placement for renderView1
renderView1.CameraPosition = [381.92783013325726, 17.10696217971447, 212.38193968082277]
renderView1.CameraViewUp = [-0.038251352375837565, 0.9991996987766649, -0.011695982474410633]
renderView1.CameraParallelScale = 113.19231422671771

# save screenshot
SaveScreenshot('C:/path/to/screenshot/magParParaviewTraceScreenshot.png', renderView1, ImageResolution=[1506, 796])

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
renderView1.CameraPosition = [381.92783013325726, 17.10696217971447, 212.38193968082277]
renderView1.CameraViewUp = [-0.038251352375837565, 0.9991996987766649, -0.011695982474410633]
renderView1.CameraParallelScale = 113.19231422671771

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).