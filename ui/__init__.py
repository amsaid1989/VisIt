# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

from VisIt.ui.main_panel import MainPanel
from VisIt.ui.project_settings import ProjectSettings
from VisIt.ui.scene_manager import SceneManager, SCENE_MANAGER_UL_vis_it_scenes
from VisIt.ui.object_library import ObjectLibrary
from VisIt.ui.camera_library import CameraLibrary
from VisIt.ui.render_manager import RenderManager

classes = [
    MainPanel,
    ProjectSettings,
    SceneManager,
    SCENE_MANAGER_UL_vis_it_scenes,
    ObjectLibrary,
    CameraLibrary,
    RenderManager
]