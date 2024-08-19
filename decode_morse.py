import os
import datetime
import pandas as pd

# Dicionário de código Morse
dict_morse = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
              "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
              "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
              "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
              "-.--": "Y", "--..": "Z", "-----": "0", ".----": "1", "..---": "2", "...--": "3",
              "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"}

# Função para decodificar código Morse
def decode_morse(msg, dict_morse):
    words = msg.split("  ")  # Palavras separadas por dois espaços
    decoded_msg = []
    for word in words:
        letters = word.split(" ")  # Letras separadas por um espaço
        decoded_word = ''.join(dict_morse.get(letter, '') for letter in letters)
        decoded_msg.append(decoded_word)
    return ' '.join(decoded_msg)

# Função para salvar a mensagem decodificada em um arquivo CSV
def save_clear_msg_csv_hdr(file_path, msg):
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode='a', index=False, header=hdr)

if __name__ == "__main__":
    # Cenários de teste
    scenarios = [
        ('.... . .-.. .-.. ---  .-- --- .-. .-.. -..', 'HELLO WORLD'),
        ('.--. .-. --- .--- . - ---  .-. . .- .-.. .. --.. .- -.. ---', 'PROJETO REALIZADO'),
        ('.-.. .. -. -.-  -.. ---  --. .. - .... ..- -...  -. .-  -.. . ... -.-. .-. .. -.-. .- ---', 'LINK DO GITHUB NA DESCRICAO')
    ]
    
    # Executando os cenários e salvando os resultados
    for morse_code, expected_output in scenarios:
        decoded_message = decode_morse(morse_code, dict_morse)
        save_clear_msg_csv_hdr("decode_morse.csv", decoded_message)
