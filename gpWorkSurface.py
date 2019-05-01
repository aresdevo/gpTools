import bpy

'''
Copyright (C) 2018 Ares Deveaux


Created by Ares Deveaux

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# Addon Info
bl_info = {
    "name": "gpWorkSurface",
    "description": "",
    "author": "Ares Deveaux",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "WIEW_3D > Properties window",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Paint"}
    
    
def to_plane(context, gp, gp_plane):
    
    bpy.ops.object.mode_set(mode='OBJECT', toggle=True)

    bpy.context.view_layer.objects.active = gp_plane
    gp_plane.select_set(state=True)
    gp.select_set(state=False)
    

def from_plane(context, gp, gp_plane):
    
    bpy.context.view_layer.objects.active = gp
    gp.select_set(state=True)
    gp_plane.select_set(state=False)
    bpy.ops.object.mode_set(mode='PAINT_GPENCIL', toggle=True)
    
    
class GPWS_OT_add_gp_plane(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "gpencil.add_plane"
    bl_label = "Add GP Plane"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (ob.type == 'GPENCIL' and ob.mode == 'PAINT_GPENCIL')

    def execute(self, context):
        if 'gp_plane' in bpy.context.scene.objects.keys():
            return {'FINISHED'}
        
        gp = context.object

        bpy.ops.object.mode_set(mode='OBJECT', toggle=True)
        
        bpy.ops.mesh.primitive_plane_add(size=10, enter_editmode=True)
        bpy.ops.mesh.subdivide(number_cuts=4)
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X')

        bpy.ops.object.mode_set(mode='OBJECT', toggle=True)
        gp_plane = context.object
        gp_plane.name = 'gp_plane'

        gp_plane.show_all_edges = True
        gp_plane.show_wire = True

        
        from_plane(context, gp, gp_plane)
        
        bpy.context.scene.tool_settings.gpencil_stroke_placement_view3d = 'SURFACE'
        bpy.context.object.data.zdepth_offset = 0.00001
        
        return {'FINISHED'}
    
    
class GPWS_OT_remove_gp_plane(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "gpencil.remove_plane"
    bl_label = "Remove GP Plane"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (ob.type == 'GPENCIL' and ob.mode == 'PAINT_GPENCIL')

    def execute(self, context):
        if 'gp_plane' not in bpy.context.scene.objects.keys():
            return {'FINISHED'}
        gp = context.object
        gp_plane = bpy.data.objects['gp_plane']

        to_plane(context, gp, gp_plane)
        
        bpy.ops.object.delete()
        
        bpy.context.view_layer.objects.active = gp
        gp.select_set(state=True)
        bpy.ops.object.mode_set(mode='PAINT_GPENCIL', toggle=True)
        
        return {'FINISHED'}


class GPWS_OT_rotate_gp_plane(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "gpencil.rotate_plane"
    bl_label = "Rotate"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (ob.type == 'GPENCIL' and ob.mode == 'PAINT_GPENCIL')

    def execute(self, context):
        gp = context.object
        gp_plane = bpy.data.objects['gp_plane']

        to_plane(context, gp, gp_plane)
        
        bpy.ops.transform.rotate('INVOKE_DEFAULT')
        
        from_plane(context, gp, gp_plane)
        
        return {'FINISHED'}
    
    
class GPWS_OT_reset_rotation_gp_plane(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "gpencil.reset_rotation"
    bl_label = "Reset Rot"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (ob.type == 'GPENCIL' and ob.mode == 'PAINT_GPENCIL')

    def execute(self, context):
        gp = context.object
        gp_plane = bpy.data.objects['gp_plane']
        
        to_plane(context, gp, gp_plane)
        
        gp_plane.rotation_euler = 0, 0, 0
        
        from_plane(context, gp, gp_plane)
        
        return {'FINISHED'}
    
    
class GPWS_OT_move_gp_plane(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "gpencil.move_plane"
    bl_label = "Move"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (ob.type == 'GPENCIL' and ob.mode == 'PAINT_GPENCIL')

    def execute(self, context):
        gp = context.object
        gp_plane = bpy.data.objects['gp_plane']
        
        to_plane(context, gp, gp_plane)
        
        bpy.ops.transform.translate('INVOKE_DEFAULT')
        
        from_plane(context, gp, gp_plane)
        
        return {'FINISHED'}
    
    
class GPWS_OT_reset_location_gp_plane(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "gpencil.reset_location"
    bl_label = "Reset Loc"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (ob.type == 'GPENCIL' and ob.mode == 'PAINT_GPENCIL')

    def execute(self, context):
        gp = context.object
        gp_plane = bpy.data.objects['gp_plane']
        
        to_plane(context, gp, gp_plane)
        
        gp_plane.location = 0, 0, 0
        
        from_plane(context, gp, gp_plane)
        
        return {'FINISHED'}
    
    
class GPWS_OT_scale_gp_plane(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "gpencil.scale_plane"
    bl_label = "Scale"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (ob.type == 'GPENCIL' and ob.mode == 'PAINT_GPENCIL')

    def execute(self, context):
        gp = context.object
        gp_plane = bpy.data.objects['gp_plane']
        
        to_plane(context, gp, gp_plane)
        
        bpy.ops.transform.resize('INVOKE_DEFAULT')
        
        from_plane(context, gp, gp_plane)
        
        return {'FINISHED'}
    
    
class GPWS_OT_reset_scale_gp_plane(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "gpencil.reset_scale"
    bl_label = "Reset Scale"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (ob.type == 'GPENCIL' and ob.mode == 'PAINT_GPENCIL')

    def execute(self, context):
        gp = context.object
        gp_plane = bpy.data.objects['gp_plane']
        
        to_plane(context, gp, gp_plane)
        
        gp_plane.scale = 1, 1, 1
        
        from_plane(context, gp, gp_plane)
        
        return {'FINISHED'}
    
    
class GPWS_PT_helper_gp_plane(bpy.types.Panel):
    bl_label = "GP WorkSurface"
    bl_idname = "GPWS_PT_helper_plane"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'GPW surface'

    def draw(self, context):
        if 'gp_plane' not in bpy.context.scene.objects.keys():
            layout = self.layout
        
            col = layout.column(align=True)
            col.operator("gpencil.add_plane",  icon='VIEW_PERSPECTIVE')
            
        else:
            
            gp_plane = bpy.data.objects['gp_plane']
            
            layout = self.layout
            
            col = layout.column(align=True)
            row = col.row()
            row.operator("gpencil.move_plane", icon='RESTRICT_SELECT_OFF', text='')
            row.operator("gpencil.rotate_plane", icon='FILE_REFRESH', text='')
            row.operator("gpencil.scale_plane", icon='FULLSCREEN_ENTER', text='')
            row.prop(gp_plane, 'show_wire', icon='VIEW_ORTHO', text='')
            row.prop(gp_plane, 'hide_viewport', text='')
            row.operator("gpencil.remove_plane",  icon='TRASH', text='')
            
            col = layout.column(align=True)
            col.prop(gp_plane, 'location')
            col.operator("gpencil.reset_location")
            
            col = layout.column(align=True)
            col.prop(gp_plane, 'rotation_euler')
            col.operator("gpencil.reset_rotation")
            
            col = layout.column(align=True)
            col.prop(gp_plane, 'scale')
            col.operator("gpencil.reset_scale")
        
        
classes = (
            GPWS_OT_rotate_gp_plane,
            GPWS_OT_move_gp_plane,
            GPWS_OT_scale_gp_plane,
            GPWS_PT_helper_gp_plane,
            GPWS_OT_reset_rotation_gp_plane,
            GPWS_OT_reset_location_gp_plane,
            GPWS_OT_reset_scale_gp_plane,
            GPWS_OT_add_gp_plane,
            GPWS_OT_remove_gp_plane
            )


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
    
