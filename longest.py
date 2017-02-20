# -*- coding: utf-8 -*-

import os, sys
import subprocess
import re


NAME_LIMIT = 10


def usage():
    print 'Usage: python', sys.argv[0], '<platform>'
    print '<platform> may be iPhoneOS, MacOSX or WatchOS'


def outputLongestNames(title, names):
    print 'Longest', title
    print '----------------'
    names = sorted(names, key=lambda item: len(item), reverse=True)
    for name in names[:NAME_LIMIT]:
        print '* [%02d] %s' % (len(name), name)
    print


if __name__ == '__main__':
    # Determine platform
    plat = ''
    if (len(sys.argv) > 1):
        plat = sys.argv[1].lower()
    
    platform_map = {
        'iphoneos': ('iPhoneOS', 'arm64'),
        'macosx': ('MacOSX', 'x86_64'),
        'watchos': ('WatchOS', 'armv7k'),
    }

    if plat not in platform_map:
        usage()
        exit(1)

    platform_name, arch = platform_map[plat]
    
    print 'Longest Names For', platform_name, arch
    print '================'
    print
    
    # SDK and frameworks root dir
    sdk_root = subprocess.check_output(['xcrun', '--sdk', plat, '--show-sdk-path']).strip()
    frameworks_root = os.path.join(sdk_root, 'System/Library/Frameworks')
    
    # Import all frameworks in one .h file
    all_headers = ''
    for framework_dir in os.listdir(frameworks_root):
        framework, ext = os.path.splitext(framework_dir)
        if ext == '.framework':
            header_path = os.path.join(frameworks_root, framework_dir, 'Headers', framework + '.h')
            if os.path.exists(header_path):
                all_headers += '#import <%s/%s.h>\n' % (framework, framework)
    
    import_filename = 'ImportAll.h'
    with open(import_filename, 'w') as import_file:
        import_file.write(all_headers)
    
    # Extract AST for all frameworks with command:
    #   clang -isysroot */SDKs/iPhoneSimulator7.0.sdk -Xclang -ast-dump -fblocks -x objective-c ImportAll.h
    FNULL = open(os.devnull, 'w')
    p = subprocess.Popen(['xcrun', 'clang',
                          '-isysroot', sdk_root,
                          '-Xclang',
                          '-ast-dump',
                          '-fblocks',
                          '-x', 'objective-c',
                          '-arch', arch,
                          import_filename],
                          stdout=subprocess.PIPE,
                          stderr=FNULL)
    
    ast, _ = p.communicate()
    os.remove(import_filename)
    
    # Remove console color codes
    ast = re.sub(r'\x1B\[[0-9;]*[mK]', '', ast)
    
    # Remove @class declarations to exclude internal interfaces.
    # In AST, @class is a standalone ObjCInterfaceDecl node without child node.
    ast = re.sub(r'\|-ObjCInterfaceDecl.+\n\|-', '|-', ast)
    
    #with open('output.txt', 'w') as output:
    #    output.write(ast)
    
    # Find longest names for each type
    types = [
        ('ObjCInterfaceDecl',  'Objective-C Interface Names'),
        ('ObjCProtocolDecl',   'Objective-C Protocol Names'),
        ('ObjCPropertyDecl',   'Objective-C Property Names'),
        ('ObjCMethodDecl',     'Objective-C Method Names'),
        ('FunctionDecl',       'C Function Names'),
        ('EnumDecl',           'Enum Names'),
        ('EnumConstantDecl',   'Enum Constant Names'),
        ('VarDecl',            'Variable Constant Names'),
    ]
    
    for type, title in types:
        names = set()
        for m in re.finditer(r'\b' + type + r'.*\<.*\>.*?(?::\d+){1,2}[\s+-]+(\S+)', ast):
            names.add(m.group(1))
        outputLongestNames(title, names)
    
        # Method names with 0 or 1 parameter
        if type == 'ObjCMethodDecl':
            short_names = [k for k in names if k.find(':', 0, len(k)-1) == -1]
            outputLongestNames(title + ' (0/1 Parameter)', short_names)
