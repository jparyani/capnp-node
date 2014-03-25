{
  'targets': [
    {
      'target_name': 'v8capnp',
      'sources': ['lib/v8capnp.cc'],
      'libraries': ['-lkj', '-lkj-async', '-lcapnp', '-lcapnpc', '-lcapnp-rpc'],
      "cflags_cc": [
        "-std=c++11"
      ],
      'cflags_cc!': [ '-fno-rtti' ],
      'conditions': [
        [ 'OS=="mac"', {

          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS' : ['-std=c++11','-stdlib=libc++'],
            'OTHER_LDFLAGS': ['-stdlib=libc++'],
            'GCC_ENABLE_CPP_RTTI': 'YES',
            'MACOSX_DEPLOYMENT_TARGET': '10.7'
            },

        }],
      ]
    }
  ]
}
