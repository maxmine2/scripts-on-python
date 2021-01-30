START_NUMBER = int(input('Enter start 4-digit number>>')[:4])
TARGET_NUMBER = 9009

current_num = [ elm for elm in str(START_NUMBER) ]

tries = 0

print(f'Start: {START_NUMBER}, Target: {TARGET_NUMBER}')

while True:
    tries += 1
    print(f'Step {tries}. Before {current_num}', end=' ')

    sm = 0
    mod_numbs = ""

    for each_numb in current_num:
        sm += int(each_numb)
    elems = current_num

    for i in range(len(elems) - 1):
        elems[i] = elems[i+1]
    
    elems[-1] = str(sm)[-1]
    
    current_num = elems
    print(f'After: {current_num}')
    if current_num == [ elm for elm in str(START_NUMBER)]:
        print(f'Start number reached in {tries} steps')
        break
    elif current_num == [ elm for elm in str(TARGET_NUMBER)]:
        print(f'Reahced target number in {tries} steps')
        break