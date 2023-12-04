class Quality:
    def __init__(self, cable):
        self.cable = cable

    def calculate_quality(self):
        if self.cable is not None and self.cable.num_of_strands != 0:
            return self.cable.diameter / self.cable.num_of_strands
        else:
            return None


class Cable:
    def __init__(self, cable_type, num_of_strands, diameter):
        self.cable_type = cable_type
        self.num_of_strands = num_of_strands
        self.diameter = diameter


if __name__ == "__main__":
    cable_sample = Cable(cable_type="Тип кабеля", num_of_strands=7, diameter=2.5)

    quality_instance = Quality(cable=cable_sample)

    quality_value = quality_instance.calculate_quality()

    # Выводим результат
    if quality_value is not None:
        print(f"Качество: {quality_value}")
    else:
        print("Невозможно определить качество без правильно установленного кабеля.")


class QualityLevel2(Quality):
    def __init__(self, cable, has_braid):
        super().__init__(cable)
        self.has_braid = has_braid

    def calculate_quality(self):
        # получение Q
        q_value = super().calculate_quality()

        # Проверка на оплеткуgi
        if self.has_braid:
            return 2 * q_value if q_value is not None else None
        else:
            return 0.7 * q_value if q_value is not None else None


if __name__ == "__main__":
    cable_sample_lvl1 = Cable(cable_type="Тип кабеля", num_of_strands=7, diameter=2.5)

    quality_instance_lvl1 = Quality(cable=cable_sample_lvl1)

    quality_value_lvl1 = quality_instance_lvl1.calculate_quality()

    quality_instance_lvl2 = QualityLevel2(cable=cable_sample_lvl1, has_braid=True)

    quality_value_lvl2 = quality_instance_lvl2.calculate_quality()

    if quality_value_lvl1 is not None:
        print(f"Качество уровня 1: {quality_value_lvl1}")
    else:
        print("Невозможно определить качество уровня 1 без правильно установленного кабеля.")

    if quality_value_lvl2 is not None:
        print(f"Качество уровня 2: {quality_value_lvl2}")
    else:
        print("Невозможно определить качество уровня 2 без правильно установленного кабеля.")
