import pygame

from asset_manager import AssetManager

pygame.init()

assets = AssetManager()

print()

print("Face:", assets.get_face())

print()

print("Olhos esquerdos:")
print(assets.eyes["left"].keys())

print()

print("Olhos direitos:")
print(assets.eyes["right"].keys())

print()

print("Sobrancelhas:")
print(assets.eyebrows["left"].keys())

print()

print("Bocas:")
print(assets.mouth["emotions"].keys())

print()

print("Visemas:")
print(assets.mouth["visemes"].keys())
