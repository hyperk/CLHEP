from hkpilot.utils.cmake import CMake

import inspect
import os


class CLHEP(CMake):

    def __init__(self, path):
        super().__init__(path)

        self._package_name = "CLHEP"
        self._package_version = "2.2.0.4"
        # self._download_url = "https://geant4-data.web.cern.ch/releases/geant4-v11.0.2.zip"

        self._cmakelist_path = "source/2.2.0.4/CLHEP"

        self._cmake_options = {
            # "WITH_TLS": "OFF"
        }

        # self._path = os.path.relpath(inspect.getfile(self.__class__))
