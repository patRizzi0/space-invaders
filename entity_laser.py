def laser(x,y):
    return {
        "v_x": 0.0,
        "v_y": 0.0,
        "x": x,
        "y": y,
        # @Patrick
        # État du laser : True = en vol/visible, False (au sommet) = rechargé.
        "is_fired": False
    }