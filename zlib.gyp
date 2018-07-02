{
    # ==========================================================================
    #   Includes
    # ==========================================================================
    'includes': [ '../config.gypi' ],

    # ==========================================================================
    #   Variables
    # ==========================================================================
    'variables': {
        'public_include_dirs': [
            'include',
            'include/zlib', # for legacy support
        ], # public_include_dirs
    }, # variables

    # ==========================================================================
    #   Target Defaults
    # ==========================================================================
    'target_defaults': {
        'direct_dependent_settings': {
            'include_dirs': [
                '<@(public_include_dirs)',
            ], # include_dirs
        }, # direct_dependent_settings

        'include_dirs': [
            '<@(public_include_dirs)',
        ], # include_dirs

        'sources': [
            'include/zlib/zconf.h',
            'include/zlib/zlib.h',
            'source/adler32.c',
            'source/compress.c',
            'source/crc32.c',
            'source/crc32.h',
            'source/deflate.c',
            'source/deflate.h',
            'source/gzclose.c',
            'source/gzguts.h',
            'source/gzlib.c',
            'source/gzread.c',
            'source/gzwrite.c',
            'source/infback.c',
            'source/inffast.c',
            'source/inffast.h',
            'source/inffixed.h',
            'source/inflate.c',
            'source/inflate.h',
            'source/inftrees.c',
            'source/inftrees.h',
            'source/trees.c',
            'source/trees.h',
            'source/uncompr.c',
            'source/zutil.c',
            'source/zutil.h',
        ], # sources
    }, # target_defaults

    # ==========================================================================
    #   Targets
    # ==========================================================================
    'targets': [
        # ----------------------------------------------------------------------
        #  Library Targets
        # ----------------------------------------------------------------------
        {
            'target_name': 'zlib',
            'type': 'static_library',
            'xcode_config_file': 'zlib_mac.xcconfig',
        }, # zlib

        # ----------------------------------------------------------------------

        {
            'target_name': 'zlib_ios',
            'conditions': [ ['OS=="mac"', { 'type': 'static_library' }, { 'type': 'none' } ] ],
            'xcode_config_file': 'zlib_ios.xcconfig',
        }, # zlib_ios

        # ----------------------------------------------------------------------
    ], # targets
}
