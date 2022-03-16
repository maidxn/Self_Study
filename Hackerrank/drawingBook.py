numberOfPages = int(input())
destinationPage = int(input())

begin = destinationPage // 2
end = (numberOfPages - destinationPage) // 2
end = 1 if destinationPage == numberOfPages - 1 and destinationPage % 2 == 1 else end

if destinationPage == 0 or destinationPage == 1:
    begin = 0
if destinationPage == numberOfPages:
    end = 0

print(begin if begin < end else end)

# My way is a little bit long, and here is the solution
if numberOfPages % 2 == 0:
    numberOfPages += 1
print(min(destinationPage // 2, (numberOfPages - destinationPage) // 2))

# Just three lines :O OMG, the problem here is I made everything too complicate ;;-;;
# The condition for begin is not neccessary.
# Page always starts from 1, and 1 // 2 equal 0 so don't mind about it.



