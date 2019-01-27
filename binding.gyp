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
    
    'conditions': [
      ['OS == "mac"', {
        'include_dirs': [
          'System/Library/Frameworks/CoreFoundation.Framework/Headers',
          'System/Library/Frameworks/Carbon.Framework/Headers',
          'System/Library/Frameworks/ApplicationServices.framework/Headers',
          'System/Library/Frameworks/OpenGL.framework/Headers',
        ],
        'link_settings': {
          'libraries': [
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
        'defines': ['IS_WINDOWS']
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