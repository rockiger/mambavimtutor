"""A VIM tutor file for Mamba"""
__pluginname__ = "VIM Tutor"
__author__ = "Marco Laspe"
__credits__ = ["Andrei Kopats", "Bryan A. Jones"]
__license__ = "GPL3"
__version__ = "0.1.0"
__maintainer__ = "Marco Laspe"
__email__ = "marco@rockiger.com"
__status__ = "Beta"
# This plugin is a copy of the Enki vimtutor plugin
# https://github.com/andreikop/enki/tree/master/enki/plugins/vimtutor

import os.path

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

from enki.core.core import core


class Plugin:

    def __init__(self):
        self._action = core.actionManager().addAction('mHelp/aVimTutor',
                                                      'Vim mode tutorial',
                                                      QIcon.fromTheme("vim"))
        self._action.triggered.connect(self._onTriggered)

    def terminate(self):
        core.actionManager().removeAction(self._action)

    def _onTriggered(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'vimtutor.md'))
        try:
            with open(path) as vimtutor_file:
                text = vimtutor_file.read()
        except Exception as ex:
            QMessageBox.warning(core.mainWindow(),
                                "Failed to read vimtutor text",
                                str(ex))
            return

        document = core.workspace().createEmptyNotSavedDocument()
        document.qutepart.text = text
        document.qutepart.detectSyntax(language='Markdown')
