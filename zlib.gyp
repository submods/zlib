{
    # ==========================================================================
    #   Includes
    # ==========================================================================
    'includes': [ '../config.gypi' ],

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

            'variables': {
                'public_include_dirs': [
                    'include',
                    'include/zlib', # for legacy support
                ], # public_include_dirs
            }, # variables

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
        }, # zlib

        # ----------------------------------------------------------------------
    ], # targets
}
