import bpy

# オペレータ カスタムプロパティ['file_name']追加
class MYADDON_OT_add_modelname(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_add_modelname"
    bl_label = "ModelName 追加"
    bl_description = "['model_name']カスタムプロパティを追加します"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # ['model_name']カスタムプロパティを追加
        context.object["model_name"] = ""

        return {"FINISHED"}