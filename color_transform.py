

def convert(h, s, v):
    i = (h // 60) % 6
    v_min = ((100 - s) * v) / 100
    a = (v - v_min) * ((h % 60) / 60)
    v_inc = v_min + a
    v_dec = v - a
    v = round((v / 100) * 255)
    v_min = round((v_min / 100) * 255)
    v_inc = round((v_inc / 100) * 255)
    v_dec = round((v_dec / 100) * 255)
    if i == 0:
        return (v, v_inc, v_min)
    if i == 1:
        return (v_dec, v, v_min)
    if i == 2:
        return (v_min, v, v_inc)
    if i == 3:
        return (v_min, v_dec, v)
    if i == 4:
        return (v_inc, v_min, v)
    if i == 5:
        return (v, v_min, v_dec)

def rgb_to_string(r, g, b):
    sr = ""
    sg = ""
    sb = ""
    if r < 16:
        sr = f"0{hex(r)[2:]}"
    else:
        sr = hex(r)[2:]
    if g < 16:
        sg = f"0{hex(g)[2:]}"
    else:
        sg = hex(g)[2:]
    if b < 16:
        sb = f"0{hex(b)[2:]}"
    else:
        sb = hex(b)[2:]
    return "#" + sr + sg + sb

def hsv_to_string(h, s, v):
    (r, g, b) = convert(h, s, v)
    return rgb_to_string(r, g, b)

print(rgb_to_string(255, 0, 0))