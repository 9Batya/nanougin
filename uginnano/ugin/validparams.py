from django.core.exceptions import ValidationError
import ipaddress
import re

"""
Валидация параметров, используется в формах и модели Device, валидируются типы данных, MAC, ip. Входные данные
device_type_id, parametrs, device_model экземпляра Device
"""


class valid:
    def __init__(self, device_type_id, parametrs, devicemodel):
        self.device_type_id = device_type_id
        self.parametrs = parametrs
        self.device_model = devicemodel

    # Из-за того, что deviceform выдает строки, нужно их конвертировать
    def convert(self):
        for key, value in self.parametrs.items():
            if value.lower() == 'true':
                self.parametrs[key] = True
            elif value.lower() == 'false':
                self.parametrs[key] = False
            try:
                value = int(value)
                self.parametrs[key] = value
            except ValueError:
                pass

    # Валидация
    def validation(self):
        regexmac = re.compile(r'^[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:'
                              r'[a-z0-9]{2}:[a-z0-9]{2}$')
        data = self.device_type_id.parametr_names.values_list('parametr_name', 'parametr_type')
        name_type_dict = dict(data)
        for key, value in self.parametrs.items():
            if value:
                # чтобы при ошибке не удалялось значение device_model
                self.device_model = self.device_model
                if key in name_type_dict:
                    if name_type_dict[key] == 'int' and not isinstance(value, int):
                        raise ValidationError(f'Значение для параметра "{key}" должно быть числом')
                    elif name_type_dict[key] == 'str' and not isinstance(value, str):
                        raise ValidationError(f'Значение для параметра "{key}" должно быть строкой')
                    elif name_type_dict[key] == 'bool' and not isinstance(value, bool):
                        raise ValidationError(f'Значение для параметра "{key}" должно быть булевым')
                if key == 'MAC':
                    match = regexmac.search(value)
                    if not match:
                        raise ValidationError(f'Значение "{value}" не соответствует виду aa:aa:aa:aa:aa:aa')
                elif key == 'ip':
                    try:
                        ipaddress.ip_address(value)
                    except Exception as exp:
                        raise ValidationError(f'Ошибка: "{exp}"')
        return {'status': 'sucsess'}
