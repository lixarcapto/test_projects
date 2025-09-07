

from btpy.Btpy import Btpy
from FrameIdentity import FrameIdentity
from Model import Model
from FrameTraits import FrameTraits
from FrameSkills import FrameSkills
from FrameConfig import FrameConfig
from FrameAppearance import FrameAppearance
from FrameExperiences import FrameExperiences

class View:

    def __init__(self):
        self.model = Model()
        self.window = Btpy.Window(
            "PJ creator"
        )
        self.button_box = Btpy.ButtonBox(
            self.window.widget
        )
        self.button_box.widget.grid(
            row = 0,
            column= 0
        )
        list_ = [
                "File",
                "Identity",
                "Traits",
                "Skills",
                "Appearance",
                "Experiences"
            ]
        self.button_box.set_components(
            list_
        )
        self.button_box.set_columns(
            len(list_)
        )
        self.button_box.add_listener_to(
            0,
            self.set_frame_config
        )
        self.button_box.add_listener_to(
            1,
            self.set_frame_identity
        )
        self.button_box.add_listener_to(
            2,
            self.set_frame_traits
        )
        self.button_box.add_listener_to(
            3,
            self.set_frame_skills
        )
        self.button_box.add_listener_to(
            4,
            self.set_frame_appearance
        )
        self.button_box.add_listener_to(
            5,
            self.set_frame_experiences
        )
        self.frame_identity = FrameIdentity(
            self.window.widget,
            self.model
        )
        self.frame_traits = FrameTraits(
            self.window.widget,
            self.model
        )
        self.frame_skills = FrameSkills(
            self.window.widget,
            self.model
        )
        self.frame_config = FrameConfig(
            self.window.widget,
            self.model
        )
        self.frame_appearance = FrameAppearance(
            self.window.widget,
            self.model
        )
        self.frame_experiences = FrameExperiences(
            self.window.widget,
            self.model
        )
        self.set_frame_identity()
        self.window.start()

    def set_frame_identity(self):
        self.frame_identity.frame.grid(
            row = 1,
            column= 0
        )
        self.frame_traits.frame\
            .grid_forget()
        self.frame_skills.frame\
            .grid_forget()
        self.frame_config.frame\
            .grid_forget()
        self.frame_appearance.frame\
            .grid_forget()
        self.frame_experiences.frame\
            .grid_forget()
        
    def set_frame_traits(self):
        self.frame_traits.frame.grid(
            row = 1,
            column= 0
        )
        self.frame_identity.frame\
            .grid_forget()
        self.frame_skills.frame\
            .grid_forget()
        self.frame_config.frame\
            .grid_forget()
        self.frame_appearance.frame\
            .grid_forget()
        self.frame_experiences.frame\
            .grid_forget()
        
    def set_frame_skills(self):
        self.frame_skills.frame.grid(
            row = 1,
            column= 0
        )
        self.frame_traits.frame\
            .grid_forget()
        self.frame_identity.frame\
            .grid_forget()
        self.frame_config.frame\
            .grid_forget()
        self.frame_appearance.frame\
            .grid_forget()
        self.frame_experiences.frame\
            .grid_forget()
        
    def set_frame_config(self):
        self.frame_config.frame.grid(
            row = 1,
            column= 0
        )
        self.frame_traits.frame\
            .grid_forget()
        self.frame_identity.frame\
            .grid_forget()
        self.frame_skills.frame\
            .grid_forget()
        self.frame_appearance.frame\
            .grid_forget()
        self.frame_experiences.frame\
            .grid_forget()
        
    def set_frame_appearance(self):
        self.frame_appearance.frame.grid(
            row = 1,
            column= 0
        )
        self.frame_traits.frame\
            .grid_forget()
        self.frame_identity.frame\
            .grid_forget()
        self.frame_skills.frame\
            .grid_forget()
        self.frame_config.frame\
            .grid_forget()
        self.frame_experiences.frame\
            .grid_forget()
        
    def set_frame_experiences(self):
        self.frame_experiences.frame.grid(
            row = 1,
            column= 0
        )
        self.frame_appearance.frame\
            .grid_forget()
        self.frame_traits.frame\
            .grid_forget()
        self.frame_identity.frame\
            .grid_forget()
        self.frame_skills.frame\
            .grid_forget()
        self.frame_config.frame\
            .grid_forget()


    