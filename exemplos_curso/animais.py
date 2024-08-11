# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:12:58 2024

@author: aleitebr

Última Atualização: 9 de Agosto de 2024, Quinta-Feira, 07:55h
"""
class Animal:
    # propriedades comuns a todos os animais, segundo o Microsoft Copilot
    CELULAS_EUCARIOTICAS = True
    MULTICELULARIDADE = True
    NUTRICAO_HETEROTROFICA = True
    PAREDE_CELULAR = False
    NOME_CIENTIFICO = 'Reino Animalia'

    # encapsulamento das propriedades
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
    
class Mamifero(Animal):
    # propriedades comuns a todos os animais mamíferos, segundo o Microsoft Copilot
    GLANDULAS_MAMARIAS = True
    PELOS = True
    DENTES_DIFERENCIADOS = True
    DIAFRAGMA = True # uma membrana muscular que separa o tórax do abdome e auxilia na ventilação dos pulmões
    HOMEOTERMIA = True # os mamíferos são homeotérmicos, ou seja, conservam a temperatura interior independente do ambiente onde estão
    CEREBRO = 'Desenvolvido'
    CAVIDADES_CORACAO = 4
    
    def possuem_glandulas_mamarias(self):
        if self.GLANDULAS_MAMARIAS:
            return True
        else:
            return False
    
    def possuem_pelos(self):
        if self.PELOS:
            return True
        else:
            return False
        
    def possuem_dentes_diferenciados(self):
        if self.DENTES_DIFERENCIADOS:
            return True
        else:
            return False
        
    def possuem_diafragma(self):
        if self.DIAFRAGMA:
            return True
        else:
            return False
        
    def sao_homeotermicos(self):
        if self.HOMEOTERMIA:
            return True
        else:
            return False
        
    def cerebro(self):
        return self.CEREBRO
    
    def cavidades_coracao(self):
        return self.CAVIDADES_CORACAO

class Anfibio(Animal):
    # propriedades comuns a todos os animais anfíbios, segundo o Microsoft Copilot
    pass

class Cachorro(Mamifero):
    # propriedades comuns a todos os cachorros, segundo o Microsoft Copilot
    pass

class Homem(Mamifero):
    # propriedades comuns a todos os homens
    GENEROS = ['M', 'F'] # neste caso específico, gênero não se confunde com orientação sexual, esse exemplo é para propósitos científicos
    NOME_CIENTIFICO = 'Homo Sapiens'
    genero = None
    
    def __init__(self, genero):
        if genero in self.GENEROS:
            self.genero = genero
        else:
            raise ValueError('Gênero desconhecido!')
        
    def generoo(self):
        return self.genero
    
    def nome_cientifico(self):
        return self.NOME_CIENTIFICO
        
class Sapo(Anfibio):
    # propriedades comuns a todos os sapos, segundo o Microsoft Copilot    
    pass

class Salamandras(Anfibio):
    # propriedades comuns a todas as salamandras, segundo o Microsoft Copilot
    pass