# Executar as funções
import models

print('*-'*30)
print('CHOOSE A QUESTION ANSWER FROM 1 OUT OF 60'.center(60))
print('*-'*30,'\n\n')
print('')

questions_dictionary = {1 : models.deslocation_by_blink_of_an_eye,
                        2: [models.average_speed_in_walk_and_run_of_73_meters_sub_question_a, 
                            models.average_speed_in_walk_and_run_of_73_meters_sub_question_b]}



if __name__ == '__main__':

    chosen_question = int(input('Choose a question: '))

    if chosen_question == 1:
        answer = questions_dictionary[1]()
        print(f'Descolamento de {answer:.3f} quilometro.')
    
    if chosen_question == 2:
        answer = ''
        choose_sub_question = str(input('choose a sub question: a, b, or c? '))
        if choose_sub_question == 'a':
            answer = questions_dictionary[2][0]()
            print(f'Velocidade média total do trajeto {answer:.2f} m/s')
        if choose_sub_question == 'b':
            answer = questions_dictionary[2][1]()
            print(f'Velocidade média total do trajeto {answer:.2f} m/s')