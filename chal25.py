# decode the morse code messages
filename = 'input25.txt'
morse_code = 'morse_code.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

messages = []
cur_message = []
for l in ls:
    if l != '            ':
        cur_message.append(l)
    else:
        messages.append(cur_message.copy())
        cur_message = []
messages.append(cur_message.copy())

# read in the morse alphabet
to_morse = dict()
from_morse = dict()
with open(morse_code) as f:
    ls = f.read().strip().split('\n')
for l in ls:
    c, code = (l.split('|'))
    code = code.strip()
    to_morse[c] = code
    from_morse[code] = c

def timeDelta(t0, t1):
    temp_t0 = list(t0.split(':'))
    end = temp_t0.pop()
    end = list(end.split('.'))
    temp_t0.extend(end)
    h0, m0, s0, ms0 = list(map(int, temp_t0))
    temp_t1 = list(t1.split(':'))
    end = temp_t1.pop()
    end = list(end.split('.'))
    temp_t1.extend(end)
    h1, m1, s1, ms1 = list(map(int, temp_t1))
    tms0 = ms0 + s0 * 1000 + m0 * 60000 + h0 * 3600000
    tms1 = ms1 + s1 * 1000 + m1 * 60000 + h1 * 3600000
    return(tms1 - tms0)

message_delays = []
for m in messages:
    cur_times = []
    last_time = ''
    while len(m) > 0:
        t0 = m.pop(0)
        t1 = m.pop(0)
        if last_time != '':
            cur_times.append(f"up:{timeDelta(last_time, t0)}")
        cur_times.append(f"down:{timeDelta(t0, t1)}")
        last_time = t1
    message_delays.append(cur_times)

messages = []
for m in message_delays:
    message = []
    cur_letter = []
    start_letter = True
    for d in m:
        if start_letter:
            cur_letter = []
            start_letter = False
        state, time = (d.split(':'))
        if state == 'up' and time == '5019':
            # space between words
            message.append(from_morse[''.join(cur_letter)])
            message.append(' ')
            start_letter = True
        elif state == 'up' and time == '2151':
            # start next letter
            message.append(from_morse[''.join(cur_letter)])
            start_letter = True
        elif state == 'down' and time == '717':
            # dot
            cur_letter.append('.')
        elif state == 'down' and time == '2151':
            # dash
            cur_letter.append('-')
        elif state == 'up' and time == '717':
            # pause between dot/dash
            continue
        else:
            print(f"Error: no condition for state={state} and time={time}")
    message.append(from_morse[''.join(cur_letter)])
    print(''.join(message))
    messages.append(''.join(message))

