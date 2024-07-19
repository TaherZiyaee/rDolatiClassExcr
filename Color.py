class Color:
    def __init__(self,rgb,name):
        self._rgb=rgb
        self._name=name

    def _get_rgb(self):
        return self._rgb
    def _set_rgb(self,rgb):
        self._rgb=rgb

    def _get_name(self):
        return self._name
    def _set_name(self,name):
        if name:
            self._name=name
        else:
            raise ValueError(f"Invalid name {name!r}")

    name=property(_get_name,_set_name)
    rgb=property(_get_rgb,_set_rgb)

c1=Color(0x3374ff,"blue")
print(c1._get_name())
print(c1._get_rgb())
c1._set_rgb(0x3374ff)
c1._set_name("red")
print(c1._get_name())
print(c1._get_rgb())

print('-'*40)

c2=Color(0x9c2de8,"purple")
print(c2.name)
c2.name="pink"
c2.rgb=0xe77ed2
print(c2.name)
print(c2.rgb)