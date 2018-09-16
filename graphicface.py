# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sample.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpetruse <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/16 15:29:03 by mpetruse          #+#    #+#              #
#    Updated: 2018/09/16 15:42:54 by mpetruse         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#'''A simple graphics example constructs a face from basic shapes.
#'''

from graphics import *


def main():
    win = GraphWin('Face', 200, 150) # give title and dimensions
    #win.yUp() # make right side up coordinates!

    head = Circle(Point(50,100), 35) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(35, 90), 7)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(55, 90), Point(70, 90)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(38, 115), Point(65, 125)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(130, 130), 'my first graphical face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()
