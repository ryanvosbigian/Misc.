import readline
import termios
import subprocess

lines = []
line = str()
lineIndex = 0

subprocess.call(['clear'])

while True:
        try:
                line = raw_input(str(lineIndex)+' | ')
                lineIndex += 1
                if line == 'exit':
                        raise SystemExit
                if (line.split())[0] == '///':
                        lineIndex = int((line.split())[1])
                if (line.split())[0] == 'del///':
                        lines[int(((line.split())[1]))] = None
                if line == '//q':
                        lineIndex += 1
                if line == '//a':
                        lineIndex -= 1
                lines[lineIndex] = line
        except KeyboardInterrupt:
                print ''
        except IndexError:
                pass
        except EOFError:
                print '\n'


#spw-self propelled weaponry-ssh using itself to copy all of it's files into the home dir... really, technically though, anything that contains its means of transport instead of being launched by other means.
