test_cases = int(input())
for test_case in range(test_cases) :
    N, K = list(map(int, input().split()))
    grid = {}
    theives_caught = 0
    for row in range(N) :
        line = list(input().split())
        if K >= N :
            policemen = line.count('P')
            theives = line.count('T')

            if theives > policemen :
                theives_caught += policemen
            else :
                theives_caught += theives
        else :
            for cell_number in range(N) :
                k_cell = cell_number
                if (cell_number + K) > N :
                    k_cell = N
                else :
                    k_cell = cell_number + K + 1

                _k_cell = cell_number
                if (cell_number - K) < 0 :
                    _k_cell = 0
                else :
                    _k_cell = cell_number - K
        
                if line[cell_number] == 'P' and line[_k_cell:k_cell].count('T') > 0 :
                    line[cell_number] = 'O'
                    index_theif = line.index('T', _k_cell, k_cell)
                    line[index_theif] = 'O'
                    theives_caught += 1
    print(theives_caught)
