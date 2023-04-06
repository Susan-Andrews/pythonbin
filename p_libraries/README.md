# p_libraries

- ##### NLP (Natural Language Processing)- It focuses on extracting meaningful information from text and train data models based on acquired insights. Primary NLP function include text mining , text classification , text analysis,word sequencing , speech recognition & generation, machine translation, and dialog systems, to name a few.   

- ##### Gensim-Target audience is the natural language processing (NLP) and information retrieval (IR) community.Used in unsupervised topic modelling and natural language processing.It is designed to extract semantic topics from documents. It can handle large text collections. Hence it makes it different from other machine learning software packages which target memory processing. Gensim also provides efficient multicore implementations for various algorithms to increase processing speed. It provides more convenient  facilities for text processing than other packages like Scikit-learn, R etc.  

- ##### FlashText-FlashText algorithm can search or replace keywords in one pass over a document.This algorithm is also designed to go for the longest match first. For an input dictionary {Machine, Learning, Machine learning} on a string 'I like Machine learning', it will only consider the longest match, which is Machine LearningThis module can be used to replace keywords in sentences or extract keywords from sentences. It is based on the FlashText algorithm.  

- ##### OpenCV- is a huge open-source library for computer vision, machine learning, and image processing. OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human. When it is integrated with various libraries, such as Numpy which is a highly optimized library for numerical operations, then the number of weapons increases in your Arsenal i.e whatever operations one can do in Numpy can be combined with OpenCV.  

- ##### Tkinter- The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications.The below code creates a popup window with minimize,maximize and a close button with a name bar at top.Tkinter provides various controls, such as buttons, labels and text boxes used in a GUI application. These controls are commonly called widgets.There are currently 15 types of widgets in Tkinter. 
                    Eg:#!/usr/bin/python

                    import Tkinter
                    top = Tkinter.Tk()
                    # Code to add widgets will go here...
                    top.mainloop()
- ##### Wxpython- Python provides wxpython module which allows us to create high functional graphical user interface. It is an Open Source module, which means it is free for anyone to use and the source code is available for anyone to look and modify. It is implemented as a set of extension modules that wrap the GUI components of wxWidgets library which is written in C++. It is cross platform GUI toolkit for python, Phoenix version Phoenix is the improved next-generation wxPython and it mainly focused on speed, maintain ability and extensibility. 
          Eg:creating a button ,

                    # Import wx module
                    import wx 
                    # creating application object
                    app1 = wx.App()
                    # creating a frame
                    frame = wx.Frame(None, title ="wxpython app")
                    pa = wx.Panel(frame) 
                    # Button creation
                    e = wx.Button(pa, -1, "Button1", pos = (120, 100))
                    # show it
                    frame.Show()
                    # start the event loop
                    app1.Mainloop()
                   
- ##### PyQt-PyQt is a GUI widgets toolkit. It is a Python interface for Qt, one of the most powerful, and popular cross-platform GUI library. PyQt is a blend of Python programming language and the Qt library. This introductory tutorial will assist you in creating graphical applications with the help of PyQt.QtGui module contains all the graphical controls. In addition, there are modules for working with XML (QtXml), SVG (QtSvg), and SQL (QtSql), etc.  
Define the size and position of window by setGeometry() method.
Enter the mainloop of application by app.exec_() method.
                    Eg:import sys
                    from PyQt4 import QtGui

                    def window():
                       app = QtGui.QApplication(sys.argv)
                       w = QtGui.QWidget()
                       b = QtGui.QLabel(w)
                       b.setText("Hello World!")
                       w.setGeometry(100,100,200,50)
                       b.move(50,20)
                       w.setWindowTitle(“PyQt”)
                       w.show()
                       sys.exit(app.exec_())

                    if __name__ == '__main__':
                       window()    
                      
             https://www.tutorialspoint.com/pyqt/images/hello_world.jpg  
 
 - ##### Pygame- pygame is a free and open-source cross-platform library for the development of multimedia applications like video games using Python. It uses the Simple DirectMedia Layer library and several other popular libraries to abstract the most common functions, making writing these programs a more intuitive task. 
                     import pygame  

                    pygame.init()  #This is used to initialize all the required module of the pygame.
                    screen = pygame.display.set_mode((400,500))  #This is used to display a window of the desired size. The return value is a Surface object which is the object where we will perform graphical operations.Parameters are width and height 
                    done = False  
                     while not done:  
                        for event in pygame.event.get():  #This is used to empty the event queue. If we do not call this, the window messages will start to pile up and, the game will become unresponsive in the opinion of the operating system.  
                            if event.type == pygame.QUIT:  #This is used to terminate the event when we click on the close button at the corner of the window.  
                                done = True  
                        pygame.display.flip()   #Pygame is double-buffered, so this shifts the buffers. It is essential to call this function in order to make any updates that you make on the game screen to make visible.  
                        it will give a simple window as an output.
   -                      
                   


                    
                    
                    
                    
                    
                    
