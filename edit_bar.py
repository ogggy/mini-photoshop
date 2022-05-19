from cgitb import text
from tkinter import BOTTOM, LEFT, W, Entry, Frame, Button, TOP, Label, Text
from tkinter import filedialog
from turtle import color
from filter_view import FilterFrame
from adjust_view import AdjustFrame
import cv2



class EditBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master, padx=10, bg='#006666',)

        self.rotate = 0
        self.new_button = Button(
            self, text="New", width=10, background='#005c99')
        self.save_button = Button(
            self, text="Save", width=10, background='#005c99')
        self.save_as_button = Button(
            self, text="Save As", width=10, background='#005c99')
        self.draw_button = Button(
            self, text="Draw", width=10, background='#005c99')
        self.crop_button = Button(
            self, text="Crop", width=10, background='#005c99')
        self.filter_button = Button(
            self, text="Filter", width=10, background='#005c99')
        self.adjust_button = Button(
            self, text="Adjust", width=10, background='#005c99')
        self.clear_button = Button(
            self, text="Clear", width=10, background='RED')
        self.rotate_button = Button(
            self, text="Rotate", width=10, background='#005c99')
        self.zoom_in_button = Button(
            self, text="Zoom +", width=10, background='#005c99')
        self.zoom_out_button = Button(
            self, text="Zoom -", width=10, background='#005c99')
        self.width_label = Label(text='Width: ')
        self.width_text_field = Entry(width=10)
        self.height_label = Label(text='Height: ')
        self.height_text_field = Entry(width=10)
        self.resize_button = Button(
            self, text="Resize", width=10, background='#005c99')

        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind(
            "<ButtonRelease>", self.save_as_button_released)
        self.draw_button.bind("<ButtonRelease>", self.draw_button_released)
        self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
        self.filter_button.bind("<ButtonRelease>", self.filter_button_released)
        self.adjust_button.bind("<ButtonRelease>", self.adjust_button_released)
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)
        self.rotate_button.bind("<ButtonRelease>", self.rotate_button_released)
        self.zoom_in_button.bind("<ButtonRelease>", self.zoom_in_button_released)
        self.zoom_out_button.bind("<ButtonRelease>", self.zoom_out_button_released)
        self.resize_button.bind("<ButtonRelease>", self.resize_button_released)

        self.new_button.pack(side=TOP, pady=10, padx=10)
        self.save_button.pack(side=TOP, pady=10, padx=10)
        self.save_as_button.pack(side=TOP, pady=10, padx=10)
        self.draw_button.pack(side=TOP, pady=10, padx=10)
        self.crop_button.pack(side=TOP, pady=10, padx=10)
        self.filter_button.pack(side=TOP, pady=10, padx=10)
        self.adjust_button.pack(side=TOP, pady=10, padx=10)
        self.rotate_button.pack(side=TOP, pady=10, padx=10)
        self.zoom_in_button.pack(side=TOP, pady=10, padx=10)
        self.zoom_out_button.pack(side=TOP, pady=10, padx=10)
        self.clear_button.pack(side=TOP, pady=10, padx=10)
        self.resize_button.pack(pady=10, padx=10)
        self.width_label.pack(pady=10, padx=5)
        self.width_label.place(in_=self.resize_button, relx=0, y=20, x=-15, rely=1.0)
        self.width_text_field.pack(padx=10, pady=10)
        self.width_text_field.place(in_=self.width_label, relx=1.0, x=5, rely=0)
        self.height_label.pack(pady=10, padx=10)
        self.height_label.place(in_=self.resize_button, relx=0, y=50, x=-15, rely=1.0)
        self.height_text_field.pack(padx=10, pady=10)
        self.height_text_field.place(in_=self.height_label, relx=1.0, x=5, rely=0)
        
        
       

    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()

            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)

            if image is not None:
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True
                
                

    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()

                save_image = self.master.processed_image
                image_filename = self.master.filename
                cv2.imwrite(image_filename, save_image)

    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                original_file_type = self.master.filename.split('.')[-1]
                filename = filedialog.asksaveasfilename()
                filename = filename + "." + original_file_type

                save_image = self.master.processed_image
                cv2.imwrite(filename, save_image)

                self.master.filename = filename

    def draw_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.draw_button:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                else:
                    self.master.image_viewer.activate_draw()

    def crop_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.crop_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_crop()

    def filter_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.filter_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = FilterFrame(master=self.master)
                self.master.filter_frame.grab_set()

    def adjust_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.adjust_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.adjust_frame = AdjustFrame(master=self.master)
                self.master.adjust_frame.grab_set()

    def clear_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.processed_image = self.master.original_image.copy()
                self.master.image_viewer.show_image()
                self.rotate = 0

    def rotate_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.rotate_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                height, width = self.master.original_image.shape[:2]
                center = (width/2, height/2)

                self.rotate += 90

               
                
                # # t = self.master.image_viewer.width
                # # self.master.image_viewer.width = self.master.image_viewer.height
                # if self.rotate % 180 != 0:
                #     # using cv2.getRotationMatrix2D() to get the rotation matrix
                #     rotate_matrix = cv2.getRotationMatrix2D(
                #         center=center, angle=self.rotate, scale=0.5)
                # else:
                #     # using cv2.getRotationMatrix2D() to get the rotation matrix
                #     rotate_matrix = cv2.getRotationMatrix2D(
                #         center=center, angle=self.rotate, scale=1)
                
                # # rotate the image using cv2.warpAffine
                # rotated_image = cv2.warpAffine(
                #     src=self.master.original_image, M=rotate_matrix, dsize=(width, height))
                # if self.rotate / 90 % 4 == 1:
                rotated_image = cv2.rotate(self.master.processed_image, cv2.ROTATE_90_CLOCKWISE)
                self.master.processed_image = rotated_image

                self.master.image_viewer.show_image()


    def zoom_in_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.zoom_in_button:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()
            height, width = self.master.processed_image.shape[:2]
            dim = (width*2, height*2)
            # self.master.processed_image = cv2.resize(self.master.processed_image, dim)
            self.master.processed_image = cv2.resize(self.master.processed_image, (0, 0), fx=2, fy=2)
            self.master.image_viewer.show_image_2()

    def zoom_out_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.zoom_out_button:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()
            height, width = self.master.processed_image.shape[:2]
            dim = (width*0.5, height*0.5)
            self.master.processed_image = cv2.resize(self.master.processed_image, (0, 0), fx=0.5, fy=0.5)
            self.master.image_viewer.show_image_2()

    def resize_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.resize_button:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()

            new_width = int(self.width_text_field.get())
            new_height = int(self.height_text_field.get())
            self.master.processed_image = cv2.resize(self.master.processed_image, (new_width, new_height))
            self.master.image_viewer.show_image_2()
