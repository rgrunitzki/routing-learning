# -*- coding: utf-8 -*-
'''
Created on Nov 23, 2013

@author: rgrunitzki
'''
from controller.Simulation import Simulation
from controller.QLearning import QLearning


port = 8813
grid = True
interface = False



if __name__ == '__main__':
    #sumo parameters    
    isGrid = grid
    
    net_directory = ''
    net_directory_shell = ''
    net_file = ''
    if(isGrid):
        net_directory = '../network/grid/'
        net_directory_shell = '../network/grid/'
        net_file = 'slice_regulated.net.xml'
    else:
        vehicles = '36606'
        net_directory = '../network/siouxfalls/'+ vehicles + '/'
        net_directory_shell = '../network/siouxfalls/'+ vehicles +'/'
        net_file = 'sioux_falls.net.xml'
    
    cfg_file = 'sumo.cfg.xml'
    route_file ='rou.xml'
    
    
    show_interface = interface
    traci_port = port
    summary_file = net_directory+'/summary/10/summary_'
    sumo_options = '-S -Q --no-step-log --remote-port '+str(traci_port) +' --summary-output '+ summary_file
    show_log = True
    max_steps = 152
    #QLearning parameters
    episodes = 500
    epislon = 0.1
    epislon_rate = 0.995
    alpha = 0.5
    gamma = 0.95
    
    qlearning = QLearning(episodes, alpha, gamma, epislon, epislon_rate)
    
    simulation = Simulation(net_directory, net_directory_shell, cfg_file, net_file, route_file, show_interface, 
                            traci_port, sumo_options, qlearning, show_log, max_steps)
    simulation.run()