q = open("input.txt")
m = q.read()
q.close()
l = open("output.txt", "w+")
m = "'data:image/svg+xml,\n" + m + "'"
m = m.replace("\n", "\\\n")
l.write(f"url({m})")
l.close()