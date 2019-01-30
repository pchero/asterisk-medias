# asterisk-medias
pchero's media file repository for the Asterisk test.

# filename
<filename>-<stereotype>_<sampling bit>_<bit rate>_<codec>.<extension>

## example
broken_short-mono_32bit_16khz_amr.amr

filename: brkoen_short
stereo type: mono
sampling bit: 32bit
bit rate: 16khz
codec: amr

# note
## ARI /play support codec
For ARI action /channels/<channel id>/play( https://wiki.asterisk.org/wiki/display/AST/Asterisk+16+Channels+REST+API#Asterisk16ChannelsRESTAPI-play ), the only PCM encoded, 16 bit, mono, 8kHz/16kHz files are supported with a lowercase '.wav' extension. And MP3 codecs.
