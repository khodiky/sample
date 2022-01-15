## https://www.codewars.com/kata/54b72c16cd7f5154e9000457

def decode_bits(bits):

    bits = bits.strip('0')

    x = [x for x in bits.split('0') if x]

    x.sort()

    y = [y for y in bits.split('1') if y]

    y.sort()

    

    if len(y) > 0 and len(y[0]) < len(x[0]):

        unit = y[0]

    else:

        unit = x[0].replace('1','0')

    

    letter = unit

    for a in range(2):

        letter = letter+unit

    

    dot = unit.replace('0','1')

    dash = unit.replace('0','1')

    for c in range(2):

        dash = dash+unit.replace('0','1')

    

    return bits.replace(letter,' ').replace(dash,'-').replace(dot,'.').replace(unit,'')

def decode_morse(morseCode):

    letters = [MORSE_CODE[x] if x != '' else ' ' for x in morseCode.split(' ')]

    return ''.join(letters).replace('  ', ' ').strip()
