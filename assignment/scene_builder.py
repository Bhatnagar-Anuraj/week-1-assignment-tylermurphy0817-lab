import maya.cmds as cmd
cmd.file(new=True, force=True)

#-----------------------------------------------------------------------
# Creates the ground for the scene at (0,0,0)
#-----------------------------------------------------------------------

Wizard_Ground_width = 50
Wizard_Ground_depth = 50
Wizard_Ground_y_position = 0

WizardPlane = cmds.polyPlane(
    name="Wizard_Ground",
    width=Wizard_Ground_width,
    height=Wizard_Ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, Wizard_Ground_y_position, 0, WizardPlane)

#-----------------------------------------------------------------------
# Creates a cube named Wizard_Cabin
#-----------------------------------------------------------------------

WizCabin_width = 5
WizCabin_height = 5
WizCabin_depth = 5
WizCabin_x = 5
WizCabin_z = 5
WizCabin_y = 2.5

Wizard_Cabin = cmds.polyCube(
    name="Wizard_Cabin",
    width=WizCabin_width,
    height=WizCabin_height,
    depth=WizCabin_depth,
)[0]
# Placing the Wizard_Cabin directly on the ground.
cmds.move(WizCabin_x, WizCabin_height / 2.0, WizCabin_z, Wizard_Cabin)

#--------------------------------------------------------------------------------------------------
# The lines named “Wizard_Treetrunk” & “Wizard_Leaves” are for making trees.
#--------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------
# Creates the Wizard_Treetrunk_I
#-----------------------------------------------------------------------

WizTrunk_radius = 1.5
WizTrunk_height = 7.5
WizTrunk_x = 5
WizTrunk_z = -5
WizTrunk_y = 2.5

Wizard_Trunk_I = cmds.polyCylinder(
    name="Wizard_Trunk_I",
    radius=WizTrunk_radius,
    height=WizTrunk_height,
  )[0]
cmds.move(WizTrunk_x, WizTrunk_height / 2.0, WizTrunk_z, Wizard_Trunk_I)

#-----------------------------------------------------------------------
# Creates the Wizard_Leaves_I
#-----------------------------------------------------------------------

WizLeaves_radius = 3
WizLeaves_height = 7.5
WizLeaves_x = 5
WizLeaves_z = -5
WizLeaves_y = 11

Wizard_Leaves_I = cmds.polyCone(
    name="Wizard_Leaves_I",
    radius=WizLeaves_radius,
    height=WizLeaves_height,
  )[0]
cmds.move(WizTrunk_x, WizLeaves_y, WizTrunk_z, Wizard_Leaves_I)
#-----------------------------------------------------------------------
# Creates the Wizard_Treetrunk_II
#-----------------------------------------------------------------------

WizTrunk2_radius = 1.5
WizTrunk2_height = 7.5
WizTrunk2_x = -5
WizTrunk2_z = 5
WizTrunk2_y = 2.5

Wizard_Trunk_II = cmds.polyCylinder(
    name="Wizard_Trunk_II",
    radius=WizTrunk2_radius,
    height=WizTrunk2_height,
  )[0]
cmds.move(WizTrunk2_x, WizTrunk2_height / 2.0, WizTrunk2_z, Wizard_Trunk_II)

#-----------------------------------------------------------------------
# Creates the Wizard_Leaves_II
#-----------------------------------------------------------------------

WizLeaves2_radius = 3
WizLeaves2_height = 7.5
WizLeaves2_x = 5
WizLeaves2_z = -5
WizLeaves2_y = 11

Wizard_Leaves_II = cmds.polyCone(
    name="Wizard_Leaves_II",
    radius=WizLeaves2_radius,
    height=WizLeaves2_height,
  )[0]
cmds.move(WizTrunk2_x, WizLeaves_y, WizTrunk2_z, Wizard_Leaves_II)
