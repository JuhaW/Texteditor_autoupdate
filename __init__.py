bl_info = {
	"name": "Text Editor Auto Updating",
	"author": "Kabu, JuhaW",
	"version": (1, 0, 0, 0),
	"blender": (2, 91, 0),
	"category": "Text",
	"location": "",
	"description": "Autoupdate external text files",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "https://blender.stackexchange.com/questions/107291/how-to-reload-all-text-editor-scripts-at-once", }

import bpy

def text_reload():
	""" Check modified external scripts in the scene and update if possible
	"""
	ctx = bpy.context.copy()
	#Ensure	 context area is not None
	ctx['area'] = ctx['screen'].areas[0]
	for t in bpy.data.texts:
		if t.is_modified and not t.is_in_memory:
			print("Updating external script:", t.name)
			# Change current context to contain a TEXT_EDITOR
			oldAreaType = ctx['area'].type
			ctx['area'].type = 'TEXT_EDITOR'
			ctx['edit_text'] = t
			bpy.ops.text.resolve_conflict(ctx, resolution='RELOAD')
			#Restore context
			ctx['area'].type = oldAreaType

	return 1



def register():
	bpy.app.timers.register(text_reload, persistent=True)
	print ("--- text editor autoupdate registered ---")
	
def unregister():
	bpy.app.timers.unregister(text_reload)
	
if __name__ == "__main__":
	register()