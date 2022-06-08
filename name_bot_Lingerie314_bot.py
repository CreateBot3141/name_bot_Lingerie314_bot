
def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    import iz_game
    import iz_main
    import time
    import iz_telegram
    
    if message_in == '/start': 
        status = '' 
        iz_telegram.save_variable (user_id,namebot,'status','')
        

    if message_in == 'Отмена': 
        status = '' 
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Отмена",'S',0) 
        iz_telegram.save_variable (user_id,namebot,'status','')

  