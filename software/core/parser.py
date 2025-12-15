def parse_line(line):
    parts = line.split()
    command = parts[0]
    params = [int(p) for p in parts[1:]]

    return command, params
