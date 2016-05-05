#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Works on python 2.7, designed only to run on Windows OS
	(so far only, I will make it work on Python 3 and Linux)
	
	Desafia a responder repetidamente e calculos de matematica (soma no caso), medindo
	quantidade de acertos e erros, tempo para responder acerto, e outras estatisticas a
	acrescentar.
"""

import msvcrt
import random
import sys
import time

__author__      = "Alejandro Mesias"
__copyright__   = 'Copyright 2016, Projeto: "Vamos brincar de calcular"'
__license__     = "LGPL"
__email__       = "meszias at gmail dot com"

print "Vamos brincar de matematica"

contador_acertos = 0
contador_erros = 0
maximo_tentativas = 3
numero_maximo = 9
tempo_resposta_acerto = []

while 1:
	a = random.randint(0, numero_maximo)
	max_b = numero_maximo - a
	b = random.randint(0, max_b)
	
	calculado = a + b
	espaco = "" if calculado > 9 else " "	
	#ra = msvcrt.getch()
	tempo_inicio = time.time()
	tentativas = 0
	while tentativas < maximo_tentativas:
		print "Calcule: %2d + %2d = %s" % (a, b, espaco),
		tecla_a = msvcrt.getche()	
		if tecla_a == '\n':
			break
		
		if calculado > 9:
			tecla_b = msvcrt.getche()
			digitado = int(tecla_a + tecla_b)
		else:
			digitado = int(tecla_a)
					
		if digitado == calculado:
			contador_acertos += 1			
			tempo_fim = time.time() - tempo_inicio
			tempo_resposta_acerto.append(tempo_fim)
			tempo_medio = sum(tempo_resposta_acerto) / len(tempo_resposta_acerto)
			print " Correto!     %.2f/%.2f [%d/%d]" % \
					(tempo_fim, tempo_medio, contador_acertos, contador_erros),		
			time.sleep(1)
			sys.stdout.write("\r")
			print " " * 32,
			sys.stdout.write("\r")
			break
		else:
			tentativas += 1
			sys.stdout.write("\x07")
			contador_erros += 1
			print " Errado! Tentativa (%d de %d) Correto: %2d (digitado: %2d)" % (tentativas, maximo_tentativas, calculado, digitado)
			time.sleep(1)
			
			