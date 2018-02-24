#!/usr/bin/env python

from os import system

pkgPath = 'com/zandu/util'
srcDir = 'src/' + pkgPath
outDir = 'out/' + pkgPath

primitiveTypes = ["boolean", "byte", "char", "short", "int", "long", "float", "double"]

templates = ['Collection', 'List', 'ArrayList']

system("mkdir -p {out}".format(out = outDir))

for primitive in primitiveTypes:
	for t in templates:
		system("gyb --line-directive= -D PrimitiveType={type} -o {out}/{capitalized}{template}.java {src}/{template}.java.gyb".format(type = primitive, capitalized = primitive.capitalize(), template = t, out = outDir, src = srcDir))
