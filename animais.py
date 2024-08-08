# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:12:58 2024

@author: aleitebr
"""
class Animal:
    # propriedades comuns a todos os animais, segundo o Microsoft Copilot
    CELULAS_EUCARIOTICAS = True
    MULTICELULARIDADE = True
    NUTRICAO_HETEROTROFICA = True
    PAREDE_CELULAR = False
    NOME_CIENTIFICO = 'Reino Animalia'

    def celulas_eucarioticas(self):
        if self.CELULAS_EUCARIOTICAS:
            return True
        else:
            return False
        
    def celulas_procarioticas(self):
        if self.CELULAS_EUCARIOTICAS:
            return False
        else:
            return True
        
    def unicelar(self):
        if self.MULTICELULARIDADE:
            return False
        else:
            return True
        
    def multicelular(self):
        if self.MULTICELULARIDADE:
            return True
        else:
            return False
        
    def nutricao_heterotrofica(self):
        if self.NUTRICAO_HETEROTROFICA:
            return True
        else:
            return False
        
    def nutricao_autotrofica(self):
        if not self.NUTRICAO_HETEROTROFICA:
            return True
        else:
            return False
        
    def ausencia_de_parede_celular(self):
        if not self.PAREDE_CELULAR:
            return True
        else:
            return False
        
    def parede_celular(self):
        if self.PAREDE_CELULAR:
            return True
        else:
            return False
        
    def nome_cientifico(self):
        return self.NOME_CIENTIFICO
    

