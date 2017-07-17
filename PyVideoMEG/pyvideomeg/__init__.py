"""Functions for accessing video-MEG audio and video files
    by Andrey Zhdanov (andrey dot zhdanov at aalto dot fi)
    
    Copyright (C) 2014 BioMag Laboratory, Helsinki University Central Hospital

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from .read_data import (AudioData, VideoData, UnknownVersionError, ts2str,
                        repair_file, EvlData, Event)
from .video_writer import OverWriteError, VideoFile
from .comp_tstamps import comp_tstamps
