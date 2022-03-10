students, subjects = map(int, input().split())
score = []
for subject in range(subjects):
    score.append(list(map(float, input().split())))

print(*list((sum(i) / len(i)) for i in zip(*score)), sep='\n')
# When using zip(* array), it means auto create zip for that
# I don't know how to explain, but, give a matrix, then use zip(* matrix)
# => new matrix, transpose matrix, or somethings likes that
