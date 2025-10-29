class SagaError(Exception):
    """Error de ejecución de la saga"""
    pass


class SagaBuilder:
    def __init__(self):
        self.steps = []

    @classmethod
    def create(cls):
        return cls()

    def action(self, do_func, compensate_func):
        """Agrega una acción con su compensación"""
        self.steps.append((do_func, compensate_func))
        return self

    def build(self):
        return SagaExecutor(self.steps)


class SagaExecutor:
    def __init__(self, steps):
        self.steps = steps

    def execute(self):
        ejecutadas = []
        try:
            for do_func, _ in self.steps:
                do_func()
                ejecutadas.append((do_func, _))
        except Exception as e:
            # Si algo falla, se ejecutan las compensaciones en orden inverso
            for _, compensate_func in reversed(ejecutadas):
                try:
                    compensate_func()
                except Exception as ce:
                    print(f"Error al compensar: {ce}")
            raise SagaError(f"Error en saga: {e}")
