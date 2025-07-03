from PyQt5.QtCore import Qt

#! Object Dock Widgets ====================================================================================================
from app.ui.widgets.dock_widgets.object_dock_widgets.media_object_dock_widget import MediaObjectDockWidget
from app.ui.widgets.dock_widgets.object_dock_widgets.audio_object_dock_widget import AudioObjectDockWidget
from app.ui.widgets.dock_widgets.object_dock_widgets.effect_object_dock_widget import EffectObjectDockWidget
from app.ui.widgets.dock_widgets.object_dock_widgets.filter_object_dock_widget import FilterObjectDockWidget
from app.ui.widgets.dock_widgets.object_dock_widgets.transition_object_dock_widget import TransitionObjectDockWidget
from app.ui.widgets.dock_widgets.object_dock_widgets.text_object_dock_widget import TextObjectDockWidget

#! Player Dock Widgets ====================================================================================================
from app.ui.widgets.dock_widgets.player_dock_widgets.preview_player_dock_widget import PreviewPlayerDockWidget
from app.ui.widgets.dock_widgets.player_dock_widgets.asset_player_dock_widget import AssetPlayerDockWidget

#! Property Dock Widgets ====================================================================================================
from app.ui.widgets.dock_widgets.property_dock_widgets.global_property_dock_widget import GlobalPropertyDockWidget
from app.ui.widgets.dock_widgets.property_dock_widgets.video_property_dock_widget import VideoPropertyDockWidget
from app.ui.widgets.dock_widgets.property_dock_widgets.audio_property_dock_widget import AudioPropertyDockWidget
from app.ui.widgets.dock_widgets.property_dock_widgets.effect_property_dock_widget import EffectPropertyDockWidget
from app.ui.widgets.dock_widgets.property_dock_widgets.filter_property_dock_widget import FilterPropertyDockWidget
from app.ui.widgets.dock_widgets.property_dock_widgets.transition_property_dock_widget import TransitionPropertyDockWidget
from app.ui.widgets.dock_widgets.property_dock_widgets.image_property_dock_widget import ImagePropertyDockWidget
from app.ui.widgets.dock_widgets.property_dock_widgets.text_property_dock_widget import TextPropertyDockWidget

#! Editor Dock Widgets ====================================================================================================
from app.ui.widgets.dock_widgets.editor_dock_widgets.timeline_editor_dock_widget import TimelineEditorDockWidget
from app.ui.widgets.dock_widgets.editor_dock_widgets.video_editor_dock_widget import VideoEditorDockWidget
from app.ui.widgets.dock_widgets.editor_dock_widgets.audio_editor_dock_widget import AudioEditorDockWidget
from app.ui.widgets.dock_widgets.editor_dock_widgets.key_editor_dock_widget import KeyEditorDockWidget
from app.ui.widgets.dock_widgets.editor_dock_widgets.text_editor_dock_widget import TextEditorDockWidget
from app.ui.widgets.dock_widgets.editor_dock_widgets.image_editor_dock_widget import ImageEditorDockWidget

class DockWidgetRegistry:
    def __init__(self):

        self.dock_areas = {
            "object": Qt.TopDockWidgetArea,
            "player": Qt.TopDockWidgetArea,
            "property": Qt.TopDockWidgetArea,
            "editor": Qt.BottomDockWidgetArea,
        }

        self.object = {
            "media": MediaObjectDockWidget(),
            "audio": AudioObjectDockWidget(),
            "effect": EffectObjectDockWidget(),
            "filter": FilterObjectDockWidget(),
            "transition": TransitionObjectDockWidget(),
            "text": TextObjectDockWidget(),
        }

        self.player = {
            "preview": PreviewPlayerDockWidget(),
            "asset": AssetPlayerDockWidget(),
        }

        self.property = {
            "global": GlobalPropertyDockWidget(),
            "video": VideoPropertyDockWidget(),
            "audio": AudioPropertyDockWidget(),
            "effect": EffectPropertyDockWidget(),
            "filter": FilterPropertyDockWidget(),
            "transition": TransitionPropertyDockWidget(),
            "image": ImagePropertyDockWidget(),
            "text": TextPropertyDockWidget(),
        }

        self.editor = {
            "timeline": TimelineEditorDockWidget(),
            "video": VideoEditorDockWidget(),
            "audio": AudioEditorDockWidget(),
            "key": KeyEditorDockWidget(),
            "text": TextEditorDockWidget(),
            "image": ImageEditorDockWidget(),
        }
