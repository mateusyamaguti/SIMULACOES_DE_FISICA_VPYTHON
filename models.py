from vpython import *
from math import ceil

# Problemas:
# 1) Durante um espirro, os olhos podem se fechar por até 0,50 s. Se você está dirigindo um carro a 90km/h e espirra, de
# quanto o carro pode se deslocar até você abrir novamente os olhos?

def deslocation_by_blink_of_an_eye():
    '''
    inter params: blink in seconds and velocity in kilometers by hours
    '''
    blink = 0.50 / 3600
    velocity = 90
    dislocation_by_blink_of_an_eye = velocity * blink
    return dislocation_by_blink_of_an_eye

# 2) Calcule a velocidade média nos dois casos: a) você caminha 73,2 m a uma velocidade de 1,22 m/s e depois corre 73,2 m a 3,05 m/s,
# em uma pista reta; b) você caminha 1,00 min com uma velocidade de 1,22 m/s e depois corre por 1,00 min a 3,05 m/s em uma pista reta.
# c) Faça o gráfico de x em função de t nos dois casos e indique de que forma a velocidade média pode ser determinada a partir do gráfico.

def average_speed_in_walk_and_run_of_73_meters_sub_question_a():
    '''
    inter params: dislocation (m), average_speeds (m/s), total_time (seconds)
    '''
    dislocation = 73.2
    average_walking_speed = 1.22
    average_running_speed = 3.05
    total_time = (dislocation/average_walking_speed) + (dislocation/average_running_speed)
    average_speed_total = dislocation*2/total_time
    return average_speed_total

def average_speed_in_walk_and_run_of_73_meters_sub_question_b():
    '''
    inter params: dislocation (m), average_speeds (m/s) and total_time (seconds)
    '''
    time  = 60
    average_walking_speed = 1.22
    average_running_speed = 3.05
    dislocation_total = (time*average_walking_speed) + (time*average_running_speed)
    average_speed_total = dislocation_total / (time*2)
    return average_speed_total

def average_speed_in_walk_and_run_of_73_meters_sub_question_c():
    particule1 = sphere(pos=vector(0, 0.5, 0), radius=2, color=color.red)
    particule2 = sphere(pos=vector(0, 0.5, 0), radius=2, color=color.green)
    floor = box(pos=vector(80, 0, 0), size=vector(360, 0.5, 10))
    '''Criação de váriavel temporal e passo'''
    dt = 0.01
    t = 0
    '''Velocidade inicial'''
    particule1.velocity = vector(1.22, 0, 0)
    particule2.velocity = vector(1.22, 0, 0)
    '''Gráfico'''
    graph1 = gdisplay(xtitle='tempo (s)', ytitle='deslocamento (m)')
    particule1_trajectory = gcurve(graph=graph1, color=color.red)
    
    graph2 = gdisplay(xtitle='tempo (s)', ytitle='deslocamento (m)')
    particule2_trajectory = gcurve(graph=graph2, color=color.green)
    '''Fator de animação'''
    ft = 10
    '''Criação do laço onde ocorre a animação'''
    while t<84:
        rate(100)
        if particule1.pos.x < 146.4:         
            particule1_trajectory.plot(t*ft, particule1.pos.x)
        
        if particule1.pos.x <= 73.2:
            particule1.pos.x += particule1.velocity.x*dt*ft
            
        elif particule1.pos.x > 73.2 and particule1.pos.x < 146.4:
            particule1.velocity = vector(3.05, 0, 0)
            particule1.pos.x += particule1.velocity.x*dt*ft    
         
        t += dt*ft

    t = 0
    while t<120:
        rate(100)    
        particule2_trajectory.plot(t, particule2.pos.x)
        
        if t <= 60:
            particule2.pos.x += particule2.velocity.x*dt*ft
              
        elif t > 60 and t < 120:
            particule2.velocity = vector(3.05, 0, 0)
            particule2.pos.x += particule2.velocity.x*dt*ft
        
        t += dt*ft

# 3) Um automóvel viaja em uma estrada retilínea por 40 km a 30 km/h. Em seguida. continuando no mesmo sentido, percorre outros 40 km a 
# 60 km/h. (a) Qual é a velocidade média do carro durante esse percurso de 80 km? (Suponha que o carro está se movendo no sentido positivo
# de x.) (b) Qual é a velocidade escalar média? (c) Desenhe o gráfico de x em função de t e mostre como calcular a velocidade média a 
# partir do gráfico.

def question_3_average_speed_over_equal_distances_but_different_speed_a(speed_1 = float, speed_2 = float, distance = 80):
    '''
    inter params: speed (k/h) and distance (km)
    '''
    time_1 = (distance/2) / speed_1
    time_2 = (distance/2) / speed_2
    speed_average = (distance)/(time_1 + time_2)
    return speed_average

def question_3_average_speed_over_equal_distances_but_different_speed_b():
    return question_3_average_speed_over_equal_distances_but_different_speed_a(speed_1 = 30, speed_2 = 60, distance = 80)

def  question_3_average_speed_over_equal_distances_but_different_speed_c():
    car = vector(0, 0, 0)
    car_speed_01 = 30
    car_speed_02 = 60
    t = 0
    dt = 0.01
    graphic = gcurve(color=color.cyan)

    while t <= 2:
        rate(100)
        if car.x <= 40:
            car.x += car_speed_01*dt
            graphic.plot(t, car.x)    
        else:
            car.x += car_speed_02*dt
            graphic.plot(t, car.x)
        t += dt
    return (ceil(car.x))

# 4) Um carro sobe uma ladeira com velocidade constante de 40km/h e desce uma ladeira com uma velocidade de 60km/h. Calcule
# a velocidade escalar média de ida e volta

def question_4_average_speed_over_equal_distances_but_different_speed_and_not_exist_information_distance(speed_1 = 40, speed_2 = 60):
    '''
    inter params: speed (km/h)
    return: average speed (km/h)
    '''
    t_1 = 1/speed_1
    t_2 = 1/speed_2
    average_speed = 2 / (t_1 + t_2)
    return (ceil(average_speed))

# A posição de um objeto que se move ao longo do eixo x é dado por x = 3t -4t² + t³, onde x está em metros e t em segundo. Determine
# a posição do objeto para os seguinte valores de t: (a) 1s, (b) 2s, (c) 3s, (d) 4s. (e) Qual é o deslocamento do objeto entre t=0 e t=4s?
# (f) Qual é a velocidade média para o intervalo de tempo de t=2s a t=4s? (g) Desenhe o gráfico de x em função de t para 0 <= t <= 4s e 
# indique comor resposta do item (f) pode ser determinada a partir do gráfico

def question_5_several_answers_about_position_in_relation_by_time_a_b_c_d(time):
    position = time*3 - (4*(time**2)) + time**3
    return position