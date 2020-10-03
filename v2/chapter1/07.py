import string

def gen_sentence(x=12, y='気温', z=22.4):
    tmpl = '$x時の$yは$z'
    template = string.Template(tmpl)
    return template.substitute({'x': x, 'y': y, 'z': z})

print(gen_sentence())
