import bpy

from .add_modelname import MYADDON_OT_add_modelname

# パネル ファイル名
class OBJECT_PT_model_name(bpy.types.Panel):
    """オブジェクトのファイルネームパネル"""
    bl_idname = "OBJECT_PT_model_name"
    bl_label = "FileName"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    # サブメニューの描画
    def draw(self, context):
        # パネルに項目を追加
        if "model_name" in context.object:
            # すでにプロパティがあればプロパティを表示
            self.layout.prop(context.object, '["model_name"]', text=self.bl_label)
        else:
            # プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_modelname.bl_idname)