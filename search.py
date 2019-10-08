import os, urllib.parse, sys
filename = 'http://www.google.com/search?' + urllib.parse.urlencode({'q': ' '.join(sys.argv[1:]) })
cmd = os.popen("lynx -dump %s" % filename)
output = cmd.read()
cmd.close()
print(output)