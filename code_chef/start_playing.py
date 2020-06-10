import os

os.system("firefox codechef.com/problems/school &")
print("opening firefox....")
print("Problem ID: ", end = '')
problem_id = input()

print("Problem name: ", end = '')
problem_name = input()

os.system("touch {}.py".format(problem_id))

os.system("echo '#Problem ID: {} \n#Problem Name: {}' | cat > {}.py".format(problem_id, problem_name, problem_id))

os.system("gnome-terminal -- vim {}.py".format(problem_id))

