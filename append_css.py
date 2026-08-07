with open('sim_utils.css', 'r') as f1:
    utils = f1.read()
with open('css/styles.css', 'a') as f2:
    f2.write('\n' + utils)
