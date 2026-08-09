def number(bus_stops):
    on_bus = 0
    for on,off in bus_stops:
        on_bus = on_bus + on - off
    return on_bus