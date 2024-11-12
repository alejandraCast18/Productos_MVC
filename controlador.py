from modelo import Modelo

class Controlador():
    def __init__(self, modelo):
        self.modelo = modelo

    def consultar_todo(self):
        info = self.modelo.SelectAll()
        return info

    def insertar(self, cod_pro, nom_pro, mod_pro, pre_pro, can_pro):
        result = self.modelo.Insert(cod_pro, nom_pro, mod_pro, pre_pro, can_pro)
        return result

    def consultar(self, cod_pro):
        info = self.modelo.Select(cod_pro)
        return info

    def actualizar(self, cod_pro, nom_pro, mod_pro, pre_pro, can_pro):
        result = self.modelo.Update(cod_pro, nom_pro, mod_pro, pre_pro, can_pro)
        return result

    def eliminar(self, cod_pro):
        info = self.modelo.Delete(cod_pro)
        return info