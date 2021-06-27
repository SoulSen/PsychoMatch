from dataclasses import dataclass, field


class _MultiStr(str):
    pass


@dataclass
class _User:
    name: str = field(default_factory=str)
    email: str = field(default_factory=str)
    phone_number: str = field(default_factory=str)
    age: int = field(default_factory=int)
    race: _MultiStr = field(default_factory=_MultiStr)
    communication: str = field(default_factory=str)
    doctor_personality: _MultiStr = field(default_factory=_MultiStr)
    meeting: str = field(default_factory=str)
    place_to_meet: str = field(default_factory=str)
    meds: str = field(default_factory=str)
    user_message: str = field(default_factory=str)

    def __init__(self, form):
        for attr in self.__dataclass_fields__.values():
            if attr.type == str:
                setattr(self, attr.name, form.get(attr.name))
            elif attr.type == int:
                setattr(self, attr.name, int(form.get(attr.name)))
            elif attr.type == _MultiStr:
                setattr(self, attr.name, " ".join(form.getlist(attr.name)))


@dataclass
class Patient(_User):
    gender: _MultiStr = field(default_factory=_MultiStr)

    def __init__(self, form):
        super().__init__(form)


@dataclass
class Psychologist(_User):
    gender: str = field(default_factory=str)
    hospital: str = field(default_factory=str)

    def __init__(self, form):
        super().__init__(form)
