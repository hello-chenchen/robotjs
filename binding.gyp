{
  'targets': [{
    'target_name': 'robotjs',
    'include_dirs': [ #COMMENT: 'include_dirs': The directories in which included header files live. These will be passed in on compilation command lines (using -I or /I options).
        "<!(node -e \"require('nan')\")"
    ],
    
    #LINK: https://gcc.gnu.org/onlinedocs/gcc-3.4.4/gcc/Warning-Options.html
    'cflags': [
      '-Wall', 
      '-Wparentheses',
      '-Winline', # warn if function not inline.
      '-Wbad-function-cast',
      '-Wdisabled-optimization'
    ],
    
    #COMMENT: 'conditions': A list of condition specifications that can modify the contents of the items in the global dictionary defined by this .gyp file based on the values of different variablwes. As implied by the above example, the most common use of a conditions section in the top-level dictionary is to add platform-specific targets to the targets list.
    'conditions': [
      ['OS == "mac"', {
        'include_dirs': [
          'System/Library/Frameworks/CoreFoundation.Framework/Headers',
          'System/Library/Frameworks/Carbon.Framework/Headers',
          'System/Library/Frameworks/ApplicationServices.framework/Headers',
          'System/Library/Frameworks/OpenGL.framework/Headers',
        ],
        #COMMENT: A dictionary of settings to be applied to targets in which this target's contents are linked. executable and shared_library targets are linkable, so if they depend on a non-linkable target such as a static_library, they will adopt its link_settings. This section can contain anything found within a target dictionary, except configurations, target_name, and type sections. Compare all_dependent_settings and direct_dependent_settings.
        'link_settings': { #COMMENT: link_settings, which contains settings that should be applied when a target’s object files are used as linker input.
          'libraries': [ #COMMENT: 	A list of list of libraries (and/or frameworks) on which this target depends.
            '-framework Carbon',
            '-framework CoreFoundation',
            '-framework ApplicationServices',
            '-framework OpenGL'
          ]
        }
      }],
      
      ['OS == "linux"', {
        'link_settings': {
          'libraries': [
            '-lpng',
            '-lz',
            '-lX11',
            '-lXtst'
          ]
        },
        
        'sources': [
          'src/xdisplay.c'
        ]
      }],

      ["OS=='win'", {
        #COMMENT: 'defines': The C preprocessor definitions that will be passed in on compilation command lines (using -D or /D options).
        'defines': ['IS_WINDOWS'] #COMMENT: defines: A list of preprocesor definitions to be passed on the command line to the C/C++ compiler (via -D or /D options).
      }]
    ],
    
    'sources': [
      'src/robotjs.cc',
      'src/deadbeef_rand.c',
      'src/mouse.c',
      'src/keypress.c',
      'src/keycode.c',
      'src/screen.c',
      'src/screengrab.c',
      'src/snprintf.c',
      'src/MMBitmap.c'
    ]
  }]
}