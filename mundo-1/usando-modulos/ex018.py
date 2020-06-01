from math import sin, cos, tan, radians

ang = int(input('Insira um ângulo aqui: '))

print('Funções trigonométricas resultantes', end=' --> ')
print('Seno: {:.2f}, cosseno: {:.2f} e tangente {:.2f}'.format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))