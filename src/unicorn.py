#!/usr/bin/env python
'''
Copyright (c) 2010 MakerBot Industries

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''
import inkex
from math import *
from unicorn.context import GCodeContext
from unicorn.svg_parser import SvgParser

class MyEffect(inkex.Effect):
  def __init__(self):
    inkex.Effect.__init__(self)
    self.arg_parser.add_argument("--pen-up-angle", type=float,
                      dest="pen_up_angle", default="50.0",
                      help="Pen Up Angle")
    self.arg_parser.add_argument("--pen-down-angle", type=float,
                      dest="pen_down_angle", default="30.0",
                      help="Pen Down Angle")
    self.arg_parser.add_argument("--start-delay", type=float,
                      dest="start_delay", default="150.0",
                      help="Delay after pen down command before movement in milliseconds")
    self.arg_parser.add_argument("--stop-delay", type=float,
                      dest="stop_delay", default="150.0",
                      help="Delay after pen up command before movement in milliseconds")
    self.arg_parser.add_argument("--xy-feedrate", type=float,
                      dest="xy_feedrate", default="3500.0",
                      help="XY axes feedrate in mm/min")
    self.arg_parser.add_argument("--z-feedrate", type=float,
                      dest="z_feedrate", default="150.0",
                      help="Z axis feedrate in mm/min")
    self.arg_parser.add_argument("--z-height", type=float,
                      dest="z_height", default="0.0",
                      help="Z axis print height in mm")
    self.arg_parser.add_argument("--finished-height", type=float,
                      dest="finished_height", default="0.0",
                      help="Z axis height after printing in mm")
    self.arg_parser.add_argument("--register-pen", type=str,
                      dest="register_pen", default="true",
                      help="Add pen registration check(s)")
    self.arg_parser.add_argument("--x-home", type=float,
                      dest="x_home", default="0.0",
                      help="Starting X position")
    self.arg_parser.add_argument("--y-home", type=float,
                      dest="y_home", default="0.0",
                      help="Starting Y position")
    self.arg_parser.add_argument("--num-copies", type=int,
                      dest="num_copies", default="1")
    self.arg_parser.add_argument("--continuous", type=str,
                      dest="continuous", default="false",
                      help="Plot continuously until stopped.")
    self.arg_parser.add_argument("--pause-on-layer-change", type=str,
                      dest="pause_on_layer_change", default="false",
                      help="Pause on layer changes.")
    self.arg_parser.add_argument("--tab", type=str, dest="tab")

  def effect(self):
    self.context = GCodeContext(self.options.xy_feedrate, self.options.z_feedrate, 
                           self.options.start_delay, self.options.stop_delay,
                           self.options.pen_up_angle, self.options.pen_down_angle,
                           self.options.z_height, self.options.finished_height,
                           self.options.x_home, self.options.y_home,
                           self.options.register_pen,
                           self.options.num_copies,
                           self.options.continuous,
                           self.options.input_file)
    parser = SvgParser(self.document.getroot(), self.options.pause_on_layer_change)
    parser.parse()
    for entity in parser.entities:
      entity.get_gcode(self.context)
    
    MyEffect.save_raw(self, self.context.generate())


if __name__ == '__main__':   #pragma: no cover
  MyEffect().run()
