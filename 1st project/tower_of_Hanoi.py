moves = 0
def solve_tower(n, start_pole, end_pole, help_pole):
    global moves

    if n == 1:
        moves += 1
        print(f'Move disk: {n} from tower: {start_pole} to tower: {end_pole}')
    else:
        moves += 1
        # move n-1 disks to the help_pole in order to free the last disk
        solve_tower(n-1, start_pole, help_pole, end_pole) 

        print (f'Move disk: {n} from tower: {start_pole} to tower: {end_pole}')
        
        # move back the disks from the help_pole to the end_pole in order to complete the tower
        solve_tower(n-1, help_pole, end_pole, start_pole) 

disks = int(input('Please enter the number of disks: '))
solve_tower(disks, 'A', 'B', 'C')
print(f'\nTotal moves: {moves}')