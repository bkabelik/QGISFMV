# **********    Properties    **********

# Layer names
Platform_lyr = "Platform"
Beams_lyr = "Beams"
Footprint_lyr = "Footprint"
FrameCenter_lyr = "Frame Center"
FrameAxis_lyr = "Frame Axis"
Trajectory_lyr = "Trajectory"
Point_lyr = "Drawings Point"
Line_lyr = "Drawings Line"
Polygon_lyr = "Drawings Polygon"

# File extensions (first is default)
Exts=["ts","mpeg4","mp4","avi","mpg","H264","mov"]

# Layers EPSG
epsg = 'EPSG:4326'

# Group Name
frames_g = "FMV Georeferenced Frames"

#DTM (Digital terrain Model)
DTM_file = "C:\\Program Files\\KadasAlbireo\\share\\kadas\\dtm_globe.tif"
#Raster square size in pixel that will be loaded from DTM
DTM_buffer_size = 5000

#Reverse geocoding service that transforms point to address
Reverse_geocoding_url="https://nominatim.openstreetmap.org/reverse.php?format=json&lat={}&lon={}"

# FFmpeg path
ffmpeg = "C:\\LegacySW\\kadas-portable_1.2.0.0\\kadas\\opt\\ffmpeg"
ffprobe = "C:\\LegacySW\\kadas-portable_1.2.0.0\\kadas\opt\\ffmpeg"

# Buffer Metadata Reader Size (IMPORTANT : IF THIS VALUE IS VERY HIGH THE PLUGIN WILL FAIL)
min_buffer_size = 8
