from tkinter import *
from tkinter import ttk

tclsh = Tcl()
s = """\
puts {Hello World}
puts "Hello, World!"
puts "Hello World!"
set name 6
puts "{hello $name}"
set x 10
set y 20

apply {{a b} {
    puts "x: $a, y: $b"
}} $x $y

set comm "{} {return $name}"
puts $comm
# set comm $comm
# puts $comm
puts [apply $comm]

puts =====

set comm "{z} {return \[expr $name + \$z\]}"
puts $comm
set comm $comm
puts $comm
puts [apply $comm 2]

puts =====

set comm "{z} {return \[expr $name+\$z\]}"
puts $comm
puts [apply $comm 2]

set _ {
    Hello, World!
    Hello World!
    {hello 6}
    x: 10, y: 20
    {} {return 6}
    6
    =====
    {z} {return [expr 6 + $z]}
    {z} {return [expr 6 + $z]}
    8
    =====
    {z} {return [expr 6+$z]}
    8
}

if { [catch { exec ls *.* } msg] } {
   puts "Something seems to have gone wrong:"
   puts "Information about it: $::errorInfo"
}

exec echo "some_binary -c some_config.cfg" >@ stdout

eval exec echo "{some_binary -c some_config.cfg}" \
     >@ stdout

eval exec echo "\\\"some_binary -c some_config.cfg\\\"" \
     >@ stdout

# the list will be converted to a string that is already properly
# quoted for interpretation by eval.
set cmd [list echo "some_binary -c some_config.cfg"]
eval exec $cmd >@ stdout

"""
tclsh.eval(s)